import cybercure

#get the ip addresses that are currently appear as active threats 
print "calling latest ip threats api"

#We are calling the api with 2 parameters , 1. return the data in stix format. 2. we tell the library to return it as text object and not as list (as we going to save it to disk)
active_blocked_ip = cybercure.get_ip_indicators('stix','stix')

#write current stix to file and save
print "saving file bad_ip.stix"
with open("bad_ip.stix", "w") as text_file:
    text_file.write(active_blocked_ip)

