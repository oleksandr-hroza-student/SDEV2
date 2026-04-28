import io
import re

po_path = "translations/ja_JP/LC_MESSAGES/messages.po"

with io.open(po_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern to collapse contiguous quoted lines inside msgid or msgstr blocks
pattern = re.compile(r'(msg(id|str)\s+""\n)((?:".*"\n)+)', re.M)

def join_lines(match):
    head = match.group(1)
    body = match.group(3)
    # Extract all "..." strings and join them
    lines = re.findall(r'"(.*)"', body)
    joined = '"' + ''.join(lines) + '"\n'
    return head + joined

new_text = pattern.sub(join_lines, text)

with io.open(po_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print('Normalized PO file:', po_path)
