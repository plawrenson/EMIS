very early attempt to use the fhir.resources library to pull information from Bundle files

1.break bundle into resource entries - by method and resource type (url)

2.loop through resources, extract attributes and assign to object

3.output object to database/parquet etc


#################################################

I've also investigated pre-built FHIR servers using htttp and REST 

I assumed this would be too simplistic to demonstrate a solution to this problem

###############################################

I've not had much time to devote to this so I can only submit a partial solution. 

I can talk through it more fully along with altalternative methods to extract and store the data 