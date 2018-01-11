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

        if checkSpamLink(spamLinkDomains, resp.url):
            return True

    if checkSpamLink(spamLinkDomains, res.url):
        return True


    text=res.text

    aTagUrlStart=0
    aTagUrlEnd=0

    while redirectionDepth>0:
        aTagUrlStart = text.find('<a href=\"',aTagUrlEnd)
        if aTagUrlStart == -1:
            return False
        else:
            aTagUrlStart += 9

        aTagUrlEnd = text.find('\"', aTagUrlStart)
        aTagUrl=text[aTagUrlStart:aTagUrlEnd]
        if checkSpamLink(spamLinkDomains,aTagUrl) : return True
        redirectionDepth -= 1

    return False


print(isSpam('spam spam https://goo.gl/nVLutc', ['tvtv24.com'], 0))






