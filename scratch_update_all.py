import os
import re

directory = 'c:/Users/inanj/OneDrive/Documents/GitHub/f9xr.github.io'

navbar_script = '''
<script>
// Smart Navbar: hide on scroll down, show on scroll up
let lastScrollY$ = window.scrollY;
const header$ = document.getElementById('main-header');
if (header$) {
    window.addEventListener('scroll', () => {
        const currentScrollY$ = window.scrollY;
        if (currentScrollY$ > lastScrollY$ && currentScrollY$ > 100) {
            header$.classList.add('-translate-y-full');
        } else {
            header$.classList.remove('-translate-y-full');
        }
        lastScrollY$ = currentScrollY$;
    });
}
</script>
'''

faq_data = {
    'ai-visibility-optimization.html': [
        ('What is AI Visibility Optimization?', 'It is the process of structuring and optimizing your brand content so it is easily discovered and cited by AI engines like ChatGPT, Gemini, and Perplexity.'),
        ('How long does it take to appear in ChatGPT?', 'Results vary depending on the platform training schedule, but structured data and high-authority links can help AI crawlers index your brand within a few weeks to months.')
    ],
    'data-management.html': [
        ('What data management services do you provide?', 'We offer data structuring, database management, scraping, organization, and automated data processing tailored to your business needs.'),
        ('Is my data kept secure?', 'Absolutely. We follow strict security protocols to ensure all client data is handled with the highest level of confidentiality and protection.')
    ],
    'discord-bot-development.html': [
        ('What kind of features can a custom Discord bot have?', 'Our custom bots can handle moderation, ticketing systems, automated role assignments, API integrations, economy systems, and custom minigames.'),
        ('Do you host the bot for me?', 'Yes, we offer deployment and ongoing maintenance/hosting services to ensure your Discord bot runs 24/7 without interruption.')
    ],
    'google-business-optimization.html': [
        ('How does Google Business optimization help my local business?', 'It increases your visibility in local search and Google Maps, driving foot traffic, phone calls, and direct inquiries from nearby customers.'),
        ('What is included in the GBP service?', 'We optimize your profile, manage reviews, post regular updates, structure your services/products, and build local citations to boost rankings.')
    ],
    'indian-professionals.html': [
        ('What kind of professionals can I hire?', 'You can hire top-tier developers, designers, virtual assistants, SEO experts, and marketers from our vetted talent pool.'),
        ('How do you ensure quality?', 'We rigorously test and vet all professionals before they join our network, ensuring they have the technical skills and communication required for global standards.')
    ],
    'social-media-posting.html': [
        ('Which platforms do you manage?', 'We manage Instagram, Facebook, LinkedIn, X (Twitter), TikTok, and Pinterest depending on your target audience and brand strategy.'),
        ('Do you create the content too?', 'Yes! We handle the entire process from strategy and graphic design/video editing to copywriting, scheduling, and community management.')
    ],
    'telegram-bot-development.html': [
        ('What can Telegram bots do for my business?', 'Telegram bots can automate customer support, process payments, broadcast messages, scrape data, and interact with your CRM or external APIs.'),
        ('How long does it take to build a Telegram bot?', 'A standard bot can be deployed in a few days, while complex bots with extensive API integrations take 1-3 weeks.')
    ],
    'we-do-for-you.html': [
        ('What directories do you submit to?', 'We submit your product to 100+ high-authority platforms including ProductHunt, BetaList, startup directories, and SaaS aggregators.'),
        ('Do you also submit to search engines?', 'Yes, we also submit your website to hundreds of search engines and ping them to ensure your product is indexed globally as fast as possible.')
    ],
    'website-rentals.html': [
        ('What is a website rental?', 'Instead of paying thousands of dollars upfront for a custom website, you pay an affordable monthly fee to rent a high-converting, fully managed site from us.'),
        ('Do I own the domain?', 'We can either use your existing domain or purchase and manage a new one for you. You always retain ownership of your brand name.')
    ]
}

def generate_faq_html(service_file):
    if service_file not in faq_data:
        return ""
    faqs = faq_data[service_file]
    
    html = '''
    <section class="mb-24 reveal" id="faq">
        <div class="flex items-center gap-4 mb-16">
            <span class="w-12 h-[2px] bg-accent-blue"></span>
            <h2 class="text-3xl md:text-5xl font-black uppercase tracking-tighter italic">Frequently Asked Questions</h2>
        </div>
        <div class="grid gap-6 max-w-4xl mx-auto">
'''
    for q, a in faqs:
        html += f'''
            <div class="faq-item bg-gunmetal border border-white/10 rounded-2xl p-6 cursor-pointer hover:border-accent-blue/50 transition-colors" onclick="this.classList.toggle('open')">
                <div class="flex justify-between items-center gap-4">
                    <h3 class="text-xl font-bold text-white">{q}</h3>
                    <i class="fa-solid fa-plus text-accent-blue transition-transform duration-300"></i>
                </div>
                <div class="faq-content overflow-hidden max-h-0 transition-all duration-300 ease-in-out">
                    <p class="text-platinum/70 mt-4 leading-relaxed font-medium">{a}</p>
                </div>
            </div>
'''
    html += '''
        </div>
        <style>
            .faq-item.open i { transform: rotate(45deg); }
            .faq-item.open .faq-content { max-height: 500px; }
        </style>
    </section>
'''
    return html

def generate_faq_schema(service_file):
    if service_file not in faq_data:
        return ""
    faqs = faq_data[service_file]
    
    schema = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": ['''
    
    entities = []
    for q, a in faqs:
        entities.append(f'''
    {{
      "@type": "Question",
      "name": "{q}",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "{a}"
      }}
    }}''')
    
    schema += ",".join(entities)
    schema += '''
  ]
}
</script>'''
    return schema

for root_dir, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root_dir, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content
            
            # 1. Fix favicons globally (use absolute paths to /assets/)
            content = re.sub(r'href="(\.\./)+assets/favicon', 'href="/assets/favicon', content)
            content = re.sub(r'href="assets/favicon', 'href="/assets/favicon', content)
            
            content = re.sub(r'href="(\.\./)+assets/apple-touch', 'href="/assets/apple-touch', content)
            content = re.sub(r'href="assets/apple-touch', 'href="/assets/apple-touch', content)
            
            content = re.sub(r'href="(\.\./)+assets/site\.webmanifest', 'href="/assets/site.webmanifest', content)
            content = re.sub(r'href="assets/site\.webmanifest', 'href="/assets/site.webmanifest', content)

            # 2. Add smart navbar if missing
            if 'let lastScrollY$' not in content and '</body>' in content:
                content = content.replace('</body>', navbar_script + '\n</body>')

            # 3. Add FAQs to services pages
            if 'services' in root_dir and file in faq_data:
                # Add FAQ Schema
                if 'FAQPage' not in content and '</head>' in content:
                    schema = generate_faq_schema(file)
                    content = content.replace('</head>', schema + '\n</head>')
                
                # Add FAQ HTML
                if 'Frequently Asked Questions' not in content and '</main>' in content:
                    faq_html = generate_faq_html(file)
                    content = content.replace('</main>', faq_html + '\n</main>')
                    
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {file}")

print("Global updates completed.")
