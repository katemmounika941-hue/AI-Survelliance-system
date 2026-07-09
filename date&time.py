import cv2
from datetime import datetime

camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()

    if ret:
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        cv2.putText(
            frame,
            time,
            (10,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        cv2.imshow("AI Surveillance Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()