
import errno
import glob
import logging
import os

import requests
import time
from multiprocessing.dummy import Pool as ThreadPool
import urllib


# TODO: Build this out into a 'safe' utility function.
# Add input/output sanity checking and error handling
def get_content_via_http(url):
    returned = requests.get(url)
    return returned.content


# TODO: Build this out into a 'safe' utility function.
# Add input/output sanity checking and error handling
def url_encode_parms(url, *kwargs):
    the_parameters = {"name": "nameString大", "age": 30}
    print '&'.join('%s=%s' % (k, v) for k, v in d_para.iteritems())
    # age=30&name=nameString大
    print '&'.join('%s=%s' % (k, urllib.quote(str(v))) for k, v in d_para.iteritems())
    # age=30&name=nameString%A4%A7

    base_url = 'null.net/'
    url = 'http://%s?%s' % (base_url, '&'.join('%s=%s' % (k, urllib.quote(str(v))) for k, v in d_para.iteritems()))
    print url
    # http://null.net/?age=30&name=nameString%A4%A7



# TODO: Build this out into a 'safe' utility function.
# Add input/output sanity checking and error handling
def multi_process_stress_test(url1, url2):
    """
    Start 4 threads, send 100 http requests to the target server
    Report on timing
    :return:
    """
    start = time.time()
    targeturl_1 = """url1"""
    targeturl_2 = """url2"""
    urls = [targeturl_1, targeturl_2]*50
    pool = ThreadPool(5)
    ret = pool.map(get_content_via_http, urls)
    pool.close()
    pool.join()
    print ('Test duration: %s' % (time.time() - start))

# FROM: 
# https://github.com/oVirt/ovirt-hosted-engine-ha/blob/master/ovirt_hosted_engine_ha/lib/util.py
def to_bool(string):
    first = str(string).lower()[:1]
    if first in ('t', 'y', '1'):
        return True
    elif first in ('f', 'n', '0'):
        return False
    else:
        raise ValueError("Invalid value for boolean: {0}".format(string))


# FROM: 
# https://github.com/oVirt/ovirt-hosted-engine-ha/blob/master/ovirt_hosted_engine_ha/lib/util.py
def __log_debug(logger, *args, **kwargs):
    if logger:
        logger.debug(*args, **kwargs)



# FROM: 
# https://github.com/oVirt/ovirt-hosted-engine-ha/blob/master/ovirt_hosted_engine_ha/lib/util.py
def mkdir_recursive(path):
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST or not os.path.isdir(path):
            raise


# FROM:
https://github.com/oVirt/ovirt-hosted-engine-ha/blob/master/ovirt_hosted_engine_ha/env/path.py
def escape_remote_path(path):
    return path.replace("_", "__").replace("/", "_")

