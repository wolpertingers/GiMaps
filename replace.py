#!/usr/bin/python

import sys
import json
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Replaces color variables in a .template file and writes a .mrules file")
    parser.add_argument("template_path", metavar='T', type=str, help="path to the template file (.template)")
    parser.add_argument("json_path", metavar='J', type=str, help="path to the .json file that holds the variable values")
    parser.add_argument("output_path", metavar="O", type=str, help="path to the output file (.mrules")
    
    args = parser.parse_args()
    
    template_file = open(args.template_path, 'r')
    template_str = template_file.read()
    
    json_file = open(args.json_path, 'r')
    variable_dict = json.load(json_file)
    
    output_str = template_str.format(**variable_dict)
    output_file = open(args.output_path, 'w')
    output_file.write(output_str)