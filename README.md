# Python-Primer

(For MacOS using VS Code)
## Install Python and Tools

1. Install Python
  - Run "brew install python3" in terminal
  - Verify installation with "python3 --version" in terminal
2. Install VS Code Python extension
  - Open https://marketplace.visualstudio.com/items?itemName=ms-python.python
  - Install extension
3. Select a Python interpreter
  - Python is an interpreted language, and in order to run Python code and get Python IntelliSense, you must tell VS Code which interpreter to use.
  - From within VS Code, select a Python 3 interpreter by opening the Command Palette (⇧⌘P), start typing the Python: Select Interpreter command to search, then select the command.
  - The command presents a list of available interpreters that VS Code can find automatically, including virtual environments. 
  - Selecting an interpreter sets the python.pythonPath value in your workspace settings to the path of the interpreter. To see the setting, select File > Preferences > Settings (Code > Preferences > Settings on macOS), then select the Workspace Settings tab.
4. Create or open a Python file to get started
  - Using terminal, create a new directory or navigate to an existing one
  - Open the directory as a VS Code workspace
  - Using either the terminal or VS Code GUI, create a new file with the .py extension

## Language Basics and examples

See [hello.py](./hello.py) for some basic examples and a brief primer on Python

## Other Resources

[Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)

[Learn the Basics on learnpython.org](https://www.learnpython.org/en/Welcome)

[Try some tutorials on realpython.com](https://realpython.com/)

[Python 3 on Codecademy (requires pro)](https://www.codecademy.com/learn/learn-python-3)