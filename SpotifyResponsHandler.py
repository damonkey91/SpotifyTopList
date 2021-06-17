import json
import LoggerWrapper
import FileReader
import Constants
from Exceptions import AccessTokenExpiredError

def getSongsUri(response):
    if response.ok:
        songsUri = __extractSongsUri(response)
        return songsUri
    elif response.status_code == 401:
        LoggerWrapper.logError(f"Access token expired. Throwing exception.")
        raise AccessTokenExpiredError('The access token expired')
    else:
        LoggerWrapper.logError(f"Response failed with status code {response.status_code}. Url = {response.url}")
        return list()

def __extractSongsUri(response):
    jsonString = response.text
    jsonDict = json.loads(jsonString)
    trackObj = jsonDict["tracks"]
    songList = trackObj["items"]
    songUris = list()
    for song in songList:
        songUri = song["track"]["uri"]
        songUris.append(songUri)
    return songUris

def extractAccessToken(response):
    if response.ok:
        responseObj = json.loads(response.text)
        accessToken = responseObj['access_token']
        FileReader.writeToFile(Constants.tokenFileName, accessToken)
        return accessToken
    else:
        LoggerWrapper.logError(f"Extracting access token failed. Response status code {response.status_code}")

