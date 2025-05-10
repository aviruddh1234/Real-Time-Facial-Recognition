# Advanced Facial Recognition Attendance System in Python  
This project is a complete facial recognition-based attendance system built using Python. It leverages computer vision techniques to detect and recognize faces in real-time and uses a graphical user interface (GUI) built with Tkinter for user interaction. The system records attendance with timestamps and stores it in a structured format.  
## Features  
- Real-time face detection using **Haar Cascade Classifier**  
- Face recognition using **LBPH (Local Binary Pattern Histogram) Algorithm**  
- Tkinter-based user-friendly GUI  
- Automatic CSV-based attendance marking with date and time  
- Add new users dynamically by capturing their facial images  
- Train and retrain model based on collected facial data  
## Algorithms Used  
- **Haar Cascade Classifier**: Used for face detection. It's a machine learning-based approach where a cascade function is trained with lots of positive and negative images to detect objects (in this case, faces).  
- **LBPH (Local Binary Pattern Histogram)**: Used for face recognition. It labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number. This makes it efficient and robust for facial feature extraction.  
## Prerequisites  
Make sure the following libraries are installed:  
- Python 3.x  
- OpenCV  
- NumPy  
- Pandas  
- Tkinter (comes pre-installed with standard Python)  
## Installation  
1. Clone the repository:  
```bash  
git clone https://github.com/yourusername/facial-recognition-attendance.git  
cd facial-recognition-attendance  
```  
2. Install required packages:  
```bash  
pip install opencv-python numpy pandas  
```  
## How to Use  
1. **Register New User**  
   - Capture face data using your webcam  
   - Assign a unique ID and name to the person  
2. **Train the Model**  
   - Run the trainer module to learn from stored images  
3. **Recognize and Mark Attendance**  
   - Run the face recognition module  
   - Detected and matched faces will be logged with name, ID, date, and time  
4. **Launch GUI**  
   - Run the main application file to use all functionalities through a GUI  
```bash  
python main.py  
```  
## File Structure  
```  
facial-recognition-attendance/  
├── main.py                 # Main GUI application  
├── register.py             # Capture face data  
├── trainer.py              # Train model using LBPH  
├── recognizer.py           # Real-time recognition and attendance  
├── Attendance/             # CSV logs of attendance  
├── dataset/                # Captured face images  
├── trainer/                # Trained LBPH model  
├── requirements.txt        # List of dependencies  
```  
## Output Example  
- Captures face images and stores in `dataset/`  
- Trains model and saves to `trainer/`  
- Attendance saved as `Attendance/Attendance_YYYY-MM-DD.csv`  
```csv  
Name,ID,Date,Time  
John Doe,3,2025-05-09,10:24:55  
``` 
---  
Built with ❤️ using Python, OpenCV, Haar Cascade, and LBPH
