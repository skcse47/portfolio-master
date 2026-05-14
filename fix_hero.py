with open('app/components/homepage/hero-section/index.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# The bad string in the file
old_str = "\"'],\"}}"
new_str = "\"'],\"}"

print('old:', repr(old_str))
print('new:', repr(new_str))
print('Found:', old_str in content)

content = content.replace(old_str, new_str, 1)

with open('app/components/homepage/hero-section/index.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed!')
