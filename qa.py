
from utils.speech import ogg_to_text
import os

workdir = os.getcwd()
ogg_file_name = 'new_file_work.ogg'
ogg_file_name = 'new_file_error.ogg'
ogg_file_path = os.path.join(workdir,"files",ogg_file_name)

with open(ogg_file_path, 'rb') as new_file:
    txt = ogg_to_text(ogg_file_path)
    print(txt)