from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
patterns = [re.compile(r"href\s*=\s*['\"].*logout.*['\"]", re.IGNORECASE),
            re.compile(r"\{\%\s*url\s+['\"]logout['\"]\s*\%\}", re.IGNORECASE),
            re.compile(r'/logout/')]

for file in root.rglob('*'):
    if file.is_file() and file.suffix.lower() in {'.html', '.htm', '.py', '.txt', '.js'}:
        text = file.read_text('utf-8', errors='ignore')
        matches = []
        for pat in patterns:
            for m in pat.finditer(text):
                start = max(0, m.start() - 40)
                end = min(len(text), m.end() + 40)
                snippet = text[start:end].replace('\n', ' ').strip()
                matches.append((m.group(0), snippet))
        if matches:
            print(file)
            for m, snippet in matches:
                print('  ', m, '=>', snippet)
            print()