from random import choice, randrange


charnames = set()
charlines = []
for line in open('data/the-office-lines-scripts.tsv'):
    splat = line.strip().split('\t')
    charlines.append((splat[5], splat[4]))
    charnames.add(splat[5])
charnames.remove('D')
charnames.remove('Michae')

def write_scene(lines):
    chars = set()
    ret = []
    prev_mention = None
    for _ in range(lines):
        x = choice(charlines)
        if len(chars) > 4 and x[0] not in chars:
            while x[0] not in chars:
                x = choice(charlines)

        if prev_mention:
            while x[0] is not prev_mention:
                x = choice(charlines)
            prev_mention = None

        for charname in charnames:
            if charname in x[1] and charname not in x[0]:
                prev_mention = charname
        chars.add(x[0])
        ret.append(f'{x[0]}:\t{x[1]}')
    return ret

with open('example_scripts.txt', 'w') as outfile:
    for i in range(1000):
        scene = '\n'.join(write_scene(randrange(4, 13)))
        outfile.write(f'\n\n{i}.\n{scene}')

# char_to_line = {}
# for line in open('data/the-office-lines-scripts.tsv'):
#     splat = line.strip().split('\t')
#     char_to_line[splat[5]] = char_to_line.get(splat[5], []) + [splat[4]]
#
# for k,v in char_to_line.items():
#     print(k, len(v))



