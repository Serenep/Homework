import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames

list = glob.glob(pattern)
print(list)

# TODO: use os.path.getsize to find each file's size

for x in list:
    if os.path.getsize(x) > 0:
            print(os.path.basename(x), os.path.getsize(x))

# TODO: Add a test to only display files that are not zero length

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()





