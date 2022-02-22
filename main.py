from fhir.resources.bundle import Bundle
from fhir.resources.patient import Patient
import pathlib
import json
filename = pathlib.Path(r"EMIS\data\Aaron697_Dickens475_8c95253e-8ee8-9ae8-6d40-021d702dc78e.json")
Bun = Bundle.parse_file(filename)

resources = []
for entry in Bun.entry:
    if entry.request.url == 'Patient':
        resources.append(entry.resource)


pat = Patient.parse_obj(resources[0]).json()   

print(pat)