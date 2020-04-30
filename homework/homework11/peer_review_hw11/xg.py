# Write a universal wrapper program that expects its command line arguments to
# contain the absolute path to any program, followed by its arguments. The
# wrapper should run that program and report its exit value

import subprocess
import sys

# version 1:
# * short version that works for simple commands
# * reports exit code by passing it to parent process; to see, use:  echo $? 
# sys.exit(subprocess.run(sys.argv[1:]).returncode)


# version 2:
# * slightly longer version that uses 'legacy' function
# * easy way to make wildcard expansion and pipes work; can be use for e.g.:
# python runprog.py find . -name \'*.py\' \| xargs grep import
result = subprocess.getstatusoutput(' '.join(sys.argv[1:]))
print(result[1])
sys.exit(result[0])
# note: exit code could be easily added to output here - not doing it because
# I think passing to parent process is cleaner
