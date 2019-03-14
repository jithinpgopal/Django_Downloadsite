import urllib.request
from urllib.request import Request, urlretrieve
import re


def image_download(url):
    req = Request(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'})
    page = urllib.request.urlopen(req).read().decode('utf-8')
#    print((page))
    p=re.findall(r'.src.*jpg.*config_height', page)
    q=str(p[0]).split('src')
    r=q[len(q)-1][3:-36]
    return(r)

