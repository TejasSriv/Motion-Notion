
# **Motion Notion**

A Python-based motion detection application using OpenCV, designed to monitor motion through a webcam. It features dynamic frame comparison, adjustable sensitivity, and options for saving video recordings and log files.

## **Features**
- Detects motion using real-time video feed.
- Adjustable sensitivity to filter motion.
- Saves video recordings of detected motion.
- Logs motion events with timestamps.
- Clean and modular Python code for easy customization.

## **Installation**

### **Prerequisites**
Ensure you have Python3 installed. The following libraries are required:
- `opencv-python`
- `numpy`

You can install the dependencies using the following command:
```bash
pip install opencv-python numpy
```

### **Setup**
1. Clone this repository:
   ```bash
   git clone https://github.com/TejasSriv/Motion-Notion.git
   cd Motion-Notion
   ```
2. Run the program:
   ```bash
   python index.py
   ```

## **Usage**
1. The program will start the webcam and begin detecting motion.
2. Press **`q`** to exit the program.
3. Press **`r`** to refresh the frame if the lighting conditions change or the camera position change. The default frame refresh is set at 10000 frames.
4. Video recordings and logs will be saved in the `Records` folder.

## **Folder Structure**
```
motion-detection/
│
├── index.py                    # Main script
├── Records/                    # Folder for saved videos and logs
│   ├── motion_log.txt          # Log file for motion events
│   ├── motion_<timestamp>.avi  # Video recordings
│
└── README.md                   # Project documentation
```

## **Contributing**
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Added a new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.