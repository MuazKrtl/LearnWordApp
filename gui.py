import sys
import cx_Freeze
from cx_Freeze import setup, Executable
sys.argv.append("build")
filename = "gui3.py"
base = None
if sys.platform == "win32":
    base = "Win32GUI"
setup(
    name = "Kelime Ogren",
    version = "2.0",
    description = "It helps you to memorize words easily!",
    executables = [Executable(filename, base=base)])