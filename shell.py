#! /usr/bin/ipython2 -i
# -*- coding: utf-8 -*-

import sys
import os

# Add local path to python path list
path_exec_dir = os.path.dirname( os.path.realpath(__file__) )
sys.path.append(path_exec_dir)

import num
import str
import obfus
import file
import pkgutil
import req
import backdoor.unix
import attack.php


# def load_all_modules_from_dir(dirname):
#     for importer, package_name, _ in pkgutil.iter_modules([dirname]):
#         full_package_name = '%s.%s' % (dirname, package_name)
#         if full_package_name not in sys.modules:
#             module = importer.find_module(package_name
#                         ).load_module(full_package_name)
#             print module
#
# bd = load_all_modules_from_dir("bd")

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
"""

