import os

# Path to index.html
index_html_path = os.path.join(os.getcwd(), 'index.html')

# Path to style.css
style_css_path = os.path.join(os.getcwd(), 'css', 'style.css')

# Path to script.js
script_js_path = os.path.join(os.getcwd(), 'js', 'script.js')

# Add HTML to index.html
with open(index_html_path, 'a') as f:
    f.write('html')

# Add CSS to style.css
with open(style_css_path, 'a') as f:
    f.write('css')

# Add JavaScript to script.js
with open(script_js_path, 'a') as f:
    f.write('javascript')

# Print 'Done' in green
print('\033[92mDone\033[0m')