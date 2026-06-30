import os
import re

filepath = 'c:/Users/inanj/OneDrive/Documents/GitHub/f9xr.github.io/assets/js/search-index.js'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_entry = '  {"title": "Talent & Brand Management | Creator Scaling | F9XR x SponsorLanes", "path": "services/talent-brand-management.html"}'

if 'talent-brand-management.html' not in content:
    # Find the last closing bracket of the array and insert the new entry
    content = content.replace('];', f',\\n{new_entry}\\n];')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated search-index.js successfully!")
else:
    print("search-index.js already contains the entry.")
