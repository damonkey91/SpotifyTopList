import unittest
import SpotifyApi

class TestSpotifyApi(unittest.TestCase):
    def testGetPlaylist(self):
        result = SpotifyApi.getPlaylist('37i9dQZEVXbIPOivNiyjjS')
        self.assertTrue(result.status_code == 200)


