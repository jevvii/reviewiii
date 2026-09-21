with open('public/module1.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if dark-theme is present
print('Has dark-theme class on html:', 'class="dark-theme"' in content)
