import json
import binascii
import codecs
import sys
from sys import platform as _platform
reload(sys)
sys.setdefaultencoding("ISO-8859-1")
import subprocess, os
import base64
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

asset = raw_input('Where would you like to go?: ')
print ("querying counterparty asset registry for the ",asset,"resource")
#aim to use a counterpartyd server instead 
asseturl = "https://xchain.io/api/asset/" + asset
data = urlopen(asseturl).read()
output = json.loads(data)
desc = (output['description'])
print "asset info found: " + desc
#todo - check if asset description is valid encoded URL before proceeding, fail gracefully if not- assuming for now it is
decodedasset = base64.b32decode(desc).decode("latin-1")
decodedasset2 = binascii.hexlify(decodedasset)
#Quick n dirty workaround to launch on linux, need to manually launch for OSX/windows
print "attempting to launch..."
if _platform == "linux" or _platform == "linux2":
	print "decoded asset URL: " + "dat://" + decodedasset2
	os.system("chmod +x beaker-browser-0.7.11-x86_64.AppImage")
	os.system("./beaker-browser-0.7.11-x86_64.AppImage " + "dat://" + decodedasset2)
elif _platform == "darwin":
	print "Please copy and paste the URL into beaker manually for now"
	print "decoded asset URL: " + "dat://" + decodedasset2
elif _platform == "win32":
	print "Please copy and paste the URL into beaker manually for now"
	print "decoded asset URL: " + "dat://" + decodedasset2
elif _platform == "win64":
	print "Please copy and paste the URL into beaker manually for now"
	print "decoded asset URL: " + "dat://" + decodedasset2