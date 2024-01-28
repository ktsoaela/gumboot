# gumboot/cli.py
import argparse
import os
import sys
import subprocess
import pkg_resources
from shutil import copytree, rmtree

def create_project(project_name, frontend_framework):
    # Get the path to the templates directory inside the package
    template_dir = pkg_resources.resource_filename('gumboot', f'templates/{frontend_framework}')

    # Copy the template to the new project
    copytree(template_dir, project_name)

    print(f"Project {project_name} created with {frontend_framework} frontend.")

    # Change to the project directory
    os.chdir(project_name)

    # Install frontend dependencies
    subprocess.run(["npm", "install"], check=True, cwd="frontend")

    # Run Vue.js development server and Django development server concurrently
    subprocess.Popen(["npm", "run", "serve"], cwd="frontend")
    subprocess.Popen(["python", "manage.py", "runserver"], cwd="backend")

def main():
    parser = argparse.ArgumentParser(description='Gumboot: Frontend Manager for Django')
    parser.add_argument('project_name', type=str, help='Name of the Django project')
    parser.add_argument('--frontend', choices=['vuejs'], default='vuejs',
                        help='Choose the frontend framework (default: vuejs)')

    args = parser.parse_args()

    # Check if the project name already exists
    if os.path.exists(args.project_name):
        print(f"Error: Project {args.project_name} already exists.")
        sys.exit(1)

    create_project(args.project_name, args.frontend)

if __name__ == "__main__":
    main()