[Back to DOCS.md](DOCS.md)



## 0. HOW TO USE THIS TEMPLATE ##


### 1. Git Clone this repository (project_name is the name of the project you want to create): ###

    git clone https://github.com/ConnorAtmos/OpenVR_Simple_Tracking <project_name>


### 2. CD into the project directory and remove the git repository: ###

    cd <project_name> && rm -rf .git


### 3. Run structure_builder.py for next steps: ###

    python3 structure_builder.py


You should then modify info.py. This file contains all the information about your project.




## 1. HOW TO INSTALL ANACONDA ##


Conda is a package manager for python. It is used to install python packages and conda packages.


### 1. CD into the home directory: ###

    cd ~


### 2. Run the following command to download the conda installer: ###


    wget [conda_install_link]


    wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh


### 3. Run the following command to install conda: ###


    bash [conda_file]


    bash Anaconda3-2022.05-Linux-x86_64.sh


### 4. Run the following command to update conda: ###

    conda update conda


### 5. Run the following command to install conda-forge: ###

    conda config --add channels conda-forge






## 2. HOW TO CREATE CONDA ENVIRONMENT ##


This is for creating a new conda environment.


### 1. Run the following command to create a new conda environment: ###

    conda create --name [project_name]


    conda create --name OpenVR_Simple_Tracking


### 2. Reload the bashrc file: ###

    source ~/.bashrc






## 4. HOW TO INSTALL REQUIREMENTS ##


This is for installing python packages and conda packages.


### 1. CD into the project directory: ###

    cd [project_dir]


    cd C:\Users\connorw\PycharmProjects\pythonProject1


### 2. Activate the conda environment: ###

    conda activate [project_name]


    conda activate OpenVR_Simple_Tracking


### 3. Install the following requirements: ###


    pip install -r [requirements_file] && conda install --file [conda_requirements_file]  && conda install -c conda-forge --file [conda_forge_requirements_file]


    pip install -r C:\Users\connorw\PycharmProjects\pythonProject1/requirements/requirements.txt && conda install --file C:\Users\connorw\PycharmProjects\pythonProject1/requirements/conda_requirements.txt  && conda install -c conda-forge --file C:\Users\connorw\PycharmProjects\pythonProject1/requirements/conda_forge_requirements.txt


### 4. Install the following apt-get requirements: ###

    [No apt-get requirements]






## A. HOW TO REMOVE CONDA ENVIRONMENT ##


This is for removing the conda environment.


### 1. Run the following command to remove the conda environment: ###

    conda env remove --name [project_name]


    conda env remove --name OpenVR_Simple_Tracking


### 2. Reload the bashrc file: ###

    source ~/.bashrc




