"""
This script demonstrate HTTP call
"""

import http.client

connection = http.client.HTTPConnection('www.google.com', 80, timeout=10)
connection.request('GET', '/')

response = connection.getresponse()

print(response.status, response.reason)
data = response.read()
print(data)

connection.close()
