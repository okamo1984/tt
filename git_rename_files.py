import argparse
from pathlib import Path
import subprocess
import os


def rename(directory: str, before: str, after: str):
    cwd = Path.cwd()
    path = Path(directory).expanduser().absolute()
    os.chdir(path)
    for file in path.glob(f"**/*"):
        name = file.name
        new_name = name.replace(before, after)
        if (new_name == name):
            continue
        new_file = file.parent / new_name
        git_move(file, new_file)

    os.chdir(cwd)


def git_move(old: Path, new: Path):
    subprocess.run(["git", "mv", str(old), str(new)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", default=".", type=str)
    parser.add_argument("--before", metavar="before pattern", required=True, type=str)
    parser.add_argument("--after", metavar="after pattern", required=True, type=str)
    known_args, _ = parser.parse_known_args()
    rename(**vars(known_args))
