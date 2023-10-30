import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

# Hàm xử lý sự kiện khi nút "Open Image" được nhấn
def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        global original_image
        original_image = cv2.imread(file_path)
        original_image = resize_image(original_image, max_height=400)  # Thay đổi kích thước ảnh
        display_original_image(original_image)

# Hàm thay đổi kích thước ảnh
def resize_image(image, max_height):
    height, width, _ = image.shape
    if height > max_height:
        scaling_factor = max_height / height
        new_height = int(height * scaling_factor)
        new_width = int(width * scaling_factor)
        image = cv2.resize(image, (new_width, new_height))
    return image

# Hàm xử lý sự kiện khi nút "Apply Thresholds" được nhấn
def apply_thresholds():
    if original_image is not None:
        global threshold1, threshold2
        threshold1 = int(threshold1_entry.get())
        threshold2 = int(threshold2_entry.get())
        processed_image = apply_edge_detection(original_image, threshold1, threshold2)
        display_processed_image(processed_image)

# Hàm hiển thị ảnh gốc trên giao diện
def display_original_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(image)
    img = ImageTk.PhotoImage(img)

    original_label.config(image=img)
    original_label.image = img




# Hàm áp dụng thuật toán tách biên
def apply_edge_detection(image, t1, t2):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, t1, t2)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

# Hàm hiển thị ảnh đã xử lý trên giao diện
def display_processed_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(image)
    img = ImageTk.PhotoImage(img)
    processed_label.config(image=img)
    processed_label.image = img

# Tạo cửa sổ giao diện tkinter
root = tk.Tk()
root.title("Edge Detection")

# Nút để mở hình ảnh từ máy tính
open_button = ttk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

# Khung nhập giá trị ngưỡng
threshold_frame = ttk.Frame(root)
threshold_frame.pack()

ttk.Label(threshold_frame, text="Threshold 1:").grid(row=0, column=0, padx=5)
threshold1_entry = ttk.Entry(threshold_frame)
threshold1_entry.grid(row=0, column=1)

ttk.Label(threshold_frame, text="Threshold 2:").grid(row=1, column=0, padx=5)
threshold2_entry = ttk.Entry(threshold_frame)
threshold2_entry.grid(row=1, column=1)

# Nút để áp dụng ngưỡng và hiển thị ảnh sau khi tách biên
apply_button = ttk.Button(root, text="Apply Thresholds", command=apply_thresholds)
apply_button.pack(pady=10)

# Label để hiển thị ảnh gốc
original_label = ttk.Label(root)
original_label.pack()

# Label để hiển thị ảnh sau khi tách biên
processed_label = ttk.Label(root)
processed_label.pack()

original_image = None
threshold1 = 0
threshold2 = 0

root.mainloop()
