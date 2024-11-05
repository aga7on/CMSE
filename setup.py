import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["tkinter", "ttkthemes", "base64", "json", "os", "shutil"],
    "include_files": [], # Add any other files like images or data files here if needed
    "excludes": []
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Cloud Meadow Save Editor",
    version="1.0",
    description="Editor for Cloud Meadow save files",
    options={"build_exe": build_exe_options},
    executables=[Executable("cmse.py", base=base, target_name="CMSE.exe")]
)