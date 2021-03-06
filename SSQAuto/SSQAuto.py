from __future__ import absolute_import
from __future__ import print_function
import splunklib.client as client
import splunklib.results as results

#Splunk Server IP Address Or HostName
HOST = "127.0.0.1"
#Splunk Mgmt Port (Default = 8089)
PORT = "8089"
#Splunk UserName
USERNAME = "admin"
#Splunk Password
PASSWORD = "TOSINSO12345"


service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)

SplunkQuery = input("[+]Please Enter The Your Search Query: ")
print ('...')
#searches for previous day
kwargs_oneshot = {"earliest_time":"@d"}
#search being run
searchquery_oneshot = SplunkQuery
#running Searching and storing results of searching
oneshotsearch_results = service.jobs.oneshot(searchquery_oneshot, **kwargs_oneshot)
# Get the results and display them using the ResultsReader
reader = results.ResultsReader(oneshotsearch_results)
print ("[-]Splunk Search Query Results: ")
for item in reader:
    print("[+]Event:\n {0}".format(item))
