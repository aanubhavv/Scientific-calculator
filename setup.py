import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['resources', 'data']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",        
    icon="resources/icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "Calculator",
    version = "4.0",
    description = "Simple calculator",
    author = "Anubhav Garg",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
