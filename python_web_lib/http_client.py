import os
from http.client import HTTPConnection
from urllib.parse import urljoin, urlparse, urlunparse
from urllib.request import urlretrieve
from html.parser import HTMLParser

class ImageParser(HTMLParser):
    def handle_startendtag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)
                
def download_image(url, data):
    if not os.path.exists("DOWNLOAD_IMAGE"):
        os.makedirs("DOWNLOAD_IMAGE")
        
    parser = ImageParser()
    parser.feed(data)
    dataSet = set(x for x in parser.result)
    
    for x in sorted(dataSet):
        imageUrl = urljoin(url, x)
        basename = os.path.basename(imageUrl)
        targetFile = os.path.join("DOWNLOAD_IMAGE", basename)

        print("DOWNLOADING...", imageUrl)
        urlretrieve(imageUrl, targetFile)
        
def main():
    host = "www.google.co.kr"
    
    conn = HTTPConnection(host)
    conn.request("GET", '')
    resp = conn.getresponse()
    
    charset = resp.msg.get_param('charset')
    data = resp.read().decode(charset)
    conn.close()
    
    print('\n >>>>>>>>>> Download Images from', host)
    url = urlunparse(('http', host, '', '', '', ''))
    download_image(url, data)
    
if __name__ == '__main__':
    main()