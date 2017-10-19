class Azure():
    _attribute_map = {"schema": {"key": "$schema", "type": "str"},
                      "contentVersion": {"key": "contentVersion", "type": "str"},
                      "parameters": {"key": "parameters", "type": "[]"},
                      "variables": {"key": "variables", "type": "[]"},
                      "resources": {"key": "resources", "type": "[]", "required": True}
                      }

    def __init__(self, parameters=None, variables=None, resources=None, outputs=None):
        self.schema = "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#"
        self.contentVersion = "1.0.0.0"
        if parameters is None:
            parameters = {}
        self.parameters = parameters
        if variables is None:
            variables = {}
        self.variables = variables
        if resources is None:
            resources = []
        self.resources = resources
        if outputs is None:
            outputs = {}
