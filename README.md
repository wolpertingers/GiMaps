# :globe_with_meridians:  GiMaps

Beautiful maps of places where a gorgeous human once lived.

## Usage
First, clone the repo an `cd` into it. It is probably best to have the *GiMaps* repo right next to the *Maperitive* directory.

Then, edit the `settings.json` or create a new JSON file inside the *Colors* directory to your liking. Aside from the colors, also edit/add your city and its geo bounds.

Now run the little python program 
```
python generate.py name_of_your_city /your/settings.json
```
You should then have a *Scripts* folder inside the *Maperitive* directory. It contains a `.mscript` file with the name of your city. You can use it to run
```
Maperitive /path/to/Scripts/your-city.mscript
```
Note that this command will download all the data inside the geo bounds you have defined in the JSON file and save it to `./Maps/you-city.osm`. If you want to rerun the script but not download all the data again (the OSM servers are already overloaded sometimes) you can run the python program again with the `--download /path/to/you-city.osm` flag.

Have fun!