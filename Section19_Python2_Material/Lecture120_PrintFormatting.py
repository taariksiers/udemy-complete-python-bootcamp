s = 'String'

print 'Place my variable here: %s' %(s)
print 'Floating point number: %1.2f' %(13.145)
print 'Floating point number: %1.3f' %(13.145)
print 'Floating point number: %21.3f' %(13.145)

# conversion format methods
print 'Convert to string %r' %(123)
print 'First: %s, Second %s, Third %s' %('hi!', 'two', 3)

print 'First: %s, Second: %s' %(2,2)
print 'First: {x}, Third {y} Second: {x}' . format(x='inserted',y='two!')

# python3 uses the print function not the print statement
# from __future__ import print_function
