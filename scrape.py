import json
import requests

# Send a GET request to the website
url = "https://raw.githubusercontent.com/the2hill/rs-flex-uptime-iad/refs/heads/master/README.md"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    resp = str(response.content)
    uptxt = 'All systems operational'
    degradedtxt = 'Degraded performance'
    fullouttxt = 'Complete outage'
    partialouttxt = 'Partial outage'
    outdict = {"schemaVersion": 1,
              "label": "status",
              "message": "operational",
              "color": "brightgreen"
              }
    if degradedtxt in resp:
        outdict['message'] = 'degraded'
        outdict['color'] = 'yellow'
    elif fullouttxt in resp:
        outdict['message'] = 'outage'
        outdict['color'] = 'red'
    elif partialouttxt in resp:
        outdict['message'] = 'partial outage'
        outdict['color'] = 'orange'
else:
    print("Failed to retrieve the website")

f = open("status.json", "w")
f.write(json.dumps(outdict))
f.close()
