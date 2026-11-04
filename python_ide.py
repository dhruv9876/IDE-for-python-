import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import sys
import keyword
import re


class PythonIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("Python IDE")
        self.root.geometry("800x600")

        self.file_path = ""

        self.create_menu()
        self.create_widgets()
        self.bind_shortcuts()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.destroy)

        menu_bar.add_cascade(label="File", menu=file_menu)

        run_menu = tk.Menu(menu_bar, tearoff=0)
        run_menu.add_command(label="Run", command=self.run_code)

        menu_bar.add_cascade(label="Run", menu=run_menu)

        self.root.config(menu=menu_bar)

    def create_widgets(self):
        self.editor = tk.Text(
            self.root,
            font=("Consolas", 12),
            wrap="none"
        )
        self.editor.pack(expand=True, fill="both")

        self.output = tk.Text(
            self.root,
            height=10,
            font=("Consolas", 12),
            bg="#1e1e1e",
            fg="white"
        )
        self.output.pack(fill="both")

        # Syntax Highlight Tags
        self.editor.tag_configure(
            "keyword",
            foreground="#569CD6"
        )

        self.editor.tag_configure(
            "string",
            foreground="#CE9178"
        )

        self.editor.tag_configure(
            "comment",
            foreground="#6A9955"
        )

        self.editor.tag_configure(
            "builtin",
            foreground="#4EC9B0"
        )

    def bind_shortcuts(self):
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())
        self.root.bind("<F5>", lambda e: self.run_code())

        self.editor.bind(
            "<KeyRelease>",
            self.highlight_syntax
        )

    def update_title(self):
        if self.file_path:
            name = self.file_path.split("/")[-1]
            self.root.title(f"Python IDE - {name}")
        else:
            self.root.title("Python IDE")

    def open_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("Python Files", "*.py")]
        )

        if not path:
            return

        try:
            with open(path, "r", encoding="utf-8") as file:
                code = file.read()

            self.editor.delete("1.0", tk.END)
            self.editor.insert("1.0", code)

            self.file_path = path
            self.update_title()

            self.highlight_syntax()

        except Exception as e:
            messagebox.showerror(
                "Open Error",
                str(e)
            )

    def save_file(self):
        if not self.file_path:
            self.save_as()
            return

        try:
            with open(
                self.file_path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    self.editor.get(
                        "1.0",
                        tk.END
                    )
                )

        except Exception as e:
            messagebox.showerror(
                "Save Error",
                str(e)
            )

    def save_as(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".py",
            filetypes=[("Python Files", "*.py")]
        )

        if not path:
            return

        try:
            with open(
                path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    self.editor.get(
                        "1.0",
                        tk.END
                    )
                )

            self.file_path = path
            self.update_title()

        except Exception as e:
            messagebox.showerror(
                "Save Error",
                str(e)
            )

    def run_code(self):
        if not self.file_path:
            messagebox.showwarning(
                "Save Required",
                "Please save your file before running."
            )
            return

        try:
            process = subprocess.Popen(
                [sys.executable, self.file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            output, error = process.communicate()

            self.output.delete(
                "1.0",
                tk.END
            )

            if output:
                self.output.insert(
                    tk.END,
                    output
                )

            if error:
                self.output.insert(
                    tk.END,
                    error
                )

        except Exception as e:
            messagebox.showerror(
                "Run Error",
                str(e)
            )

    def highlight_syntax(self, event=None):

        content = self.editor.get(
            "1.0",
            tk.END
        )

        self.editor.tag_remove(
            "keyword",
            "1.0",
            tk.END
        )

        self.editor.tag_remove(
            "string",
            "1.0",
            tk.END
        )

        self.editor.tag_remove(
            "comment",
            "1.0",
            tk.END
        )

        self.editor.tag_remove(
            "builtin",
            "1.0",
            tk.END
        )

        # Python Keywords
        for kw in keyword.kwlist:

            start = "1.0"

            while True:

                start = self.editor.search(
                    r"\m" + kw + r"\M",
                    start,
                    stopindex=tk.END,
                    regexp=True
                )

                if not start:
                    break

                end = f"{start}+{len(kw)}c"

                self.editor.tag_add(
                    "keyword",
                    start,
                    end
                )

                start = end

        # Strings
        for match in re.finditer(
            r'".*?"|\'.*?\'',
            content
        ):

            start = f"1.0+{match.start()}c"
            end = f"1.0+{match.end()}c"

            self.editor.tag_add(
                "string",
                start,
                end
            )

        # Comments
        for match in re.finditer(
            r"#.*",
            content
        ):

            start = f"1.0+{match.start()}c"
            end = f"1.0+{match.end()}c"

            self.editor.tag_add(
                "comment",
                start,
                end
            )

        # Builtins
        builtins = [
            "print",
            "input",
            "len",
            "range",
            "int",
            "str",
            "list",
            "dict"
        ]

        for func in builtins:

            start = "1.0"

            while True:

                start = self.editor.search(
                    r"\m" + func + r"\M",
                    start,
                    stopindex=tk.END,
                    regexp=True
                )

                if not start:
                    break

                end = f"{start}+{len(func)}c"

                self.editor.tag_add(
                    "builtin",
                    start,
                    end
                )

                start = end


if __name__ == "__main__":
    root = tk.Tk()
    app = PythonIDE(root)
    root.mainloop()
