import sys
def printAaron(num):
    for i in range(int(num)):
        print(i, 'Aaron')
if __name__ == '__main__':
    printAaron(sys.argv[1])