.. Cybercure.ai Python SDK library documentation master file, created by
   sphinx-quickstart on Sat Aug  4 10:57:16 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. Cybercure.ai Python SDK library documentation master file, created by
   sphinx-quickstart on Sat Aug  4 10:57:16 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Cybercure.ai: Threat Intelligence for Humans
===========================================================
Release v\ |version|. (:ref:`Installation <install>`)

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg
    :target: https://saythanks.io/to/grispan56

.. image:: https://img.shields.io/badge/format-stix2-green.svg
    :target: https://oasis-open.github.io/cti-documentation/stix/intro

.. image:: https://img.shields.io/badge/format-json-green.svg
    :target: https://saythanks.io/to/grispan56

.. image:: https://img.shields.io/badge/format-csv-green.svg
    :target: https://saythanks.io/to/grispan56

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
    :target: https://saythanks.io/to/grispan56

-------------------

SDK Calls
******************

Cyber Cure expose several calls for use with cybercure.ai api.

* get_hash_indicators() - Allows to receive Hash indicators that are known to be currently spreading in the wild.
* get_ip_indictors() - Allows to receive list of ip addresses that are currently attacking.
* get_url_indicators() - Allows to receive list of URLs that are used by malware.

several parameters can be specified for the different calls, for example, the requested output to be returned.
The examples folder contains several examples to show how the API can be used to gather the intelligence and spread
to different targets, for example sending by CEF format using syslog or saving the output as STIX.

**Installation**

The easiest way to install cybercure python library is by using pip:

``pip install cybercure``    


**Code example**


    >>> import cybercure
    >>> active_blocked_ip = cybercure.get_ip_indicators(output_type)
    >>> print ("Okay.. I got %s records, now showing them:" % active_blocked_ip['count'])
    >>>	for threat in active_blocked_ip['data']['ip']:
    >>>		print "Are you blocking %s ?" % threat


Make sure to checkout complete and updated documentation at:

`cybercure documentaion <https://docs.cybercure.ai/docs>`_

and also check for updates on `www.cybercure.ai <www.cybercure.ai>`_

