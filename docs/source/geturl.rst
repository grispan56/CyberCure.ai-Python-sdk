get_url_indicators()
===================

Overview
''''''''

`Cybercure.ai <http://www.cybercure.ai>`_  `URL API <https://docs.cybercure.ai/docs/blocked-urls-api>`_ provides a live list of URL addresses that are currently known to be spreading or asscoiated with cyber attacks. 


Code example
''''''''''''

    >>> import cybercure
    >>> active_blocked_urls = cybercure.get_url_indicators('json')
    >>> print ("Okay.. I got %s records, now showing them:" % active_blocked_urls['count'])
    >>> for threat in active_blocked_ip['data']['urls']:
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
| list     | ip list file, each with new line.                                                    |
+----------+--------------------------------------------------------------------------------------+
| cef      | cef format via http for arcsight and friends.                                        |
+----------+--------------------------------------------------------------------------------------+
| stix     | stix2 json format returned as a stix bundle with indicator objects.                  |
+----------+--------------------------------------------------------------------------------------+
