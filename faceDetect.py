import json, sys, os, requests
import httplib, urllib, base64
import urllib3

urllib3.disable_warnings()

subscription_key = "4c9f57cd09c741cf92e852d98129b8b8"   
assert subscription_key

detect_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
verify_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/verify'
myFace_url = 'https://avatars3.githubusercontent.com/u/17981265?s=400&u=747aacb4e4333efe4d9414f5cc04b4028b3e5572&v=4'
#createPersonGroup_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/persongroups/'
baseUrl = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'

headers1 = { 'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/json'}

params1 = {
   'returnFaceId': 'true',
   'returnFaceLandmarks': 'false',
   'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}
# post image url, get response and print face id

# print temp[0]

# params2 = {
#     'personGroupId': 'alexanderGroup',
#     "userData": temp[0]
#}

#def createPersonGroup():
    # response = requests.put(createPersonGroup_url, params=params2, headers=headers)
    # data = response.json()
    # return data

# create person group id 
#response2 = requests.put(createPersonGroup_url, params=params2, headers=headers, name="group1", userData=data)
#data = response.json()
#print data

def createFace(image_url):
    response = requests.post(detect_url, params=params1, headers=headers1, json={"url": image_url})
    data = response.json()
    return data

temp = createFace(myFace_url)

def createPersonGroup(person_group_id, name=None, user_data=None):
    name = name or person_group_id
    url = 'persongroups/{}'.format(person_group_id)
    json = {
        'name': name,
        'userData': user_data,
    }
    #return requestMethod('PUT', url, json=json)
    return requestMethod('PUT', url, data=temp, json=json)

def requestMethod(method, url, data=None, json=None, headers=None, params=None):
    if not url.startswith('https://'):
        url = baseUrl + url
    #url = baseUrl + url
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = 'application/json'
    headers['Ocp-Apim-Subscription-Key'] = subscription_key

    response = requests.request(method, url, params=params, data=data, json=json, headers=headers, verify=False)

    result = None
    if response.text:
        print response
        result = response.json()
    else:
        result = {}

    return result

temp2 = createPersonGroup('alex', 'alex', temp)
#createPersonGroup(10, 10, temp[0]['faceId'])
#print temp2


#check arguments from github examples of person group, 