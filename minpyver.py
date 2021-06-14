import sys

# See also: https://github.com/saltstack/salt-pylint/blob/master/saltpylint/minpyver.py

class MinPy:

    def __init__(self, major_version=3, minor_version=5, dot3_version=0):
        self.MIN_PYTHON_MAJOR_VERSION=major_version
        self.MIN_PYTHON_MINOR_VERSION=minor_version
        self.MIN_PYTHON_DOT3_VERSION=dot3_version
        self.FAILED_MIN_PYTHON_VERSION=1
   
 
    def insist_on_python_vthree(self):
        min_major_version = self.MIN_PYTHON_MAJOR_VERSION
        min_minor_version = self.MIN_PYTHON_MINOR_VERSION
        min_dot3_version = self.MIN_PYTHON_DOT3_VERSION
        major_version = sys.version_info[0]
        minor_version = sys.version_info[1]
        dot3_version = sys.version_info[2]
        # The 'print' below may not be appropriate for all use cases.
        print("Running Python {}.{}.{}".format(major_version,minor_version,dot3_version))
        if (major_version < min_major_version):
            print("We need Python {}, you are running {}".format(min_major_version,major_version))
            sys.exit(self.FAILED_MIN_PYTHON_VERSION)
        if (minor_version < min_minor_version):
            print("We need Python {}.{} or above. Your environment is running {}.{}.{}".format(min_major_version,min_minor_version,major_version, minor_version,dot3_version))
            sys.exit(self.FAILED_MIN_PYTHON_VERSION)


if __name__ == '__main__':
    chkpy = MinPy(major_version=3,minor_version=7)
    chkpy.insist_on_python_vthree()

