'''
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the Solution class:

Solution() Initializes the object of the system.
String encode(String longUrl) Returns a tiny URL for the given longUrl.
String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
'''

class Solution:
    def __init__(self):
        self.tiny = {}
        self.url = {}
        self.id = 0  
        self.base_url = "http://tinyurl.com/"

    def encode(self, longUrl):
        if longUrl in self.tiny:
            return self.tiny[longUrl]
        short_key = str(self.id)
        self.id += 1
        shortUrl = self.base_url + short_key
        self.tiny[longUrl] = shortUrl
        self.url[shortUrl] = longUrl

        return shortUrl

    def decode(self, shortUrl):
        return self.url.get(shortUrl, "")

