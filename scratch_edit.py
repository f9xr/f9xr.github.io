import re

with open('services/we-do-for-you.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace meta tags
content = re.sub(r'<title>.*?</title>', '<title>Done For You - Bulk Directory Submissions | F9XR Team</title>', content)
content = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="We take the pain out of bulk website submission. We submit your product to 100+ directories manually so you don\'t have to.">', content)
content = re.sub(r'<meta name="keywords" content=".*?">', '<meta name="keywords" content="bulk website submission, directory submissions, product launch, producthunt submission">', content)
content = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://f9xr.github.io/services/we-do-for-you.html">', content)
content = re.sub(r'<meta property="og:url" content=".*?">', '<meta property="og:url" content="https://f9xr.github.io/services/we-do-for-you.html">', content)
content = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Done For You - Bulk Directory Submissions">', content)
content = re.sub(r'<meta property="og:description" content=".*?">', '<meta property="og:description" content="We take the pain out of bulk website submission. We submit your product to 100+ directories manually so you don\'t have to.">', content)
content = re.sub(r'<meta name="twitter:url" content=".*?">', '<meta name="twitter:url" content="https://f9xr.github.io/services/we-do-for-you.html">', content)
content = re.sub(r'<meta name="twitter:title" content=".*?">', '<meta name="twitter:title" content="Done For You - Bulk Directory Submissions">', content)
content = re.sub(r'<meta name="twitter:description" content=".*?">', '<meta name="twitter:description" content="We take the pain out of bulk website submission. We submit your product to 100+ directories manually so you don\'t have to.">', content)

# Replace Schema (first one)
schema_1 = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": ["Service", "Product"],
  "name": "We Do For You - Directory Submissions",
  "serviceType": "Directory Submission",
  "provider": {
    "@type": "LocalBusiness",
    "name": "F9XR Team",
    "url": "https://f9xr.github.io/",
    "logo": "https://f9xr.github.io/logo.webp",
    "description": "Global digital agency specializing in AI-powered web development, Local SEO, and AI visibility optimization.",
    "contactPoint": {
      "@type": "ContactPoint",
      "telephone": "+91-90320-65784",
      "contactType": "customer service",
      "email": "tontufytservices@gmail.com",
      "availableLanguage": "en"
    },
    "sameAs": [
      "https://wa.me/message/X3KGWTAJ6Z6NB1",
      "https://www.facebook.com/profile.php?id=61586225441401",
      "https://instagram.com/f9xrteam",
      "https://linkedin.com/company/f9xrteam"
    ],
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Remote",
      "addressCountry": "Global"
    }
  },
  "description": "We take the pain out of bulk website submission. We submit your product to 100+ directories manually so you don\'t have to.",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "INR",
    "availability": "https://schema.org/InStock"
  }
}
</script>'''
content = re.sub(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema\.org",\s*"@type": \["Service", "Product"\],.*?</script>', schema_1, content, flags=re.DOTALL)

# Replace Breadcrumb Schema
schema_2 = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [{
    "@type": "ListItem",
    "position": 1,
    "name": "Home",
    "item": "https://f9xr.github.io/"
  }, {
    "@type": "ListItem",
    "position": 2,
    "name": "Services",
    "item": "https://f9xr.github.io/pages/services.html"
  }, {
    "@type": "ListItem",
    "position": 3,
    "name": "We Do For You",
    "item": "https://f9xr.github.io/services/we-do-for-you.html"
  }]
}
</script>'''
content = re.sub(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema\.org",\s*"@type": "BreadcrumbList",.*?</script>', schema_2, content, flags=re.DOTALL)

# Replace main content
new_main = '''<main id="main-content" class="pt-32 pb-20 px-6 max-w-7xl mx-auto flex-grow">
    <section class="mb-24 reveal">
        <div class="grid md:grid-cols-2 gap-12 items-center">
            <div class="reveal">
                <span class="text-accent-blue font-black uppercase tracking-[0.4em] text-xs mb-4 block">Done For You Submissions</span>
                <h1 class="text-5xl md:text-8xl font-black tracking-tighter leading-[0.9] mb-8 uppercase italic">
                    We Do For <br> <span class="text-stroke">You.</span>
                </h1>
                <p class="text-xl md:text-3xl text-platinum/70 font-medium leading-relaxed italic">
                    We take the pain out of bulk website submission. We manually submit your product to all top directories, so you don't have to.
                </p>
                <div class="bg-gunmetal border border-accent-blue/20 p-8 rounded-[2.5rem] backdrop-blur-md hidden lg:block shadow-[0_0_30px_rgba(59,130,246,0.1)] mt-8">
                    <p class="text-[10px] uppercase tracking-widest text-accent-blue font-black mb-4 italic flex items-center gap-2"><i class="fa-solid fa-rocket"></i> Launch Faster</p>
                    <h4 class="text-2xl font-black text-white italic">100+ High-Value Directories.</h4>
                    <p class="text-sm text-platinum/60 mt-2 font-medium tracking-tight">Earn backlinks, traffic, and initial users effortlessly.</p>
                </div>
                <div class="flex flex-col sm:flex-row justify-center lg:justify-start items-center gap-6 mt-8">
                    <a href="../directories/product-launch-directories.html"
                        class="group bg-accent-blue text-white px-10 py-5 rounded-full font-black text-lg uppercase tracking-wider hover:bg-blue-500 hover:scale-105 transition-all shadow-[0_0_40px_rgba(59,130,246,0.3)] flex items-center gap-3">
                        View Directory List
                        <i class="fa-solid fa-arrow-right-long group-hover:translate-x-1 transition-transform"></i>
                    </a>
                    <a href="https://wa.me/message/X3KGWTAJ6Z6NB1" target="_blank"
                        class="group px-8 py-5 rounded-full font-black text-lg uppercase tracking-wider text-white bg-white/5 border border-white/10 hover:bg-white/10 hover:border-accent-blue/50 transition-all flex items-center gap-3">
                        <i class="fa-brands fa-whatsapp text-green-400"></i>
                        <span>Contact Us</span>
                    </a>
                </div>
            </div>
            <div class="reveal">
                <img src="../assets/illustrations/Startup-rafiki.svg" width="500" height="500" alt="Done For You Directory Submission" class="w-full h-auto max-w-lg mx-auto" fetchpriority="high">
            </div>
        </div>
    </section>

    <section class="mb-24 reveal" id="features">
        <div class="flex items-center gap-4 mb-16">
            <span class="w-12 h-[2px] bg-accent-blue"></span>
            <h2 class="text-3xl md:text-5xl font-black uppercase tracking-tighter italic">Why Choose Us?</h2>
        </div>
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div class="feature-card p-8 rounded-[2.5rem]">
                <div class="w-12 h-12 bg-accent-blue/10 rounded-2xl flex items-center justify-center mb-6">
                    <i class="fas fa-hand-pointer text-accent-blue text-xl"></i>
                </div>
                <h3 class="text-lg font-black mb-3 uppercase tracking-tight">Manual Submission</h3>
                <p class="text-sm text-platinum/60 leading-relaxed">No bots. We manually fill out profiles ensuring high approval rates across top-tier directories.</p>
            </div>
            <div class="feature-card p-8 rounded-[2.5rem]">
                <div class="w-12 h-12 bg-accent-blue/10 rounded-2xl flex items-center justify-center mb-6">
                    <i class="fas fa-link text-accent-blue text-xl"></i>
                </div>
                <h3 class="text-lg font-black mb-3 uppercase tracking-tight">Quality Backlinks</h3>
                <p class="text-sm text-platinum/60 leading-relaxed">Build strong domain authority with links from established sites like ProductHunt and BetaList.</p>
            </div>
            <div class="feature-card p-8 rounded-[2.5rem]">
                <div class="w-12 h-12 bg-accent-blue/10 rounded-2xl flex items-center justify-center mb-6">
                    <i class="fas fa-clock text-accent-blue text-xl"></i>
                </div>
                <h3 class="text-lg font-black mb-3 uppercase tracking-tight">Save Hundreds of Hours</h3>
                <p class="text-sm text-platinum/60 leading-relaxed">Bulk submission is tedious. We do the heavy lifting so you can focus on building your product.</p>
            </div>
        </div>
    </section>
</main>'''

content = re.sub(r'<main id="main-content".*?</main>', new_main, content, flags=re.DOTALL)

with open('services/we-do-for-you.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("we-do-for-you.html updated successfully.")
