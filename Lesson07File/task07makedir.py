import os
from pathlib import Path

os.mkdir('new_os_dir1')
Path('new_path_dir1').mkdir()

# если необходимо создать несколько вложенных друг в друга каталогов, код будет следующим:

os.makedirs('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').mkdir() # FileNotFoundError
Path('some_dir/dir/new_path_dir2').mkdir(parents=True)
