import SpotifyApi
import FileReader
import SpotifyResponsHandler
from Exceptions import AccessTokenExpiredError
import os

def getSongsUriFromPlaylists(playlistsId):
    listOfWantedSongsUri = list()

    for playlistId in playlistsId:
        songsUri = getPlaylistSongs(playlistId)
        wantedSongsUri = getFirstAmountOfSongsUri(songsUri, 15)
        listOfWantedSongsUri += wantedSongsUri

    return listOfWantedSongsUri

def getPlaylistSongs(playlistId):
    response = SpotifyApi.getPlaylist(playlistId)
    try:
        songsUri = SpotifyResponsHandler.getSongsUri(response)
        return songsUri
    except AccessTokenExpiredError:
        SpotifyApi.renewAccessToken()

    response = SpotifyApi.getPlaylist(playlistId)
    songsUri = SpotifyResponsHandler.getSongsUri(response)
    return songsUri

def getFirstAmountOfSongsUri(songsUri, nrOfSongs):
    endIndex = nrOfSongs + 1
    return songsUri[:endIndex]

def onlyUniqueValues(aList):
    listConvertedToSet = set(aList)
    convertedBackToList = list(listConvertedToSet)
    return convertedBackToList

def createFileIfNotExists(filename):
    if not os.path.exists(filename):
        FileReader.writeToFile(filename, '1337')