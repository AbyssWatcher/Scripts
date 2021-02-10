"""A Python script that goes through a GPM (Google Play Music) library and returns a JSON of the songs and their metadata.

***
    According to Google (https://youtube.googleblog.com/2020/05/youtube-music-transfer-google-play-music-library.html),
    Google Play Music will cease to exist around December 2020. Google's music streaming service is now YouTube Music.
***

"""
import toml
import json
import os
import platform
from gmusicapi import Mobileclient

def one_time_oauth(api):
    """Performs a one-time interaction with Google OAuth to store OAuth credentials locally."""
    api.perform_oauth()
    print(api.OAUTH_FILEPATH) # Returns location of the credential file.
    # Mobileclient.perform_oauth(storage_filepath=<object object>, open_browser=False)
    # Should specify the "storage_filepath=<object object>" for good practice.
    # Should be run once per machine to store credentials to disk.

def find_device_id(api):
    """Attempts an invalid device id, which prints the correct device id to the command line."""
    # Just run 'api.oauth_login()' with an invalid device_id and the correct device_id will be in the traceback.
    api.oauth_login('<a previously-registered device id>')

def api_testing(api):
    """Tests different features of the gmusicapi."""
    print(api.get_registered_devices()) # List of devices.

def perform_checks(api):
    """Checks if the client is authenticated and the account is subscribed to GPM."""
    return api.is_authenticated() and api.is_subscribed

def library_to_json(api):
    """Creates a JSON file of the songs currently in your GPM library."""
    library = api.get_all_songs() # GPM library
    print(len(library)) # Size of GPM library.
    library.sort(key=lambda s: s['recentTimestamp']) # Sort songs from oldest to newest.

    def time_formatting(song):
        """Convert durationMillis into durationSecs(length in seconds) and time(clock format, ex. 5:30)"""
        durationSecs = int(song['durationMillis']) // 1000 # Divide by 1000 to get seconds.
        minutes = str(durationSecs // 60)
        seconds = durationSecs % 60
        if seconds < 10: seconds = "0" + str(seconds)
        else: seconds = str(seconds)
        time = "{}:{}".format(minutes, seconds)
        return durationSecs, time

    data = {}
    data['songs'] = []
    counter = 0
    for song in library:
        durationSecs, time = time_formatting(song)
        data['songs'].append({
            'orderNum': counter,
            'title': song['title'],
            'artist': song['artist'],
            'album': song['album'],
            'trackNumber': song['trackNumber'],
            'year': song['year'],
            'genre': song['genre'],
            'durationSecs': durationSecs,
            'time': time
        })
        counter += 1
    # Write list of songs to songs.json
    with open('songs.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    api = Mobileclient()
    # one_time_oauth(api)
    # find_device_id(api)
    file_path = None
    if platform.system() == 'Windows':
        file_path = os.getcwd() + '\\gpm.toml' # Get the path to the TOML configuration file.
    else:
        file_path = os.getcwd() + '/gpm.toml' # Get the path to the TOML configuration file.
    device_id = toml.load(file_path)['info']['device_id'] # Get device_id from TOML configuration file.
    api.oauth_login(device_id) # Login to GPM
    if perform_checks(api):
        library_to_json(api)

if __name__ == "__main__":
    main()
