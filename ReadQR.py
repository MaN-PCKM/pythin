import cv2
from pyzbar import pyzbar

def detect_qr_code():
    # Open the video stream from the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect and decode QR codes
        qr_codes = pyzbar.decode(gray)

        # If QR code is detected, print the decoded information
        if qr_codes:
            print("Decoded Information:")
            for qr_code in qr_codes:
                decoded_info = qr_code.data.decode("utf-8")
                print(decoded_info)

        # Display the frame
        cv2.imshow("QR Code Detection", frame)

        # Exit if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video stream and close windows
    cap.release()
    cv2.destroyAllWindows()

# Call the function to detect QR codes from webcam
detect_qr_code()