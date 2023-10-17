import os
from pathlib import Path
import shutil
# os.rmdir('dir') # OSError
# Path('some_dir').rmdir() # OSError
os.rmdir('dir/other_dir/new_os_dir')
Path('some_dir/dir/new_path_dir2').rmdir()

# Если необходимо удалить каталог со всем его содержимым (вложенные каталоги и
# файлы), подойдёт функция из модуля shutil

shutil.rmtree('dir/other_dir')
shutil.rmtree('some_dir')

