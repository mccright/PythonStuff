#!/usr/bin/env python3
import errno
import glob
import logging
import os
import re

import requests
import time
from multiprocessing.dummy import Pool as ThreadPool
import urllib


# Review later:
# https://github.com/anilmuppalla/python-unix-utils/blob/master/grep.py
# https://github.com/yennanliu/web_scraping
# https://github.com/yennanliu/CS_basics
# See about converting this for use in virtual environments:
#    https://github.com/LonamiWebs/Py-Utils/blob/master/misc/pipu


# Ref: https://github.com/shpala/pybuild_utils/blob/master/base/system_info.py
# TODO: Figure out how to identify if in WLS and implement in code
import platform
def get_os() -> str:
    """
    Identify OS family
    :param questionablestring: NONE
    :return: os_name_string
    """
    uname_str = platform.system()
    if 'MINGW' in uname_str:
        return 'windows'
    elif uname_str == 'Windows':
        return 'windows'
    elif uname_str == 'Linux':
        return 'linux'
    elif uname_str == 'Darwin':
        return 'macosx'
    elif uname_str == 'FreeBSD':
        return 'freebsd'
    elif uname_str == 'Android':
        return 'android'
    else:
        return 'unknown'


# Ref: https://github.com/shpala/pybuild_utils/blob/master/base/system_info.py
# Then if Linux
# TODO: Are there other distributions that I need to catch?
def linux_get_dist():
    """
    Return the running distribution group
    RHEL == RHEL, CENTOS, FEDORA
    DEBIAN == UBUNTU, DEBIAN
    :param: NONE
    :return: distribution_name_string
    """
    linux_tuple = platform.linux_distribution()
    dist_name = linux_tuple[0]
    dist_name_upper = dist_name.upper()

    if dist_name_upper in ["RHEL", "CENTOS LINUX", "FEDORA"]:
        return "RHEL"
    elif dist_name_upper in ["DEBIAN", "UBUNTU"]:
        return "DEBIAN"
    raise NotImplemented("Unknown platform '%s'" % dist_name)


# Work on a cross-OS safe directory/file test and create function
# This is still only the most spare skeleton
def create_dir(dir_full_path):
    # TODO: sanity check the input - safe for directory?
    # Safe location? Safe characters?
    # TODO: set the OS-specific path construction
    # TODO: wrap each step in a try / catch
    if os.path.isdir(dir_full_path):
        return ("%s already exists" % dir_full_path)
    else:
        os.mkdir(dir_full_path)
        # ?? os.chdir(dir_full_path)
    return dir_full_path


# Ref: https://github.com/vered1986/PythonUtils/blob/master/academic_tools/references/common.py
def normalize_tainted_string(questionablestring):
    """
    Trim, remove any non alphanumeric character and lower-case a questionable string
    :param questionablestring: tainted string
    :return: the normalized string
    """
    return re.sub('\s+', ' ', re.sub('[\W_]+', ' ', questionablestring.lower()))


# Ref: https://github.com/shpala/pybuild_utils/blob/master/base/utils.py
def read_file_line_by_line_to_list(file) -> list:
    """
    Read file into an array
    :param file: input file
    :return: file lines in an array
    """
    if not os.path.exists(file):
        raise BuildError('file path: {0} not exists'.format(file))

    file_array = []
    with open(file, "r") as ins:
        for line in ins:
            file_array.append(line.strip())

    return file_array


# Ref: https://github.com/shpala/pybuild_utils/blob/master/base/utils.py
def read_file_line_by_line_to_set(file) -> set:
    """
    Read file into a set
    :param file: input file
    :return: file lines in a set
    """
    if not os.path.exists(file):
        raise BuildError('file path: {0} not exists'.format(file))

    file_set = set()
    with open(file, "r") as ins:
        for line in ins:
            file_set.add(line.strip())

    return file_set


# Ref: https://github.com/shpala/pybuild_utils/blob/master/base/utils.py
# TODO: Work on thie download_file() function - make it more general & support proxies
from urllib.request import urlopen
# class for special err handling
class DownloadError(Exception):
    def __init__(self, value):
        self.value_ = value

    def __str__(self):
        return self.value_

# TODO: Sanity check the buffer sizing an file write; add try/catch
def download_file(url, current_dir):
    """
    Attempt to download file from URL using sane buffer and write to file
    :param file: input URL
    :return: full path to downloaded file
    """
    file_name = url.split('/')[-1]
    response = urlopen(url)
    if response.status != 200:
        raise DownloadError(
            "Can't download url: {0}, status: {1}, response: {2}".format(url, response.status, response.reason))

    f = open(file_name, 'wb')
    file_size = 0
    header = response.getheader("Content-Length")
    if header:
        file_size = int(header)

    print("Downloading: {0} Bytes: {1}".format(file_name, file_size))

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = response.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        percent = 0 if not file_size else file_size_dl * 100. / file_size
        status = r"%10d  [%3.2f%%]" % (file_size_dl, percent)
        status += chr(8) * (len(status) + 1)
        print(status, end='\r')

    f.close()
    return os.path.join(current_dir, file_name)


# https://github.com/daveoncode/python-string-utils
# Installation
# pip install python-string-utils
import string_utils

# TODO: Build this out into a 'safe' utility function.
# Also use this as an example of how terse you can be in a hurry.
# Add input/output sanity checking and error handling
# See 'download_file()' above.
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
    Attempt to download file from URL using sane buffer and write to file
    Start 4 threads, send 100 http requests to the target server
    Report on timing when finished
    :param url1, url2: input full URL1 and URL2
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


# FROM: https://github.com/shpala/pybuild_utils/blob/master/base/utils.py
# This is an interesting idea.
# TODO: Review the code and think about real-world applications
import subprocess
import shutil
def git_clone(url: str, current_dir: str, remove_dot_git=True):
    common_git_clone_line = ['git', 'clone', '--depth=1', url]
    cloned_dir = os.path.splitext(url.rsplit('/', 1)[-1])[0]
    common_git_clone_line.append(cloned_dir)
    subprocess.call(common_git_clone_line)
    os.chdir(cloned_dir)

    common_git_clone_init_line = ['git', 'submodule', 'update', '--init', '--recursive']
    subprocess.call(common_git_clone_init_line)
    directory = os.path.join(current_dir, cloned_dir)
    if remove_dot_git:
        shutil.rmtree(os.path.join(directory, '.git'))
    return directory


# FROM: https://github.com/shpala/pybuild_utils/blob/master/base/utils.py
# This is another interesting idea and has many real-world applications.
# TODO: Review the code.
def is_role_based_email(email: str) -> bool:
    r = re.compile('([^@]+)@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$')
    match = r.match(email)
    if not match:
        return False

    start = match.group(1)
    for x in ['noreply', 'support', 'admin', 'postmaster']:
        if start == x:
            return True

    return False
