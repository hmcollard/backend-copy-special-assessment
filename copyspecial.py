#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Haley Collard with help from study hall demo"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    files = os.listdir(dirname)
    special_files = []
    for f in files:
        if re.search(r'__\w+__', f):
            special_files.append(os.path.abspath(os.path.join(dirname, f)))
    return special_files


def copy_to(path_list, dest_dir):
    """Copy special files to new directory"""
    if dest_dir not in os.listdir('.'):
        os.makedirs(dest_dir)
    for path in path_list:
        shutil.copy(path, dest_dir)


def zip_to(path_list, dest_zip):
    """Zip special files."""
    cmd = ['zip', '-j', dest_zip]
    cmd.extend(path_list)
    print("Command I'm going to do:")
    print(' '.join(cmd))
    subprocess.check_output(cmd)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'from_dir', help='dirname to check for special files')
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions

    special_files = get_special_paths(ns.from_dir)

    if len(args) < 1:  # might need (ns)
        print('usage: python copyspecial.py from_dir' +
              '{--todir dir | --tozip zipfile}')
        sys.exit(1)

    if ns.todir:
        copy_to(special_files, ns.todir)
    elif ns.tozip:
        zip_to(special_files, ns.tozip)
    else:
        print("\n".join(special_files))


if __name__ == "__main__":
    main(sys.argv[1:])
