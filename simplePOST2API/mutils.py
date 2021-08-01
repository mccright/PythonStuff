import requests


def log_me(debug_level):
    # Logging for debugging as suggested in:
    # "Python requests is slow and takes very long to complete HTTP or HTTPS request" 
    # https://stackoverflow.com/questions/62599036/python-requests-is-slow-and-takes-very-long-to-complete-http-or-https-request
    import logging
    import http.client
    http.client.HTTPConnection.debuglevel = debug_level
    
    # Initialize logging to see the debug output.
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
    

def deal_with_cert_issues():
    # Deal with some certificate issues:
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def checkpyver():
    import sys
    if sys.version_info < (3, 7):
        raise Exception("Use only with Python 3.7 or higher")
    else:
        return True


def do_timer(timeevent):
    from datetime import time, datetime
    from dateutil import parser, tz

    if timeevent == 'start' or timeevent == 'end':
        timer_str = datetime.now(tz=tz.tzlocal())
        return timer_str
    else:
        return "error"
