# SQL-Formatter

Simple SQL formatter for work related queries.
The simple python3 app takes a list of usernames that are divided by a newline and formats them for work related SQL queries.
Executable was build using the [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/) library.

To build using pyinstaller, go into the directory where username_formatter.py is located and run the command:

`pyinstaller -F --noconsole username_formatter.py`

The `-F` flag will created a single executable and the `--noconsole` will stop a blank console from opening up once the executable is launched.
