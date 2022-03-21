from urllib.request import urlopen
from xml.etree.ElementTree import parse

url_path = 'http://planet.python.org/rss20.xml'


def test_one():
    u = urlopen(url_path)
    doc = parse(u)

    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        date = item.findtext('pubDate')
        link = item.findtext('link')

        print(title)
        print(date)
        print(link)
        print()


if __name__ == '__main__':
    #  lxml is better than xml, so do it from lxml.etree import parse replace the second line.
    test_one()