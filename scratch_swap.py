import re

with open('directories/product-launch-directories.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to swap the "We Do For You Banner" section with the "Live Launch Directories" section.
# The banner has: <!-- We Do For You Banner --> ... </section>
# The directories list has: <div class="mb-12 ... id="launch-directories"> or similar. Let's find it.

we_do_match = re.search(r'<!-- We Do For You Banner -->\s*<section.*?We Do For You\..*?</section>', content, re.DOTALL)
if we_do_match:
    we_do_html = we_do_match.group(0)
    # Remove it from content
    content = content.replace(we_do_html, '')
    
    # Now find where the list ends and insert it after.
    # We can insert it right before </main>
    content = content.replace('</main>', we_do_html + '\n</main>')
    
    with open('directories/product-launch-directories.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Swapped sections.")
else:
    print("Could not find We Do For You section.")
