#!/usr/bin/env python3
import requests
import os
import getopt
import sys

# Sometimes you need to know what types of files are in a github repo along
# with their layout in order to prepare for some follow-on analysis.
# This script is a model for extracting a list of files in tree format

# This version is for GH environments where there are organizations


def main(argv):
    if sys.version_info < (3, 10):
        raise Exception("Use only with Python 3.10 or higher")

    username = ''
    orgname = ''
    repo = ''

    if not (sys.argv[1:]):
        print('Get list of repo tree file names from github.com.')
        print('Inputs required: githubfilestree.py -u <user> -r <repo> -o <organization>')
        sys.exit(2)

    try:
        opts, args = getopt.getopt(argv, 'hu:r:o:', ['user=','repo=','org='])
    except getopt.GetoptError as err:
        print(err)
        print('Get list of repo tree file names from github.com.')
        print('githubfilestree.py -u <user> -r <repo> -o <organization>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('Get list of repo tree file names from github.com.')
            print('githubfilestree.py -u <user> -r <repo> -o <organization>')
            sys.exit()
        elif opt in ("-u", "--user"):
            username = arg
        elif opt in ("-r", "--repo"):
            repo = arg
        elif opt in ("-o", "--org"):
            orgname = arg

    """
    username = '<UserNameHere>'
    orgname = '<OrganizationNameHere>'
    repo = '<RepositoryNameHere>'
    token = '<PersonalTokenFromEnvironmentorSecretStoreHere>'
    # or get the token from the environment:
    """
    token = os.environ['GHPAT']
    url = "https://api.github.com/repos/{}/{}/git/trees/main?recursive=1".format(orgname, repo)
    reposeparator = "="*80

    # Authenticate & create session
    ####
    gh_session = requests.Session()
    gh_session.auth = (username, token)

    # Fetch repo data
    ####
    r = gh_session.get(url)
    response = r.json()

    # Report
    ####
    print(reposeparator)

    numberoffiles = len(response["tree"])
    print(f"Github user: {username}")
    print(f"Github org:  {orgname}")
    print(f"Github repo: {repo}")
    print(f"{str(numberoffiles)} files in {orgname}/{repo} include: ")
    for file in response["tree"]:
        print(file["path"])

    print(reposeparator)


if __name__ == '__main__':
    main(sys.argv[1:])
