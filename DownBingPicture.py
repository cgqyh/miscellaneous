import re
import sys
import os
import requests


# get bing 
url = 'http://www.bing.com/'
print("Request Bing.com")
bingweb = requests.get(url=url)

# f = open('test.html','w')
# f.write(bingweb.text)
# f.close()

# find pattern
pattern = r'g_img={url:\'(http.*jpg)\',id:\'bgDiv\','
m = re.search(pattern, bingweb.content)
if m:
    picurl = m.group(1)
    print("Picture url:\n{0}".format(picurl))
else:
    print("Not Found picture url.")
    sys.exit(-1)

filename = os.path.basename(picurl)
print('File name:%s' % filename)
if os.path.isfile(filename):
    print("The Picture [%s]' has download." % filename)
    raw_input("Press any key.")
    sys.exit(0)

# download picture
print("Download Picture...")
data = requests.get(picurl,stream=True)
with open(filename, 'wb') as picfile:
        for chunk in data.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                picfile.write(chunk)
                picfile.flush()
        picfile.close()

print("Finished.")
raw_input("Press any key.") 