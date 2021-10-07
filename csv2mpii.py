import os
import glob
import json
import tqdm

cwd = os.getcwd()
target_formats = ("*.csv", "*.txt")
target_name = "input"
target_path = os.path.join(cwd, target_name)

result_name = "output"
result_path = os.path.join(cwd, result_name)

if __name__ == "__main__":
    if not os.path.exists(target_path):
        os.mkdir(target_path)
    
    if not os.path.exists(result_path):
        os.mkdir(target_path)

    dir_list = [name for name in os.listdir(target_path) if os.path.isdir(os.path.join(target_path, name))]
    for dname in dir_list:
        destination = os.path.join(result_path, dname)
        if not os.path.exists(destination):
            os.mkdir(destination)

    files_grabbed = []
    for ftype in target_formats:
        files_grabbed.extend(glob.glob(os.path.join(target_path, ftype)))
        files_grabbed.extend(glob.glob(os.path.join(target_path, "*",  ftype)))

    for fpath in tqdm.tqdm(files_grabbed):
        basename = os.path.basename(path)
        dirname = os.path.dirname(path)[-1]

        fread = open(fpath, "r", encoding="utf-8")
        content = fread.read()
        all_lines = content.split("\n")