from stratosphere.azure import Azure
from stratosphere.aws import AWS

MAX_MAPPINGS = 100
MAX_OUTPUTS = 60
MAX_PARAMETERS = 6
MAX_RESOURCES = 200
PARAMETER_TITLE_MAX = 255
MAX_LENGTH = 24


class Template(Azure):

    def __init__(self, parameters=None, variables=None, resources=None, outputs=None, Description=None, Metadata=None):
        super().__init__()

    def handle_duplicate_key(self, key):
        raise ValueError('duplicate key "%s" detected' % key)

    def _update(self, attr, values):
        if isinstance(values, list):
            for v in values:
                if v.name in d:
                    self.handle_duplicate_key(v.name)
                attr[v.name] = v
        else:
            if values.name in attr:      
                self.handle_duplicate_key(values.name)
            if isinstance(attr, list): 
                attr.append(values)
            elif isinstance(attr, dict):
                attr[values.name] = values
            else:
                raise AttributeError('Wrong Input Type detected')
        return values

    def add_output(self, output):
        if len(self.outputs) >= MAX_OUTPUTS:
            raise ValueError('Maximum outputs %d reached' % MAX_OUTPUTS)
        return self._update(self.outputs, output)

    def add_parameter(self, parameter):
        if len(self.parameters) >= MAX_PARAMETERS:
            raise ValueError('Maximum parameters %d reached' % MAX_PARAMETERS)
        return self._update(self.parameters, parameter)

    def add_resource(self, resource):
        if len(self.resources) >= MAX_RESOURCES:
            raise ValueError('Maximum number of resources %d reached' % MAX_RESOURCES)
        return self._update( self.resources, resource)

    def add_version(self, version=None):
        if version:
            self.version = version
        else:
            self.version = "2010-09-09"

    def __str__(self):
        return   json.dumps(self)