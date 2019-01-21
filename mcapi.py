import requests
import json
from requests.auth import HTTPBasicAuth

###############################################################################
# Global Variables
###############################################################################
user = 'admin'
password = 'Blue1coat!'


###############################################################################
# This section demonstrates listing all policies
###############################################################################
#url='https://mc.bluecoat.ninja:8082/api/policies'
#r = requests.get(url, auth=HTTPBasicAuth(user, password), verify=False)
#print(r.status_code, "\n", r.json())




###############################################################################
# This section demonstrates grabbing the content from a shared object.
###############################################################################
#url='https://mc.bluecoat.ninja:8082/api/policies/61BD083F-FE7A-453A-B160-11744EB0F4EA/content'
#r = requests.get(url, auth=HTTPBasicAuth(user, password), verify=False)
#print(r.status_code, "\n", r.json())




###############################################################################
# This section demonstrates pushing content to a shared object.
###############################################################################
#url='https://mc.bluecoat.ninja:8082/api/policies/61BD083F-FE7A-453A-B160-11744EB0F4EA/content'
#jsonContent= { "content" : { "urls" : [ { "description" : "", "url" : "www.cnn.com", "enabled" : "true" }, { "description" : "", "url" : "www.bluecoat.ninja", "enabled" : "true" }, { "description" : "", "url" : "www.fox.com", "enabled" : "false" } ] }, "contentType" : "URL_LIST", "schemaVersion" : "1.0", "changeDescription" : "Change comment" }
#r = requests.post(url, auth=HTTPBasicAuth(user, password), json=jsonContent, verify=False)
#print(r.status_code, "\n", r.json())




###############################################################################
# This section demonstrates installing a policy.
###############################################################################
url='https://mc.bluecoat.ninja:8082/api/policies/5C9F824C-33F0-4E4D-A50D-8A78392D842E/install'
r = requests.post(url, auth=HTTPBasicAuth(user, password), verify=False)
print(r.status_code, "\n", r.json())