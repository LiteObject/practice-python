"""
In this example, the script imports the `urllib.request` module to 
make an HTTP GET request to the URL specified in the url variable. 
The response is stored in the response variable, and the read() 
method is used to retrieve the response data. Finally, the script 
prints the response data to the console using the print() function.

Note that you may need to install additional libraries, such as requests, 
if you need to make more advanced HTTP requests or handle HTTP responses 
in a specific way.
"""

import urllib.request
import json

# Set the URL to make a request to
URL = "https://official-joke-api.appspot.com/random_joke"

# Send an HTTP GET request to the URL
response = urllib.request.urlopen(URL)

# Read the response and print it
data = response.read()
#print(data)

# Python Pretty Print JSON String
json_object = json.loads(data)
json_formatted_str = json.dumps(json_object, indent=2)
print(json_formatted_str)
