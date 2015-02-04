#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def findpath(dir):
  filenames = os.listdir(dir)
  specials = re.findall(r'\S+__\w+__\S+', ' '.join(filenames))
  paths = []
  for filename in specials:
    paths.append(os.path.abspath(os.path.join(dir, filename)))
  return paths

def copydir(todir, paths):
  if not os.path.exists(todir):
    os.mkdir(todir)
  cmd = ''
  for filename in paths:
    shutil.copy(filename, os.path.join(todir, os.path.basename(filename)))
  return

def copyzip(tozip, paths):
  cmd = 'zip -j '+ tozip + ' ' + ' '.join(paths)  
  (status, output) = commands.getstatusoutput(cmd)
  return






def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  paths = []
  paths = findpath(args[0])
  
  if todir:
    copydir(todir, paths)
  elif tozip:
    copydir(tozip, paths)
  else:
    print '\n'.join(paths)

if __name__ == "__main__":
  main()
