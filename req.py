#!/c/Python27/python

import requests
#print (requests.get('http://www.google.com')
       

url = 'http://www.google.com'
r = requests.get(url)
print ("URL: " + str(url))
#print ("Status: " + str(r.status_code))
#rint ("Header: " + str(r.headers['content-type']))
#print ("Encoding: " + str(r.encoding))
#print ("Body: (:200)...".format(r.text))
