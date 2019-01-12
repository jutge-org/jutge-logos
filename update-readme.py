#!/usr/bin/env python3

import glob


text = '''
# Logos for Jutge.org

'''

for png in glob.glob('*.png'):
    text += '''- %s\n\n  ![%s](%s)\n\n''' % (png, png, png)

with open('README.md', 'w') as file:
    file.write(text)
