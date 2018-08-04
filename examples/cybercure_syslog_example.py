import cybercure
import argparse
import logging
import logging.handlers

# Help, just in case someone forgot to read the README..
parser = argparse.ArgumentParser("cybercure_syslog_example")
parser.add_argument("syslog_ip", help="The IP Address of the remote syslog server", type=str)
parser.add_argument("syslog_port", help="The Port of the syslog remote server", type=int)
parser.add_argument("output_type", help="Choose the messages format to broadcast: json,csv,cef", type=str)

args = parser.parse_args()
output_type=(args.output_type)
syslog_ip=(args.syslog_ip)
syslog_port=(args.syslog_port)

cc_logger = logging.getLogger('CCLogger')

#We will pass the message as INFO?!?
cc_logger.setLevel(logging.INFO)

#Define SyslogHandler
handler = logging.handlers.SysLogHandler(address = (syslog_ip,syslog_port))
cc_logger.addHandler(handler)


#get the ip addresses that are currently appear as active threats 
active_blocked_ip = cybercure.get_ip_indicators(output_type)

#iterate the list of ip addresses that should be blocked and send using syslog
if output_type == 'json':
	print ("Okay.. I got %s records, now sending them using syslog:" % active_blocked_ip['count'])
	for threat in active_blocked_ip['data']['ip']:
		cc_logger.info(threat)
                print ("Sending %s" % threat)

elif output_type == 'csv' or output_type == 'cef':
	b = active_blocked_ip.split(",")
	for threat in b:
		cc_logger.info(threat)
		print ("Sending %s" % threat)
