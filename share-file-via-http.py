import os
# This script started with advice from:
# https://github.com/yennanliu/utility_Python/blob/master/hack/pass_file_via_python_httpserver.py
# Thank you Yennan (Yen) Liu.
# 
# CAUTION:
# Everything about this approach makes your data temporarily insecure and it needs to be 
# risk appropriate for your use case.  Your data communications will be in clear text, 
# and any party or automation could download your file(s) while your http server is running. 
# This approach is not for everyone or every sharing context.
# If you are unsure about using this approach, don't!
# For sharing between team members on a single host or on a single private network, it may be OK.
#
# On the server & directory where the source data is currently stored (i.e., FROM)
# Example : cd ~/sharedData/timeSeriesDataYouNeed
# 
# python 3

IP_ADDRESS = '127.0.0.1'
TCP_PORT = '18765' 

print("On the server hosting the data, 'cd' into the directory where the file is located.")
print("and run the web server only long enough to copy the needed file.") 
print("Use this command:  ")
# Python 3.7 will stop getting security updates in June 2023. 
# 3.8, 3.9, 3.10, and 3.11 are available and you should
# upgrade if you are using 3.7 or below.
if os.sys.version_info > (3, 9):
    print(f"\npython3 -m http.server <TCP_PORT> --bind <IP_ADDRESS>")
    print("For example, port 18765 on localhost: ")
    print(f"python3 -m http.server {TCP_PORT} --bind {IP_ADDRESS}")

# python 2
# https://stackoverflow.com/questions/24444343/no-module-named-http-server/43939794
elif os.sys.version_info < (3):
    print(f"\npython -m SimpleHTTPServer <TCP_PORT> --bind <IP_ADDRESS>")
    print("For example, port 18765 on localhost: ")
    print(f"python -m SimpleHTTPServer {TCP_PORT} --bind {IP_ADDRESS}")

else:
    print("Either python is not installed, or this script misunderstands your current environment.")
    print("Exiting...")
    exit(1)

# In a terminal on the destination host (i.e., TO),
# downloak the file you need with the 'wget' command.
# For example if you are on the same host, but only need another user to access the file: 
# wget localhost:18765/theTimeSeriesFile.csv
print("\nThen download the file on the destination endpoint using the command below:")
print("wget <server_ip>:18765/<fileName>\n")
