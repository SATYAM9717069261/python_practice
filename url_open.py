import urllib.request
data=urllib.request.urlopen('https://www.python.org/')
for i in data:
        print(((str(i)).strip("b'")).strip('\\n'))






