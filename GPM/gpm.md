# Convert Google Play Music song library to .json

## Additional Note
Google Play Music was "[killed by Google](https://killedbygoogle.com/)" on December 2020 and replaced with YouTube Music.

Both [gmusicapi](https://github.com/simon-weber/gmusicapi) and the script no longer work as the entire service was discontinued.

## About
The script extensively uses [gmusicapi](https://github.com/simon-weber/gmusicapi),
which is an unofficial Python wrapper of the Google Play Music API.

Due to the limitations in how documented the API is, only songs added to your library (not playlists or auto-generated playlists) will have full song metadata access.

## Instructions
1. Clone the respository and navigate to its folder using the command line.
1. Install pipenv by running `pip install --user pipenv`.
2. Run `pipenv install` to install the necessary Python packages (toml and gmusicapi).
3. Un-comment out`one_time_auth()` in `main()` and comment out the other lines. Then run `pipenv run python gpm-to-json.py`. This stores the Google OAuth credentials locally.
4. Un-comment out `find_device_id()` in `main()` and comment out the other lines. Then run `pipenv run python gpm-to-json.py`. This allows you to obtain your device id (found in the traceback of your command line). Keep track of that device id.
5. Revert `main()` back to its original state (both `one_time_auth()` and `find_device_id()` are commented out).
6. Store the device id you got from `find_device_id()` in a TOML configuration file named `gpm.toml`. The only difference is including your own device id.

**Example TOML configuration file**: `gpm.toml`
```toml
# This is the GPM config document.
title = "GPM Config"
[info]
device_id = "device_id"
```

7. Now you can create a `songs.json` file of your Google Play Music library (in the order that you added the songs) by running `pipenv run python gpm-to-json.py`

**Example JSON song entry**:
```json
{
		"orderNum": 0,
		"title": "Instant Crush (feat. Julian Casablancas)",
		"artist": "Daft Punk",
		"album": "Random Access Memories",
		"trackNumber": 5,
		"year": 2013,
		"genre": "Dance/Electronic",
		"durationSecs": 337,
		"time": "5:37"
}
```

## Typical usage example
Run `pipenv run python gpm-to-json.py` in the command line.

## Files

`gpm-to-json.py` GPM python script

`gpm.toml` GPM config file (your private device_id)

`songs.json` Song list JSON

`Pipfile` Used with pipenv

`Pipfile.lock` Used with pipenv
