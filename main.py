import argparse
import pandas as pd
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Demo - Trafic Sign")
parser.add_argument("-I", "--image", help="Imagem a ser analisada")

args = parser.parse_args()

labels_csv_path = 'Labels.csv'
df_label = pd.read_csv(labels_csv_path)
img_height = 25
img_width = 25
model = load_model('modelofinal.h5')


def main(image):
    img = tf.keras.preprocessing.image.load_img(
        image, target_size=(img_height, img_width)
    )
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    predictions = model.predict(img_array)
    id_predict = np.argmax(predictions)
    print(f'Id da classe foi : {id_predict} Descrição da placa: {df_label.iloc[id_predict].SignName}')


if __name__ == "__main__":
    main(args.image)
# python main.py -I Train/20/00020_00000_00000.png 





