#!/usr/bin/python

import sys
import json
import argparse
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generates both a Maperitive script and a ruleset for it, based on a .json file with colors and geo bounds")
    parser.add_argument("--name", metavar="-N", type=str, help="Name of the city to create the rules for", default="default")
    parser.add_argument("template_path", metavar='T', type=str, help="path to the template folder (contains rules.template & script.template)")
    parser.add_argument("--download", metavar='-d', type=str, help="if path to directory of OSM data is provided, the script will not download via overpass.")
    parser.add_argument("json_path", metavar='J', type=str, help="path to the .json file that holds the variable values")
    parser.add_argument("--output_path", metavar="-O", type=str, help="path to the output directory, default is the current one", default=".")
    
    args = parser.parse_args()
    
    template_path = Path(args.template_path).resolve()
    rules_template_file = open(template_path/"rules.template", 'r')
    
    if args.download is not None:
        script_template_file = open(template_path/"disk_script.template", 'r')
    else:
        script_template_file = open(template_path/"web_script.template", 'r')
        
    rules_template_str = rules_template_file.read()
    script_template_str = script_template_file.read()
    
    json_file = open(Path(args.json_path).resolve(), 'r')
    variable_dict = json.load(json_file)
    
    output_path = Path(args.output_path).resolve()
    rules_output_str = rules_template_str.format(**variable_dict["colors"])
    rules_output_file = open(output_path/f"Rules/{args.name}.mrules", 'w+')
    rules_output_file.write(rules_output_str)
    
    script_output_str = script_template_str.format(**variable_dict[f"{args.name}"], map_path=args.download)
    script_output_file = open(output_path/f"Scripts/{args.name}.mscript", 'w+')
    script_output_file.write(script_output_str)