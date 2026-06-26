import re

with open('services/we-do-for-you.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the new bullet point
new_bullet = '''<li class="flex items-center gap-3 text-sm text-platinum/80"><i class="fa-solid fa-check text-accent-blue"></i> We also submit your website to 100s of Search Engines for you too.</li>'''

# Insert it in the feature section. Let's just find "Save Hundreds of Hours" and add a new card, or add it to the hero description.
# The user asked: "we also submit your website to 100s of Search Engines for you too"
# Let's add it to the hero paragraph.
search_str = "We manually submit your product to all top directories, so you don't have to."
replace_str = "We manually submit your product to all top directories, and we also submit your website to 100s of Search Engines for you too, so you don't have to."

content = content.replace(search_str, replace_str)

with open('services/we-do-for-you.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated we-do-for-you.html")
