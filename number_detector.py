import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import color
import os
from tensorflow.keras.models import load_model
import platform

#C:\Users\ADMIN\Desktop\Number Detector\number_detector.py
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
os.environ["SM_FRAMEWORK"] = "tf.keras"
model=load_model('model.h5')

# ustawienie ścieżki do foldera
path = "menu_data"

if platform.system() == "Windows":
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')
    
def detect(obraz):
    maxy = 0
    wynik = model.predict(np.array([obraz]))
    wynik = list(wynik.reshape(wynik.shape[0] * wynik.shape[1], ))
    for el in wynik:
        if el > maxy:
            maxy = el
    suma = 0
    for elem in wynik:
        if elem != maxy:
            suma = suma + 1
        if elem == maxy:
            suma_ost = suma
    return (suma_ost,maxy)

def menu(img=0):
    clear()
    print('#' * 100)
    print('    1. Explanation of how the program works')
    print('    2. Load image')
    print('    3. Start')
    print('    4. Display selected image')
    print('    5. Exit')
    print('#' * 100)
    x = int(input('    '))
    if x == 1:
        clear()
        print(
            'Load an image of size 28x28 from the selected folder (Digits), then choose "Start" and see if \n'
            'the program guessed your number correctly.\n\n'
            '   The "Digits" folder should be located at the path: ' + path + '\n\n')
        q = input('Type "q" to exit ')
        if q == 'q':
            clear()
            menu()
    if x == 2:
        clear()
        images = np.sort(os.listdir(path))
        # display files
        print('List of available files:')
        index = 0
        slownik = {}
        for elem in images:
            print('{}. {}'.format(index, elem))
            slownik[index] = elem
            index = index + 1
        # selecting the file for detection
        x = int(input('Select file number: \n'))
        selected = slownik[x]
        print('Selected file: {}\n'.format(selected))
        # loading the file
        img = cv2.imread(path + '/' + selected)
        clear()
        menu(img=img)
    if x == 3:
        img1 = color.rgb2gray(img)
        img1 = np.array((img1 * 255).reshape(784, ))
        print('The predicted number is: {} with a confidence of {}%'.format(detect(img1)[0], detect(img1)[1]*100))
        # first, a function that processes the received image to the correct size and predicts the result
        # then, a function that displays what number it is
        q = input('Type "q" to return to the menu: ')
        if q == 'q':
            menu(img=img)
    if x == 4:
        plt.imshow(img)
        plt.show()
        menu(img=img)
    if x == 5:
        clear()
menu()