import requests
import json

apikey = "fc0bffbf1a792d2b6d97f06456c19a4d451029e91318ac05ff671fa529efc769"

#Mimikatz Hashes
md5 = "6c042d2609b037b2adec7f2f2562ba6a"
sha1 = "7e577e3019408edfcc245faa4421d77655f2e447"
sha2 = "d429f6915975af38adf75e0bfce3195b54895e15cac3abbf790f8fa666ed87ee"

#Get Hashes from file
f = open('hashes.txt', "r")
hashes = f.readlines()
f.close()

print ("Hashes from readlines:")
for hash in hashes:
    print(hash)

wait_time = 15
url = 'https://www.virustotal.com/vtapi/v2/file/report'
params = {'apikey': apikey, 'resource': md5}
response = requests.get(url, params=params)
dictresponse = response.json()

print ('This is the API key: ' + apikey)
#print(response.json())
#print(json.loads(response.json()))
for key in ("md5","sha1","sha256"):
    print("The " + key + " hash is " + dictresponse[key])


print(response.status_code)
