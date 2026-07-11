# 📸 Real-Time Instagram Style Filters

A Computer Vision project built using **Python** and **OpenCV** as part of the AI/ML cohort Week 4 Assignment.

This application captures live video from the webcam and applies multiple Instagram-style filters in real time. Users can switch filters using keyboard shortcuts and save filtered images directly from the webcam.

## Link to video preview
https://drive.google.com/file/d/1fDye8JeZ7o0h_vUC363Bo4S7stEtLBRa/view?usp=sharing

## 🚀 Features

- 🎥 Live webcam feed
- 🎨 9 real-time image filters
- ⌨️ Keyboard-controlled filter switching
- 💾 Capture and save filtered images
- 🕒 Live date and time display
- 📢 Welcome message on startup
- 📂 Automatic image saving inside the `captures` folder
- 🧩 Modular code using separate filter functions


## 🛠️ Technologies Used

- Python 3
- OpenCV
- NumPy


## 📁 Project Structure

```text
real-time-instagram-filters/
│
├── main.py
├── filters.py
├── requirements.txt
├── README.md
├── .gitignore
├── captures/
└── screenshots/
```


## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/kaurrrgurleen/real-time-instagram-filters.git
```

Move into the project directory:

```bash
cd real-time-instagram-filters
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```


## 🎮 Keyboard Controls

| Key | Action |
|------|--------|
| 0 | Original |
| 1 | Black & White |
| 2 | Sepia |
| 3 | Sketch |
| 4 | Cartoon |
| 5 | Vintage |
| 6 | Warm |
| 7 | Cool |
| 8 | Cinematic |
| C | Capture Image |
| Q | Quit |


# 📸 Project Screenshots

## Original

<img width="640" height="480" alt="Original_20260712_015108" src="https://github.com/user-attachments/assets/91ebf363-0811-4a16-b12c-cc29c9acf690" />


---

## Black & White

<img width="640" height="480" alt="Black   White_20260712_020508" src="https://github.com/user-attachments/assets/22918d39-d010-455e-9dbd-d9fb650b4e68" />


---

## Sepia

<img width="640" height="480" alt="Sepia_20260712_020513" src="https://github.com/user-attachments/assets/48abd2f5-9a72-4208-821a-6a3e9f17f656" />


---

## Sketch

<img width="640" height="480" alt="Sketch_20260712_020519" src="https://github.com/user-attachments/assets/19a5c524-e481-4f18-82fe-1dd1eedc6787" />


---

## Cartoon

<img width="640" height="480" alt="Cartoon_20260712_020523" src="https://github.com/user-attachments/assets/3c7419ec-b757-4a90-9000-06e4f020bda8" />


---

## Vintage

<img width="640" height="480" alt="Vintage_20260712_020528" src="https://github.com/user-attachments/assets/5e4678cb-2064-4301-bd4c-4f45f181e71b" />


---

## Warm

<img width="640" height="480" alt="Warm_20260712_020531" src="https://github.com/user-attachments/assets/657ab8df-8f65-4d76-8200-9bc18f88bd9f" />


---

## Cool

<img width="640" height="480" alt="Cool_20260712_020535" src="https://github.com/user-attachments/assets/358f8425-8d2a-436d-bd79-0f40f61d0b47" />


---

## Cinematic

<img width="640" height="480" alt="Cinematic_20260712_020537" src="https://github.com/user-attachments/assets/909832ad-d08a-4bbd-bdbb-cb03b85f15d7" />

---


## 💡 Future Improvements

- Face Detection
- Face Filters
- Adjustable filter intensity
- GUI buttons instead of keyboard shortcuts
- Video recording support
- Additional artistic filters

---

## 👩‍💻 Author

**Gurleen Kaur**

## ✅ Results

The project successfully performs real-time image processing using OpenCV and a webcam.

### Key Outcomes

- Successfully captures live video from the webcam.
- Applies 9 different image filters in real time.
- Allows users to switch filters instantly using keyboard shortcuts.
- Saves filtered images with unique timestamp-based filenames.
- Displays the current filter name, project title, date & time, and keyboard shortcuts on the video feed.
- Organizes the code using separate filter functions for better readability and maintainability.

## 📚 Learning Outcomes

Through this project, I gained hands-on experience with:

- Real-time image processing using OpenCV
- Webcam integration in Python
- Color space transformations
- Edge detection and image filtering techniques
- Modular Python programming
- Working with keyboard events in OpenCV
- Saving processed images programmatically
- Project documentation using GitHub

> **Note:** This project was developed as part of my AI/ML Internship (Week 4 – Computer Vision), focusing on real-time image processing using Python and OpenCV.
