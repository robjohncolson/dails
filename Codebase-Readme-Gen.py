import os
import re

def get_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

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
            link_pattern = rf'<li>{script_type}:.*?</li>'
            new_link = f'<li>{script_type}: <a href="https://github.com/robjohncolson/dails/blob/main/{script_name}">{description}</a></li>'
            
            if re.search(link_pattern, readme_content):
                readme_content = re.sub(link_pattern, new_link, readme_content)
            else:
                # If the link doesn't exist, add it to the appropriate section
                section_pattern = rf'<ul>\s*<li>{script_type[0]}.*?</ul>'
                section_match = re.search(section_pattern, readme_content, re.DOTALL)
                if section_match:
                    section = section_match.group(0)
                    updated_section = section.replace('</ul>', f'    {new_link}\n</ul>')
                    readme_content = readme_content.replace(section, updated_section)

    return readme_content

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