import requests, json, pprint, os, sys

subscription_key = "4c9f57cd09c741cf92e852d98129b8b8"
assert subscription_key

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
image_url = 'https://avatars3.githubusercontent.com/u/17981265?s=400&u=747aacb4e4333efe4d9414f5cc04b4028b3e5572&v=4'
#image_url = 'https://static.businessinsider.com/image/58ad74e2dd089560288b48f6/image.jpg' #rooney
#image_url = 'http://sse.royalsociety.org/2015/media/8703/facefacts_averages-full-size.png' # 4 faces
#image_url = 'http://talksport.com/sites/default/files/tscouk_old_image/81188326.jpg' #man utd 07/08 group

headers = { 'Ocp-Apim-Subscription-Key': subscription_key , 'Content-Type': 'application/json'}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
faces = response.json()
prettyFaces = json.dumps(faces, indent=4)
file = open(sys.path[0] + '\index.json', 'w')
#file.write('Detected %d faces in the image: %s' % (len(faces), image_url))
#file.write('<br>')
print prettyFaces
file.write(prettyFaces)
