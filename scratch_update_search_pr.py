import os
import re

filepath = 'c:/Users/inanj/OneDrive/Documents/GitHub/f9xr.github.io/assets/js/search-index.js'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_entry = '  {"title": "Partnership Announcement | F9XR Team x SponsorLanes Agency", "path": "announcements/f9xr-sponsorlanes-partnership.html"}'

if 'f9xr-sponsorlanes-partnership.html' not in content:
    content = content.replace('];', f',\\n{new_entry}\\n];')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated search-index.js successfully!")
else:
    print("search-index.js already contains the entry.")
