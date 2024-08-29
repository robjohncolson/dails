import os
import re
import html2text


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
            
            # Extract description from the script content
            description = re.search(r'#\s*(.*)', content)
            description = description.group(1) if description else "No description available"
            
            # Create or update the link in README
            new_link = f"* [{script_name}](https://github.com/robjohncolson/dails/blob/main/{script_name}): {description}\n"
            
            # Check if the file is already mentioned in the README
            if script_name in readme_content:
                # Replace the existing line
                readme_content = re.sub(f".*{re.escape(script_name)}.*\n", new_link, readme_content)
            else:
                # Add the new link to the end of the file
                readme_content += new_link

    return readme_content

# ... rest of the code remains the same ...

def main():
    codebase = {}
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(('.sh', '.py')):
                file_path = os.path.join(root, file)
                codebase[file_path] = get_file_content(file_path)

    readme_path = 'README.md'
    readme_content = get_file_content(readme_path)
    
    # Convert HTML to Markdown
    h = html2text.HTML2Text()
    h.ignore_links = False
    markdown_content = h.handle(readme_content)
    
    updated_readme = update_readme(markdown_content, codebase)
    
    with open(readme_path, 'w') as file:
        file.write(updated_readme)
    
    print(f"README.md has been updated based on the current codebase.")

if __name__ == "__main__":
    main()