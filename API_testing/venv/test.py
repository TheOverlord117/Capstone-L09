from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import json


app = ClarifaiApp(api_key='ac3e2c2bfc094e94b32c36679d7060b1')
model = app.public_models.general_model

response = model.predict([ClImage(filename='C:\\Users\\Tim\\OneDrive\\Documents\\School\\4oi6\\Captures\\metal_crop.jpeg')])

#For now, load the json file to experiment with parsing.
#with open('paper-resp.json', 'r') as infile:
#    response = json.load(infile)

# First, make sure that the operation was sucessful (status code = 10000)
if (response['status']['code'] != 10000):
    print('Error: Status is not OK. Recieved code {} ({})'.format(response['status']['code'],
                                                                  response['status']['description']))
    exit(1)

#print(response)
data = response['outputs'][0]['data']['concepts']
for entry in data:
    print('{}\n'.format(entry))

with open('metal-crop-resp.json', 'w') as outfile:
    json.dump(response, outfile)