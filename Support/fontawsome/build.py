"""
Source:

https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/metadata/icons.json

"""

import json
import os
import sys

with open(os.path.join(os.path.dirname(__file__), 'icons.json')) as json_file:
    data = json.load(json_file)

need_icons = []
prefixes = {'brands': 'fab', 'solid': 'fas', 'regular': 'far'}
for icon_name in data.keys():
    icon = data[icon_name]
    styles = icon['styles']
    lable = icon['label']

    for style in styles:
        prefix = prefixes[style]
        value = '{0} fa-{1}'.format(prefix, icon_name)
        need_icons.append(
            '{{name: "{0} ({1})", value: "{2}"}}'.format(lable, style, value)
        )

out = sys.stdout.write(', \\\n'.join(need_icons))
