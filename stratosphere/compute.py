from stratosphere.template import Resource, SubResource


class VirtualMachine(Resource):
    """Microsoft.Compute/virtualMachines
    Args:
        name (str): The name of the resource
        location (str): The location of the resource
        description (str): a description of the resource
        tags: ({str}): a dictionary of tags
        dependsOn: ([]): a list of resources
        plan (Plan):  The purchase plan when deploying virtual machine from VM Marketplace images.
        resources ([Nitions/extensionsChild]):  
        hardwareProfile (HardwareProfile):  The hardware profile.
        storageProfile (StorageProfile):  The storage profile.
        osProfile (OSProfile):  The OS profile.
        networkProfile (NetworkProfile):  The network profile.
        diagnosticsProfile (DiagnosticsProfile):  The diagnostics profile.
        availabilitySet (SubResource):  The reference Id of the availability set to which the virtual machine belongs.
        licenseType (str):  Specifies that the image or disk that is being used was licensed on-premises.
            This element is only used for images that contain the Windows Server
            operating system.  
    """

    type = 'Microsoft.Compute/virtualMachines'
    apiVersion = '2016-04-30-preview'
    
    _attribute_map = {
        'apiVersion': {'key': 'apiVersion', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'str'},
        'dependsOn': {'key': 'dependsOn', 'type': '[str]'},
        'plan': {'key': 'plan', 'type': 'Plan'},
        'resources': {'key': 'resources', 'type': '[Nitions/extensionsChild]'},
        'hardwareProfile': {'key': 'properties.hardwareProfile', 'type': 'HardwareProfile'},
        'storageProfile': {'key': 'properties.storageProfile', 'type': 'StorageProfile'},
        'osProfile': {'key': 'properties.osProfile', 'type': 'OSProfile'},
        'networkProfile': {'key': 'properties.networkProfile', 'type': 'NetworkProfile'},
        'diagnosticsProfile': {'key': 'properties.diagnosticsProfile', 'type': 'DiagnosticsProfile'},
        'availabilitySet': {'key': 'properties.availabilitySet', 'type': 'SubResource'},
        'licenseType': {'key': 'properties.licenseType', 'type': 'str'}   
    }

    def __init__(self, name, location=None, description=None, tags=None, dependsOn=None, plan=None, resources=None, hardwareProfile=None, storageProfile=None, osProfile=None, networkProfile=None, diagnosticsProfile=None, availabilitySet=None, licenseType=None):
        self.name = name
        if location is None:
            location = '[resourceGroup().location]'
        self.location = location
        self.description = description
        self.tags = tags
        self.dependsOn = dependsOn
        self.plan = plan
        self.resources = resources
        self.hardwareProfile = hardwareProfile
        self.storageProfile = storageProfile
        self.osProfile = osProfile
        self.networkProfile = networkProfile
        self.diagnosticsProfile = diagnosticsProfile
        self.availabilitySet = availabilitySet
        self.licenseType = licenseType