import csv
import json
import urllib.request

# Basic script to convert input json url to csv output
url = '<json url>'
data = urllib.requests.urlopen(url)
d = json.loads(data.read().decode())

f = csv.writer(open('C:\\temp\\output.csv', 'w', encoding='utf8', newline=''))
f.writerow(['OBJECTID','AssessmentNumber','LevyCode','LevyDescription','LevyRate','LevyAmount','FormattedValuationID','CapitalValue'])

for x in d:
    #print(x)
    for i, val in enumerate(x):
        #print(i, val)
        f.writerow([
            val['attributes']['OBJECTID'],
            val['attributes']['AssessmentNumber'],
            val['attributes']['LevyCode'],
            val['attributes']['LevyDescription'],
            val['attributes']['LevyRate'],
            val['attributes']['LevyAmount'],
            val['attributes']['FormattedValuationID'],
            val['attributes']['CapitalValue']
        ])