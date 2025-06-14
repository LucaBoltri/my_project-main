from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np


def indentificador (imagen):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("./keras_model.h5", compile=False)

    # Load the labels
    class_names = open("./labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(imagen).convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)

    if index == 0:
        return "Las tubas son los cimientos de la banda. Son enormes y tienen un sonido profundo y potente. Se necesita buen pulmón y resistencia. No es lo más ágil del mundo, pero sí súper importante para dar cuerpo al sonido."
    elif index == 1:
        return "Las trompetas suenan fuerte y claro, muchas veces llevan la melodía. Requieren precisión, buena embocadura y bastante práctica para controlar la afinación. ¡Un clásico en cualquier orquesta!"
    elif index == 2:
        return "Las trompas tienen un sonido suave y melancólico, pero son de los instrumentos más complicados de tocar. Embocadura exigente, muchas notas posibles por válvula… ¡no son para cualquiera!"
    elif index == 3:
        return "El trombón tiene un sonido potente y flexible. Usa vara (no pistones), así que hay que tener buen oído para afinar. Ideal para hacer pasajes suaves entre notas y efectos. Muy divertido, pero requiere coordinación."
