#!/usr/local/bin/python3

# Basic Imports
import os
import sys
from os.path import expanduser

# Global - add files you want to ignore in the current directory
IGNORED_FILES = ["bootstrap.py", "README.md", "LICENSE", ".DS_Store"]

if __name__ == "__main__":
    """
    Run this out of the .dotfiles directory to symlink the appropriate
    files into your home directory
    """

    currentDirectory = os.getcwd()
    home = os.getenv("HOME")

    if not currentDirectory.endswith("dotfiles"):
        print("Are you running this outside of the dotfiles directory?")
        sys.exit(1)

    else:
        dotfiles  = os.listdir(currentDirectory)

        for f in dotfiles:
            if f.endswith("~") or os.path.isdir(f) or (f in IGNORED_FILES):
                print("Ignoring temp file or directory: %s" % f)
                continue
            
            elif f.startswith("."):
                original = currentDirectory + "/" + f
                homeFile = home + "/" + f
                print("Linking: %s --> %s" % (original, homeFile))
                os.system("ln -fsi %s %s" % (original, homeFile))

            else:
                print("We encountered some weird file and are ignoring it %s" % f)

        workon_home = os.getenv("WORKON_HOME", expanduser("~") + "/code/environments") 
        print("Making virtualenv directory: %s" % workon_home)
        os.makedirs(workon_home, exist_ok=True)
    print("Done linking...")

