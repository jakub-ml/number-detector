# Number Detector

## Project Summary

The goal of this project was to develop a simple yet effective digit recognition system based on image data. By using a trained neural network model, the system is able to classify 28x28 grayscale images of handwritten digits and predict the number they represent.

This project demonstrates how image data can be preprocessed, visualized, and passed through a machine learning model to achieve accurate classification results. It serves both as a practical implementation of digit recognition and as an educational tool for understanding image-based AI models.

The project can be run either using Docker or by installing the required dependencies listed in the requirements.txt file.
## Data:

The image shows a portion of a dataset where each row represents a flattened 28x28 grayscale image, with pixel values ranging from pixel1 to pixel784. All pixel values in the visible portion are zeros, indicating that these particular images are likely completely black or empty.


<p align="center">
  <img src="https://github.com/user-attachments/assets/23ae7d54-964e-45b2-ad4a-854f5f00aece" alt="image">
</p>

Each image can be represented as a specific data index and then displayed.

<p align="center">
  <img src="https://github.com/user-attachments/assets/0a59580f-8bf8-41d3-8cb4-9095aa44a74d" alt="image">
</p>

## Training process:

*Model Architecture*:

<p align="center">
  <img src="https://github.com/user-attachments/assets/68f81d89-8b77-4722-99e8-6f5bb3d07604" alt="image">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/94acf2b1-f8be-472e-a39f-238353a48325" alt="image">
</p>

*Accuracy function*:

<p align="center">
  <img src="tmp50wlmavl.gif" alt="image">
</p>

*Loss function*:

<p align="center">
  <img src="tmpakthgjb3.gif" alt="image">
</p>


Plots generated with: **open_atmos_jupyter_utils**

## How it works:
1. Open the terminal and navigate to the folder where the number_detector.py file is saved.
<p align="center">
  <img src="https://github.com/user-attachments/assets/758bf823-1f3a-44cd-8eab-e68993b78d33" alt="image">
</p>


2. Run the program with the command:
```python
   python number_detector.py
```

3. You'll see the following menu:
<p align="center">
  <img src="https://github.com/user-attachments/assets/62b1031b-30e1-400c-bc7f-f97ef1dd9490" alt="image">
</p>


4. The option "Explanation of how the program works" briefly describes what the program does.
<p align="center">
  <img src="https://github.com/user-attachments/assets/92d6f7a5-c84e-48a9-9e8d-46dc4c13c341" alt="image">
</p>

6. The "Load image" option lets you choose a specific 28x28 image file from the menu_data folder.
You can also add your own images, as long as they match the resolution of the sample data.
<p align="center">
  <img src="https://github.com/user-attachments/assets/7df2e9bb-5235-4cd0-a2c4-17db11966adc" alt="image">
</p>



8. The "Start" option allows you to recognize the digit in the selected image.
It returns the predicted number and the model's confidence level.
<p align="center">
  <img src="https://github.com/user-attachments/assets/f5e428c5-979d-4b5d-bc09-0026bd9f4f3a" alt="image">
</p>

9. The "Display selected image" option opens a window with the currently loaded image.
<p align="center">
  <img src="https://github.com/user-attachments/assets/41d562fa-f647-4fed-a7d1-886d0ea1a3a8" alt="image">
</p>

10. The "Exit" option closes the program.

