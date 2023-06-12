"""Code to run before generating the project."""

import re
import sys

# Cancel the project generation if the provided project_name doesn't match the regular expression.
MODULE_REGEX = re.compile(r'^[_a-zA-Z][_a-zA-Z0-9\- ]+$')
project_name = '{{ cookiecutter.project_name }}'

if not MODULE_REGEX.match(project_name):
    print(
        f"ERROR: {project_name} is not a valid project name.\n\nThe project name must start with a letter or underscore and not contain any special characters except '_' or '-'. Try again with a valid project name.\n"
    )
    # Exit to cancel project
    sys.exit(1)