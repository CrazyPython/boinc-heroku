import os, time, requests, uuid

print(

os.system("boinccmd --project_attach http://universeathome.pl/universe/ 26444_75b49274e2105b916557e65ea236e7e4")

)

instance_id = str(uuid.uuid4())
lead_url = "a001-bonic.herokuapp.com"
report_back_postfix = "/internals/v0.01-ping/"

while True:
   time.sleep(10)
   requests.post(lead_url + report_back_postfix + instance_id)
   pass