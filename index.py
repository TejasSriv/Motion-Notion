import cv2
import datetime
import logging

logging.basicConfig(
    filename = "motion_log.txt",
    level = logging.INFO,
    format = "%(asctime)s - %(message)s",
)

cap = cv2.VideoCapture(0)

_, first_frame = cap.read()
first_frame = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_frame = cv2.GaussianBlur(first_frame, (21, 21), 0)

codec = cv2.VideoWriter_fourcc(*'XVID')
out = None
recording = False

print("Motion Notion started.\n")

frame_counter = 0
update_interval = 10000
motion_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break
    
    frame_counter+=1
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    
    if frame_counter%update_interval == 0:
        first_frame = gray_frame.copy()
        print("Background refreshed.")
    
    frame_diff = cv2.absdiff(first_frame, gray_frame)
    
    _, thresh_frame = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
    
    motion_detected = False
    contours, _ = cv2.findContours(thresh_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue
        motion_detected = True
        
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    if motion_detected:
        motion_count+=1
        logging.info(f"Motion detected! Event #{motion_count}. ")
    
    if motion_detected and not recording:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        out = cv2.VideoWriter(f"motion_{timestamp}.avi", codec, 20.0, (frame.shape[1], frame.shape[0]))
        recording = True
        print("Recording started")
        
    if not motion_detected and recording:
        recording = False
        out.release()
        print("Recording stopped")
        
    if recording and out is not None:
        out.write(frame)
        
    cv2.imshow("Motion Notion", frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
    
    if key == ord('r'):
        first_frame = gray_frame
        print("Background refreshed.")
        
    if cv2.getWindowProperty("Motion Notion", cv2.WND_PROP_VISIBLE) <1:
        break

cap.release()

if out is not None:
    out.release()

cv2.destroyAllWindows()

summary = f"Motion detection ended. Total events logged: {motion_count}\n"
with open("motion_summary.txt", "w") as summary_file:
    summary_file.write(summary)

print(summary)