import unittest
import SpotifyResponsHandler
from Tests.TestData import testJsonSongResponse, testJsonAccessTokenResponse
from Exceptions import AccessTokenExpiredError

class TestResponseHandler(unittest.TestCase):

    def testGetSongsUri(self):
        mockedResponse = self.__createResponseObject(200, testJsonSongResponse)
        songSet = SpotifyResponsHandler.getSongsUri(mockedResponse)
        self.assertIs(len(songSet), 3)

    def testGetSongsUri401(self):
        mockedResponse = self.__createResponseObject(401, '')
        try:
            songSet = SpotifyResponsHandler.getSongsUri(mockedResponse)
        except AccessTokenExpiredError:
            return
        self.assertFalse(True)

    def testGetSongsUri403EmptySet(self):
        mockedResponse = self.__createResponseObject(403, '')
        songSet = SpotifyResponsHandler.getSongsUri(mockedResponse)
        self.assertIs(len(songSet), 0)

    def testExtractRefreshToken(self):
        mockedResponse = self.__createResponseObject(200, testJsonAccessTokenResponse)
        accessToken = SpotifyResponsHandler.extractAccessToken(mockedResponse)
        self.assertIsNotNone(accessToken)
        self.assertIsNot(len(accessToken), 0)

    def testExtractRefreshToken401(self):
        mockedResponse = self.__createResponseObject(401, '')
        accessToken = SpotifyResponsHandler.extractAccessToken(mockedResponse)
        self.assertIsNone(accessToken)

    def __createResponseObject(self, statusCode, body):
        class MockResponse:
            def __init__(self, status_code, body):
                self.ok = 200 <= statusCode < 300
                self.status_code = status_code
                self.text = body
                self.url = 'https://api.spotify.com/v1/playlists/'

        return MockResponse(statusCode, body)