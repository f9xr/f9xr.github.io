import os
import re

filepath = 'c:/Users/inanj/OneDrive/Documents/GitHub/f9xr.github.io/announcements/f9xr-sponsorlanes-partnership.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title, Meta Description, Keywords
content = re.sub(r'<title>.*?</title>', '<title>Partnership Announcement | F9XR Team x SponsorLanes Agency</title>', content)
content = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="F9XR Team and SponsorLanes Agency announce an official partnership to launch an elite Talent & Brand Management engine for creators.">', content)
content = re.sub(r'<meta name="keywords" content=".*?">', '<meta name="keywords" content="F9XR Team, SponsorLanes Agency, partnership, press release, influencer management, creator agency">', content)

# 2. Update OG and Twitter Metas
content = re.sub(r'<meta property="og:url" content=".*?">', '<meta property="og:url" content="https://f9xr.github.io/announcements/f9xr-sponsorlanes-partnership.html">', content)
content = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Official Partnership | F9XR Team x SponsorLanes Agency">', content)
content = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="F9XR Team and SponsorLanes Agency announce an official partnership to launch an elite Talent & Brand Management engine for creators.">', content)

content = re.sub(r'<meta name="twitter:url" content=".*?">', '<meta name="twitter:url" content="https://f9xr.github.io/announcements/f9xr-sponsorlanes-partnership.html">', content)
content = re.sub(r'<meta name="twitter:title" content=".*?">', '<meta name="twitter:title" content="Official Partnership | F9XR Team x SponsorLanes Agency">', content)
content = re.sub(r'<meta name="twitter:description" content=".*?">', '<meta name="twitter:description" content="F9XR Team and SponsorLanes Agency announce an official partnership to launch an elite Talent & Brand Management engine for creators.">', content)

# 3. Update Canonical
content = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://f9xr.github.io/announcements/f9xr-sponsorlanes-partnership.html">', content)

# 4. Remove Service/Product Schema since this is a NewsArticle/PR.
script_blocks = re.findall(r'<script type="application/ld\+json">.*?</script>', content, re.DOTALL)
for block in script_blocks:
    content = content.replace(block, '')

# Inject PR schema before </head>
pr_schema = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "NewsArticle",
  "headline": "F9XR Team and SponsorLanes Agency Announce Strategic Merger to Launch Elite Talent & Brand Management Engine",
  "datePublished": "2026-06-27T08:00:00+00:00",
  "dateModified": "2026-06-27T08:00:00+00:00",
  "author": [{
      "@type": "Organization",
      "name": "F9XR Team",
      "url": "https://f9xr.github.io"
  }],
  "publisher": {
    "@type": "Organization",
    "name": "F9XR Team",
    "logo": {
      "@type": "ImageObject",
      "url": "https://f9xr.github.io/logo.webp"
    }
  },
  "description": "F9XR Team and SponsorLanes Agency announce a joint venture to provide comprehensive talent and brand management services for the modern creator economy."
}
</script>'''

content = content.replace('</head>', pr_schema + '\\n</head>')

# 5. Extract <main> and replace it
main_start = content.find('<main id="main-content"')
main_end = content.find('</main>') + len('</main>')

new_main_content = '''<main id="main-content" class="pt-32 pb-20 px-6 max-w-4xl mx-auto flex-grow">
    
    <div class="mb-12 border-b border-white/10 pb-8 mt-12 reveal">
        <span class="text-accent-blue font-bold tracking-widest uppercase text-sm mb-4 block"><i class="fa-solid fa-bullhorn mr-2"></i> FOR IMMEDIATE RELEASE</span>
        <h1 class="text-4xl md:text-5xl lg:text-6xl font-black text-white leading-tight tracking-tighter italic mb-6">
            F9XR Team and SponsorLanes Agency Announce Strategic Partnership to Launch Elite <span class="text-accent-blue">"Talent & Brand Management Engine"</span>
        </h1>
        <div class="flex items-center gap-4 text-platinum/60 font-medium text-sm uppercase tracking-widest">
            <span><i class="fa-regular fa-calendar mr-2"></i> June 27, 2026</span>
            <span>|</span>
            <span>Global Operations</span>
        </div>
    </div>

    <article class="prose prose-invert prose-lg max-w-none text-platinum/80 leading-relaxed font-medium reveal">
        <p class="text-xl text-white font-bold leading-relaxed mb-10">
            F9XR Team, the premier digital architecture and AI automation agency, today announced an official partnership with SponsorLanes Agency, a specialized influencer growth firm. Together, the two entities have launched a comprehensive "Talent & Brand Management Engine" designed specifically to bridge the gap between high-level creative content and corporate brand budgets in the modern digital ecosystem.
        </p>

        <h3 class="text-2xl font-bold text-white mb-4 mt-12 uppercase tracking-tighter italic"><i class="fa-solid fa-bolt text-accent-blue mr-2"></i> Disrupting the Creator Economy</h3>
        <p class="mb-8">
            The partnership disrupts traditional influencer representation models by merging SponsorLanes' aggressive sponsorship acquisition and contract negotiation expertise with F9XR Team's elite web engineering, AI automation, and advanced operational infrastructure.
        </p>

        <blockquote class="border-l-4 border-accent-blue pl-6 my-12 bg-white/5 py-6 pr-6 rounded-r-2xl italic text-xl text-platinum">
            "The creator economy has matured beyond simple brand deals. Today's mega-creators are functioning as enterprise media companies. By partnering with SponsorLanes, we are providing creators with an operational backbone. We automate their content pipelines, build their digital ecosystems, and engineer their monetization funnels, completely removing burnout while scaling revenue to enterprise levels."
            <footer class="mt-4 text-sm text-accent-blue font-bold uppercase tracking-widest not-italic">- AKM, Lead Digital Architect at F9XR Team</footer>
        </blockquote>

        <h3 class="text-2xl font-bold text-white mb-4 mt-12 uppercase tracking-tighter italic"><i class="fa-solid fa-layer-group text-accent-blue mr-2"></i> A 3-Tier Growth Architecture</h3>
        <p class="mb-6">The new joint venture offers a tailored operational structure based on audience scale:</p>
        <ul class="space-y-4 mb-12 bg-gunmetal p-8 rounded-3xl border border-white/5">
            <li class="flex items-start gap-4">
                <i class="fa-solid fa-rocket text-accent-blue mt-1"></i> 
                <div>
                    <strong class="text-white block mb-1 text-lg">The Creator Accelerator (10K-100K Followers)</strong>
                    Engineered for micro-creators, focusing on data-driven content hooks, baseline monetization, and professional media kit deployment.
                </div>
            </li>
            <li class="flex items-start gap-4">
                <i class="fa-solid fa-crown text-accent-blue mt-1"></i> 
                <div>
                    <strong class="text-white block mb-1 text-lg">Elite Talent Representation (100K-500K Followers)</strong>
                    Built for established talent, providing 24/7 inbound deal management, proactive outbound pitching, multi-currency invoicing, and legal contract reviews.
                </div>
            </li>
            <li class="flex items-start gap-4">
                <i class="fa-solid fa-building text-accent-blue mt-1"></i> 
                <div>
                    <strong class="text-white block mb-1 text-lg">Personal Brand Operations (500K+ Followers)</strong>
                    Designed for mega-creators, offering long-term brand equity positioning, high-volume AI script automation, private SaaS/Merch funnels, and Discord/Telegram community infrastructure.
                </div>
            </li>
        </ul>

        <div class="my-16 flex justify-center reveal">
            <a href="../services/talent-brand-management.html" class="group relative inline-flex items-center justify-center px-10 py-5 font-black text-white bg-accent-blue rounded-2xl overflow-hidden transition-all hover:scale-105 hover:shadow-[0_0_40px_rgba(59,130,246,0.5)] text-lg uppercase tracking-widest">
                <span class="absolute inset-0 bg-white/20 translate-y-full group-hover:translate-y-0 transition-transform duration-300 ease-out"></span>
                <span class="relative flex items-center gap-3">View Full Service Details <i class="fa-solid fa-arrow-right group-hover:translate-x-2 transition-transform"></i></span>
            </a>
        </div>

        <h3 class="text-2xl font-bold text-white mb-6 mt-16 border-b border-white/10 pb-4 uppercase tracking-tighter italic">Media Contacts & Application Portal</h3>
        <p class="mb-6">Creators and brands seeking immediate representation or collaborative campaigns are encouraged to apply directly through the authorized SponsorLanes contact nodes.</p>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 not-prose mb-12">
            <a href="http://lepem.xyz" target="_blank" class="bg-white/5 border border-white/10 p-6 rounded-2xl text-center hover:bg-white/10 hover:border-accent-blue/50 transition-all group flex flex-col items-center">
                <div class="w-12 h-12 rounded-full bg-accent-blue/10 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                    <i class="fa-solid fa-globe text-accent-blue text-xl"></i>
                </div>
                <span class="text-platinum font-bold block mb-1">Official Website</span>
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
                <span class="text-platinum font-bold block mb-1">Press Inquiries</span>
                <span class="text-sm text-platinum/50">sponsorlane@gmail.com</span>
            </a>
        </div>
    </article>

</main>'''

content = content[:main_start] + new_main_content + content[main_end:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated PR page successfully!")
