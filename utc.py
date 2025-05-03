import ntplib
import time


def local_to_utc(t):
    """
    Get the time from an ntp server (or pool).
    Print the current day date & time in UTC.
    Make sure that the dst flag is -1 -- this tells mktime to take daylight
    savings into account
    Function FROM: https://feihonghsu.blogspot.com/2008/02/converting-from-local-time-to-utc.html
    """
    return time.strftime("%a %b %d %Y %H:%M:%S", time.gmtime(t))


client = ntplib.NTPClient()
# Use of pool.ntp.org from inside your organization may be inappropriate
# or or it may be inaccessible (NTP may be blocked at your perimeter).
# Your organization may have an "internal" NTP server. If so, replace
# "pool.ntp.org" with your trusted server.
ntpserver = 'pool.ntp.org'
try:
    response = client.request(ntpserver, version=3)
except (Exception, ntplib.NTPException) as e:
    print(f"ntplib error occured while querying the server. {e}")
except Exception as ex:
    print(f"Unexpected error occured while querying the server. {ex}")
else:
    print(f"{local_to_utc(response.tx_time)} UTC")
