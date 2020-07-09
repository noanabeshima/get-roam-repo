''' main.py '''

import os
import fire
import pyperclip


def print_dir(root: dict, n_indent: int = 0):
    res = ""
    for d in root.keys():
        if d != '_files':
            res += f"{' '*4*n_indent}- ### {d}\n"
            res += print_dir(root[d], n_indent+1)
    assert '_files' in root.keys(), root
    for f in root['_files']:
        res += f"{' '*4*n_indent}- {f}\n"

    return res

def main(repo = "githubtraining/hellogitworld"):
    root = dict()
    os.system(f"git clone --quiet --depth 1 --single-branch https://github.com/{repo} /tmp/{repo}")

    for curdir, dirs, files in os.walk(f"/tmp/{repo}"):
        if ('.git' in dirs):
            dirs.remove('.git')
        head = root
        for d in curdir.split("/")[4:]:
            head = head[d]
        for d in dirs:
            head[d] = dict()
        files = ["**"+f+"**" if f != "__init__.py" else "$$\_\_$$**init**$$\_\_$$**.py**" for f in files]

        head["_files"] = files

    os.system(f"rm -rf /tmp/{repo}")

    result = print_dir(root)[:-1] # remove last \n
    print(result)
    pyperclip.copy(result)


if __name__=='__main__':
    fire.Fire(main)
