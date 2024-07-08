import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

# Attempt to initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Failed to open webcam.")
    exit()

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print('Collecting data for class {}'.format(j))

    done = False
    while not done:
        ret, frame = cap.read()
        if not ret:
            print("Failed to retrieve frame from the webcam.")
            break

        cv2.putText(frame, 'Ready? Press "Q" !', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            done = True

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Failed to retrieve frame from the webcam.")
            break

        cv2.imshow('frame', frame)
        cv2.waitKey(100)  # wait a bit longer to ensure frames are captured
        image_path = os.path.join(class_dir, '{}.jpg'.format(counter))
        cv2.imwrite(image_path, frame)
        print(f"Captured image {counter} for class {j}")
        counter += 1

cap.release()
cv2.destroyAllWindows()
