"""Code to run after generating the project."""

import os
import shutil

REMOVE_PATHS = [
    '{% if cookiecutter.license == "No" %} LICENSE {% endif %}',
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

print("** PROJECT CREATION COMPLETE **\n")
print("Next steps:")
print("Add {{cookiecutter.project_name}} to {{cookiecutter.github_or_gitlab}}")