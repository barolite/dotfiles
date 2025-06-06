# this script convers colors to translucent colors for waybar

import re

input_path = "/home/barolite/.cache/wal/colors-waybar.css"
output_path = "/home/barolite/.config/waybar/colors_translucent.css"
alpha = "0.5"  # 50% opacity

def hex_to_rgba(hex_code, alpha):
    hex_code = hex_code.lstrip('#')
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    return f"rgba({r}, {g}, {b}, {alpha})"

with open(input_path, "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # look for lines like: @define-color name #rrggbb;
    match = re.match(r"(\s*@define-color\s+)([^\s]+)(\s+)#([0-9a-fA-F]{6})(;)", line)
    if match:
        prefix, name, spacing, hex_code, suffix = match.groups()
        rgba = hex_to_rgba(hex_code, alpha)
        new_name = name + "t"
        new_line = f"{prefix}{new_name}{spacing}{rgba}{suffix}\n"
        new_lines.append(new_line)
    else:
        new_lines.append(line)

with open(output_path, "w") as f:
    f.writelines(new_lines)

print(f"✅ Transparent color file saved to: {output_path}")

