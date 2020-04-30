# To tun the code use "python3 file.py file.txt"

from sys import argv

def get_line(file):
    line = get_line_80()
    new_line = ""
    for text_line in open(file, 'r'):
        for word in text_line.split():
            if len(new_line) < 81 and (len(new_line) + len(f" {word}") > 80):
                line = get_line_80()
                yield new_line
            next(line)
            new_line = line.send(word)

    yield new_line


def get_line_80():
    new_line = ''
    while True:
        input_word = yield
        if not new_line:
            new_line = input_word
        else:
            new_line += f' {input_word}'
        yield new_line

filename = argv[1]

for line in get_line(filename):
    print(line)

