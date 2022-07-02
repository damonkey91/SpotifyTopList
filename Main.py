import SpotifyApi
import LoggerWrapper
from Constants import spotifyChartsPlaylistsIds, tokenFileName
import Other

import ConverterHelper

def start():
    Other.createFileIfNotExists(tokenFileName)
    songsUri = Other.getSongsUriFromPlaylists(spotifyChartsPlaylistsIds)
    uniqueSongsUri = Other.onlyUniqueValues(songsUri)
    jsonUniqueSongsUri = ConverterHelper.createJsonData(uniqueSongsUri)
    response = SpotifyApi.replacePlaylist(jsonUniqueSongsUri)

    if response.ok:
        LoggerWrapper.logError(f'Success! Created new list with response {response.status_code}')
    else:
        LoggerWrapper.logError(f'Failed! Could not create new list with. Error response {response.status_code}')

try:
    start()
except Exception as err:
    LoggerWrapper.logError('Error in your code = {0}'.format(err))
