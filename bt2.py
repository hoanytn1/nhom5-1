import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

# Hàm để quay ảnh
def rotate_image(image_path):
    # Đọc ảnh từ đường dẫn
    img = cv2.imread(image_path)

    # Nhập góc quay từ người dùng qua giao diện Tkinter
    angle = float(rotate_angle.get())

    # Thực hiện quay ảnh
    height, width = img.shape[:2]
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))

    # Hiển thị ảnh ban đầu
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # Hiển thị ảnh sau khi quay
    plt.subplot(1, 2, 2)
    plt.title(f"Rotated (Angle={angle} degrees)")
    plt.imshow(cv2.cvtColor(rotated_img, cv2.COLOR_BGR2RGB))
    plt.show()

# Hàm để mở ảnh từ máy tính
def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Hiển thị ảnh đã mở
        img = Image.open(file_path)
        img.thumbnail((400, 400))  # Để hiển thị ảnh nhỏ hơn
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img
        # Cập nhật đường dẫn ảnh đã mở
        rotate_image_button['state'] = tk.NORMAL
        global selected_image_path
        selected_image_path = file_path

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Rotate Image")

# Nhãn và ô nhập góc quay
rotate_angle_label = tk.Label(root, text="Góc quay (độ):")
rotate_angle_label.pack()
rotate_angle = tk.Entry(root)
rotate_angle.pack()

# Nút để mở ảnh từ máy tính
open_image_button = tk.Button(root, text="Mở ảnh", command=open_image)
open_image_button.pack()

# Nhãn và hình ảnh để hiển thị ảnh đã mở
image_label = tk.Label(root)
image_label.pack()

# Nút để thực hiện quay ảnh
rotate_image_button = tk.Button(root, text="Quay ảnh", command=lambda: rotate_image(selected_image_path))
rotate_image_button.pack()
rotate_image_button['state'] = tk.DISABLED

# Biến lưu trữ đường dẫn ảnh đã chọn
selected_image_path = None

root.mainloop()
