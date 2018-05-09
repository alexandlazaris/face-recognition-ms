#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw
from matplotlib import patches
from io import BytesIO
import requests, json, sys, os

subscription_key = "4c9f57cd09c741cf92e852d98129b8b8"
assert subscription_key

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
#image_url = 'https://avatars3.githubusercontent.com/u/17981265?s=400&u=747aacb4e4333efe4d9414f5cc04b4028b3e5572&v=4'
image_url = 'https://media.licdn.com/dms/image/C4E03AQEWEvn7ZsSFIw/profile-displayphoto-shrink_800_800/0?e=1530748800&v=beta&t=fVkjElyGM94ZE7lqFO_1amYqDa57TfOyJOKzIBGxliY'

headers = { 'Ocp-Apim-Subscription-Key': subscription_key , 'Content-Type': 'application/json'}
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

def annotate_image(url):
    response = requests.post(face_api_url, params=params, headers=headers, json={"url": url})
    faces = response.json()
    
    image_file = BytesIO(requests.get(url).content)
    image = Image.open(image_file)
    
    plt.figure(figsize=(8,8))
    ax = plt.imshow(image)
    for face in faces:
        id = face["faceId"]
        fr = face["faceRectangle"]
        fa = face["faceAttributes"]
        origin = (fr["left"], fr["top"])
        p = patches.Rectangle(origin, fr["width"], fr["height"], fill=False, linewidth=2, color='b', alpha=0.5)
        ax.axes.add_patch(p)
        plt.text(origin[0], origin[1], "%s, %d, smile: %s"%(fa["gender"].capitalize(), fa["age"], fa["smile"]), fontsize=20, weight="bold", va="bottom", color="white", bbox=dict(facecolor='blue', alpha=0.5))
    plt.axis("off")
    #plt.savefig('myFaceOverlay.png', bbox_inches='tight')
    plt.savefig(id + '.png')

annotate_image(image_url)
#annotate_image('https://images.ctfassets.net/m9n2td3uf91z/2fdLiVBmK8m8ew4s0mgkq6/395fef6c77c29039fc673372748363fd/Alexander-Lazaris-Feature.jpg')
#annotate_image('https://dzamqefpotdvf.cloudfront.net/078909dd-1f61-4401-904d-deb50c951804.200x0x1.jpg')
#annotate_image('https://media.licdn.com/dms/image/C5603AQGVrQo32P4qeQ/profile-displayphoto-shrink_200_200/0?e=1529233200&v=beta&t=6qeVzYZN8eFfk4WmFjh5aB94oO4qzGXiuWQJDM-R8AY')
#annotate_image('https://image-store.slidesharecdn.com/78bda1c3-4187-48cc-aafc-0150b9d536c0-large.jpeg')
#annotate_image('https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fstatic.giantbomb.com%2Fuploads%2Foriginal%2F11%2F115901%2F2165235-portrait_alex.jpg')       

#file = open(sys.path[0] + '\index.html', 'w')
#file.write("Complete")