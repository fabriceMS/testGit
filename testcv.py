import cv2

camIP = 'rtsp://admin:fab1801@192.168.2.63:554//live1.sdp'

print('Start Program')
cap = cv2.VideoCapture(camIP)

print('End Program')

while True:

    print('About to start the Read command')
    ret, frame = cap.read()
    print('About to show frame of Video.')
    cv2.imshow("Capturing",frame)
    print('Running..')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()