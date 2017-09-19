stratoshere
=====
Python library to create Azure Resource Templates

Overview
--------

Azure Resource Template Generator

Installation / Usage
--------------------

To install use pip:

    $ pip install stratosphere


Or clone the repo:

    $ git clone https://github.com/aheumaier/stratosphere.git
    $ python setup.py install


Contributing
------------

Peter Hoffmann
Andreas Heumaier

Example
-------
A simple example to create an instance would look like this::
```
from stratoshere.base import Template, dumps
from stratoshere.compute import OSDisk, ImageReference, OSProfile, StorageProfile, LinuxConfiguration, SshPublicKey, NetworkProfile, VirtualHardDisk, SshConfiguration, VirtualMachine, HardwareProfile
from stratoshere.storage import StorageAccount, Sku
from stratoshere.network import VirtualNetwork, PublicIPAddress, IpConfiguration, AddressSpace, Subnet, Id, NetworkInterface
from stratoshere.func import uniqueString, _raw, resourceId, concat

vmname = "testvm"
vmsize = "Standard_DS3_v2"
storagetype = "Standard_LRS"
storagename = "teststorage"
admin_user = "testuser"
ssh_key = open("id_rsa.pub").read()


vnet = VirtualNetwork(name="vnet1",
                      addressSpace=AddressSpace(['192.168.0.0/24']),
                      subnets=[Subnet("default", addressPrefix='192.168.0.0/24')])


public_ip = PublicIPAddress(name="{}public".format(vmname),
                            publicIPAllocationMethod="Dynamic",
                            idleTimeoutInMinutes=4
                            )

network_interface = NetworkInterface(
    name="{}ic".format(vmname),
    ipConfigurations=[
        IpConfiguration(
            name="{}-ip-config".format(vmname),
            subnet=Id(concat(resourceId(vnet.type, vnet.name), '/subnets/', 'default')),
            privateIPAllocationMethod="Static",
            privateIPAddress='192.168.0.5',
            publicIPAddress=Id(resourceId(public_ip.type, public_ip.name)))],
    enableIPForwarding=False,
    dependsOn=[resourceId(public_ip.type, public_ip.name),
               resourceId(vnet.type, vnet.name)]
)

storage = StorageAccount(
    name=concat(
        uniqueString(
            _raw("subscription().subscriptionId"),
            _raw("resourceGroup().name")),
        storagename),
    sku=Sku(name=storagetype),
    kind="Storage")

osdisk = OSDisk(
    name="{}-osdisk".format(vmname),
    caching="None",
    createOption="FromImage",
    vhd=VirtualHardDisk(
        concat(
            "https://",
            storage.name,
            ".blob.core.windows.net/vhds/",
            vmname,
            "-osdisk.vhd")))

storage_profile = StorageProfile(
    osDisk=osdisk,
    imageReference=ImageReference(
        publisher="credativ",
        offer="Debian",
        sku="8",
        version="latest"))

os_profile = OSProfile(
    computerName=vmname,
    adminUsername=admin_user,
    linuxConfiguration=LinuxConfiguration(disablePasswordAuthentication=True,
                                          ssh=SshConfiguration([SshPublicKey("/home/{}/.ssh/authorized_keys".format(admin_user), ssh_key)])))

network_profile = NetworkProfile([Id(resourceId(network_interface.type, network_interface.name))])

vm = VirtualMachine(name=vmname,
                    dependsOn=[resourceId(storage.type, storage.name),
                               resourceId(network_interface.type, network_interface.name),
                               resourceId(public_ip.type, public_ip.name),
                               ],
                    hardwareProfile=HardwareProfile(vmSize=vmsize),
                    storageProfile=storage_profile,
                    osProfile=os_profile,
                    networkProfile=network_profile)

t = Template(resources=[vnet, vm, network_interface, public_ip, storage])
print(dumps(t))
```
Documentation
-------------
Clone the resource manager json schemas

    $ git clone https://github.com/Azure/azure-resource-manager-schemas.git

Clone Azure Management Python Api

    $ git clone https://github.com/Azure/azure-sdk-for-python.git

Azure Compute Models

https://github.com/Azure/azure-sdk-for-python/tree/master/azure-mgmt-compute/azure/mgmt/compute/models