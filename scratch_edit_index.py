import re

with open('services/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make canonical links point to services/index.html
content = re.sub(r'<link rel="canonical" href="https://f9xr.github.io/pages/services.html">', '<link rel="canonical" href="https://f9xr.github.io/services/index.html">', content)
content = re.sub(r'<meta property="og:url" content="https://f9xr.github.io/pages/services.html">', '<meta property="og:url" content="https://f9xr.github.io/services/index.html">', content)
content = re.sub(r'<meta name="twitter:url" content="https://f9xr.github.io/pages/services.html">', '<meta name="twitter:url" content="https://f9xr.github.io/services/index.html">', content)

# Change links from /services/ai-visibility-optimization.html to ai-visibility-optimization.html since we are in the same folder now?
# Wait, it's better to keep absolute paths starting with / if they exist, to avoid breaking links. The site uses absolute /services/ link formats. Let's leave them.

# I need to insert a new card for 'We Do For You' into the service grid.
# The grid starts after '<!-- Services Grid -->' or similar.
# Let's just find the closing tag of the last service card and inject the new one.
# It seems there are multiple <div class="service-card...
new_card = '''<!-- We Do For You -->
                <div class="service-card rounded-3xl p-8 relative overflow-hidden group">
                    <div class="absolute inset-0 bg-gradient-to-br from-accent-blue/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                    <div class="relative z-10 flex flex-col h-full">
                        <div class="w-16 h-16 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-500">
                            <i class="fa-solid fa-rocket text-accent-blue text-2xl"></i>
                        </div>
                        <h3 class="text-2xl font-black mb-3 text-white italic tracking-tight">Bulk Submissions</h3>
                        <p class="text-platinum/60 font-medium leading-relaxed mb-8 flex-grow">
                            We manually submit your startup or product to 100+ high-value directories. Get backlinks, traffic, and early users effortlessly.
                        </p>
                        <ul class="space-y-3 mb-8">
                            <li class="flex items-center gap-3 text-sm text-platinum/80"><i class="fa-solid fa-check text-accent-blue"></i> Manual Submissions</li>
                            <li class="flex items-center gap-3 text-sm text-platinum/80"><i class="fa-solid fa-check text-accent-blue"></i> High Quality Backlinks</li>
                            <li class="flex items-center gap-3 text-sm text-platinum/80"><i class="fa-solid fa-check text-accent-blue"></i> Save Hundreds of Hours</li>
                        </ul>
                        <a href="/services/we-do-for-you.html" class="inline-flex items-center justify-between w-full p-4 rounded-xl bg-white/5 hover:bg-accent-blue text-white font-bold transition-all group/btn mt-auto">
                            <span>Explore Service</span>
                            <i class="fa-solid fa-arrow-right group-hover/btn:translate-x-2 transition-transform"></i>
                        </a>
                    </div>
                </div>'''

# Insert it before the grid's closing div. We can use a regex to find the place, but let's append it right after the discord bot development card.
discord_card = r'<h3 class="text-2xl font-black mb-3 text-white italic tracking-tight">Discord Bot Dev.*?</a>\s*</div>\s*</div>'
content = re.sub(discord_card, lambda m: m.group(0) + '\n' + new_card, content, flags=re.DOTALL)

with open('services/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("services/index.html updated successfully.")
