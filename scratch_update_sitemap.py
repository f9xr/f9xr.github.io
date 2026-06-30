import os
import re

filepath = 'c:/Users/inanj/OneDrive/Documents/GitHub/f9xr.github.io/pages/sitemap.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_sitemap_link1 = '<li><a href="../services/talent-brand-management.html" class="block p-4 bg-white/5 border border-white/5 rounded-2xl hover:bg-white/10 transition-all hover-card font-bold"><i class="fas fa-star mr-3 text-yellow-500"></i> Talent & Brand Management</a></li>'

if 'talent-brand-management.html' not in content:
    content = content.replace(
        '<li><a href="../services/we-do-for-you.html"',
        new_sitemap_link1 + '\\n                          <li><a href="../services/we-do-for-you.html"'
    )
    
    new_sitemap_link2 = '<a href="/services/talent-brand-management.html" class="flex items-center text-2xl lg:text-[28px] font-bold text-white hover:text-accent-blue transition-colors tracking-tight"><i class="fa-solid fa-star text-accent-blue/50 mr-3 text-xl w-6 text-center"></i>Talent Management</a>'
    
    content = content.replace(
        '<a href="/services/telegram-bot-development.html"',
        new_sitemap_link2 + '\\n                        <a href="/services/telegram-bot-development.html"'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated sitemap.html successfully!")
else:
    print("sitemap.html already contains the entry.")
