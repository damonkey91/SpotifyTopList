#Api to handle spotify requests

import requests
import ConverterHelper
import SpotifyResponsHandler
import ConstantsGitIgnore
import Constants
import FileReader

global accessToken
accessToken = None

def renewAccessToken():
    refreshToken = __getRefreshToken()
    url = 'https://accounts.spotify.com/api/token'
    header = {'Authorization': 'Basic ' + ConverterHelper.convertToBase64(ConstantsGitIgnore.clientIdSpotifyApi + ':' + ConstantsGitIgnore.secretClientIdSpotifyApi)}
    body = {'grant_type': 'refresh_token',
            'refresh_token': refreshToken}
    response = requests.post(url, headers= header, data= body)
    global accessToken
    accessToken = SpotifyResponsHandler.extractAccessToken(response)

def __getRefreshToken():
    return ConstantsGitIgnore.refreshToken

def getPlaylist(playlistId):
    url = 'https://api.spotify.com/v1/playlists/' + playlistId
    header = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + __getAccessToken()
    }

    response = requests.get(url, headers= header)
    return response

def replacePlaylist(jsonSongIds):
    playlist = '5heFT5tiaG9tld8U37rEIg'
    url = 'https://api.spotify.com/v1/playlists/'+playlist+'/tracks'
    header = {'Content-Type': 'application/json',
              'Accept': 'application/json',
              'Authorization': 'Bearer ' + __getAccessToken()}
    data = jsonSongIds
    response = requests.put(url, headers= header, data= data);
    return response

def __getAccessToken():
    global accessToken
    if accessToken == None:
        textList = FileReader.readFromFile(Constants.tokenFileName)
        accessToken = textList[0].strip()
    return accessToken









def authorizesSpotify():
    spotifyAuth = requests.get('https://accounts.spotify.com/authorize?client_id=' + clientId + '&response_type=code&redirect_uri=http:%2F%2Fexample.com%2Fcallback%2F&scope=playlist-modify-private%20user-read-private%20user-library-read%20user-library-modify&state=')
    return spotifyAuth
