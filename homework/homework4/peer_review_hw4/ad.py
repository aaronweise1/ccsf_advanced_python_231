''' Generators II
Write a program to lazily rewrap text from the filename passed
so that it fits an 80 column window without breaking any words.
Use a generator that yields the next lines of text,
each containing as many words as possible.
'''
import textwrap, sys

''' Please pass in a text file as an argument when you run this program.
I tested this code using a previous peer review .pr file in my directory.
'''

# generator that yields the next lines of text
def gen(txt_list):
	for i in txt_list:
		yield i

def main():
	# application code here
	file = open(sys.argv[1],'r+').read()
	# text output should fit an 80 column window without breaking any words
	# https://docs.python.org/3/library/textwrap.html
	columns = textwrap.wrap(text=file, width=80)
	# lazily rewrap text using yield in generator
	line_gen = gen(columns)

	try:
		# print out each line of file
		while True:
			# next returns next element of the stream
			print(next(line_gen))
	# exception raised by next method when there are no more items in iterator
	except StopIteration:
		pass

if __name__ == "__main__":
	main()

