import ntplib
from time import ctime
client = ntplib.NTPClient()
# Use inside your organization pool.ntp.org may be inappropriate or inaccessible.
# Your organization may have an "internal" NTP server.  If so, replace
# pool.ntp.org with your trusted server.
ntpserver = 'pool.ntp.org'
try:
    response = client.request(ntpserver, version=3)
except (Exception, ntplib.NTPException) as e:
    print(f"ntplib error occured while querying the server. {e}")
except Exception as ex:
    print(f"Unexpected error occured while querying the server. {ex}")
else:
    print('{0} {1} - ntp stratum: {2}, precision: {3} seconds'.format(ctime(response.tx_time), ntpserver, response.stratum, (response.precision*.001)))
#
# or use this as a function and return a timestamp as a string
#
# The options below might be useful for narrow problem-solving use cases:
# print(ctime(response.tx_time))
# print('ntp version: %s' % response.version)
# print('ntp mode: %s' % response.mode)
# print('round-trip delay: %s' % response.delay)
# print('root delay: %s' % response.root_delay)
# print('ntp precision: %s' % response.precision)
# print('ntp stratum: %s' % response.stratum)
# print('ntp root_delay: %s' % response.root_delay)
# print('ntp root_dispersion: %s' % response.root_dispersion)
# sleep(3)
# print(ctime(response.tx_time))
