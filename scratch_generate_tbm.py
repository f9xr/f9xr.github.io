# -*- coding: utf-8 -*-
import os
import re

filepath = 'c:/Users/inanj/OneDrive/Documents/GitHub/f9xr.github.io/services/talent-brand-management.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title, Meta Description, Keywords
content = re.sub(r'<title>.*?</title>', '<title>Talent & Brand Management | Creator Scaling | F9XR x SponsorLanes</title>', content)
content = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Monetize your influence and scale your personal brand with elite talent representation, custom AI automation, and direct brand pipelines from F9XR & SponsorLanes.">', content)
content = re.sub(r'<meta name="keywords" content=".*?">', '<meta name="keywords" content="Talent management, influencer representation, brand deals, SponsorLanes Agency, F9XR, creator automation, personal branding, creator accelerator.">', content)

# 2. Update OG and Twitter Metas
content = re.sub(r'<meta property="og:url" content=".*?">', '<meta property="og:url" content="https://f9xr.github.io/services/talent-brand-management.html">', content)
content = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Talent & Brand Management | Creator Scaling | F9XR x SponsorLanes">', content)
content = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="Monetize your influence and scale your personal brand with elite talent representation, custom AI automation, and direct brand pipelines from F9XR & SponsorLanes.">', content)

content = re.sub(r'<meta name="twitter:url" content=".*?">', '<meta name="twitter:url" content="https://f9xr.github.io/services/talent-brand-management.html">', content)
content = re.sub(r'<meta name="twitter:title" content=".*?">', '<meta name="twitter:title" content="Talent & Brand Management | Creator Scaling | F9XR x SponsorLanes">', content)
content = re.sub(r'<meta name="twitter:description" content=".*?">', '<meta name="twitter:description" content="Monetize your influence and scale your personal brand with elite talent representation, custom AI automation, and direct brand pipelines from F9XR & SponsorLanes.">', content)

# 3. Update Canonical
content = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://f9xr.github.io/services/talent-brand-management.html">', content)

# 4. Update Schema
schema_product_old = r'"name": "AI Visibility Optimization",\s*"serviceType": "Generative Engine Optimization \(GEO\)",'
schema_product_new = '"name": "Talent & Brand Management",\n      "serviceType": "Talent Agency & Creator Management",'
content = re.sub(schema_product_old, schema_product_new, content)

schema_desc_old = r'"description": "Optimize your online presence for AI search engines including ChatGPT, Google Gemini, Microsoft Copilot, and Perplexity — making your brand discoverable in AI-generated responses.",'
schema_desc_new = '"description": "Elite talent representation, personal brand automation, and direct pipeline brand sponsorships delivered by F9XR and SponsorLanes.",'
content = re.sub(schema_desc_old, schema_desc_new, content)

# Breadcrumb Schema
content = re.sub(r'"name": "AI Visibility Optimization"', '"name": "Talent & Brand Management"', content)
content = re.sub(r'"item": "https://f9xr.github.io/services/ai-visibility-optimization.html"', '"item": "https://f9xr.github.io/services/talent-brand-management.html"', content)

# 5. Extract <main> and replace it
main_start = content.find('<main id="main-content"')
main_end = content.find('</main>') + len('</main>')

new_main_content = '''<main id="main-content" class="pt-32 pb-20 px-6 max-w-7xl mx-auto flex-grow">
    <!-- Hero Section -->
    <header class="text-center mb-24 reveal mt-12">
        <span class="text-accent-blue font-black uppercase tracking-[0.4em] text-sm mb-6 block drop-shadow-[0_0_15px_rgba(59,130,246,0.3)]">
            <i class="fa-solid fa-handshake mr-2"></i> F9XR Team x SponsorLanes Agency
        </span>
        <h1 class="text-5xl md:text-7xl lg:text-8xl font-black text-white mb-8 leading-tight tracking-tighter uppercase italic">
            Monetize Your <br class="hidden md:block" /> <span class="text-stroke-sm">Influence.</span> <br class="hidden md:block"/> Scale Your <span class="text-accent-blue drop-shadow-[0_0_20px_rgba(59,130,246,0.2)]">Personal Brand.</span>
        </h1>
        <p class="text-xl md:text-2xl text-platinum/70 max-w-3xl mx-auto leading-relaxed mb-12 font-medium">
            We bridge the gap between creative content and corporate brand budgets. A strategic partnership engineered to handle your backend operations, content strategy, and multi-channel monetization while you focus purely on creating.
        </p>
        <div class="flex flex-col sm:flex-row justify-center gap-6">
            <a href="#contact" class="group relative inline-flex items-center justify-center px-8 py-4 font-bold text-white bg-accent-blue rounded-xl overflow-hidden transition-all hover:scale-105 hover:shadow-[0_0_30px_rgba(59,130,246,0.4)]">
                <span class="absolute inset-0 bg-white/20 translate-y-full group-hover:translate-y-0 transition-transform duration-300 ease-out"></span>
                <span class="relative flex items-center gap-2">Apply for Representation <i class="fa-solid fa-arrow-right group-hover:translate-x-1 transition-transform"></i></span>
            </a>
            <a href="#solutions" class="group relative inline-flex items-center justify-center px-8 py-4 font-bold text-white border-2 border-white/10 rounded-xl overflow-hidden transition-all hover:bg-white/5">
                <span class="relative flex items-center gap-2"><i class="fa-solid fa-layer-group"></i> View Creator Solutions</span>
            </a>
        </div>
    </header>

    <!-- Partnership Synergy Block -->
    <section class="mb-32 reveal">
        <div class="bg-gunmetal border border-white/5 rounded-[2rem] p-8 md:p-16 relative overflow-hidden group">
            <div class="absolute -top-40 -right-40 w-96 h-96 bg-accent-blue/10 rounded-full blur-[100px] group-hover:bg-accent-blue/20 transition-all duration-700"></div>
            <div class="absolute -bottom-40 -left-40 w-96 h-96 bg-purple-500/10 rounded-full blur-[100px] group-hover:bg-purple-500/20 transition-all duration-700"></div>
            <div class="relative z-10 text-center max-w-4xl mx-auto">
                <h2 class="text-3xl md:text-5xl font-black uppercase tracking-tighter italic mb-8">Two Powerhouses. <br class="hidden md:block"/> <span class="text-accent-blue">One Complete Creator Engine.</span></h2>
                <p class="text-xl text-platinum/70 leading-relaxed font-medium">
                    <strong class="text-white">F9XR Team</strong> brings elite tech maintenance, custom AI automation, and high-converting web architecture. <strong class="text-white">SponsorLanes Agency</strong> delivers direct pipelines to verified brands, contract legalities, and aggressive sponsorship outreach. Together, we turn social channels into high-valuation digital businesses.
                </p>
            </div>
        </div>
    </section>

    <!-- The 3 Core Architecture Tiers -->
    <section id="solutions" class="mb-32">
        <div class="text-center mb-16 reveal">
            <h2 class="text-4xl md:text-6xl font-black uppercase tracking-tighter italic text-white mb-6">Growth <span class="text-stroke-sm">Architecture</span></h2>
            <p class="text-xl text-platinum/60">Tailored operational structures based on your audience scale.</p>
        </div>
        
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <!-- Tier 1 -->
            <div class="service-card rounded-3xl p-8 flex flex-col h-full reveal relative overflow-hidden group">
                <div class="absolute inset-0 bg-gradient-to-br from-accent-blue/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="w-16 h-16 bg-white/5 rounded-2xl flex items-center justify-center mb-8 border border-white/10 group-hover:scale-110 transition-transform duration-500 group-hover:border-accent-blue/30 relative z-10">
                    <i class="fa-solid fa-rocket text-2xl text-accent-blue"></i>
                </div>
                <h3 class="text-2xl font-black uppercase tracking-tight text-white mb-2 relative z-10">The Creator Accelerator</h3>
                <p class="text-accent-blue font-bold text-sm mb-6 uppercase tracking-widest relative z-10">Micro-Creators (10K-100K)</p>
                <p class="text-platinum/70 mb-8 flex-grow relative z-10">Structural growth and baseline monetization frameworks engineered for rapid scaling.</p>
                <ul class="space-y-4 mb-8 relative z-10">
                    <li class="flex items-start gap-3"><i class="fa-solid fa-check text-accent-blue mt-1"></i> <span class="text-platinum/80">Profile & Link-in-Bio Optimization</span></li>
                    <li class="flex items-start gap-3"><i class="fa-solid fa-check text-accent-blue mt-1"></i> <span class="text-platinum/80">Data-Driven Content Strategy & Hooks</span></li>
                    <li class="flex items-start gap-3"><i class="fa-solid fa-check text-accent-blue mt-1"></i> <span class="text-platinum/80">Custom Media Kit & Rate Card Design</span></li>
                    <li class="flex items-start gap-3"><i class="fa-solid fa-check text-accent-blue mt-1"></i> <span class="text-platinum/80">Unified Affiliate & UGC Funnel Setup</span></li>
                </ul>
                <a href="#contact" class="w-full text-center py-4 border border-white/10 rounded-xl text-white font-bold hover:bg-white/5 transition-colors relative z-10">Select Tier</a>
            </div>

            <!-- Tier 2 -->
            <div class="service-card rounded-3xl p-8 flex flex-col h-full reveal relative overflow-hidden group border-accent-blue/30 shadow-[0_0_30px_rgba(59,130,246,0.1)]">
                <div class="absolute inset-0 bg-gradient-to-br from-accent-blue/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="absolute top-0 right-8 bg-accent-blue text-white text-xs font-black uppercase tracking-widest px-4 py-1 rounded-b-lg">Most Popular</div>
                <div class="w-16 h-16 bg-white/5 rounded-2xl flex items-center justify-center mb-8 border border-white/10 group-hover:scale-110 transition-transform duration-500 group-hover:border-accent-blue/30 relative z-10">
                    <i class="fa-solid fa-crown text-2xl text-accent-blue"></i>
                </div>
                <h3 class="text-2xl font-black uppercase tracking-tight text-white mb-2 relative z-10">Elite Talent Representation</h3>
                <p class="text-accent-blue font-bold text-sm mb-6 uppercase tracking-widest relative z-10">Established Talent (100K-500K)</p>
                <p class="text-platinum/70 mb-8 flex-grow relative z-10">End-to-end business operations & active brand monetization through direct agency pipelines.</p>
                <ul class="space-y-4 mb-8 relative z-10">
                    <li class="flex items-start gap-3"><i class="fa-solid fa-check text-accent-blue mt-1"></i> <span class="text-platinum/80">24/7 Inbound Brand Deal Management</span></li>
                    <li class="flex items-start gap-3"><i class="fa-solid fa-check text-accent-blue mt-1"></i> <span class="text-platinum/80">Aggressive Outbound Pitching & PR</span></li>
                    <li class="flex items-start gap-3"><i class="fa-solid fa-check text-accent-blue mt-1"></i> <span class="text-platinum/80">Legal Contract Reviews & Invoicing</span></li>
                    <li class="flex items-start gap-3"><i class="fa-solid fa-check text-accent-blue mt-1"></i> <span class="text-platinum/80">Monthly Brand Campaign ROI Analytics</span></li>
                </ul>
                <a href="#contact" class="w-full text-center py-4 bg-accent-blue rounded-xl text-white font-bold hover:bg-accent-blue/90 transition-colors relative z-10 shadow-[0_0_20px_rgba(59,130,246,0.3)]">Apply for Elite</a>
            </div>

            <!-- Tier 3 -->
            <div class="service-card rounded-3xl p-8 flex flex-col h-full reveal relative overflow-hidden group">
                <div class="absolute inset-0 bg-gradient-to-br from-accent-blue/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                <div class="w-16 h-16 bg-white/5 rounded-2xl flex items-center justify-center mb-8 border border-white/10 group-hover:scale-110 transition-transform duration-500 group-hover:border-accent-blue/30 relative z-10">
                    <i class="fa-solid fa-building text-2xl text-accent-blue"></i>
                </div>
                <h3 class="text-2xl font-black uppercase tracking-tight text-white mb-2 relative z-10">Personal Brand Operations</h3>
                <p class="text-accent-blue font-bold text-sm mb-6 uppercase tracking-widest relative z-10">Mega-Creators (500K+)</p>
                <p class="text-platinum/70 mb-8 flex-grow relative z-10">High-tier brand positioning, complex automation, and long-term equity infrastructure.</p>
                <ul class="space-y-4 mb-8 relative z-10">
                    <li class="flex items-start gap-3"><i class="fa-solid fa-check text-accent-blue mt-1"></i> <span class="text-platinum/80">Advanced Long-Term Brand Positioning</span></li>
                    <li class="flex items-start gap-3"><i class="fa-solid fa-check text-accent-blue mt-1"></i> <span class="text-platinum/80">High-Volume Content Automation</span></li>
                    <li class="flex items-start gap-3"><i class="fa-solid fa-check text-accent-blue mt-1"></i> <span class="text-platinum/80">Community Infrastructure (Discord/Telegram)</span></li>
                    <li class="flex items-start gap-3"><i class="fa-solid fa-check text-accent-blue mt-1"></i> <span class="text-platinum/80">Private Merch, Course, or SaaS Funnels</span></li>
                </ul>
                <a href="#contact" class="w-full text-center py-4 border border-white/10 rounded-xl text-white font-bold hover:bg-white/5 transition-colors relative z-10">Select Tier</a>
            </div>
        </div>
    </section>

    <!-- The Service Matrix -->
    <section class="mb-32 reveal">
        <div class="text-center mb-16">
            <h2 class="text-4xl md:text-5xl font-black uppercase tracking-tighter italic text-white mb-4">The Backend <span class="text-stroke-sm">Matrix</span></h2>
            <p class="text-xl text-platinum/60 max-w-2xl mx-auto">A comprehensive breakdown of the digital infrastructure we handle so you can focus entirely on your craft.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div class="feature-card p-8 rounded-2xl group">
                <i class="fa-solid fa-file-contract text-3xl text-accent-blue mb-6 group-hover:scale-110 transition-transform"></i>
                <h3 class="text-xl font-bold text-white mb-4">Talent Management</h3>
                <p class="text-platinum/70">Contract legalities, strict rate negotiations, and automated invoice chasing.</p>
            </div>
            <div class="feature-card p-8 rounded-2xl group">
                <i class="fa-solid fa-id-badge text-3xl text-accent-blue mb-6 group-hover:scale-110 transition-transform"></i>
                <h3 class="text-xl font-bold text-white mb-4">Personal Branding</h3>
                <p class="text-platinum/70">Custom logos, optimized bios, defined content pillars, and micro-niche positioning.</p>
            </div>
            <div class="feature-card p-8 rounded-2xl group">
                <i class="fa-solid fa-chess-knight text-3xl text-accent-blue mb-6 group-hover:scale-110 transition-transform"></i>
                <h3 class="text-xl font-bold text-white mb-4">Content Strategy</h3>
                <p class="text-platinum/70">Trend research engines, content calendars, and burnout prevention structures.</p>
            </div>
            <div class="feature-card p-8 rounded-2xl group">
                <i class="fa-solid fa-bullhorn text-3xl text-accent-blue mb-6 group-hover:scale-110 transition-transform"></i>
                <h3 class="text-xl font-bold text-white mb-4">Outreach & PR</h3>
                <p class="text-platinum/70">Pitching you directly to target brands, podcasts, and media collaborations.</p>
            </div>
            <div class="feature-card p-8 rounded-2xl group">
                <i class="fa-solid fa-video text-3xl text-accent-blue mb-6 group-hover:scale-110 transition-transform"></i>
                <h3 class="text-xl font-bold text-white mb-4">Content Production</h3>
                <p class="text-platinum/70">Editing reels, custom YouTube thumbnails, and high-retention scripting.</p>
            </div>
            <div class="feature-card p-8 rounded-2xl group">
                <i class="fa-solid fa-users text-3xl text-accent-blue mb-6 group-hover:scale-110 transition-transform"></i>
                <h3 class="text-xl font-bold text-white mb-4">Community Management</h3>
                <p class="text-platinum/70">Active Telegram/Discord server automation and audience retention logic.</p>
            </div>
        </div>
    </section>

    <!-- Verified Partner Contact Portal -->
    <section id="contact" class="mb-32 reveal">
        <div class="bg-carbon-black border border-white/10 rounded-[2rem] p-8 md:p-12 max-w-4xl mx-auto shadow-2xl relative overflow-hidden">
            <div class="absolute top-0 right-0 w-64 h-64 bg-accent-blue/10 rounded-full blur-[80px]"></div>
            <div class="relative z-10 text-center mb-12">
                <span class="text-accent-blue font-bold tracking-widest uppercase text-sm mb-4 block"><i class="fa-solid fa-satellite-dish mr-2"></i> Authorized Node</span>
                <h2 class="text-4xl md:text-5xl font-black uppercase tracking-tighter italic text-white mb-6">Direct Pipeline to <br/> <span class="text-stroke-sm">SponsorLanes</span></h2>
                <p class="text-xl text-platinum/70 max-w-2xl mx-auto">Let's collaborate. We connect creators directly with verified global brands and premium clients through our dedicated agency channels.</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <a href="http://lepem.xyz" target="_blank" class="bg-white/5 border border-white/10 p-6 rounded-2xl text-center hover:bg-white/10 hover:border-accent-blue/50 transition-all group flex flex-col items-center">
                    <div class="w-12 h-12 rounded-full bg-accent-blue/10 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                        <i class="fa-solid fa-globe text-accent-blue text-xl"></i>
                    </div>
                    <span class="text-platinum font-bold block mb-1">Website</span>
                    <span class="text-sm text-platinum/50">lepem.xyz</span>
                </a>
                
                <a href="https://wa.me/919147923093" target="_blank" class="bg-white/5 border border-white/10 p-6 rounded-2xl text-center hover:bg-white/10 hover:border-accent-blue/50 transition-all group flex flex-col items-center">
                    <div class="w-12 h-12 rounded-full bg-accent-blue/10 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                        <i class="fa-brands fa-whatsapp text-accent-blue text-xl"></i>
                    </div>
                    <span class="text-platinum font-bold block mb-1">WhatsApp Hotline</span>
                    <span class="text-sm text-platinum/50">+91-91479-23093</span>
                </a>
                
                <a href="mailto:sponsorlane@gmail.com" class="bg-white/5 border border-white/10 p-6 rounded-2xl text-center hover:bg-white/10 hover:border-accent-blue/50 transition-all group flex flex-col items-center">
                    <div class="w-12 h-12 rounded-full bg-accent-blue/10 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                        <i class="fa-solid fa-envelope text-accent-blue text-xl"></i>
                    </div>
                    <span class="text-platinum font-bold block mb-1">Official Inquiries</span>
                    <span class="text-sm text-platinum/50">sponsorlane@gmail.com</span>
                </a>
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section class="py-32 px-6 max-w-4xl mx-auto" id="faq">
        <div class="text-center mb-20 reveal">
            <span class="text-accent-blue font-black uppercase tracking-[0.4em] text-xs mb-4 block"><i class="fa-solid fa-question-circle mr-2"></i> KNOWLEDGE BASE</span>
            <h2 class="text-4xl md:text-6xl font-black text-white italic tracking-tighter">Frequently Asked <span class="text-stroke-sm">Questions.</span></h2>
        </div>
        <div class="space-y-4">
            <div class="faq-item group bg-white/5 border border-white/5 rounded-3xl transition-all reveal">
                <button onclick="toggleFAQ(this)"
                    class="w-full px-10 py-8 flex justify-between items-center text-left font-bold text-2xl group-hover:text-platinum">
                    How do you match me with brands?
                    <i class="fas fa-plus transition-transform group-[.open]:rotate-45 text-accent-blue"></i>
                </button>
                <div class="faq-content overflow-hidden max-h-0 transition-[max-height] duration-400 ease-in-out">
                    <div class="px-10 pb-10 text-xl text-platinum/60 leading-relaxed">
                        We leverage the SponsorLanes network to proactively pitch your profile to relevant brands that align perfectly with your niche and audience demographics.
                    </div>
                </div>
            </div>
            
            <div class="faq-item group bg-white/5 border border-white/5 rounded-3xl transition-all reveal">
                <button onclick="toggleFAQ(this)"
                    class="w-full px-10 py-8 flex justify-between items-center text-left font-bold text-2xl group-hover:text-platinum">
                    Do I have to sign a long-term contract?
                    <i class="fas fa-plus transition-transform group-[.open]:rotate-45 text-accent-blue"></i>
                </button>
                <div class="faq-content overflow-hidden max-h-0 transition-[max-height] duration-400 ease-in-out">
                    <div class="px-10 pb-10 text-xl text-platinum/60 leading-relaxed">
                        No. We believe our results should keep you with us, not a rigid contract. We offer flexible term agreements tailored to your specific growth stage.
                    </div>
                </div>
            </div>

            <div class="faq-item group bg-white/5 border border-white/5 rounded-3xl transition-all reveal">
                <button onclick="toggleFAQ(this)"
                    class="w-full px-10 py-8 flex justify-between items-center text-left font-bold text-2xl group-hover:text-platinum">
                    Can you help if I only have 10,000 followers?
                    <i class="fas fa-plus transition-transform group-[.open]:rotate-45 text-accent-blue"></i>
                </button>
                <div class="faq-content overflow-hidden max-h-0 transition-[max-height] duration-400 ease-in-out">
                    <div class="px-10 pb-10 text-xl text-platinum/60 leading-relaxed">
                        Absolutely. Our 'Creator Accelerator' tier is specifically designed for micro-creators. Brands love highly-engaged micro-audiences, and we build the exact framework to monetize them.
                    </div>
                </div>
            </div>

            <div class="faq-item group bg-white/5 border border-white/5 rounded-3xl transition-all reveal">
                <button onclick="toggleFAQ(this)"
                    class="w-full px-10 py-8 flex justify-between items-center text-left font-bold text-2xl group-hover:text-platinum">
                    How do payments from brand deals work?
                    <i class="fas fa-plus transition-transform group-[.open]:rotate-45 text-accent-blue"></i>
                </button>
                <div class="faq-content overflow-hidden max-h-0 transition-[max-height] duration-400 ease-in-out">
                    <div class="px-10 pb-10 text-xl text-platinum/60 leading-relaxed">
                        SponsorLanes handles all the invoicing and contract legalities. Once a brand pays for a campaign, the funds are securely routed to you directly after the agreed agency commission.
                    </div>
                </div>
            </div>

            <div class="faq-item group bg-white/5 border border-white/5 rounded-3xl transition-all reveal">
                <button onclick="toggleFAQ(this)"
                    class="w-full px-10 py-8 flex justify-between items-center text-left font-bold text-2xl group-hover:text-platinum">
                    Do you help with content editing?
                    <i class="fas fa-plus transition-transform group-[.open]:rotate-45 text-accent-blue"></i>
                </button>
                <div class="faq-content overflow-hidden max-h-0 transition-[max-height] duration-400 ease-in-out">
                    <div class="px-10 pb-10 text-xl text-platinum/60 leading-relaxed">
                        Yes, our backend team at F9XR handles high-retention scripting, custom YouTube thumbnails, and professional reel editing to ensure your content consistently goes viral.
                    </div>
                </div>
            </div>
        </div>
        <style>
            .faq-item.open .faq-content { max-height: 500px; }
        </style>
    </section>

</main>'''

content = content[:main_start] + new_main_content + content[main_end:]

# Replace FAQ Schema manually since we overwrote the whole ai-visibility-optimization one with exactly what we want.
old_faq_schema_start = content.find('{"@context": "https://schema.org","@type": "FAQPage"')
if old_faq_schema_start == -1:
    old_faq_schema_start = content.find('{\n  "@context": "https://schema.org",\n  "@type": "FAQPage"')
if old_faq_schema_start != -1:
    old_faq_schema_end = content.find('</script>', old_faq_schema_start)
    
    new_faq_schema = '''{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do you match me with brands?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We leverage the SponsorLanes network to proactively pitch your profile to relevant brands that align perfectly with your niche and audience demographics."
      }
    },
    {
      "@type": "Question",
      "name": "Do I have to sign a long-term contract?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. We believe our results should keep you with us, not a rigid contract. We offer flexible term agreements tailored to your specific growth stage."
      }
    },
    {
      "@type": "Question",
      "name": "Can you help if I only have 10,000 followers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Absolutely. Our 'Creator Accelerator' tier is specifically designed for micro-creators. Brands love highly-engaged micro-audiences, and we build the exact framework to monetize them."
      }
    },
    {
      "@type": "Question",
      "name": "How do payments from brand deals work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "SponsorLanes handles all the invoicing and contract legalities. Once a brand pays for a campaign, the funds are securely routed to you directly after the agreed agency commission."
      }
    },
    {
      "@type": "Question",
      "name": "Do you help with content editing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, our backend team at F9XR handles high-retention scripting, custom YouTube thumbnails, and professional reel editing to ensure your content consistently goes viral."
      }
    }
  ]
}
'''
    # We replace the object within the script tag
    content = content[:old_faq_schema_start] + new_faq_schema + content[old_faq_schema_end:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated talent-brand-management.html successfully!")
