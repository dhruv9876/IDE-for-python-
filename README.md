# Python Code Editor

A lightweight desktop-based Python IDE built using Python and Tkinter. The application provides an intuitive environment for writing, editing, saving, and executing Python programs while offering syntax highlighting, live syntax checking, integrated output display, keyboard shortcuts, and file management.

Designed for students, beginners, and developers, the editor delivers a focused coding experience without the complexity of larger Integrated Development Environments (IDEs).

---

## Features

- Open, Save, and Save As support
- Python code execution with F5 (auto-saves before running)
- Integrated output console
- Syntax highlighting for Python keywords
- Built-in function highlighting
- String and comment highlighting
- Live syntax error detection while typing (error line turns red, message shown in the status bar)
- Runtime error highlighting (failing line is highlighted in the editor)
- Plain-language error suggestions shown below each error
- Background thread execution, so the interface never freezes
- 10-second timeout to stop infinite loops automatically
- Keyboard shortcuts (Ctrl+S, Ctrl+O, F5)
- Error handling and execution feedback
- Dynamic file tracking
- Object-oriented architecture

---

## Technologies Used

- Python 3
- Tkinter
- Subprocess Module
- Threading and Queue
- AST Module
- File Handling
- Regular Expressions (Regex)
- Object-Oriented Programming (OOP)

---

## Project Structure

```text
IDE-for-python-/
│
├── python_ide.py
├── README.md
└── screenshots/
```

---

## How It Works

The application provides a text editor where users can write Python code. While typing, the code is checked using Python's ast module, and any syntax error is highlighted in red with its message shown in the status bar.

When the Run option is selected, the file is saved automatically and executed using Python's subprocess module inside a background thread, so the editor stays responsive. Standard output and error messages are captured and displayed within the integrated output console. If the script fails, the failing line is highlighted in the editor and a plain-language suggestion is shown below the error. Scripts that run longer than 10 seconds are stopped automatically.

---

## Installation

### Prerequisites

- Python 3.x
- Tkinter (included with most Python installations)

### Clone the Repository

```bash
git clone https://github.com/your-username/IDE-for-python-.git
```

### Navigate to the Project Directory

```bash
cd IDE-for-python-
```

### Run the Application

```bash
python python_ide.py
```

---

## User Interface

### File Menu

- Open
- Save
- Save As
- Exit

### Run Menu

- Execute Python Program (F5)

### Editor Area

- Write and edit Python code
- Syntax highlighting support
- Live syntax error detection
- Keyboard shortcuts

### Output Console

- Display program output
- Show runtime errors and exceptions
- Show suggestions for fixing common errors

### Status Bar

- Show syntax check results
- Show running, finished, and timeout status

---

## Key Learning Outcomes

This project demonstrates practical knowledge of:

- Python Programming
- GUI Development with Tkinter
- Object-Oriented Programming
- File Handling
- Event-Driven Programming
- Multithreading and Thread-Safe UI Updates
- Process Management using subprocess
- Code Parsing using ast and Regular Expressions
- Desktop Application Development
- Error Handling and Debugging

---

## Future Enhancements

- Interactive Input Support for input()
- Live Output Streaming and Stop Button
- Line Numbers
- Dark Mode
- Find and Replace
- Auto Completion
- Multiple File Tabs
- Project Explorer
- Theme Customization
- Integrated Debugger

---

## Use Cases

- Learning Python Programming
- Practicing Python Coding
- Running Small Python Scripts
- Understanding GUI Application Development
- Educational and Academic Projects

---

## Author

**Dhruv Tiwari**

Feel free to fork, modify, and enhance this project. Contributions, suggestions, and feedback are welcome.
