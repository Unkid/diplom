from tensorflow import keras
from PIL import Image
from io import BytesIO
import numpy as np

class EmotionModel:
    def __init__(self, model_image):
        self.model = keras.models.load_model(model_image)
        self.classes = [
                'angry',
                'disgust',
                'fear',
                'happy',
                'neutral',
                'sad',
                'surprise'
        ]

    def class_name(self, ix):
        return self.classes[np.array(ix).flatten()[0]]

    def remove_transparency(self, img, bg_colour=(255, 255, 255)):
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            alpha = img.convert('RGBA').split()[-1]
            bg = Image.new("RGBA", img.size, bg_colour + (255,))
            bg.paste(g, mask=alpha)
            return bg
        else:
            return img

    def resize_image(self, img):
        width, height = img.size
        square_side = min(width, height)
        img = img.crop((
            np.ceil((width - square_side) / 2),
            np.ceil((height - square_side) / 2),
            np.ceil((width + square_side) / 2),
            np.ceil((height + square_side) / 2)
        ))
        img.thumbnail((48, 48))
        img = self.remove_transparency(img).convert('L')
        np_array = np.array(img) / 255
        
        return np_array

    def predict_emotion(self,face, frame):
        crop_img = frame[face[1]:face[3], face[0]:face[2]]
        img_pil=Image.fromarray(crop_img)
        img = self.resize_image(img_pil)
        img = img.reshape( 48, 48, 1)
        fer_class = self.model.predict(np.array([img]))
        class_text = self.class_name(np.argmax(fer_class))

        return class_text

    

