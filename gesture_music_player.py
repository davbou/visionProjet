import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
from vlc_player import VLCPlayer
from argparse import ArgumentParser


def main_cam_loop(player, mpHands, hands, mpDraw, model, cap, classNames):
    classes_buffer = []

    while True:
        # Read each frame from the webcam
        _, frame = cap.read()

        x, y, _ = frame.shape

        # Flip the frame vertically
        frame = cv2.flip(frame, 1)
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        put_legend_on_frame(frame)

        # Get hand landmark prediction
        result = hands.process(framergb)

        className = ""

        # post process the result
        if result.multi_hand_landmarks:
            landmarks = []
            for handslms in result.multi_hand_landmarks:
                for lm in handslms.landmark:
                    # print(id, lm)
                    lmx = int(lm.x * x)
                    lmy = int(lm.y * y)

                    landmarks.append([lmx, lmy])

                # Drawing landmarks on frames
                mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

                # Predict gesture
                prediction = model.predict([landmarks])
                classID = np.argmax(prediction)
                className = classNames[classID]

        classes_buffer.append(className)
        if len(set(classes_buffer)) > 1:
            classes_buffer = classes_buffer[-1:]
        elif len(classes_buffer) >= 4:
            action = record_action_on_player(player, className)

            cv2.putText(frame, action, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # Show the final output
        cv2.imshow("Output", frame)

        if cv2.waitKey(1) == ord("q"):
            break


def put_legend_on_frame(frame):
    orig_point = (10, 360)
    fontscale = 0.6
    color = (255, 0, 0)
    thickness = 1
    y_increment = 25

    lines = ["Legende:", "Peace -> Play", "Main Pleine -> Pause", "Thumbs up -> Next", "Thumbs down -> Previous"]

    for i, line in enumerate(lines):
        cv2.putText(
            frame,
            line,
            (orig_point[0], orig_point[1] + i * y_increment),
            cv2.FONT_HERSHEY_SIMPLEX,
            fontscale,
            color,
            thickness,
            cv2.LINE_AA,
        )


def record_action_on_player(player, className):
    if className == "thumbs up":
        player.forward()
        return "Forward"
    elif className == "thumbs down":
        player.back()
        return "Backward"
    elif className == "peace":
        player.play()
        return "Play"
    elif className == "stop" or className == "live long":
        player.pause()
        return "Pause"


def main(args):
    # initialize vlc player
    player = VLCPlayer(args.path)

    # initialize mediapipe
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.8)
    mpDraw = mp.solutions.drawing_utils

    # Load the gesture recognizer model
    model = load_model("mp_hand_gesture")

    # Load class names
    with open("gesture.names", "r") as f:
        classNames = f.read().split("\n")

    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    main_cam_loop(player, mpHands, hands, mpDraw, model, cap, classNames)

    # release the webcam and destroy all active windows
    cap.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("--path", type=str, default="music", help="Path containing mp3 audio files.")

    args = parser.parse_args()
    main(parser.parse_args())
