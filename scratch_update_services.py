import os

filepath = 'c:/Users/inanj/OneDrive/Documents/GitHub/f9xr.github.io/pages/services.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_card = '''                    <a href="../services/talent-brand-management.html" class="service-card p-10 rounded-[3rem] group block relative overflow-hidden">
                        <div class="absolute -bottom-20 -right-20 w-64 h-64 bg-accent-blue/5 rounded-full blur-3xl group-hover:bg-accent-blue/10 transition-all"></div>
                        <i class="fas fa-star text-5xl text-accent-blue mb-8"></i>
                        <h3 class="text-3xl font-black mb-6 tracking-tighter uppercase">Talent & Brand Management</h3>
                        <p class="text-lg text-platinum/60 leading-relaxed mb-6">
                            Monetize your influence and scale your personal brand. End-to-end backend management, PR outreach, and direct pipelines to brand sponsorships.
                        </p>
                        <span class="inline-flex items-center gap-2 text-accent-blue font-black text-sm uppercase tracking-widest group-hover:gap-4 transition-all">
                            View Service <i class="fa-solid fa-arrow-right-long"></i>
                        </span>
                    </a>
'''

if 'talent-brand-management.html' not in content:
    # Insert right before the closing </div> of the grid, which is after the telegram-bot-development.html card
    insert_point = content.find('</a>', content.find('telegram-bot-development.html')) + 4
    
    # Wait, better yet, just replace the last card with last card + new card
    search_str = '</a>\\n                </div>\\n            </div>'
    
    if search_str in content:
        pass # Actually the exact formatting might vary.
        
    # Safe replacement
    # Just find the telegram bot card and append it after
    telegram_card_start = content.find('<a href="../services/telegram-bot-development.html"')
    telegram_card_end = content.find('</a>', telegram_card_start) + 4
    
    if telegram_card_start != -1:
        content = content[:telegram_card_end] + '\\n' + new_card + content[telegram_card_end:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated services.html successfully!")
    else:
        print("Could not find insertion point.")
else:
    print("services.html already contains the entry.")
