get_ip_indicators()
===================

Overview
''''''''

`Cybercure.ai <http://www.cybercure.ai>`_  `IP API <https://docs.cybercure.ai/docs/blocked-ip-api>`_ provides a live list of addresses that are currently known to be attacking on the internet. This list contains bots, command and controls, infected computers with malware and ip addresses that are known to be used for attacks right now. 


Code example
''''''''''''

    >>> import cybercure
    >>> active_blocked_ip = cybercure.get_ip_indicators('json')
    >>> print ("Okay.. I got %s records, now showing them:" % active_blocked_ip['count'])
    >>> for threat in active_blocked_ip['data']['ip']:
    >>>         print "Are you blocking %s ?" % threat

data is always returned inside a data dictionary, in this API call the ip key will contain an array of the ip addresses that should be watched for.


Return Output
'''''''''''''

get_ip_indicators() accept 1 parameter and it should be one of the table shown below:

+----------+--------------------------------------------------------------------------------------+
| Type     | Description                                                                          |
+==========+======================================================================================+
| json     | returns json document with standard response.                                        |
+----------+--------------------------------------------------------------------------------------+
| csv      | delimited text file that uses a comma to separate values It stores tabular data.     |
+----------+--------------------------------------------------------------------------------------+
| iptables | iptables firewall formatted bash script to automatically and easily digest the feed. |
+----------+--------------------------------------------------------------------------------------+
| list     | ip list file, each with new line.                                                    |
+----------+--------------------------------------------------------------------------------------+
| cef      | cef format via http for arcsight and friends.                                        |
+----------+--------------------------------------------------------------------------------------+
| stix     | stix2 json format returned as a stix bundle with indicator objects.                  |
+----------+--------------------------------------------------------------------------------------+
