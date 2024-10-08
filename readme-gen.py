import os
import re
import html2text

def update_readme(markdown_content, codebase):
    # Example: Add a list of all Python and Shell scripts to the README.md
    script_list = "\n\n## Script List\n"
    for file_path in sorted(codebase.keys()):
        script_list += f"- `{file_path}`\n"
    
    # Append the script list to the existing README content
    updated_content = markdown_content + script_list
    return updated_content


def is_user_created_file(file_path):
    # Add logic here to determine if a file is user-created
    # For example, you might check if it's in a specific directory or has a certain naming convention
    # For now, we'll assume all non-hidden files in non-hidden directories are user-created
    return not any(part.startswith('.') for part in file_path.split(os.sep))

def get_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    readme_path = 'README.md'
    readme_content = get_file_content(readme_path)
    codebase = {}
    for root, dirs, files in os.walk('.'):
        # Exclude hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith(('.sh', '.py')):
                file_path = os.path.join(root, file)
                if is_user_created_file(file_path):
                    codebase[file_path] = get_file_content(file_path)

    readme_path = 'README.md'
    readme_content = get_file_content(readme_path)
    
    h = html2text.HTML2Text()
    h.ignore_links = False
    markdown_content = h.handle(readme_content)
    
    updated_content = update_readme(markdown_content, codebase)
    
    with open(readme_path, 'w') as file:
        file.write(updated_content)

if __name__ == "__main__":
    main()