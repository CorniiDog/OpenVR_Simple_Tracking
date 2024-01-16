import os

# This is the data that is used throughout the project.

data = {
    "conda_install_link": "https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh",
    "path_to_services": "/etc/systemd/system",
    "project_dir": os.path.dirname(os.path.realpath(__file__)),
    "home_dir": os.path.expanduser("~"),
    "docs_folder_dir": "docs",
    "Ubuntu_Username": "connor",
    "github_image": "https://avatars.githubusercontent.com/u/69062901?v=4",
    "github_name": "ConnorAtmos",
    "linked_in_url": "https://www.linkedin.com/in/connor-white-38a5501a0/",
    "path_to_logo": "/storage/logo.png",
    "email": "connor.sw.personal@gmail.com",
    "full_name": "Connor White",
}

data["about"] = """
# OpenVR Simple Tracking
OPENVR Steam Position Tracking in Python that retreives X Y and Z position and rotation

Open the project in VSCode or some python IDE, while running SteamVR.

Install requirements...
```angular2html
pip install -r requirements.txt
```
Afterwards, open main.py and modify settings to how you see fit, then run main.py with
```angular2html
python main.py
```
When you are done recording, press [Enter] in the command line to automatically save and/or replay what was recorded.

This can track the VR headset, base stations, controllers, and trackers. Modify however you see fit, I don't care lol.
"""

data["project_name"] = "OpenVR_Simple_Tracking"
data["project_link"] = f"https://github.com/{data['github_name']}/{data['project_name']}"
data["github_url"] = f"https://github.com/{data['github_name']}"
data["path_to_conda_python"] = f"{data['home_dir']}/anaconda3/envs/{data['project_name']}/bin/python3"
data["file_to_run"] = f"{data['project_dir']}/main.py"
data["requirements_folder"] = f"{data['project_dir']}/requirements"
data["storage_folder"] = f"{data['project_dir']}/storage"
data["toolbox_folder"] = f"{data['project_dir']}/toolbox"
data["requirements_file"] = f"{data['requirements_folder']}/requirements.txt"
data["conda_requirements_file"] = f"{data['requirements_folder']}/conda_requirements.txt"
data["conda_forge_requirements_file"] = f"{data['requirements_folder']}/conda_forge_requirements.txt"
data["docs_folder"] = f"{data['project_dir']}/{data['docs_folder_dir']}"
data["service_name"] = f"{data['project_name']}.service"
data["service_path"] = f"{data['storage_folder']}/{data['service_name']}"
data["service_moved_path"] = f"{data['path_to_services']}/{data['service_name']}"
data["conda_file"] = data["conda_install_link"].split("/")[-1]

# This is for service file, located in storage. It is moved to /etc/systemd/system to allow
# This script to automatically run on startup
data["service_information"] = f"""
[Unit]
Description={data["project_name"]}
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User={data["Ubuntu_Username"]}
ExecStart={data["path_to_conda_python"]} {data["file_to_run"]}
WorkingDirectory={data["project_dir"]}
Restart=always
RestartSec=120

[Install]
WantedBy=multi-user.target
"""

# This is for the apt-get requirements, located in requirements/apt_get_requirements.txt
apt_get_str = ""
with open("requirements/apt_get_requirements.txt", "r") as f:
    for line in f:
        apt_get_str += line.strip() + " "
if len(apt_get_str) > 0:
    apt_get_str = "sudo apt-get install -y " + apt_get_str
else:
    apt_get_str = "[No apt-get requirements]"

data["apt_get_str"] = apt_get_str
