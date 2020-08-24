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

# y - positions in image for the 4 rows
rows = [399, 463, 526, 590]
# x - position for first key in the 4 rows
cols = [703, 95, 111, 143]
pos = []

# Position indexes (with qwerty keys)
# row 0: 0 -, 1 =
# row 1: 2 q, 3 w, 4 e, 5 r, 6 t, 7 y, 8 u, 9 i, 10 o, 11 p, 12 [, 13 ]
# row 2: 14 a, 15 s, 16 d, 17 f, 18 g, 19 h, 20 j, 21 k, 22 l, 23 ;, 24 '
# row 3: 25 z, 26 x, 27 c, 28 v, 29 b, 30 n, 31 m, 32,, 33 ., 34 /

# row 0
for i in range(0, 2):
    pos.append((cols[0] + i * 64, rows[0]))
# row 1
for i in range(2, 14):
    pos.append((cols[1] + (i - 2) * 64, rows[1]))
# row 2
for i in range(14, 25):
    pos.append((cols[2] + (i - 14) * 64, rows[2]))
# row 3
for i in range(25, 35):
    pos.append((cols[3] + (i - 25) * 64, rows[3]))

# tuple = (key, weight), 1 = green, 2 = yellow, 3 = red
qwerty_keys = {
        # row 0
        '-' : (0, 3),
        '_' : (0, 3),
        '=' : (1, 3),
        '+' : (1, 3),
        # row 1
        'q' : (2, 2),
        'w' : (3, 2),
        'e' : (4, 2),
        'r' : (5, 2),
        't' : (6, 3),
        'y' : (7, 3),
        'u' : (8, 2),
        'i' : (9, 2),
        'o' : (10, 2),
        'p' : (11, 2),
        '[' : (12, 3),
        '{' : (12, 3),
        ']' : (13, 3),
        '}' : (13, 3),
        # row 2
        'a' : (14, 1),
        's' : (15, 1),
        'd' : (16, 1),
        'f' : (17, 1),
        'g' : (18, 2),
        'h' : (19, 2),
        'j' : (20, 1),
        'k' : (21, 1),
        'l' : (22, 1),
        ';' : (23, 1),
        ':' : (23, 1),
        '\'' : (24, 2),
        '"' : (24, 2),
        # row 3
        'z' : (25, 2),
        'x' : (26, 2),
        'c' : (27, 2),
        'v' : (28, 2),
        'b' : (29, 3),
        'n' : (30, 2),
        'm' : (31, 2),
        ',' : (32, 2),
        '<' : (32, 2),
        '.' : (33, 2),
        '>' : (33, 2),
        '/' : (34, 2),
        '?' : (34, 2),
        }

colemak_keys = {
        # row 0
        '-' : (0, 3),
        '_' : (0, 3),
        '=' : (1, 3),
        '+' : (1, 3),
        # row 1
        'q' : (2, 2),
        'w' : (3, 2),
        'f' : (4, 2),
        'p' : (5, 2),
        'g' : (6, 3),
        'j' : (7, 3),
        'l' : (8, 2),
        'u' : (9, 2),
        'y' : (10, 2),
        ';' : (11, 2),
        ':' : (11, 2),
        '[' : (12, 3),
        '{' : (12, 3),
        ']' : (13, 3),
        '}' : (13, 3),
        # row 2
        'a' : (14, 1),
        'r' : (15, 1),
        's' : (16, 1),
        't' : (17, 1),
        'd' : (18, 2),
        'h' : (19, 2),
        'n' : (20, 1),
        'e' : (21, 1),
        'i' : (22, 1),
        'o' : (23, 1),
        '\'' : (24, 2),
        '"' : (24, 2),
        # row 3
        'z' : (25, 2),
        'x' : (26, 2),
        'c' : (27, 2),
        'v' : (28, 2),
        'b' : (29, 3),
        'k' : (30, 2),
        'm' : (31, 2),
        ',' : (32, 2),
        '<' : (32, 2),
        '.' : (33, 2),
        '>' : (33, 2),
        '/' : (34, 2),
        '?' : (34, 2),
        }

# x + 960
dvorak_keys = {
        # row 0
        '[' : (0, 3),
        '{' : (0, 3),
        ']' : (1, 3),
        '}' : (1, 3),
        # row 1
        '\'' : (2, 2),
        '"' : (2, 2),
        ',' : (3, 2),
        '<' : (3, 2),
        '.' : (4, 2),
        '>' : (4, 2),
        'p' : (5, 2),
        'y' : (6, 3),
        'f' : (7, 3),
        'g' : (8, 2),
        'c' : (9, 2),
        'r' : (10, 2),
        'l' : (11, 2),
        '/' : (12, 3),
        '?' : (12, 3),
        '=' : (13, 3),
        '+' : (13, 3),
        # row 2
        'a' : (14, 1),
        'o' : (15, 1),
        'e' : (16, 1),
        'u' : (17, 1),
        'i' : (18, 2),
        'd' : (19, 2),
        'h' : (20, 1),
        't' : (21, 1),
        'n' : (22, 1),
        's' : (23, 1),
        '-' : (24, 2),
        '_' : (24, 2),
        ';' : (25, 2),
        ':' : (25, 2),
        'q' : (26, 2),
        'j' : (27, 2),
        'k' : (28, 2),
        'x' : (29, 3),
        'b' : (30, 2),
        'm' : (31, 2),
        'w' : (32, 2),
        'v' : (33, 2),
        'z' : (34, 2),
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

imgix = 0

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

    savename = 'output/img_' + '{:05d}'.format(imgix) + '.png'
    imgix += 1

    # Background
    im = Image.open('background.png')
    d = ImageDraw.Draw(im)
    currix = 0

    # Draw circles for current character
    #key_weight = colemak_keys[curchar]
    key_weight = qwerty_keys[curchar]
    key = key_weight[0]
    weight = key_weight[1]
    x = pos[key][0]
    y = pos[key][1]
    qscore = weight
    d.ellipse((x + 4, y + 4, x + 60, y + 60), outline = 'blue', width = 5)
    if qscore == 1:
        gq += 1
    elif qscore == 2:
        yq += 1
    elif qscore == 3:
        rq += 1

    key_weight = dvorak_keys[curchar]
    key = key_weight[0]
    weight = key_weight[1]
    x = pos[key][0] + 960
    y = pos[key][1]
    dscore = weight
    d.ellipse((x + 4, y + 4, x + 60, y + 60), outline = 'blue', width = 5)
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

