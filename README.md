# Face Detection In Python

## Introduction

The definition of face detection refers to computer technology that is able to identify the presence of people’s faces within digital images. In order to work, face detection applications use machine learning and formulas known as algorithms to detecting human faces within larger images. These larger images might contain numerous objects that aren’t faces such as landscapes, buildings and other parts of humans (e.g. legs, shoulders and arms).

One of the most important applications of face detection, however, is facial recognition. Face recognition describes a biometric technology that goes way beyond recognizing when a human face is present. It actually attempts to establish whose face it is. The process works using a computer application that captures a digital image of an individual’s face (sometimes taken from a video frame) and compares it to images in a database of stored records. While facial recognition isn’t 100% accurate, it can very accurately determine when there is a strong chance that an person’s face matches someone in the database.

**Note:** This is a example of face detection not face recognition.


![Face](github-readme-contants/face.gif)

**Note:** This prototype is using Haar Cascade Classifier as a major component to perform face detection.


## Technology & Framework

- Python 3.8
- OpenCV

### Why OpenCV?

OpenCV is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel, it was later supported by Willow Garage then Itseez. The library is cross-platform and free for use under the open-source Apache 2 License.

**Note:** OpenCV framework plays a major role in this prototype.


## Configuration & Setup

- Installing OpenCV

```
pip install opencv-python
```

## Haar Cascade Algorithm

 It is an Object Detection Algorithm used to identify faces in an image or a real time video. The algorithm uses edge or line detection features proposed by Viola and Jones in their research paper “Rapid Object Detection using a Boosted Cascade of Simple Features” published in 2001

 ![Face](github-readme-contants/a1.png)

![Face](github-readme-contants/a2.jpg)

![Face](github-readme-contants/a3.png)

**Researh Paper:** https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/viola-cvpr-01.pdf


## Project Structure

**Note:** There are 3 python scripts are in this project folders, those are the following.

- run-with-images.py - *To run with images*
- run-with-videos.py - *To run with video files*
- run-with-webcam.py - *To run with webcam*

![Face](github-readme-contants/github.jpg)


## Run with Images (run-with-images.py)

- To execute this script

```
Python run-with-images.py

```

### Output

![Face](github-readme-contants/run-with-images-output.jpg)

### To try with different images

![Face](github-readme-contants/run-with-images-output-code.jpg)

**Note** To change different images, edit the image path in the cv2.imread() function.

## Run with videos (run-with-videos.py)

- To execute this script

```
Python run-with-videos.py

```

### Output

![Face](github-readme-contants/run-with-video-output.gif)

### To try with different webcam

![Face](github-readme-contants/run-with-videos-output-code.jpg)

**Note** To change different videos, edit the video path in the cv2.VideoCapture() function.

## Run with webcam (run-with-webcam.py)

- To execute this script

```
Python run-with-webcam.py

```

### Output

![Face](github-readme-contants/webcam.gif)

### To try with different webcam

![Face](github-readme-contants/webcam-code.jpg)

**Note** To change different webcam, change the index in the cv2.VideoCapture() function. "0" means the first camera, "1" means the second camera and so on.

# Contact

### 🌐 Website:
[![Visit](https://img.shields.io/badge/Visit%3A%20www.mpowerr.com-%23007ACC?style=flat&logo=google-chrome&logoColor=white&labelWidth=200)](https://www.mpowerr.com)

---

### 📱 Social Media:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/mpowerr-info)
[![Facebook](https://img.shields.io/badge/Facebook-%231877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/mpowerr.info)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/mpowerr.info)
[![X (Twitter)](https://img.shields.io/badge/X-%231DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/MpowerrInfo)
[![TikTok](https://img.shields.io/badge/TikTok-%23000000?style=for-the-badge&logo=tiktok&logoColor=white)](https://www.tiktok.com/@mpowerr.info)
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@mpowerrinfo)

---
