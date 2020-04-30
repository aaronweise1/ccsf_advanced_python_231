import concurrent.futures
import sys

pool = concurrent.futures.ThreadPoolExecutor()

def utf8_check(path, encod='UTF-8'):
  fo = open(path, "rb").read()
  try:
    fo.decode("utf-8")
    print(f'{path} is in UTF-8')
  except UnicodeDecodeError:
    print(f'{path} is NOT in utf-8')


pool.map(utf8_check, sys.argv[1:])
