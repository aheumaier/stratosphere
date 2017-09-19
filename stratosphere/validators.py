# Copyright (c) 2012-2017, Andreas Heumaier<andreas.heumaier@microsoft.com>
# All rights reserved.
#
# See LICENSE file for full license.

def integer(x):
    if x in [True, 1, '1', 'true', 'True']:
        return "true"
    if x in [False, 0, '0', 'false', 'False']:
        return "false"
    raise ValueError
