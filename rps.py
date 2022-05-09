import cv2
from keras.models import load_model
import numpy as np

model = load_model('keras_model.h5')

cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True:
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) /
                        127.0) - 1  # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)

    pred = [prediction[0][0], prediction[0][1],
            prediction[0][2], prediction[0][3]]

    max_pred = pred.index(max(pred))

    print("Rock: ", round(pred[0], 2), end=' ')
    print("Paper: ", round(pred[1], 2), end=' ')
    print("Scissor: ", round(pred[2], 2), end=' ')
    print("Nothing: ", round(pred[3], 2), end=' => ')

    if max_pred == 0:
        print("Rock")
    elif max_pred == 1:
        print("Paper")
    elif max_pred == 2:
        print("Scissor")
    else:
        print("Nothing")

    cv2.imshow('frame', frame)

    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
