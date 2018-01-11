import requests

def findUrl(content):
    urlStart = content.find('http')
    urlEnd = content.find(' ', urlStart)
    if urlEnd == -1:
        urlEnd = len(content)

    url = content[urlStart:urlEnd]
    return url

def isSpam(content, spamLinkDomains, redirectionDepth):
    url=findUrl(content)

isSpam('spam spam https://goo.gl/nVLutc', None, 0)






