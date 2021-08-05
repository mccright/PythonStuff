#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# StringFinder
# This is a harness for evaluating the contents of files 
# (in a directory and all child directories) using 
# a collection of your own regex's. 
# It is not something that you can just download and use without customization. 
# It is a harness for you to use your regex's against a bunch of files. 
#
# Install:
# binaryornot, DateTime
#
# Test your regex's with: https://regex101.com/
#
# I started trying to use the utilities below, but ended up using their ideas & some code here.
# SecretFinder: Burp Suite Extension to find and search apikeys/tokens from a webpage 
# by m4ll0k
# https://github.com/m4ll0k/SecretFinder/blob/master/BurpSuite-SecretFinder/SecretFinder.py
# and
# TruffleHog: https://github.com/dxa4481/truffleHog
# https://github.com/dxa4481/truffleHogRegexes/blob/master/truffleHogRegexes/regexes.json

# Code Credits:
# OpenSecurityResearch CustomPassiveScanner: https://github.com/OpenSecurityResearch/CustomPassiveScanner
# PortSwigger example-scanner-checks: https://github.com/PortSwigger/example-scanner-checks
# https://github.com/redhuntlabs/BurpSuite-Asset_Discover/blob/master/Asset_Discover.py
# Then morphed the original code using ideas from:
# https://stackoverflow.com/questions/39293968/how-do-i-search-directories-and-find-files-that-match-regex
# https://pymotw.com/2/re/
# https://github.com/dxa4481/truffleHog/blob/dev/scripts/searchOrg.py
# https://thispointer.com/python-how-to-get-list-of-files-in-directory-and-sub-directories/
# Use the [re.I] 'ignore case' flag.
# re.findall( '[0-9a-fA-F]{40}', theString, re.I )
#
# Track your regex collection
# | Site      | Regex                                         | Reference                                                                     |
# | --------- | --------------------------------------------- | ----------------------------------------------------------------------------- |
# | name      | xox.-[0-9]{12}-[0-9]{12}-[0-9a-zA-Z]{24}      | https://api.slack.com/docs/oauth                                              |
# | GCP       | [A-Za-z0-9_]{21}--[A-Za-z0-9_]{8}             | undocumented (obtained by generating token)                                   |
# | ID in URL | [a-zA-Z0-9!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ]{0,64}[a-zA-Z]{3,10}://[\w\-\.:0-9/]+@[\w\-\.:/0-9]+',  #[0-9a-zA-Z.-/_]{3,200}@[\\s]{3,200}]'|
# | AWS ?1    | ((aws_|AWS_|_aws|_AWS)[a-zA-Z0-9!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]{1,1024})                                                   |
# | AWS ?2    | ([a-zA-Z0-9!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ]{0,48}(aws_|AWS_|_aws|_AWS)[a-zA-Z0-9!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ]{1,1024})|
# | AWS ?2    | ((aws-|AWS-|-aws|-AWS)[a-zA-Z0-9!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]{1,1024})                                                   |

import re
import datetime
import os
from binaryornot.check import is_binary

myprintablecharacters = "a-zA-Z0-9!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
# The following are just ideas for you:
regexs = {
    "hard-coded host": "(@DN)",
    "hard-coded host": "(FQDN)",
    "hard-coded identity": "(<identityString>)",
    "string_of_interest": "(<stringOfInterest>)",
    "aws_string_of_interest1": "((aws_|AWS_|_aws|_AWS)[a-zA-Z0-9!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]{1,1024})",
    "aws_string_of_interest2": "([a-zA-Z0-9!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ]{0,48}(aws_|AWS_|_aws|_AWS)[a-zA-Z0-9!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ]{1,1024})",
    "aws_string_of_interest3": "((aws-|AWS-|-aws|-AWS)[a-zA-Z0-9!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]{1,1024})",
    'pgp_private_block' : '-----BEGIN PGP PRIVATE KEY BLOCK-----',
    'rsa_private_key' : '-----BEGIN RSA PRIVATE KEY-----',
    'ssh_dsa_private_key' : '-----BEGIN DSA PRIVATE KEY-----',
    'ssh_ec_private_key' : '-----BEGIN EC PRIVATE KEY-----',
    'ssh_openssh_private key': '-----BEGIN OPENSSH PRIVATE KEY-----',
    'Identity in URL1': '[a-zA-Z0-9!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ]{0,64}[a-zA-Z]{3,10}://[\w\-\.:0-9/]+@[\w\-\.:/0-9]+',  #[0-9a-zA-Z.-/_]{3,200}@[\\s]{3,200}]',
    'Identity in URL2': '[a-zA-Z0-9!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ]{0,48}[a-zA-Z]{3,10}://[^/\\s:@]{3,20}:[^/\\s:@]{3,20}@.{1,100}[\"\\s]'
}

start = datetime.datetime.now()
dirName = os.getcwd()
listOfFiles = list()

# Documenting the start & end time  
print("-------------------------------------------------------------")
print(__file__ + " Report started at: %s" % start)
print("Root of target filesystem: %s" % dirName)
print("-------------------------------------------------------------")
print("\r\n")

for (dirpath, dirnames, filenames) in os.walk(dirName):
    # Build a list of filenames
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
    # Process each the files
for theFile in listOfFiles:
    # Iterate through each of the regexes in the regexs collection above
    for reg in regexs.items():
        # 'reg[0]' is the description
        # 'reg[1]' is the regex
        # Test for binary files (this catches most of them)
        if is_binary(theFile):
            continue
        else:
            lineNumber = 0
            try:
                # Important: Open the file read-only, and 
                # use Latin1 encoding on a Windows host so the regexes 
                # can be used against strings instead of bytes.
                for line in open(theFile, 'r', encoding='Latin1'):
                    lineNumber = lineNumber + 1
                    for match in re.finditer(reg[1], line):
                        print("File: %s:%d | possible secret: %s | matched: %s" % (
                            theFile, lineNumber, reg[0], match.string))
            except Exception as e:
                # This is used to deal with the few binary files that are missed by 'is_binary()'
                print('Can\'t process file: {0}!  Error is: {1}'.format(theFile, e))
                # Now break out of this loop & increment to next file
                # Don't try any more regex's for a binary or otherwise hosed file
                break

scriptEnded = datetime.datetime.now()
print("-------------------------------------------------------------")
print(__file__ + " Report ended at: %s" % scriptEnded)
print("Search Report took: %s " % str(scriptEnded - start))
print("Root of target filesystem: %s" % dirName)
print("-------------------------------------------------------------")
print("\r\n")
