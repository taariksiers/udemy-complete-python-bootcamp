# Lecture 96 StringIO

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

message = 'This is just a normal string'
f = StringIO(message) 
# now we have an object that we will be able to treat like a file
print(f.read())
