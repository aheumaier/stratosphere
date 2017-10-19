import os,sys,inspect

from stratosphere import *


DEBUG=False

# generate template 
template = Template()

vm_instance = template.add_resource( VirtualMachine(
    location = 'westus',
    hardware_profile ='HardwareProfile(vmSize=vmsize)',
    storage_profile ='storage_profile',
    os_profile ='os_profile',
    network_profile ='network_profile'
))

print(dumps(template))


