import requests

def findUrl(content):
    urlStart = content.find('http')
    urlEnd = content.find(' ', urlStart)
    if urlEnd == -1:
        urlEnd = len(content)

    url = content[urlStart:urlEnd]
    return url

def checkSpamLink(spamLinkDomains, url):
    for spamLinkDomain in spamLinkDomains:
        if not url.find(spamLinkDomain)==-1 :
            return True
    return False


def isSpam(content, spamLinkDomains, redirectionDepth):
    url=findUrl(content)

    if checkSpamLink(spamLinkDomains, url):
        return True

    res = requests.get(url)
    for resp in res.history:
        if redirectionDepth <= 0:
            return False

        if resp.status_code == 301 or resp.status_code == 302:
            redirectionDepth -= 1
        else:
            continue

        if resp.url == url: continue

        if checkSpamLink(spamLinkDomains, resp.url):
            return True

    if checkSpamLink(spamLinkDomains, res.url):
        return True

    return False







print(isSpam('spam spam https://goo.gl/nVLutc', ['tvtv24.com'], 1))






