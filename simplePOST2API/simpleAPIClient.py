#!/usr/bin/python3
# This model is one way to POST data to a simple API

import mutils
import argparse
import requests
import urllib3
import os
from datetime import time, datetime
from dateutil import parser, tz
import socket
from requests.packages.urllib3.exceptions import ConnectionError
from requests.packages.urllib3.exceptions import MaxRetryError
from requests.packages.urllib3.exceptions import TimeoutError
from requests.packages.urllib3.exceptions import SSLError as _SSLError
from requests.packages.urllib3.exceptions import HTTPError as _HTTPError
from requests.exceptions import ConnectionError, Timeout, SSLError

# Set some defaults
debug_level = 0
do_timings = False
disable_cert_security = False
proxy_needed = False
PROXY_URL = None

# set up the parser
parser = argparse.ArgumentParser(
    prog="sampleAPIClient",
    description="sampleAPIClient: an API Client POST skeleton for problem-solving")

# add all the arguments
parser.add_argument(
    "-d", "--debug",
    default="False",
    action='store_true',
    help="Use to send debug logging to console")

parser.add_argument(
    "-t", "--timing",
    default="False",
    action='store_true',
    help="Use to send timing to console")

parser.add_argument(
    # Set 'disable_cert_security' to True to disable some SSL warnings
    # This can be a security risk concern.  Use with caution.
    "-s", "--disable_cert_security",
    default="False",
    action='store_true',
    help="Use to disable SSL security checking.\nThis can be a security risk concern.\nUse with caution.")

parser.add_argument(
    "-p", "--proxy_needed",
    default="False",
    action='store_true',
    help="Use to enable a proxy")

parser.add_argument(
    "-x", "--proxy_url",
    default="None",
    type=ascii,
    help="When enabling a proxy, this is the full URL")

parser.add_argument(
    "-u", "--api_url",
    required=True,
    type=ascii,
    help="Target api-endpoint - full URL")

arglist = parser.parse_args()


def do_args(args):
    global PROXY_URL
    if args.debug == True:
        debug_level = 1
        mutils.log_me(debug_level)
    else:
        debug_level = 0

    if args.timing == True:
        do_timings = True
    else:
        do_timings = False

    if args.disable_cert_security == True:
        if disable_cert_security:
            mutils.deal_with_cert_issues()

    if args.proxy_needed == True:
        if args.proxy_url:
            PROXY_URL = args.proxy_url
            proxy_needed = True
    else:
        proxy_needed = False
        PROXY_URL = False

    if args.api_url:
        URL = args.api_url

    else:
        parser.print_help()

    return URL.strip(), debug_level, do_timings, proxy_needed, PROXY_URL


def do_api_call(URL, HEADER_PARAMS, POST_DATA, REQUIRED_PROXY=None):
    # Needed to strip the quotes to deal with a
    # requests.exceptions.InvalidSchema error
    URL = URL.replace('"', '')
    URL = URL.replace("'", "")
    try:
        if REQUIRED_PROXY:
            REQUIRED_PROXY = REQUIRED_PROXY.replace('"', '')
            REQUIRED_PROXY = REQUIRED_PROXY.replace("'", "")
            print("REQUIRED_PROXY: " + REQUIRED_PROXY)
            r = requests.post(URL, verify=False, data=POST_DATA, headers=HEADER_PARAMS, timeout=5,
                              proxies={"https": REQUIRED_PROXY})
            # do_api_call_via_proxy(URL, HEADER_PARAMS, POST_DATA, REQUIRED_PROXY)
        else:
            r = requests.post(URL, data=POST_DATA, headers=HEADER_PARAMS, timeout=5)
    except socket.error as sockerr:
        print('---------------------------------------------------------------')
        print('socket.error --------------------------------------------------')
        print('Something bad happened.  Hostname correct?  Network OK?')
        print('---------------------------------------------------------------')
        raise ConnectionError(sockerr)
    except MaxRetryError as e:
        raise MaxRetryError(e)
    except ConnectionError as e:
        raise ConnectionError(e)
    except (_SSLError, _HTTPError) as e:
        if isinstance(e, _SSLError):
            raise SSLError(e)
        elif isinstance(e, TimeoutError):
            raise Timeout(e)
        else:
            raise Timeout('Request timed out.')
    except OSError as msg:
        print('---------------------------------------------------------------')
        print('Reached OSError -----------------------------------------------')
        print('Something bad happened.  Hostname correct?  Network OK?')
        print('---------------------------------------------------------------')
        raise OSError()

    return r


def do_api_call_via_proxy(URL, HEADER_PARAMS, POST_DATA, PROXY_URL):
    r = requests.post(URL, verify=False, data=POST_DATA, headers=HEADER_PARAMS, proxies={"https": PROXY_URL})
    return r


if __name__ == '__main__':
    mutils.checkpyver()
    URL, debug_level, do_timings, proxy_needed, PROXY_URL = do_args(arglist)
    """
    # For script debugging
    print("URL: " + str(URL))
    print("do_timings: " + str(do_timings))
    print("debug_level: " + str(debug_level))
    print("proxy_needed: " + str(proxy_needed))
    print("PROXY_URL: " + str(PROXY_URL))
    """
    if do_timings:
        start = mutils.do_timer("start")
        # For time formatting options see: https://strftime.org/
        TIME_FORMAT = "%a, %b %d, %Y at %H:%M:%S %p %Z"
        print("Started at: {0}".format(start.strftime(TIME_FORMAT)))
    # define a params dict for the parameters to be sent to the API
    # There are many common headers that might be relevant, 'Authorization' 
    # might be common for you:.  See a longer list at:
    # https://en.wikipedia.org/wiki/List_of_HTTP_header_fields#Request_fields
    HEADER_PARAMS = {'Accept': 'application/json',
                     'Content-Type': 'application/json',
                     'User-Agent': 'mccrightSample1APIcaller'}
    # define a POST data dict 
    POST_DATA = {'somekey': 'somevalue',
                 'sometoken': 'somevalue',
                 'emailaddr': 'user.name@mydomain.com'}
    if proxy_needed:
        # PROXY_URL=os.environ.get('HTTPS_PROXY')
        returndata = do_api_call(URL, HEADER_PARAMS, POST_DATA, REQUIRED_PROXY=PROXY_URL)
    else:
        returndata = do_api_call(URL, HEADER_PARAMS, POST_DATA)

    print(f"This is the return data: {returndata}")

    if do_timings:
        end = mutils.do_timer("end")
        print("Ended at: {0}".format(end.strftime(TIME_FORMAT)))
        print(f"Elapsed time: {end - start}")
