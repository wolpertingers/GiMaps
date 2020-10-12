#!/usr/bin/python

import sys
import json
import argparse
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generates both a Maperitive script and a ruleset for it, based on a .json file with colors and geo bounds")
    parser.add_argument("name", type=str, 
                        help="Name of the city to create the rules for. Coordinates must be provided in the settings JSON file.")
    parser.add_argument("json", type=str, 
                        help="path to the .json file that holds the variable values.")
    parser.add_argument("--style", metavar="-S", type=str, 
                        help="Name of the style/theme that should be used for colouring the map.", 
                        default="navigator")
    parser.add_argument("--temp", metavar='-T', type=str, 
                        help="path to the template folder (contains rules.template & script.template).", 
                        default=Path("./Templates").resolve())
    parser.add_argument("--map", metavar='-M', type=str, 
                        help="if path to directory of OSM data is provided, the script will not download via overpass.", 
                        default=None)
    parser.add_argument("--out", metavar="-O", type=str, 
                        help="path to the output directory, default is the current one.", 
                        default=Path("../Maperitive").resolve())
    
    # parsing the arguments
    args = parser.parse_args()
    
    # finding and opening in the template file for the rules
    template_path = Path(args.temp).resolve()
    rules_template_file = open(template_path/"rules.template", 'r')
    
    # download OSM data or not?
    if args.map is not None:
        script_template_file = open(template_path/"disk_script.template", 'r')
    else:
        script_template_file = open(template_path/"web_script.template", 'r')
        
    # reading in the rules and script templates
    rules_template_str = rules_template_file.read()
    script_template_str = script_template_file.read()
    
    # loading and reading the data for filling the templates
    json_file = open(Path(args.json).resolve(), 'r')
    variable_dict = json.load(json_file)
    
    # setting output for the rules and generating it based on the JSON and the
    # template file
    output_path = Path(args.out).resolve()
    rules_output_str = rules_template_str.format(**variable_dict["styles"][f"{args.style}"])
    rules_output_file = open(output_path/f"Rules/{args.name}.mrules", 'w+')
    rules_output_file.write(rules_output_str)
    
    # setting output for the Maperitive script and generating it based on the 
    # JSON and the respective template file
    if args.map is not None:
        script_output_str = script_template_str.format(**variable_dict["locations"][f"{args.name}"], name=f"{args.name}", map_path=args.map)
    else:
        script_output_str = script_template_str.format(**variable_dict["locations"][f"{args.name}"], name=f"{args.name}")
    script_output_file = open(output_path/f"Scripts/{args.name}.mscript", 'w+')
    script_output_file.write(script_output_str)