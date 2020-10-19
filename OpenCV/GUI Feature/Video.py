import cv2

# Capture the video
cap = cv2.VideoCapture(0)

# Output the video
fourcc = cv2.VideoWriter_fourcc(*'DVIX')
out = cv2.VideoWriter('Output.mp4', fourcc, 20, (640, 480))

while True:
    # capture frame by frame
    ret, frame = cap.read()  # ret == True/False
    print(cap.get(4))
    if ret is True:
        # Operation on the frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #frame = cv2.flip(frame, 0)

        out.write(gray)

        # Display the resulting frame
        cv2.imshow('Frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
