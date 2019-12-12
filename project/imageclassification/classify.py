from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

#
# use class or function this will not work with openapi

model = ResNet50(weights='imagenet')

img = image.load_img(temp.jpg)
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = model.predict(x)
retJson[decode_predictions(preds, top=3)]
print('Predicted:', decode_predictions(preds, top=3)[0])
with open("text.txt") as f:
    json.dump(retJson)
