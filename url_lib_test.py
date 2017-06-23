"""
This module is to test and learn urllib2 module
"""
import urllib2
import urllib

URL = "http://www.google.com"
data = { 'q': 'vikas'}

values = urllib.urlencode(data);
print values
full_url = URL + "/?" + values

print full_url
REQ = urllib2.Request(full_url)

print REQ
RESPONSE = urllib2.urlopen(REQ)

# print RESPONSE.read()
