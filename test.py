import os,sys,inspect

from stratosphere import *

DEBUG=False

if DEBUG:
    print(sys.modules)
    print('')
    print('')

# generate template 
t = Template()
print(dumps(t))

#print('SchemeURL: '+ t.schema )
print( 'Anything else: '+str(t.__dict__) )


