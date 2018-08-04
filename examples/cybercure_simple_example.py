import cybercure
import argparse


# Help, just in case someone forgot to read the README..
parser = argparse.ArgumentParser("cybercure_simple_example")
parser.add_argument("output_type", help="you can use any of the supported types: json,csv,stix,cef", type=str)
args = parser.parse_args()
output_type=(args.output_type)

#get the ip addresses that are currently appear as active threats 
active_blocked_ip = cybercure.get_ip_indicators(output_type)

#iterate the list of ip addresses that should be blocked and do something
if output_type == 'json':
	print ("Okay.. I got %s records, now showing them:" % active_blocked_ip['count'])
	for threat in active_blocked_ip['data']['ip']:
		print "Are you blocking %s ?" % threat
else:
	# if its not json, we are going to get text holding the data in the requested format
	print active_blocked_ip
