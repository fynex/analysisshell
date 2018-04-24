#! /usr/bin/ipython2 -i
# -*- coding: utf-8 -*-

import sys
import os

from inspect import getmembers, isfunction
from forbiddenfruit import curse

# Add local path to python path list
path_exec_dir = os.path.dirname( os.path.realpath(__file__) )
sys.path.append(path_exec_dir)

import num
import st
import obfus
import file
import mdns as dns
import pkgutil
import req
import give
import backdoor.unix
import attack.php
import attack.html


# def load_all_modules_from_dir(dirname):
#     for importer, package_name, _ in pkgutil.iter_modules([dirname]):
#         full_package_name = '%s.%s' % (dirname, package_name)
#         if full_package_name not in sys.modules:
#             module = importer.find_module(package_name
#                         ).load_module(full_package_name)
#             print module
#
# bd = load_all_modules_from_dir("bd")

def load(a_module, data_type):
    functions_list = [o for o in getmembers(a_module) if isfunction(o[1])]
    
    for name, func in functions_list:
        curse(data_type, name, func)



print """
[*] Usage
    The module describes the input value. So if you have
    an number and you want to parse it into a reversed
    binary string, you search in the module "number".

    Usable modules:
    * num
    * str
    * obfus
    * file
    * bd
    * dns
    * req
"""

