from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import json


app = ClarifaiApp(api_key='ac3e2c2bfc094e94b32c36679d7060b1')

#Get our model
model = app.models.get('recycle-items')

# Add images as training inputs
filename = "C:\\Users\\Tim\\OneDrive\\Documents\\School\\4OI6\\Captures\\Crops\\Sample01.jpg"
outname = "paper-test1.json"
#app.inputs.create_image_from_filename(filename, concepts=['paper'], not_concepts=['metal', 'glass'])

# Try predicting with the model
response = model.predict_by_filename(filename)

# First, make sure that the operation was sucessful (status code = 10000)
if (response['status']['code'] != 10000):
    print('Error: Status is not OK. Recieved code {} ({})'.format(response['status']['code'],
                                                                  response['status']['description']))
    exit(1)

#print(response)
data = response['outputs'][0]['data']['concepts']
for entry in data:
    print('{}\n'.format(entry))

with open(outname, 'w') as outfile:
    json.dump(response, outfile)