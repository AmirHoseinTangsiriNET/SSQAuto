from __future__ import absolute_import
from __future__ import print_function
import splunklib.client as client
import splunklib.results as results

HOST = "localhost"
PORT = 8089
USERNAME = "admin"
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














"""
from __future__ import absolute_import
from __future__ import print_function
import splunklib.client as client
import splunklib.results as results


service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)

#searches for previous day
kwargs_oneshot = {"earliest_time":"@d"}
#search being run
SearchQouery = """
#index="splunkautomation" sourcetype="wineventlog:system" "type=warning"
"""
#running and storing results
SearchQouery_results = service.jobs.oneshot(SearchQouery, **kwargs_oneshot)
 # Get the results and display them using the ResultsReader
reader = results.ResultsReader(SearchQouery_results)
for item in reader:
    print(item)
    print(item['avg(PercentMemory)'])


print ("[-]:List Of Splunk App:")
for app in service.apps:
    print ("  [+] {0}".format(app.name))

"""