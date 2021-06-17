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
    SpotifyApi.replacePlaylist(jsonUniqueSongsUri)

try:
    start()
except Exception as err:
    LoggerWrapper.logError('Error in your code = {0}'.format(err))
