import os
from glob import glob
import json
import shutil


def makedir(directory):
    print(f"Making path: {directory}")
    try:
        os.mkdir(directory)
    except FileExistsError:
        print("Already exists!")


def process_md(md):
    return md.read()


root_test_path: str = "../return-stem-guides"
md_dest_path: str = "public/"

dest_path = os.path.join(root_test_path, md_dest_path)

source_path = 'guide/'

for course_dir in glob(f"{source_path}*/"):
    dest_course_dir = os.path.basename(os.path.normpath(course_dir))
    course_path = os.path.join(dest_path, dest_course_dir)
    makedir(course_path)

    metadata_path = os.path.join(course_dir, "metadata.json")
    try:
        os.remove(os.path.join(dest_path, dest_course_dir, "metadata.json"))
    except:
        pass
    shutil.copy(metadata_path, os.path.join(dest_path, dest_course_dir))

    with open(metadata_path) as metadataFile:
        metadata = json.load(metadataFile)

        for lesson in metadata["lessons"]:
            lesson_path = os.path.join(dest_course_dir, lesson["href"])
            try:
                shutil.copytree(os.path.join(source_path, lesson_path), os.path.join(dest_path, lesson_path))
            except Exception as e:
                if isinstance(e, FileNotFoundError):
                    makedir(os.path.join(source_path, lesson_path))
                elif isinstance(e, FileExistsError):
                    shutil.rmtree(os.path.join(dest_path, lesson_path))
                    shutil.copytree(os.path.join(source_path, lesson_path), os.path.join(dest_path, lesson_path))

            try:
                with open(os.path.join(source_path, lesson_path) + ".md", "r", encoding="utf-8") as md:
                    processed_md = process_md(md)
                    with open(os.path.join(dest_path, lesson_path) + ".mdx", "w+", encoding="utf-8") as dest_md:
                        dest_md.write(processed_md)
            except FileNotFoundError:
                pass
