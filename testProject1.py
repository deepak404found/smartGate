import cv2
import pytesseract

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 30, 150)

    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = float(w) / h

        if aspect_ratio >= 2.5 and aspect_ratio <= 4:
            license_plate_image = gray[y:y+h, x:x+w]
            license_plate_text = pytesseract.image_to_string(license_plate_image, lang='eng')
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            #cv2.putText(frame, license_plate_text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            print(license_plate_text)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

