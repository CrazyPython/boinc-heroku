import os, time, requests, uuid

print(os.system("mkdir boinc-data"))  # create boinc data directory

print(os.system("boinc --dir ./boinc-data & "))

time.sleep(0.5)  # wait for boinc to start

print(
os.system("boinccmd --host 127.0.0.1 --dir ./boinc-data --passwd  26444_75b49274e2105b916557e65ea236e7e4 project_attach http://universeathome.pl/universe/ &")
)

instance_id = str(uuid.uuid4())
lead_url = "https://boincoku.herokuapp.com/"
report_back_postfix = "/internals/v0.01-ping"

while True:
   time.sleep(10)
   requests.post(lead_url + report_back_postfix + instance_id)
   pass