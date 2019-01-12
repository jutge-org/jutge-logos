#!/usr/bin/env python3

import glob


text = '''
# Logos for Jutge.org

'''

for png in sorted(glob.glob('*.png')):
    text += '''- %s\n\n  <a href='%s'><img src='%s' height='200'></a>\n\n''' % (png, png, png)

with open('README.md', 'w') as file:
    file.write(text)
