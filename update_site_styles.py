import os
import re

# Define files to exclude
EXCLUDE_FILES = {'index.html', '.git', 'assets'}

# Updated Footer Content (Exact from index.html with bg-[#212529])
NEW_FOOTER = """<footer class="bg-[#212529] pt-20 no-print overflow-hidden">
        <!-- ========================================
         SECTION 13: FOOTER
         ======================================== -->

        <!-- 1. Top Marquee Ticker (Brand Identity) -->
        <div class="bg-accent-blue py-4 border-y border-white/10 overflow-hidden select-none mb-20">
            <div class="flex whitespace-nowrap animate-marquee">
                <div
                    class="flex items-center gap-10 px-4 text-carbon-black font-black uppercase tracking-[0.3em] text-xs md:text-sm italic">
                    <span>Amazing Design</span> <i class="fas fa-asterisk text-[10px]"></i>
                    <span>AI-Powered Solutions</span> <i class="fas fa-asterisk text-[10px]"></i>
                    <span>Brand Growth</span> <i class="fas fa-asterisk text-[10px]"></i>
                    <span>High Performance SEO</span> <i class="fas fa-asterisk text-[10px]"></i>
                    <span>Modern Architectures</span> <i class="fas fa-asterisk text-[10px]"></i>
                    <!-- Repeated for infinite scroll -->
                    <span>Amazing Design</span> <i class="fas fa-asterisk text-[10px]"></i>
                    <span>AI-Powered Solutions</span> <i class="fas fa-asterisk text-[10px]"></i>
                    <span>Brand Growth</span> <i class="fas fa-asterisk text-[10px]"></i>
                    <span>High Performance SEO</span> <i class="fas fa-asterisk text-[10px]"></i>
                    <span>Modern Architectures</span> <i class="fas fa-asterisk text-[10px]"></i>
                </div>
            </div>
        </div>

        <div class="max-w-7xl mx-auto px-6">

            <!-- 2. Large CTA Header (Reference Image Style) -->
            <div
                class="flex flex-col md:flex-row justify-between items-center pb-16 mb-16 border-b border-white/5 gap-8 reveal">
                <div class="text-center md:text-left">
                    <h2 class="text-5xl md:text-8xl font-black tracking-tighter italic uppercase leading-none">
                        Let's Build <br class="hidden md:block"> <span class="text-stroke text-transparent"
                            style="-webkit-text-stroke: 1px #f8f9fa;">Something Great.</span>
                    </h2>
                </div>
                <a href="/contact.html"
                    class="group bg-accent-blue text-white px-10 py-5 rounded-full font-black text-xl hover:scale-110 active:scale-95 transition-all shadow-[0_20px_50px_rgba(59,130,246,0.3)] flex items-center gap-4">
                    Hire Team <i
                        class="fa-solid fa-arrow-right-long transition-transform group-hover:translate-x-2"></i>
                </a>
            </div>

            <!-- 3. Main Navigation Grid -->
            <div class="grid grid-cols-2 md:grid-cols-2 lg:grid-cols-5 gap-12 mb-24">

                <!-- Branding & Github -->
                <div class="col-span-2 space-y-8">
                    <div>
                        <h3 class="text-4xl font-black mb-4 tracking-tighter italic uppercase">F9XR TEAM.</h3>
                        <p class="text-lg text-platinum/50 leading-relaxed max-w-sm">
                            Global digital studio crafting high-end experiences for growth-focused brands.
                        </p>
                    </div>
                    <div class="flex flex-wrap gap-4">
                        <a href="https://github.com/f9xr/f9xr.github.io" target="_blank"
                            class="bg-white/5 px-5 py-2.5 rounded-xl border border-white/5 font-bold hover:bg-white/10 transition-colors flex items-center gap-3 text-xs uppercase tracking-widest">
                            <i class="fab fa-github"></i> View Open Source
                        </a>
                    </div>
                </div>

                <!-- Page Navigation -->
                <div class="space-y-8">
                    <h4 class="text-[10px] uppercase tracking-[0.3em] font-black text-iron-grey">Navigation</h4>
                    <ul class="space-y-4 font-bold text-lg text-platinum/70">
                        <li><a href="/about.html" class="hover:text-accent-blue transition-colors">About Us</a></li>
                        <li><a href="/services.html" class="hover:text-accent-blue transition-colors">Services</a></li>
                        <li><a href="/portfolio.html" class="hover:text-accent-blue transition-colors">Portfolio</a>
                        </li>
                        <li><a href="/contact.html" class="hover:text-accent-blue transition-colors">Contact Us</a>
                        </li>
                    </ul>
                </div>

                <!-- Legal Links (New Section) -->
                <div class="space-y-8">
                    <h4 class="text-[10px] uppercase tracking-[0.3em] font-black text-iron-grey">Transparency</h4>
                    <ul class="space-y-4 font-bold text-sm text-platinum/60">
                        <li><a href="/agreement.html"
                                class="hover:text-white transition-colors underline decoration-white/10 underline-offset-4">Service
                                Agreement</a></li>
                        <li><a href="/terms.html"
                                class="hover:text-white transition-colors underline decoration-white/10 underline-offset-4">Terms
                                of Service</a></li>
                        <li><a href="/privacy.html"
                                class="hover:text-white transition-colors underline decoration-white/10 underline-offset-4">Privacy
                                Policy</a></li>
                        <li><a href="/shipping.html"
                                class="hover:text-white transition-colors underline decoration-white/10 underline-offset-4">Shipping
                                Policy</a></li>
                        <li><a href="/refund.html"
                                class="hover:text-white transition-colors underline decoration-white/10 underline-offset-4">Refund
                                Policy</a></li>
                    </ul>
                </div>

                <!-- The Team -->
                <div class="space-y-8">
                    <h4 class="text-[10px] uppercase tracking-[0.3em] font-black text-iron-grey">The Architects</h4>
                    <ul class="space-y-4 font-bold text-sm text-platinum/60">
                        <li><a href="https://inakm.github.io" target="_blank"
                                class="hover:text-accent-blue transition-colors flex items-center justify-between group">AKM
                                <i
                                    class="fa-solid fa-arrow-up-right-from-square text-[10px] opacity-0 group-hover:opacity-100"></i></a>
                        </li>
                        <li><a href="https://aryansh.site" target="_blank"
                                class="hover:text-accent-blue transition-colors flex items-center justify-between group">Aryansh
                                <i
                                    class="fa-solid fa-arrow-up-right-from-square text-[10px] opacity-0 group-hover:opacity-100"></i></a>
                        </li>
                    </ul>
                </div>
            </div>

            <!-- 4. Bottom Copyright Bar -->
            <!-- Giant Brand Text -->
            <div class="relative py-24 overflow-hidden select-none pointer-events-none opacity-60">
                <h1 class="text-[12vw] font-black text-center leading-none tracking-tighter uppercase text-transparent translate-y-8 drop-shadow-[0_0_15px_rgba(255,255,255,0.3)]"
                    style="-webkit-text-stroke: 1.5px rgba(255,255,255,0.7);">
                    F9XR TEAM
                </h1>
                <div class="absolute inset-x-0 bottom-0 h-32 bg-gradient-to-t from-[#212529] to-transparent"></div>
            </div>

            <div
                class="py-12 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-8 text-center md:text-left">
                <div class="space-y-2">
                    <p class="font-bold text-platinum/40 text-sm italic">&copy; 2025 F9XR Team. Handcrafted with
                        Precision Engineering.</p>
                    <div
                        class="flex justify-center md:justify-start gap-6 text-[10px] font-black uppercase tracking-[0.2em] text-iron-grey">
                        <a href="https://instagram.com/f9xrteam" class="hover:text-pink-500">Instagram</a>
                        <a href="https://wa.me/message/X3KGWTAJ6Z6NB1" class="hover:text-green-500">WhatsApp</a>
                        <a href="mailto:tontufytservices@gmail.com" class="hover:text-accent-blue">Email Support</a>
                    </div>
                </div>

                <div class="flex gap-8 font-black tracking-widest uppercase text-[10px]">
                    <span class="flex items-center gap-2 italic text-iron-grey">Remote Global <i
                            class="fa-solid fa-globe text-accent-blue"></i></span>
                    <span
                        class="flex items-center gap-2 italic text-white underline decoration-accent-blue decoration-2">EST.
                        2024</span>
                </div>
            </div>
        </div>

        <!-- Ticker CSS Animation (Add to your global styles) -->



    </footer>"""

def update_files():
    root_dir = r"c:\Users\Dell\Documents\GitHub\f9xr.github.io"
    for filename in os.listdir(root_dir):
        if filename.endswith(".html") and filename not in EXCLUDE_FILES:
            filepath = os.path.join(root_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Replace backgrounds
                # Use AllowMultiple=True logic equivalent
                content = content.replace("bg-zinc-950", "bg-[#212529]")
                content = content.replace("bg-zinc-900", "bg-[#212529]")
                content = content.replace("from-zinc-950", "from-[#212529]")

                # Replace Footer
                # Uses regex to find any footer block
                if "<footer" in content:
                    content = re.sub(r'<footer[\s\S]*?</footer>', NEW_FOOTER, content, count=1)
                else:
                    print(f"Warning: No footer found in {filename}")

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    update_files()
