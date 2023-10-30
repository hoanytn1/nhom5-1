import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        global original_image
        original_image = cv2.imread(file_path)
        original_image = resize_image(original_image, max_height=400)
        display_original_image(original_image)
        display_rotated_image(original_image)

def resize_image(image, max_height):
    height, width, _ = image.shape
    if height > max_height:
        scaling_factor = max_height / height
        new_height = int(height * scaling_factor)
        new_width = int(width * scaling_factor)
        image = cv2.resize(image, (new_width, new_height))
    return image

def apply_thresholds():
    if original_image is not None:
        global threshold1, threshold2
        threshold1 = int(threshold1_entry.get())
        threshold2 = int(threshold2_entry.get())
        processed_image = apply_edge_detection(original_image, threshold1, threshold2)
        display_processed_image(processed_image)

def apply_edge_detection(image, t1, t2):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, t1, t2)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

def update_zoomed_image():
    if original_image is not None:
        x = int(x_entry.get())
        y = int(y_entry.get())
        zoomed_image = zoom_image(original_image, x, y)
        display_zoomed_image(zoomed_image)

def zoom_image(image, x, y):
    zoomed_image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    return zoomed_image

def rotate_image():
    if original_image is not None:
        angle_str = rotation_entry.get()
        try:
            angle = int(angle_str)
            rotated_image = rotate(original_image, angle)
            display_rotated_image(rotated_image)
        except ValueError:
            # Handle the case where the input angle is not a valid integer.
            # You can show an error message or take appropriate action here.
            pass

def rotate(image, angle):
    height, width, _ = image.shape
    rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

def display_original_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(image)
    img = ImageTk.PhotoImage(img)
    original_label.config(image=img)
    original_label.image = img

def display_processed_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(image)
    img = ImageTk.PhotoImage(img)
    processed_label.config(image=img)
    processed_label.image = img

def display_zoomed_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(image)
    img = ImageTk.PhotoImage(img)
    zoomed_label.config(image=img)
    zoomed_label.image = img

def display_rotated_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(image)
    img = ImageTk.PhotoImage(img)
    rotated_label.config(image=img)
    rotated_label.image = img

root = tk.Tk()
root.title("Image Manipulation")

open_button = ttk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

threshold_frame = ttk.Frame(root)
threshold_frame.pack()

ttk.Label(threshold_frame, text="Threshold 1:").grid(row=0, column=0, padx=5)
threshold1_entry = ttk.Entry(threshold_frame)
threshold1_entry.grid(row=0, column=1)

ttk.Label(threshold_frame, text="Threshold 2:").grid(row=1, column=0, padx=5)
threshold2_entry = ttk.Entry(threshold_frame)
threshold2_entry.grid(row=1, column=1)

apply_button = ttk.Button(root, text="Apply Thresholds", command=apply_thresholds)
apply_button.pack(pady=10)

zoom_frame = ttk.Frame(root)
zoom_frame.pack()
ttk.Label(zoom_frame, text="Zoom X:").grid(row=0, column=0, padx=5)
x_entry = ttk.Entry(zoom_frame)
x_entry.grid(row=0, column=1)
ttk.Label(zoom_frame, text="Zoom Y:").grid(row=1, column=0, padx=5)
y_entry = ttk.Entry(zoom_frame)
y_entry.grid(row=1, column=1)

zoom_button = ttk.Button(root, text="Zoom Image", command=update_zoomed_image)
zoom_button.pack(pady=10)

rotate_frame = ttk.Frame(root)
rotate_frame.pack()
ttk.Label(rotate_frame, text="Rotation Angle:").grid(row=0, column=0, padx=5)
rotation_entry = ttk.Entry(rotate_frame)
rotation_entry.grid(row=0, column=1)
rotate_button = ttk.Button(root, text="Rotate Image", command=rotate)
rotate_button.pack(pady=10)

original_label = ttk.Label(root)
original_label.pack()

processed_label = ttk.Label(root)
processed_label.pack()

zoomed_label = ttk.Label(root)
zoomed_label.pack()

rotated_label = ttk.Label(root)
rotated_label.pack()

original_image = None
threshold1 = 0
threshold2 = 0

root.mainloop()
