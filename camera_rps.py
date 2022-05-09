import numpy as np
from keras.models import load_model
import cv2

import random
import time


def get_prediction(model_name, no_sec):
    model = load_model(model_name, compile=False)

    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Timer starts
    starttime = time.time()
    lasttime = starttime

    cnt = no_sec - 1

    while True:
        ret, frame = cap.read()
        resized_frame = cv2.resize(
            frame, (224, 224), interpolation=cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) /
                            127.0) - 1  # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)

        cv2.imshow('frame', frame)

        if lasttime + 1 <= time.time():
            print(f"{cnt}...", end=' ', flush=True)
            cnt -= 1
            lasttime = time.time()

        # Press q to close the window
        if (cv2.waitKey(1) & 0xFF == ord('q')) or (starttime + no_sec <= time.time()):
            print("\nTime is up!")
            break

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    return [prediction[0][0], prediction[0][1], prediction[0][2], prediction[0][3]]


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def get_user_choice(no_sec):
    print("Please show your choice: ")

    while(True):
        pred = get_prediction("keras_model.h5", no_sec)

        max_pred = pred.index(max(pred))

        if max_pred == 0:
            print("You have chosen Rock => ", end='')
            user_choice = "rock"
        elif max_pred == 1:
            print("You have chosen Paper => ", end='')
            user_choice = "paper"
        elif max_pred == 2:
            print("You have chosen Scissor => ", end='')
            user_choice = "scissor"
        else:
            print("You have chosen Nothing => ", end='')
            user_choice = None

        print("Rock:", round(pred[0], 2), "Paper:", round(pred[1], 2), "Scissor:",
              round(pred[2], 2), "Nothing:", round(pred[3], 2))

        if user_choice != None:
            break
        else:
            print("Please show a valid choice!")

    return user_choice


def get_winner(computer_choice, user_choice):
    if computer_choice == "rock":
        if user_choice == "rock":
            return "tie"
        elif user_choice == "paper":
            return "User"
        else:
            return "Computer"

    if computer_choice == "paper":
        if user_choice == "rock":
            return "Computer"
        elif user_choice == "paper":
            return "tie"
        else:
            return "User"

    if computer_choice == "scissors":
        if user_choice == "rock":
            return "User"
        elif user_choice == "paper":
            return "Computer"
        else:
            return "tie"


def play():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice(5)

        print(f"The computer has chosen {computer_choice}.")

        winner = get_winner(computer_choice, user_choice)

        if winner == "tie":
            print(f"There is no winner at round {rounds}.")
        else:
            print(f"The winner is {winner} at round {rounds}.")

            if winner == "Computer":
                computer_wins += 1
            if winner == "User":
                user_wins += 1

        print(f"Current score: Computer {computer_wins} - {user_wins} User.\n")

        if computer_wins == 3:
            print(f"Computer beats User by {computer_wins}-{user_wins}.")
            break

        if user_wins == 3:
            print(f"User beats Computer by {user_wins}-{computer_wins}")
            break

        rounds += 1


if __name__ == '__main__':
    play()
