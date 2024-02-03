from pathlib import Path
import os

file_path=Path('G:\\Books\\Asif Ruhani')
x=file_path.cwd().is_absolute()
print(x)
