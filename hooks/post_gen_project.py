"""Code to run after generating the project."""

import os
import shutil
import json

def remove_files():
    REMOVE_PATHS = [
        '{% if cookiecutter.license == "No" %} LICENSE {% endif %}',
        '{% if cookiecutter.inverse_mappings == "No" %} config/inverse_predicate_map.yml {% endif %}',
        '{% if cookiecutter.github_or_gitlab == "github" %} .gitlab-ci.yml {% endif %}',
        '{% if cookiecutter.github_or_gitlab == "gitlab" %} .github {% endif %}',
    ]

    for path in REMOVE_PATHS:
        path = path.strip()
        if path and os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.unlink(path)


def create_or_update_cruft_file():
    project_cruft_file = "config/project-cruft.json"

    # Check if project-cruft.json already exists
    if os.path.exists(project_cruft_file):
        # Load the existing data from project-cruft.json
        with open(project_cruft_file, "r") as file:
            project_cruft_data = json.load(file)
    else:
        project_cruft_data = {"context": {"cookiecutter": {}}}

    # Get the values from the cookiecutter variables
    template_data = {"project_name": "{{cookiecutter.project_name}}",
                    "project_description": "{{cookiecutter.project_description}}",
                    "github_or_gitlab": "{{cookiecutter.github_or_gitlab}}",
                    "git_org": "{{cookiecutter.git_org}}",
                    "full_name": "{{cookiecutter.full_name}}",
                    "email": "{{cookiecutter.email}}",
                    "license": "{{cookiecutter.license}}",
                    "inverse_mappings": "{{cookiecutter.inverse_mappings}}"
                }
    
    # Update project-cruft.json with variables from cookiecutter.json
    for key, value in template_data.items():
        # Exclude variables that start with "_"
        if not key.startswith("_"):
            project_cruft_data["context"]["cookiecutter"][key] = value

    # Remove variables from project-cruft.json that are not present in cookiecutter.json
    for key in list(project_cruft_data["context"]["cookiecutter"].keys()):
        if key not in template_data:
            project_cruft_data["context"]["cookiecutter"].pop(key)
            
    # Write the updated data to project-cruft.json
    with open(project_cruft_file, "w") as file:
        json.dump(project_cruft_data, file, indent=2)


def print_next_steps(update_run):
    if update_run:
        print("\n** PROJECT UPDATE COMPLETE **\n")
    else:
        print("** PROJECT CREATION COMPLETE **")
        print("Next steps:")

        if "{{cookiecutter.github_or_gitlab}}" == "github":
            print("1. Go to https://github.com/new and follow the instructions. \
                        Be sure to set 'Owner' = '{{cookiecutter.git_org}}' and 'Repository name' = '{{cookiecutter.project_name}}'. \
                        Also, do NOT add a README or .gitignore file (this cookiecutter template will take care of this for you).")
            print("2. Setup the project for git:")
            print("    cd {{cookiecutter.project_name}}")
            print("    git init")
            print("    git add .")
            print("    git commit -m 'Initial commit' -a")
            print("3. Add the remote to your local git repository:")
            print("    git remote add origin https://github.com/{{cookiecutter.git_org}}/{{cookiecutter.project_name}}.git")
            print("    git branch -M main")
            print("    git push -u origin main\n")

        if "{{cookiecutter.github_or_gitlab}}" == "gitlab":
            print("1. Go to https://gitlab.com/projects/new#blank_project and follow the instructions. \
                        Be sure to set 'Project URL' = '{{cookiecutter.git_org}}' and 'Project name' = '{{cookiecutter.project_name}}'. \
                        Also, do NOT add a README file (this cookiecutter template will take care of this for you).")
            print("2. Follow the instructions to 'Push an existing folder':")
            print("    cd {{cookiecutter.project_name}}")
            print("    git init --initial-branch=main")
            print("    git remote add origin https://gitlab.com/{{cookiecutter.git_org}}/{{cookiecutter.project_name}}.git")
            print("    git add .")
            print('    git commit -m "Initial commit"')
            print("    git push -set-upstream origin main\n")


def main():
    remove_files()

    # Check if the config/project-cruft.json file exists as a way of determining if this was a project creation or an update.
    update_run = False
    # Check if project-cruft.json already exists
    if os.path.exists("config/project-cruft.json"):
        update_run = True

    create_or_update_cruft_file()
    print_next_steps(update_run)


if __name__ == "__main__":
    main()