#!/usr/bin/env python

from PIL import Image, ImageDraw, ImageFont

# Corpus text (first paragraph of Brave New World)
sa =  [ 'The enormous room on the ground floor faced towards the north. Cold for all the summer beyond the panes,',
        'for all the tropical heat of the room itself, a harsh thin light glared through the windows, hungrily seeking',
        'some draped lay figure, some pallid shape of academic goose-flesh, but finding only the glass and nickel and',
        'bleakly shining porcelain of a laboratory. Wintriness responded to wintriness. The overalls of the workers were',
        'white, their hands gloved with a pale corpse-coloured rubber. The light was frozen, dead, a ghost. Only from',
        'the yellow barrels of the microscopes did it borrow a certain rich and living substance, lying along the',
        'polished tubes like butter, streak after luscious streak in long recession down the work tables.'
        ]


# x,y = coordinates in background.png image for each colored key
# tuple = x, y, weight (1 = green, 2 = yellow, 3 = red)
qwerty_keys = {
        '-' : (703, 399, 3),
        '_' : (703, 399, 3),
        '=' : (767, 399, 3),
        '+' : (767, 399, 3),
        'q' : (95, 463, 2),
        'w' : (159, 463, 2),
        'e' : (223, 463, 2),
        'r' : (287, 463, 2),
        't' : (351, 463, 3),
        'y' : (415, 463, 3),
        'u' : (479, 463, 2),
        'i' : (543, 463, 2),
        'o' : (607, 463, 2),
        'p' : (671, 463, 2),
        '[' : (735, 463, 3),
        '{' : (735, 463, 3),
        ']' : (799, 463, 3),
        '}' : (799, 463, 3),
        'a' : (111, 526, 1),
        's' : (175, 526, 1),
        'd' : (239, 526, 1),
        'f' : (303, 526, 1),
        'g' : (367, 526, 2),
        'h' : (431, 526, 2),
        'j' : (495, 526, 1),
        'k' : (559, 526, 1),
        'l' : (623, 526, 1),
        ';' : (687, 526, 1),
        ':' : (687, 526, 1),
        '\'' : (751, 526, 2),
        '"' : (751, 526, 2),
        'z' : (143, 590, 2),
        'x' : (207, 590, 2),
        'c' : (271, 590, 2),
        'v' : (335, 590, 2),
        'b' : (399, 590, 3),
        'n' : (463, 590, 2),
        'm' : (527, 590, 2),
        ',' : (591, 590, 2),
        '<' : (591, 590, 2),
        '.' : (655, 590, 2),
        '>' : (655, 590, 2),
        '/' : (719, 590, 2),
        '?' : (719, 590, 2),
        }

# x + 960
dvorak_keys = {
        '[' : (703, 399, 3),
        '{' : (703, 399, 3),
        ']' : (767, 399, 3),
        '}' : (767, 399, 3),
        '\'' : (95, 463, 2),
        '"' : (95, 463, 2),
        ',' : (159, 463, 2),
        '<' : (159, 463, 2),
        '.' : (223, 463, 2),
        '>' : (223, 463, 2),
        'p' : (287, 463, 2),
        'y' : (351, 463, 3),
        'f' : (415, 463, 3),
        'g' : (479, 463, 2),
        'c' : (543, 463, 2),
        'r' : (607, 463, 2),
        'l' : (671, 463, 2),
        '/' : (735, 463, 3),
        '?' : (735, 463, 3),
        '=' : (799, 463, 3),
        '+' : (799, 463, 3),
        'a' : (111, 526, 1),
        'o' : (175, 526, 1),
        'e' : (239, 526, 1),
        'u' : (303, 526, 1),
        'i' : (367, 526, 2),
        'd' : (431, 526, 2),
        'h' : (495, 526, 1),
        't' : (559, 526, 1),
        'n' : (623, 526, 1),
        's' : (687, 526, 1),
        '-' : (751, 526, 2),
        '_' : (751, 526, 2),
        ';' : (143, 590, 2),
        ':' : (143, 590, 2),
        'q' : (207, 590, 2),
        'j' : (271, 590, 2),
        'k' : (335, 590, 2),
        'x' : (399, 590, 3),
        'b' : (463, 590, 2),
        'm' : (527, 590, 2),
        'w' : (591, 590, 2),
        'v' : (655, 590, 2),
        'z' : (719, 590, 2),
        }

# Coordinates for counters
qwerty_count = {
        'r' : (529, 811),
        'y' : (529, 882),
        'g' : (529, 950),
        }

dvorak_count = {
        'r' : (1110, 811),
        'y' : (1110, 882),
        'g' : (1110, 950),
        }

l = 0
for s in sa:
    l += len(s)

# Font
fnt = ImageFont.truetype('/usr/share/fonts/ubuntu-font-family/UbuntuMono-R.ttf', 32)
dx, dy = fnt.getsize('A')

# sx, sy = corpus text start coordinates, dy = offset between lines
sx = 66
sy = 39
dy = 38

# Counters, rq = red qwerty etc
rq = 0
yq = 0
gq = 0
rd = 0
yd = 0
gd = 0

# Loop through each character in corpus text
for i in range(l):
    # get curchar
    currix = 0
    curchar = ''
    for line_ix in range(len(sa)):
        s = sa[line_ix]
        if i >= currix and i < (currix + len(s)):
            line_i = i - currix
            curchar = s[line_i].lower()
        currix += len(s)
    # Skip keys that are not colored
    if curchar == ' ' or (not curchar in qwerty_keys) or (not curchar in dvorak_keys):
        continue

    savename = 'output/img_' + '{:05d}'.format(i) + '.png'
    # Background
    im = Image.open('background.png')
    d = ImageDraw.Draw(im)
    currix = 0

    # Draw circles for current character
    qwerty = qwerty_keys[curchar]
    x = qwerty[0]
    y = qwerty[1]
    d.ellipse((x + 4, y + 4, x + 60, y + 60), outline = 'blue', width = 5)
    qscore = qwerty[2]
    if qscore == 1:
        gq += 1
    elif qscore == 2:
        yq += 1
    elif qscore == 3:
        rq += 1

    dvorak = dvorak_keys[curchar]
    x = dvorak[0] + 960
    y = dvorak[1]
    d.ellipse((x + 4, y + 4, x + 60, y + 60), outline = 'blue', width = 5)
    dscore = dvorak[2]
    if dscore == 1:
        gd += 1
    elif dscore == 2:
        yd += 1
    elif dscore == 3:
        rd += 1

    # Draw corpus text
    for line_ix in range(len(sa)):
        x = sx
        y = sy + dy * line_ix
        s = sa[line_ix]
        if i >= currix and i < (currix + len(s)):
            # i is on current line
            line_i = i - currix
            txt_left = s[:line_i]
            txt_right = s[line_i + 1:]
            d.text((x + dx * line_i, y), s[line_i], font=fnt, fill='blue', stroke_width = 1)
            d.text((x + dx * (line_i + 1), y), txt_right, font=fnt, fill=(0, 0, 0))
        else:
            txt_left = s

        d.text((x, y), txt_left, font=fnt, fill=(0, 0, 0))
        currix += len(s)

    # Draw counts
    x = qwerty_count['r'][0]
    y = qwerty_count['r'][1]
    d.text((x, y), str(rq), font=fnt, fill=(0, 0, 0))
    x = dvorak_count['r'][0]
    y = dvorak_count['r'][1]
    d.text((x, y), str(rd), font=fnt, fill=(0, 0, 0))
    x = qwerty_count['g'][0]
    y = qwerty_count['g'][1]
    d.text((x, y), str(gq), font=fnt, fill=(0, 0, 0))
    x = dvorak_count['g'][0]
    y = dvorak_count['g'][1]
    d.text((x, y), str(gd), font=fnt, fill=(0, 0, 0))
    x = qwerty_count['y'][0]
    y = qwerty_count['y'][1]
    d.text((x, y), str(yq), font=fnt, fill=(0, 0, 0))
    x = dvorak_count['y'][0]
    y = dvorak_count['y'][1]
    d.text((x, y), str(yd), font=fnt, fill=(0, 0, 0))

    im.save(savename)
    im.close()

