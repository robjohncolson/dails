import os
import re

def get_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        # If UTF-8 fails, try reading as binary
        with open(file_path, 'rb') as file:
            return file.read().decode('utf-8', errors='ignore')

def update_readme(readme_content, codebase):
    # Update script links and descriptions
    for file, content in codebase.items():
        if file.endswith(('.sh', '.py')):
            script_name = os.path.basename(file)
            script_type = script_name.split('.')[0]
            
            # Extract description from the script content
            description = re.search(r'#\s*(.*)', content)
            description = description.group(1) if description else "No description available"
            
            # Create or update the link in README
            link_pattern = rf'\*\s*{script_type}:.*'
            new_link = f'* {script_type}: [{description}](https://github.com/robjohncolson/dails/blob/main/{script_name})'
            
            if re.search(link_pattern, readme_content, re.MULTILINE):
                readme_content = re.sub(link_pattern, new_link, readme_content, flags=re.MULTILINE)
            else:
                # If the link doesn't exist, add it to the end of the file
                readme_content += f'\n{new_link}'

    return readme_content

# ... rest of the code remains the same ...

def main():
    codebase = {}
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith(('.sh', '.py')):
                file_path = os.path.join(root, file)
                codebase[file_path] = get_file_content(file_path)

    readme_path = 'README.md'
    readme_content = get_file_content(readme_path)
    
    updated_readme = update_readme(readme_content, codebase)
    
    with open(readme_path, 'w') as file:
        file.write(updated_readme)
    
    print(f"README.md has been updated based on the current codebase.")

if __name__ == "__main__":
    main()