import re

with open('directories/product-launch-directories.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to add a banner linking to our new service.
banner_html = '''
        <!-- We Do For You Banner -->
        <section class="mb-16 mt-8 reveal">
            <div class="bg-gunmetal border border-accent-blue/30 p-8 md:p-12 rounded-[2.5rem] shadow-[0_0_40px_rgba(59,130,246,0.15)] relative overflow-hidden group">
                <div class="absolute inset-0 bg-gradient-to-br from-accent-blue/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="relative z-10 flex flex-col md:flex-row items-center justify-between gap-8">
                    <div>
                        <span class="text-accent-blue font-black uppercase tracking-[0.4em] text-xs mb-4 block"><i class="fa-solid fa-rocket mr-2"></i> Tired of Manual Submissions?</span>
                        <h2 class="text-3xl md:text-5xl font-black text-white italic tracking-tighter mb-4">We Do For <span class="text-stroke-sm">You.</span></h2>
                        <p class="text-platinum/80 text-lg leading-relaxed max-w-2xl font-medium">
                            Don't waste hundreds of hours manually submitting your product to these directories. Our team handles the heavy lifting, ensuring high-quality backlinks and traffic so you can focus on building your startup.
                        </p>
                    </div>
                    <a href="/services/we-do-for-you.html" class="shrink-0 bg-accent-blue text-white px-8 py-5 rounded-full font-black text-lg uppercase tracking-wider hover:bg-blue-500 hover:scale-105 transition-all shadow-[0_0_30px_rgba(59,130,246,0.4)] flex items-center gap-3">
                        View Service
                        <i class="fa-solid fa-arrow-right-long group-hover:translate-x-1 transition-transform"></i>
                    </a>
                </div>
            </div>
        </section>
'''

# Find a good place to insert this banner. Right after the hero section (before the list of directories).
# The list starts somewhere after the first <section> or <main>. Let's insert it right after the closing tag of the first <section> inside <main>.
content = re.sub(r'(<main id="main-content"[^>]*>.*?</section>)', lambda m: m.group(1) + banner_html, content, count=1, flags=re.DOTALL)

with open('directories/product-launch-directories.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("directories/product-launch-directories.html updated successfully.")
