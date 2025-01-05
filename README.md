# MLB
My Little Botnet is a very simple tool that let's you execute python code on participating machines. 
This botnet does not have any ways of replicating itself. This is a personal project which involves 
"infecting" (manually adding to startup applications) a bunch of school computers, playing some
spooky sounds and deleting itself. But you can use it however you like.

"My" because it requires physical access to machine.

"Little" because client is only 37 lines of code.

## Installing

On both client and server:
```bash
git clone https://github.com/PythonWannabe1/MLB.git
```

### Server

Open the server.py file and in the very top of it you'll see a lot of variables. I think
they're pretty much self-explanatory, but here's what they do:


|Variable name|What it does|Data type|
|COMMAND_URL|Specifies the URL of the command and control server (Only scheme and host)|str|
|CONTROL_PANEL_ROUTE|Specifies the route to control panel|str|
|PAYLOAD_ROUTE|Specifies the route to payload|str|
|TOKENS|Specifies all tokens that will grant access to changing payload (maybe you share this botnet with friends)|list[str]|
|MAX_JOURNAL_ENTRIES|Specifies the maximum amout of entries kept in RAM|int|
|RESULTS_ROUTE|Path client uses to report results back to command server|str|
|LOG_PAYLOAD_REQUESTS|Specifies whether accesses to payload are logged|bool|

For examle if COMMAND_URL is set to "http://4.20.69.0" and PAYLOAD_ROUTE is set
to "/payload" then the payload will be requested from "http://4.20.69.0/payload".

### Client

COMMAND_HOST, PAYLOAD_ROUTE and RESULTS_ROUTE in client.py must have the same values as COMMAND_URL, 
PAYLOAD_ROUTE and RESULTS_ROUTE in server.py.

Add the client.py to startup (and rename it to client.py**w** on windows) and enjoy.
