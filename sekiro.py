import requests
requests.packages.urllib3.disable_warnings()
data = {
    "group": "ws-group-chinadrugtrials",
    "action": "executeJs",
    "code": "document.cookie"
}
import time
# 'http://www.python886.com:5620/business-demo/mock-allocate?ip=sekiro.virjar.com'
while True:
    a=time.time()
    res = requests.post(url="http://123.56.54.211:5601/asyncInvoke", data = data, verify=False)
    b=time.time()
    print(b-a)
    print(res.text)