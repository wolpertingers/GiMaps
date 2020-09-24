# :globe_with_meridians:  GiMaps

Beautiful maps of places where a gorgeous human once lived.

## Usage
Frist, clone repo an `cd` into it.

Then, edit the `default.json` or create a new JSON file inside the *Colors* directory to your liking. Aside from the colors, also edit/add your city and its geo bounds.

Now run the little python program 
```
python generate.py /your/templates/folder /your/json/file.json --name your-city
```
You should then have a *Scripts* folder. It contains a `.mscript` file with the name of your city. You can use it to run
```
Maperitive /path/to/Scripts/your-city.mscript
```
Note that this command will download all the data inside the geo bounds you have defined in the JSON file and save it to `./Maps/you-city.osm`. If you want to rerun the script but not download all the data again (the OSM servers are already overloaded sometimes) you can run the python program again with the `--download /path/to/you-city.osm` flag.

Have fun!