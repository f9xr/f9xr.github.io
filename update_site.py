import os
import re

base_dir = r"c:\Users\inanj\OneDrive\Documents\GitHub\f9xr.github.io"

# 1. Get header and footer from index.html
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    index_html = f.read()

header_match = re.search(r'(<header id="main-header".*?</header>)', index_html, re.DOTALL)
footer_match = re.search(r'(<footer.*?</footer>)', index_html, re.DOTALL)

if not header_match or not footer_match:
    print("Could not find header or footer in index.html")
    exit(1)

header_html = header_match.group(1)
footer_html = footer_match.group(1)

# Fix paths in header to be root-relative
header_html = header_html.replace('href="./', 'href="/')
header_html = header_html.replace('href="pages/', 'href="/pages/')
header_html = header_html.replace('href="services/', 'href="/services/')
header_html = header_html.replace('href="legals/', 'href="/legals/')
header_html = header_html.replace('src="./', 'src="/')
header_html = header_html.replace('src="assets/', 'src="/assets/')

# Fix paths in footer
footer_html = footer_html.replace('href="./', 'href="/')
footer_html = footer_html.replace('href="pages/', 'href="/pages/')
footer_html = footer_html.replace('href="services/', 'href="/services/')
footer_html = footer_html.replace('href="legals/', 'href="/legals/')
footer_html = footer_html.replace('src="./', 'src="/')
footer_html = footer_html.replace('src="assets/', 'src="/assets/')

# 2. Find all HTML files
html_files = []
for root, dirs, files in os.walk(base_dir):
    # Fix the directory skip logic
    if "\\.git" in root or "\\node_modules" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

# 3. Process each HTML file
updated_count = 0
for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    original_content = content
    
    # Remove skel-overlay
    content = re.sub(r'[ \t]*<div\s+id="skel-overlay"[\s\S]*?Loading\.\.\.</div>\s*</div>\s*</div>\n?', '', content)
    
    # Replace header safely using lambda
    content = re.sub(r'<header id="main-header".*?</header>', lambda m: header_html, content, flags=re.DOTALL)
    
    # Replace footer safely using lambda
    content = re.sub(r'<footer.*?</footer>', lambda m: footer_html, content, flags=re.DOTALL)
    
    if content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        updated_count += 1
        print(f"Updated {file_path}")

print(f"\nSuccessfully updated {updated_count} HTML files.")
