import os
import re

files = os.listdir()
for i in ["series", "movies"]:
    try:
        os.mkdir(i)
    except FileExistsError:
        pass
for file in files:
    if match_group := re.findall("([a-zA-Z_\.\d]+)([sS]\d{1,3})(E\d{1,3})[\w_\-\.]+(\.\w{3,})", file):  # series
        name = match_group[0][0].replace(".", " ").replace("_", " ").strip().replace(" ", "_")
        season = match_group[0][1].replace("s", "").replace("S", "")
        episode = match_group[0][2].replace("e", "").replace("E", "")
        file_format = match_group[0][3]
        for i in [name, f"{name}/Season {season}"]:
            try:
                os.mkdir(f"series/{i}")
            except FileExistsError:
                pass
        os.replace(file, dst=f"series/{name}/Season {season}/{name}_S{season}_E{episode}{file_format}")
    elif match_group := re.findall("([a-zA-Z_\.\s]+)[\w_\-\.]+(\.\w{3,})", file):  #movies
        name = match_group[0][0].replace(".", " ").replace("_", " ").strip().replace(" ", "_")
        file_format = match_group[0][1]
        try:
            os.mkdir(f"movies/{name}")
        except FileExistsError:
            pass
        os.replace(file, dst=f"movies/{name}/{name}{file_format}")
