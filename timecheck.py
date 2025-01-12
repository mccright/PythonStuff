from time import gmtime, localtime, asctime, strftime, tzset
import os
# This is just some experimenting with a number of approaches to 
# configuring and presenting "time."
# This approach is only useful when you have tight controls over the local time.
# For shared code, use the approach outlined in the ntpTime/ directory.

def myDateTime(): return (strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
def syslogGmtime(): return (strftime("%b %d %H:%M:%S", gmtime()))
def myLocalTime(): return (strftime("%a, %d %b %Y %H:%M:%S %Z", localtime()))
def syslogLocaltime(): return (strftime("%b %d %H:%M:%S %Z", localtime()))
def myAscTime(): return (asctime())
def syslogLocaltimeGMT(): return (strftime("%b %d %H:%M:%S %Z", localtime()))
def syslogLocaltimeUCT(): return (strftime("%b %d %H:%M:%S %Z", localtime()))

print(f"gmtime function says:              {myDateTime()} GMT")
print(f"localtime function says:           {myLocalTime()}")
print(f"asctime function says:             {myAscTime()}")
print(f"syslog time format from gmtime:    {syslogGmtime()}")
print(f"syslog time format from localtime: {syslogLocaltime()}")
print(f"\n------------------------------------------------\n")
# Now explicitly set the timezone as we should.  This assumes
# we are on a unix box having a ZoneInfo timezone database
# at /usr/share/zoneinfo
print(f"Now we explicitly set the timezone to GMT")
os.environ['TZ'] = 'GMT'
tzset()
syslogLocaltimeGMTstr = syslogLocaltimeGMT()
print(f"Now we explicitly set the timezone to UCT")
os.environ['TZ'] = 'UCT'
tzset()
syslogLocaltimeUCTstr = syslogLocaltimeUCT()
print(f"Now we explicitly set the timezone to US/Central")
print(f"Have any of the dates changed?")
os.environ['TZ'] = 'US/Central'
tzset()
print(f"gmtime function says:                               {myDateTime()} GMT")
print(f"localtime function says:                            {myLocalTime()}")
print(f"asctime function says:                              {myAscTime()}")
print(f"syslog time format from localtime GMT tzone:        {syslogLocaltimeGMTstr}")
print(f"syslog time format from localtime UCT tzone:        {syslogLocaltimeUCTstr}")
print(f"syslog time format from localtime US/Central tzone: {syslogLocaltime()}")

print(f"\n------------------------------------------------\n")
