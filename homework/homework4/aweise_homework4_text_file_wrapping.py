import sys 


# Rewrites line to be under the 80 character limit 
# and yields the truncated line
def constructLine(text_line):
    cur_len = 0
    max_len = 80
    line = ''
    word_array = text_line.split()
    for index,word in enumerate(word_array):
        cur_len = len(line)
        if cur_len + len(word) > max_len:
            yield line
            line = word + ' '
            cur_len = 0
        else:
            line = line + word + ' '
    yield line[:-1]


# Iterates through each line of the text file 
# and prints the new wrapped line
def wrapFileText(text_file):
    for line in text_file:
        for wrapped_line in constructLine(line):
            print(wrapped_line)


# Validates if a correct file was given. 
# Continues to word wrapping if so, returns error if not
def validateFile(file_path):
    if len(file_path) > 1:
        try:
            text_file = open(file_path[1],'r')
            wrapFileText(text_file)
            text_file.close()
        except FileNotFoundError:
            sys.stdout.write('The file given does not exist. \n')
    else:
        sys.stdout.write('File path not given. Please include a file path. \n')


validateFile(sys.argv)