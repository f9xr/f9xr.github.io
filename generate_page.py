import os
import re

base_dir = r"c:\Users\inanj\OneDrive\Documents\GitHub\f9xr.github.io"
index_file = os.path.join(base_dir, "index.html")
target_file = os.path.join(base_dir, "directories", "product-launch-directories.html")

with open(index_file, "r", encoding="utf-8") as f:
    index_html = f.read()

# Extract header, footer, head
head_match = re.search(r'(<head>.*?</head>)', index_html, re.DOTALL)
header_match = re.search(r'(<header id="main-header".*?</header>)', index_html, re.DOTALL)
footer_match = re.search(r'(<footer.*?</footer>)', index_html, re.DOTALL)

head_html = head_match.group(1) if head_match else ""
header_html = header_match.group(1) if header_match else ""
footer_html = footer_match.group(1) if footer_match else ""

# Modify head for SEO
head_html = re.sub(r'<title>.*?</title>', '<title>Best Places to Launch Your Product along with ProductHunt | F9XR</title>', head_html)
head_html = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Discover the best places to launch your product, startup, or SaaS. F9XR Team offers Done-for-You directory submissions to ProductHunt, BetaList, and 100+ others.">', head_html)
head_html = re.sub(r'<meta property="og:title" content=".*?">', '<meta property="og:title" content="Best Places to Launch Your Product along with ProductHunt">', head_html)
head_html = re.sub(r'<link rel="canonical" href=".*?">', '<link rel="canonical" href="https://f9xr.github.io/directories/product-launch-directories.html">', head_html)

# Clean out specific index schemas to replace with new ones
head_html = re.sub(r'<script type="application/ld\+json">.*?</script>', '', head_html, flags=re.DOTALL)

new_schema = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": ["Service", "WebPage"],
  "name": "Done-for-You Directory Submissions",
  "description": "We submit your product to top directories that earn valuable backlinks and attract visitors who care about what you build.",
  "provider": {
    "@type": "LocalBusiness",
    "name": "F9XR Team",
    "url": "https://f9xr.github.io/"
  },
  "mainEntity": {
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "Why are directory submissions important for my SaaS or startup?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Every approved listing creates a permanent backlink pointing to your website. Search engines and AI assistants like ChatGPT, Perplexity, and Google crawl these directories regularly. This improves your domain authority and organic search rankings."
        }
      },
      {
        "@type": "Question",
        "name": "How does F9XR's directory submission service work?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Our team manually submits your product to 100+ of the best directories, avoiding bots or shortcuts. We ensure your submissions get approved, indexed, and provide a comprehensive report for all the quality backlinks you gain."
        }
      }
    ]
  }
}
</script>
"""

head_html = head_html.replace('</head>', new_schema + '\n</head>')

# Ensure CSS imports in head use root-relative paths if they don't already
head_html = head_html.replace('href="assets/', 'href="/assets/')

# Main content
main_content = """
<main id="main-content" class="flex-grow pt-32 lg:pt-40 pb-20 px-4 md:px-8 max-w-[1440px] mx-auto w-full relative z-[10]">

    <section class="mb-16 relative">
        <div class="absolute inset-0 bg-accent-blue/10 blur-[100px] rounded-full pointer-events-none"></div>
        <div class="text-center max-w-4xl mx-auto relative z-10">
            <h1 class="text-4xl md:text-5xl lg:text-7xl font-black mb-6 tracking-tighter leading-tight reveal">
                Best Places to Launch Your Product along with <span class="text-accent-blue">ProductHunt</span>
            </h1>
            <p class="text-lg md:text-xl text-platinum/80 leading-relaxed font-medium mb-8 reveal">
                We add new Directories each day for you to launch your Product, SaaS, or Startup. Discover where founders go to get their first real users, valuable feedback, and long-term SEO backlinks.
            </p>
            <div class="flex flex-wrap justify-center gap-4 reveal">
                <a href="/pages/contact.html" class="px-8 py-4 bg-accent-blue hover:bg-blue-600 text-white rounded-xl font-bold transition-all hover:scale-105 shadow-[0_0_20px_rgba(59,130,246,0.4)]">
                    Get Started Today
                </a>
                <a href="#directories-list" class="px-8 py-4 bg-white/5 border border-white/10 hover:bg-white/10 text-white rounded-xl font-bold transition-all">
                    View Directories List
                </a>
            </div>
        </div>
    </section>

    <!-- Done-For-You Service Section -->
    <section class="mb-24 reveal">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center bg-carbon-black/40 border border-white/10 rounded-3xl p-8 lg:p-12 shadow-2xl relative overflow-hidden">
            <div class="absolute -right-20 -top-20 w-64 h-64 bg-accent-blue/20 blur-[80px] rounded-full"></div>
            
            <div class="relative z-10">
                <div class="inline-block px-3 py-1 bg-accent-blue/20 border border-accent-blue/30 text-accent-blue rounded-full text-xs font-bold uppercase tracking-wider mb-6">Our Premium Service</div>
                <h2 class="text-3xl md:text-4xl font-bold mb-6 text-white leading-tight">Done-for-You Directory Submissions</h2>
                <p class="text-platinum/70 text-lg mb-6 leading-relaxed">
                    We submit your product to top directories that earn valuable backlinks and attract visitors who care about what you build. We handle every listing, send a clear report for each submission, and let you stay focused on shipping, selling, and growing.
                </p>
                <div class="space-y-4">
                    <h3 class="text-xl font-bold text-white mb-4">What you get:</h3>
                    <ul class="grid grid-cols-1 md:grid-cols-2 gap-3 text-sm text-platinum/80 font-medium">
                        <li class="flex items-center gap-3"><i class="fa-solid fa-circle-check text-accent-blue"></i> Manual submission to directories</li>
                        <li class="flex items-center gap-3"><i class="fa-solid fa-circle-check text-accent-blue"></i> Quality backlinks & SEO boost</li>
                        <li class="flex items-center gap-3"><i class="fa-solid fa-circle-check text-accent-blue"></i> Complete report provided</li>
                        <li class="flex items-center gap-3"><i class="fa-solid fa-circle-check text-accent-blue"></i> Enhanced search rankings</li>
                        <li class="flex items-center gap-3"><i class="fa-solid fa-circle-check text-accent-blue"></i> Perfect for all product types</li>
                        <li class="flex items-center gap-3"><i class="fa-solid fa-circle-check text-accent-blue"></i> Targeted traffic generation</li>
                        <li class="flex items-center gap-3"><i class="fa-solid fa-circle-check text-accent-blue"></i> Long-term SEO benefits</li>
                        <li class="flex items-center gap-3"><i class="fa-solid fa-circle-check text-accent-blue"></i> Improved domain reputation</li>
                        <li class="flex items-center gap-3"><i class="fa-solid fa-circle-check text-accent-blue"></i> Save 40+ hours of manual work</li>
                        <li class="flex items-center gap-3"><i class="fa-solid fa-circle-check text-accent-blue"></i> Professional submission process</li>
                    </ul>
                </div>
            </div>

            <div class="bg-[#121212] rounded-2xl p-8 border border-white/5 relative z-10">
                <h3 class="text-2xl font-bold text-white mb-4">No Bots. Just Real Submissions.</h3>
                <p class="text-platinum/60 text-sm mb-6 leading-relaxed">
                    Our team manually submits your product to the best directories. No shortcuts - just real submissions that get approved and indexed by search engines. Getting your product listed on 100+ directories sounds time-consuming, right? That's where we come in. Simply fill out our quick form with your product details, and we'll handle everything else.
                </p>
                <a href="/pages/contact.html" class="w-full block text-center px-6 py-4 bg-white/10 hover:bg-accent-blue text-white rounded-xl font-bold transition-colors">
                    Start Your Submission Campaign
                </a>
            </div>
        </div>
    </section>

    <!-- Why This Works -->
    <section class="mb-24">
        <div class="text-center mb-12 reveal">
            <h2 class="text-3xl md:text-4xl font-bold text-white mb-4">Why This Works</h2>
            <p class="text-platinum/60 max-w-2xl mx-auto">Discover how high-quality directory listings generate compounding returns for your business.</p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="feature-card p-8 rounded-2xl reveal">
                <div class="w-12 h-12 bg-accent-blue/20 text-accent-blue rounded-xl flex items-center justify-center text-xl mb-6">1</div>
                <h3 class="text-xl font-bold text-white mb-3">Targeted Discovery</h3>
                <p class="text-platinum/60 text-sm leading-relaxed">
                    We submit your project to curated launch directories with active communities of founders, makers, and early adopters. These platforms are where people go specifically to discover new tools and products. The result? You get your first real users - people who are excited to try new solutions, give feedback, and share what they discover.
                </p>
            </div>
            <div class="feature-card p-8 rounded-2xl reveal delay-100">
                <div class="w-12 h-12 bg-accent-blue/20 text-accent-blue rounded-xl flex items-center justify-center text-xl mb-6">2</div>
                <h3 class="text-xl font-bold text-white mb-3">Permanent Backlinks</h3>
                <p class="text-platinum/60 text-sm leading-relaxed">
                    Every approved listing creates a permanent backlink. Unlike paid ads that disappear when your budget runs out, these backlinks keep working 24/7. They build credibility with search engines like Google and Bing, driving organic traffic without recurring costs.
                </p>
            </div>
            <div class="feature-card p-8 rounded-2xl reveal delay-200">
                <div class="w-12 h-12 bg-accent-blue/20 text-accent-blue rounded-xl flex items-center justify-center text-xl mb-6">3</div>
                <h3 class="text-xl font-bold text-white mb-3">You Grow with AI</h3>
                <p class="text-platinum/60 text-sm leading-relaxed">
                    Over the following months, you'll see your domain authority score increase. AI tools like ChatGPT, Claude, and Perplexity pull data from these high-authority directories. Your product gets featured in AI responses when users ask for solutions in your category.
                </p>
            </div>
        </div>
    </section>

    <!-- JSON Directory List -->
    <section id="directories-list" class="mb-24 reveal">
        <div class="flex items-center justify-between mb-8 border-b border-white/10 pb-4">
            <h2 class="text-2xl font-bold text-white">Live Launch Directories</h2>
            <span class="text-xs font-bold bg-white/10 text-white/70 px-3 py-1 rounded-full uppercase tracking-wider">Updated Daily</span>
        </div>
        
        <div id="directory-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            <!-- Directory items will be loaded here via JS -->
            <div class="col-span-full text-center py-12 text-platinum/50">
                <i class="fa-solid fa-circle-notch fa-spin text-3xl mb-4 text-accent-blue"></i>
                <p>Loading the best launch directories...</p>
            </div>
        </div>
    </section>

    <!-- AEO / SEO FAQ Section -->
    <section class="mb-24 reveal">
        <h2 class="text-3xl md:text-4xl font-bold text-center text-white mb-12">Frequently Asked Questions</h2>
        <div class="max-w-3xl mx-auto space-y-4">
            <details class="group bg-white/5 border border-white/10 rounded-xl overflow-hidden">
                <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-6 text-white hover:text-accent-blue transition-colors">
                    <span>How does directory submission help with AI Search (AEO)?</span>
                    <span class="transition group-open:rotate-180"><i class="fa-solid fa-chevron-down"></i></span>
                </summary>
                <div class="text-platinum/70 text-sm p-6 pt-0 leading-relaxed border-t border-white/5 mt-2">
                    Answer Engine Optimization (AEO) focuses on getting your business cited by AI tools like ChatGPT, Claude, and Perplexity. These AI models source their information from high-authority domains, review sites, and curated directories. By having your product listed across 100+ prominent directories, you dramatically increase the likelihood of being referenced as a top solution in AI-generated answers.
                </div>
            </details>
            <details class="group bg-white/5 border border-white/10 rounded-xl overflow-hidden">
                <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-6 text-white hover:text-accent-blue transition-colors">
                    <span>Are these backlinks safe for Google SEO?</span>
                    <span class="transition group-open:rotate-180"><i class="fa-solid fa-chevron-down"></i></span>
                </summary>
                <div class="text-platinum/70 text-sm p-6 pt-0 leading-relaxed border-t border-white/5 mt-2">
                    Yes. We manually submit your site to curated, high-quality, and relevant startup and software directories. We strictly avoid spammy link farms or automated bot submissions. This process builds a natural and diverse backlink profile that aligns perfectly with Google's helpful content and spam guidelines.
                </div>
            </details>
            <details class="group bg-white/5 border border-white/10 rounded-xl overflow-hidden">
                <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-6 text-white hover:text-accent-blue transition-colors">
                    <span>Do you guarantee acceptance on all directories?</span>
                    <span class="transition group-open:rotate-180"><i class="fa-solid fa-chevron-down"></i></span>
                </summary>
                <div class="text-platinum/70 text-sm p-6 pt-0 leading-relaxed border-t border-white/5 mt-2">
                    While we have a very high success rate due to our professional manual submission process, acceptance ultimately depends on the directory's editorial team and the quality/relevance of your product. We ensure your submission is perfectly tailored to maximize approval rates on every platform.
                </div>
            </details>
        </div>
    </section>

    <!-- Interlinking / Related Services -->
    <section class="mb-12 reveal">
        <h3 class="text-2xl font-bold text-white mb-6">Explore Our Other Growth Services</h3>
        <div class="flex flex-wrap gap-4">
            <a href="/services/ai-visibility-optimization.html" class="px-5 py-3 bg-white/5 border border-white/10 rounded-lg text-sm text-platinum hover:bg-accent-blue hover:border-accent-blue transition-colors font-medium">AI Visibility Optimization</a>
            <a href="/services/google-business-optimization.html" class="px-5 py-3 bg-white/5 border border-white/10 rounded-lg text-sm text-platinum hover:bg-accent-blue hover:border-accent-blue transition-colors font-medium">Google Business Optimization</a>
            <a href="/services/social-media-posting.html" class="px-5 py-3 bg-white/5 border border-white/10 rounded-lg text-sm text-platinum hover:bg-accent-blue hover:border-accent-blue transition-colors font-medium">Social Media Growth</a>
            <a href="/services/telegram-bot-development.html" class="px-5 py-3 bg-white/5 border border-white/10 rounded-lg text-sm text-platinum hover:bg-accent-blue hover:border-accent-blue transition-colors font-medium">Telegram Bots</a>
        </div>
        
        <h3 class="text-xl font-bold text-white mt-12 mb-4">Helpful Resources</h3>
        <div class="flex flex-wrap gap-x-6 gap-y-2 text-sm">
            <a href="/tools/digital-presence.html" class="text-accent-blue hover:underline">Digital Presence Score</a>
            <a href="/tools/local-seo-score.html" class="text-accent-blue hover:underline">Local SEO Grader</a>
            <a href="/pages/portfolio.html" class="text-accent-blue hover:underline">Our Success Stories</a>
            <a href="https://growwithguidance.blogspot.com/2025/05/namecheap-latest-active-coupon-promo.html" target="_blank" class="text-accent-blue hover:underline">Namecheap Promo Codes</a>
            <a href="https://growwithguidance.blogspot.com/2025/05/elfsight-latest-active-coupon-promo.html" target="_blank" class="text-accent-blue hover:underline">Elfsight Promo Codes</a>
        </div>
    </section>

</main>

<script>
    // Reveal Animation
    document.addEventListener('DOMContentLoaded', () => {
        const reveals = document.querySelectorAll('.reveal');
        
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: "0px 0px -50px 0px"
        });

        reveals.forEach(reveal => revealObserver.observe(reveal));
        
        // Fetch JSON Data
        fetch('/directories/launch-directories.json')
            .then(response => response.json())
            .then(data => {
                const grid = document.getElementById('directory-grid');
                grid.innerHTML = '';
                
                if(data.length === 0) {
                    grid.innerHTML = '<p class="text-platinum/50 col-span-full text-center">No directories found.</p>';
                    return;
                }
                
                data.forEach(item => {
                    // Extract domain for display
                    let domain = '';
                    try {
                        domain = new URL(item.url).hostname.replace('www.', '');
                    } catch(e) {
                        domain = item.url;
                    }
                    
                    const card = document.createElement('a');
                    card.href = item.url;
                    card.target = "_blank";
                    card.rel = "noopener noreferrer nofollow";
                    card.className = "flex items-center justify-between p-5 bg-white/5 border border-white/5 hover:border-accent-blue/50 hover:bg-white/10 rounded-xl transition-all group";
                    
                    card.innerHTML = `
                        <div class="flex flex-col">
                            <span class="font-bold text-white text-base mb-1 group-hover:text-accent-blue transition-colors">${item.name}</span>
                            <span class="text-xs text-platinum/50 font-medium">${domain}</span>
                        </div>
                        <div class="w-8 h-8 rounded-full bg-white/5 flex items-center justify-center text-white/50 group-hover:bg-accent-blue group-hover:text-white transition-all transform group-hover:translate-x-1">
                            <i class="fa-solid fa-arrow-right text-xs"></i>
                        </div>
                    `;
                    grid.appendChild(card);
                });
            })
            .catch(err => {
                console.error("Error loading directories:", err);
                document.getElementById('directory-grid').innerHTML = '<p class="text-red-400 col-span-full text-center">Failed to load directory list. Please try again later.</p>';
            });
    });
</script>
"""

# Assemble page
html_content = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
{head_html}
<body class="text-bright-snow font-sans selection:bg-accent-blue selection:text-white min-h-screen flex flex-col bg-[#121212]">

    <div class="fixed inset-0 -z-50 h-full w-full bg-black">
        <div class="absolute bottom-0 left-0 right-0 top-0 bg-[linear-gradient(to_right,#4f4f4f2e_1px,transparent_1px),linear-gradient(to_bottom,#8080800a_1px,transparent_1px)] bg-[size:14px_24px]"></div>
        <div class="absolute left-0 right-0 top-[-10%] h-[1000px] w-[1000px] rounded-full bg-[radial-gradient(circle_400px_at_50%_300px,#fbfbfb36,#000)]"></div>
    </div>

{header_html}

{main_content}

{footer_html}

</body>
</html>
"""

with open(target_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Created {target_file}")
