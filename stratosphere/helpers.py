#
# This is a string helper class proving tsring mixins helper function 
# used in all this gem
#
import json
from stratosphere.azure import Azure
from stratosphere.template import Template


class TemplateFunction(object):
    pass

def quote(e):
    if isinstance(e, TemplateFunction):
        return str(e)
    elif isinstance(e, str):
        return "'{}'".format(e)
    else:
        return str(e)

class _raw(TemplateFunction):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

class parameters(TemplateFunction):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "parameters('{}')".format(self.name)

class variables(TemplateFunction):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "variables('{}')".format(self.name)

class uniqueString(TemplateFunction):
    def __init__(self, *args):
        self.args = args
    def __str__(self):
        return "uniqueString({})".format(", ".join(map(quote, self.args)))


class concat(TemplateFunction):
    def __init__(self, *args):
        self.args = args
    def __str__(self):
        return "concat({})".format(", ".join(map(quote, self.args)))

class resourceId(TemplateFunction):
    def __init__(self, type_, name):
        self.type_ = type_
        self.name = name
    def __str__(self):
        return "resourceId({}, {})".format(quote(self.type_), quote(self.name))

def _raise_type(self, name, value, expected_type):
    raise TypeError('%s: %s.%s is %s, expected %s' % (self.__class__,
                                                      self.title,
                                                      name,
                                                      type(value),
                                                      expected_type))

def validate_title(self):
    if not valid_names.match(self.title):
        raise ValueError('Name "%s" not alphanumeric' % self.title)


def validate(self):
    pass

def dump(obj):
    if isinstance(obj, Template):
        res = {}
        for k, d in obj._attribute_map.items():
            if hasattr(obj, k) and (getattr(obj, k) or d.get("required", False)):
                value = getattr(obj, k)
                key = d["key"]
                parts = key.split(".")
                if len(parts) == 2:
                    sub, key = parts
                    if not sub in res:
                        res[sub] = {}
                    res[sub][key] = dump(value)
                else:
                    res[key] = dump(value)
    elif isinstance(obj, TemplateFunction):
        res = "[{}]".format(obj)
    elif isinstance(obj, dict):
        res = {key: dump(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        res = [dump(value) for value in obj]
    else:
        res = obj
    return res

def dumps(obj):
    return json.dumps(dump(obj), indent=2)