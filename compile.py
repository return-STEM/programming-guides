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


def strip_comments(md_text):
    anchor = md_text.find("%%")
    while anchor != -1:
        next = md_text.find("%%", anchor + 1)
        md_text = md_text[:anchor] + md_text[next + 2:]
        anchor = md_text.find("%%")
    return md_text

# class Range:
#     start:int
#     end:int
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#     def is_inside(self, loc):
#         return self.start < loc < self.end
#
#
# def find_fenced_code(md_text: str):
#     """Finds fenced code blocks inside markdown"""
#     ranges: list[Range] = []
#     anchor = md_text.find("\n```")
#     while anchor != -1:
#         next = md_text.find("\n```", anchor + 3)
#         ranges.append(Range(anchor, next + 3 if next != -1 else len(md_text)))
#         anchor = md_text.find("\n```", next + 3)
#     return ranges
#
# def find_html_code(md_text: str):
#     """Finds fenced code blocks inside markdown"""
#     ranges: list[Range] = []
#     anchor = md_text.find("<code>")
#     while anchor != -1:
#         next = md_text.find("</code>", anchor + 5)
#         ranges.append(Range(anchor, next + 5 if next != -1 else len(md_text)))
#         anchor = md_text.find("<code>", next + 3)
#     return ranges
#
# def find_inline_code(md_text: str):
#     bound = len(md_text)
#     ranges: list[Range] = []
#
#     def jump_to_backtick_end(loc):
#         while loc + 1 < bound and md_text[loc + 1] == '`':
#             loc += 1
#         return loc
#
#     anchor = md_text.find("`")
#
#     while anchor != -1:
#         anchor = jump_to_backtick_end(anchor)
#         next = min(md_text.find("`", anchor), md_text.find('\n'), anchor)
#
#         ranges.append(Range(anchor, next if next != -1 else len(md_text)))
#         anchor = md_text.find("`", next)
#     return ranges
#
# def generate_code_map(md_text):
#     ranges = find_fenced_code(md_text) + find_html_code(md_text) + find_inline_code(md_text)
#     return ranges
#
# def convert_obsidian_embeds(md_text):
#     code_map = generate_code_map()
#     anchor = md_text.find("![[")
#     while [x for x in code_map if x.is_inside(anchor)]:
#         anchor = md_text.find("![[", anchor + 2)
#
#




def process_md(md):
    md_text = md.read()
    md_text = strip_comments(md_text)

    print(f"Finished processing {md.name}")

    return md_text


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
