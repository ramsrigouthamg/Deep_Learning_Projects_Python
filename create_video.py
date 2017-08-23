
import cv2
import numpy as np



if __name__ == "__main__":

    # Videocapture object to read the video.
    cap = cv2.VideoCapture('MVI_2424.MOV')#.subclip(20,25)
    # Define the codec and create VideoWriter object
    # fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter('output.avi', fourcc, 29.0, (1920, 1080))
    counter = 0
    while (cap.isOpened()):
        # Read an image
        ret, frame = cap.read()

        cv2.imshow('frame', frame)
        # Write the final image to videoWriter
        # out.write(final_output)
        if counter % 45 ==0:
            for i in range(5):
                out.write(frame)

        counter = counter + 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()