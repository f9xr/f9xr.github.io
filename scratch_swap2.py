import re

with open('directories/product-launch-directories.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Match the exact block
start_str = '        <!-- We Do For You Banner -->'
end_str = '        </section>'

start_idx = content.find(start_str)
if start_idx != -1:
    end_idx = content.find(end_str, start_idx) + len(end_str)
    we_do_html = content[start_idx:end_idx]
    
    # Remove from original position
    content = content[:start_idx] + content[end_idx:]
    
    # Insert right before </main>
    main_end = content.find('</main>')
    if main_end != -1:
        content = content[:main_end] + '\n' + we_do_html + '\n' + content[main_end:]
        with open('directories/product-launch-directories.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Swapped sections successfully.")
    else:
        print("Could not find </main>.")
else:
    print("Could not find start string.")
