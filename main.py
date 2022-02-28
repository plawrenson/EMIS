from fhir.resources.bundle import Bundle
from fhir.resources.patient import Patient

import pathlib
import json
filename = pathlib.Path(r"data\Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.json")
Bun = Bundle.parse_file(filename)


#extract resources from Bundle
#url and method could be made dynamic 
resources = []
for entry in Bun.entry:
        if entry.request.url == 'Patient' and entry.request.method == 'POST':  
                resources.append(entry.resource)

#loop through resources, set attributes and assign to object
id = resources[0].id



""" resources = []
for entry in Bun.entry:
    if entry.request.url == 'Patient':
        resources.append(entry.resource.json())

print(resources[0]) """

""" pat = Patient.parse_obj(resources[0]).json()   

urls = []

for entry in Bun.entry:
        urls.append(entry.request.url)


urls = list(set(urls))

print (urls) """