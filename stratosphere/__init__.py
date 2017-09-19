# Copyright (c) 2012-2017, Andreas Heumaier<andreas.heumaier@microsoft.com>
# All rights reserved.
#
# See LICENSE file for full license.


import collections
import json
import re
import sys
import types

from stratosphere.azure import Azure
from stratosphere.aws import AWS
from stratosphere.template import Template
from stratosphere.helpers import *
from stratosphere.compute import *



__version__ = "0.0.1"

valid_names = re.compile(r'^[a-zA-Z0-9]+$')

# Template Limits
MAX_MAPPINGS = 100
MAX_OUTPUTS = 60
MAX_PARAMETERS = 60
MAX_RESOURCES = 200
PARAMETER_TITLE_MAX = 255
MAX_LENGTH=24