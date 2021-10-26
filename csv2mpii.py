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
        os.mkdir(result_path)

    dir_list = [name for name in os.listdir(target_path) if os.path.isdir(os.path.join(target_path, name))]
    for dname in tqdm.tqdm(dir_list, desc="label types"):
        destination = os.path.join(result_path, dname)
        if not os.path.exists(destination):
            os.mkdir(destination)

        fout = open(os.path.join(destination, "mpii_style.json"), "w", encoding="utf-8")

        instances = []

        files_grabbed = []
        for ftype in target_formats:
            files_grabbed.extend(glob.glob(os.path.join(target_path, dname, ftype)))
            files_grabbed.extend(glob.glob(os.path.join(target_path, dname, "*",  ftype)))

        for fpath in tqdm.tqdm(files_grabbed, desc="files in label type"):
            basename = os.path.basename(fpath).split(".")[0]

            fread = open(fpath, "r", encoding="utf-8")
            content = fread.read()
            all_lines = content.split("\n")

            vis = []
            joints = []
            for line in all_lines:
                snippets = line.split(",")
                if "world" in snippets[0]:
                    continue
                elif " x" in snippets:
                    continue
                else:    
                    count = 0
                    coords = []
                    for snip in snippets:
                        try:
                            coord = float(snip)
                            count+=1

                            if count < 3:
                                coords.append(coord)
                        except:
                            pass
                    
                    vis.append(1)
                    joints.append(coords)
        
            instance = {"joints_vis" : vis, "joints" : joints,
                       "image" : basename + ".png", "scale" : 255/300,
                       "center" : [255/2, 255/2]}
            instances.append(instance)
    
        json.dump(instances, fout, ensure_ascii=False)
