import os, re
import info
# Set project directory to current directory

output_instructions = True

if not os.path.exists(info.data["requirements_folder"]):
    os.mkdir(info.data["requirements_folder"])

if not os.path.exists(info.data["storage_folder"]):
    os.mkdir(info.data["storage_folder"])

output = ""
documentation = ""

# Iterate through instructions folder
for file in sorted(os.listdir("instructions")):
    with open(f"instructions/{file}", "r") as f:
        output += "=" * 30 + "\n\n"
        output += "-=[" + file.replace(".txt", "").replace("_", " ").upper() + "]=-\n\n"
        output += f.read() + "\n\n"

if output_instructions:

    def format_for_readme(text, document_path=""):
        global documentation
        if document_path != "":
            documentation += f"## {document_path.split('/')[-1].replace('-', ' ')} ##\n\n"
        new_text = ""
        for text_line in text.split("\n"):
            if text_line.startswith("-=["):
                new_text += f"## {text_line[3:-3]} ##\n" + "\n"
                if document_path != "":
                    documentation += f"[{text_line[3:-3]}](/{document_path}#{text_line[3:-3].lower().replace(' ', '-').replace('.', '')})\n\n"
            elif len(text_line) > 0 and text_line[0] in "1234567890":
                new_text += f"### {text_line} ###\n" + "\n"
                # new_text += line + "\n" + "\n"
            elif text_line.startswith("=="):
                new_text += "\n"
            elif len(text_line) == 0:
                new_text += "\n"
            else:
                new_text += text_line + "\n" + "\n"
        return new_text


    keys = info.data.keys()
    for key in keys:
        search_item2 = "!<" + key + ">"
        if search_item2 in output:
            # Replace with the value
            output = output.replace(search_item2, info.data[key])

    turn_to_readme = format_for_readme(output, document_path="docs/INSTRUCTIONS.md")

    with open("../../Downloads/Template-master/Template-master/README.md", "w") as f:
        # Add all lines from ABOUT.md to README.md
        with open("../../Downloads/Template-master/Template-master/ABOUT.md", "r") as about:
            for line in about.readlines():

                for key, value in info.data.items():
                    line = line.replace("<" + key + ">", str(value))

                f.write(line)
            f.write("\n\n")
        f.write("""## DOCUMENTATION\n\n""")
        f.write("[For Documentation, Click Here](docs/DOCS.md)\n\n")

    with open(info.data["docs_folder"] + "/INSTRUCTIONS.md", "w") as f:
        # Provide link to go back to DOCS.md
        f.write(f"[Back to DOCS.md](DOCS.md)\n\n")
        f.write(turn_to_readme)

    documentation += f"# API #\n\n"

    # walk through every .py file in the toolbox folder
    for root, dirs, files in os.walk(info.data["project_dir"]):
        for file in files:
            if file[0] == ".":
                continue

            if file.endswith(".py"):
                # open the file
                with open(os.path.join(root, file), "r") as f:
                    # Get path between project directory and file
                    file_path = os.path.join(root, file).replace(info.data["project_dir"], "")
                    if file_path.startswith("/"):
                        file_path = file_path[1:]
                    # Split the path into folders
                    folders = str(file_path).split("/")
                    last_part = folders[-1].split(".")[0]
                    file_document_path = info.data["docs_folder_dir"] + "/" + (str(file_path).strip().replace("/", "-").upper().split(".PY")[0]) + ".md"

                    file2 = open(file_document_path, "w")
                    # Provide link to go back to DOCS.md
                    file2.write(f"[Back to DOCS.md](DOCS.md)\n\n")
                    # Turn into a "from ... import ..." statement
                    join_stuff = ".".join(folders[:-1])
                    if len(join_stuff) == 0:
                        import_statement = "import " + last_part
                    else:
                        import_statement = "from " + ".".join(folders[:-1]) + " import " + last_part
                    file2.write(f"Import Statement: `{import_statement}`\n\n")
                    # Turn into a "from ... import *" statement
                    # Remove extension first
                    folders[-1] = folders[-1].split(".")[0]
                    import_statement = "from " + ".".join(folders) + " import *"
                    file2.write(f"Alternative Import Statement: `{import_statement}`\n\n")
                    # read the file as a list
                    lines = f.readlines()

                    def get_function_name(text_line):
                        return text_line.strip().split("def ")[1].split("(")[0]

                    def get_class_name(text_line):
                        return text_line.strip().split("class ")[1].split("(")[0].split(":")[0]

                    def count_spaces_at_beginning(text_line):
                        count = 0
                        for c in text_line:
                            if c == " ":
                                count += 1
                            else:
                                break
                        return count

                    def get_function_documentation(k, offset=0):
                        if len(lines) <= k or lines[k].strip().startswith("def "):
                            return ""
                        if lines[k].strip() == "\"\"\"":
                            docs = ""
                            j = k + 1
                            while j < len(lines) and lines[j].strip() != "\"\"\"":
                                docs += lines[j]
                                j += 1
                            return docs
                        else:
                            if offset > 10:
                                return ""
                            else:
                                return get_function_documentation(k + 1, offset=offset + 1)

                    def get_class_documentation(k, offset=0):
                        if len(lines) <= k or lines[k].strip().startswith("class "):
                            return ""
                        if lines[k].strip() == "\"\"\"":
                            docs = ""
                            j = k + 1
                            while j < len(lines) and lines[j].strip() != "\"\"\"":
                                docs += lines[j]
                                j += 1
                            return docs
                        else:
                            if offset > 10:
                                return ""
                            else:
                                return get_class_documentation(k + 1, offset=offset + 1)

                    def document_data(i, name, line, docs, parent_string="", obj_type="function", spaces = "> "):
                        # Remove underscores from front and back only, not in the middle
                        name = name.strip("_")
                        name = parent_string + name
                        file2.write(f"# {spaces} {obj_type + ' ' + name} #\n\n")
                        class_declaration = line
                        file2.write(f"### [{class_declaration.strip()}](./../{file_path}#L{i + 1}) \n\n")
                        file_documentation = f"/{file_document_path}#{obj_type}-{name.lower().replace(' ', '-').replace('.', '')}"
                        writing_header = f"### {spaces}[{obj_type + ' ' + name}]({file_documentation}) \n\n"
                        documents = get_class_documentation(i + 1)
                        sections = ["Note", "Param", "Return", "Example", "Reference", "Desc"]
                        new_documentation = ""
                        for section in sections:
                            if section in documents:
                                file2.write(section + "\n\n")
                                new_documentation += section + "\n\n"
                                sect_back = documents.find(section) + len(section) + 1
                                while documents[sect_back] == "\n" or documents[sect_back] == "-":
                                    sect_back += 1
                                sect_front = 9999999
                                for sect2 in sections:
                                    if sect2 == section:
                                        continue
                                    sect_front2 = documents.find(sect2)
                                    if sect_front2 != -1:
                                        if sect_front > sect_front2 > sect_back:
                                            sect_front = sect_front2
                                section_combined = documents[sect_back:sect_front].strip()

                                # remove first line if its first character is a dash
                                if section_combined[0] == "-":
                                    section_combined = section_combined.split("\n", 1)[1]
                                file2.write("```python\n" + section_combined + "\n```\n\n")
                                new_documentation += "\n```python\n" + section_combined + "\n```\n\n"

                        class_declaration_reference = f"[{class_declaration.strip()}](./../{file_path}#L{i + 1}) \n\n"
                        # Add dropdown to docs with the documentation
                        docs += f"\n <details>\n<summary>\n\n{writing_header}\n\n</summary>\n\n{class_declaration_reference + new_documentation}\n\n"
                        # Identify level of tabbing for any statements after the class
                        tab_level2 = 0
                        for j in range(i+1, len(lines)):
                            # If there is text, then set the tab level
                            if len(lines[j].strip()) > 0:
                                tab_level2 = count_spaces_at_beginning(lines[j])
                                break
                        # Locate functions and classes within the class, if their tab level is equal to tab_level2
                        # Once the tab level is less than tab_level2, then we know we have reached the end of the class

                        identified_functions_or_classes = False
                        for j in range(i+1, len(lines)):
                            if count_spaces_at_beginning(lines[j]) == tab_level2:
                                if lines[j].strip().startswith("def ") or lines[j].strip().startswith("class "):
                                    identified_functions_or_classes = True
                                    break
                            if count_spaces_at_beginning(lines[j]) < tab_level2:
                                # if not empty
                                if len(lines[j].strip()) > 0:
                                    break

                        if identified_functions_or_classes:
                            file2.write(f"\n <details>\n<summary>\n\n#### Functions and Classes\n\n</summary>\n\n")
                            for j in range(i+1, len(lines)):
                                if count_spaces_at_beginning(lines[j]) == tab_level2:
                                    if lines[j].strip().startswith("def "):
                                        name2 = get_function_name(lines[j])
                                        docs = document_data(j, name2, lines[j], docs, parent_string=name+".", obj_type="function", spaces=spaces + " " + spaces.split(" ")[0] + " ")
                                    elif lines[j].strip().startswith("class "):
                                        name2 = get_class_name(lines[j])
                                        docs = document_data(j, name2, lines[j], docs, parent_string=name+".", obj_type="class", spaces=spaces + " " + spaces.split(" ")[0] + " ")
                                if count_spaces_at_beginning(lines[j]) < tab_level2:
                                    # if not empty
                                    if len(lines[j].strip()) > 0:
                                        break
                            file2.write(f"</details>\n\n")

                        docs += "</details>\n\n"
                        return docs

                    found = False
                    other_docs = ""
                    for i, line in enumerate(lines):
                        # If we find a class definition
                        if line.startswith("class"):
                            found = True
                            name = get_class_name(line)
                            other_docs = document_data(i, name, line, other_docs, obj_type="class")
                        # If we find a function definition
                        elif line.startswith("def"):
                            found = True
                            name = get_function_name(line)
                            other_docs = document_data(i, name, line, other_docs, obj_type="function")
                    if found:
                        # Provide link to md file
                        documentation += f"\n<details>\n<summary>\n\n## Documentation For [{file_path}](/{file_document_path})\n\n</summary>\n\n{other_docs}<br></details>\n\n"
                    file2.close()

    with open(info.data["docs_folder"] + "/DOCS.md", "w") as f:
        # Add the capability to go back to README.md
        f.write(f"[Back to README.md](/README.md)\n\n")
        f.write("# DOCUMENTATION TABLE OF CONTENTS #\n\n")
        f.write(f"This is the documentation for the project {info.data['project_name']}.\n\n")
        f.write(documentation)

keys = info.data.keys()
for key in keys:
    search_item = "<" + key + ">"
    if search_item in output:
        # Replace with the value
        output = output.replace(search_item, info.data[key])
# Remove blank lines from output
output = "\n".join([s for s in output.splitlines() if s.strip() != ""])
# Color the lines (like === and ---) and numbers like 1. 2. 3. etc. red
output = re.sub(r"^(=+)$", r"\033[91m\1\033[0m", output, flags=re.MULTILINE)

print(output)
