import requests
from requests.structures import CaseInsensitiveDict

# make headers
def getHeaders(session):
    headers = CaseInsensitiveDict()
    headers["cookie"] = "JSESSIONID=" + session + ";"
    return headers

# fake verify view
def verify(host, session, repeat):
    for i in range(repeat):
        base = "https://www."
        tail = "/aioverify.html?idVideo=maKl5kVcUbo"
        url = base + host + tail
        resp = requests.get(url, headers=getHeaders(session))
        print(resp.text)

# activate the subscription
def finish(host, session):
    base = "https://www."
    tail = "/aiofinish.html"
    url = base + host + tail
    resp = requests.get(url, headers=getHeaders(session))
    print(resp.text)

# login into the application
def login(host, username, password):
    base = "https://www."
    tail = "/signinclick.html"
    data = "?email=" + username + "&idchannel=" + password + "&isSignIn=true&name="
    url = base + host + tail + data
    resp = requests.get(url)
    # return the JSESSIONID cookie
    return resp.headers["Set-Cookie"].split("JSESSIONID=")[1].split(";")[0]

# choose the plan
def choosePlan(host, session, planId):
    base = "https://www."
    tail = "/aiomarket.html?idPlan=" + str(planId)
    url = base + host + tail
    log = requests.get(url, headers=getHeaders(session))
    if (log.status_code == 200):
        print("[+] Activated")
    else:
        print("[-] Failed")


# main
def main():
    # make pairs of hosts, usernames, passwords and channels
    hosts = {"1": "subscribers.video", "2": "submenow.com"}
    usernames = {"1": "YOUR-EMAIL-FOR-ACCOUNT-ONE", "2": "YOUR-EMAIL-FOR-ACCOUNT-TWO"}
    passwords = {"1": "YOUR-CHANNEL-ID-ONE", "2": "YOUR-CHANNEL-ID-TWO"}
    channels = {"1": "YOUR-CHANNEL-NAME-ONE", "2": "YOUR-CHANNEL-NAME-TWO"}

    # menu options to choose a host and a channel
    for id, host in hosts.items():
        print("Press " + str(id) + " For ", host)
    hostId = input("Host Id: ")
    host = hosts[hostId]
    for id, channel in channels.items():
        print("Press " + str(id) + " For ", channel)
    channelId = input("Channel Id: ")

    # do login
    session = login(host, usernames[channelId], passwords[channelId])

    # choose the plan
    if (hostId == "1"):
        choosePlan(host, session, "6")
        verify(host, session, 29)
    if (hostId == "2"):
        choosePlan(host, session, "8")
        verify(host, session, 79)


    # finish the subscription
    finish(host, session)

# now run the main function
main() 
