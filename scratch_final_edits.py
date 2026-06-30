import os
import re

talent_path = 'c:/Users/inanj/OneDrive/Documents/GitHub/f9xr.github.io/services/talent-brand-management.html'
pr_path = 'c:/Users/inanj/OneDrive/Documents/GitHub/f9xr.github.io/announcements/f9xr-sponsorlanes-partnership.html'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Authoritative Sources block
    auth_source_pattern = re.compile(r'<div class="mb-12">\s*<h3 class="text-4xl.*?Authoritative.*?Sources\..*?</p>\s*</div>', re.DOTALL)
    content = auth_source_pattern.sub('', content)

    # In case the pattern didn't match perfectly, let's also do a fallback exact substring removal if found
    auth_header_idx = content.find('>Authoritative <span')
    if auth_header_idx != -1:
        start_div = content.rfind('<div', 0, auth_header_idx)
        end_div = content.find('</div>', auth_header_idx) + 6
        content = content[:start_div] + content[end_div:]

    # 2. Replace URLs
    content = content.replace('http://lepem.xyz', 'http://sponsorlanes.lepem.xyz')
    content = content.replace('lepem.xyz', 'sponsorlanes.lepem.xyz')

    return content

# --- Process Talent Page ---
talent_content = process_file(talent_path)

# Move banner to the top
banner_start = talent_content.find('<!-- Partnership Announcement Banner -->')
if banner_start != -1:
    banner_end = talent_content.find('</a>', banner_start) + 4
    banner_html = talent_content[banner_start:banner_end]
    talent_content = talent_content[:banner_start] + talent_content[banner_end:]
    
    # Restyle the banner to sit perfectly at the absolute top of the page
    new_banner_html = '''
    <!-- Partnership Announcement Banner -->
    <a href="../announcements/f9xr-sponsorlanes-partnership.html" class="block w-full bg-gradient-to-r from-accent-blue/90 via-purple-600/90 to-accent-blue/90 text-center py-2 z-[6000] relative hover:opacity-90 transition-all group">
        <span class="text-white font-bold text-xs md:text-sm uppercase tracking-widest flex items-center justify-center gap-2">
            <i class="fa-solid fa-rocket animate-bounce mt-1"></i> 
            BREAKING: F9XR Team & SponsorLanes Agency announce official partnership. Read Press Release 
            <i class="fa-solid fa-arrow-right group-hover:translate-x-1 transition-transform"></i>
        </span>
    </a>
'''
    # Insert right after <body>
    body_idx = talent_content.find('<body')
    if body_idx != -1:
        insert_idx = talent_content.find('>', body_idx) + 1
        talent_content = talent_content[:insert_idx] + new_banner_html + talent_content[insert_idx:]

# Link contact page
talent_content = talent_content.replace('href="#contact"', 'href="../pages/contact.html"')
talent_content = talent_content.replace('href="#solutions"', 'href="#solutions"')

with open(talent_path, 'w', encoding='utf-8') as f:
    f.write(talent_content)

# --- Process PR Page ---
pr_content = process_file(pr_path)

# Interlink AKM
pr_content = pr_content.replace('AKM, Lead Digital Architect', '<a href="https://inakm.github.io" target="_blank" class="text-white underline hover:text-accent-blue transition-colors">AKM</a>, Lead Digital Architect')
pr_content = pr_content.replace('AKM', '<a href="https://inakm.github.io" target="_blank" class="text-white underline hover:text-accent-blue transition-colors">AKM</a>')
# Fix double replacements if they occurred
pr_content = pr_content.replace('<a href="https://inakm.github.io" target="_blank" class="text-white underline hover:text-accent-blue transition-colors"><a href="https://inakm.github.io" target="_blank" class="text-white underline hover:text-accent-blue transition-colors">AKM</a></a>', '<a href="https://inakm.github.io" target="_blank" class="text-white underline hover:text-accent-blue transition-colors">AKM</a>')

# Add Image
image_html = '''
    <div class="mb-12 rounded-3xl overflow-hidden border border-white/10 shadow-[0_0_40px_rgba(59,130,246,0.15)] reveal">
        <img src="https://images.unsplash.com/photo-1521791136064-7986c2920216?q=80&w=2069&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="F9XR and SponsorLanes Partnership" class="w-full h-[400px] object-cover hover:scale-105 transition-transform duration-700">
    </div>
'''
# Insert image after the immediate release header but before the prose article
article_idx = pr_content.find('<article')
if article_idx != -1:
    pr_content = pr_content[:article_idx] + image_html + pr_content[article_idx:]

with open(pr_path, 'w', encoding='utf-8') as f:
    f.write(pr_content)

print("Updates completed successfully.")
