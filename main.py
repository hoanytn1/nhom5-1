import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

# Hàm để thay đổi kích thước ảnh
def zoom_image():
    # Đọc ảnh gốc
    img = cv2.imread('so2.jpg', cv2.IMREAD_GRAYSCALE)

    # Nhập tỉ lệ x và y từ người dùng qua giao diện Tkinter
    fx = float(scale_x.get())
    fy = float(scale_y.get())

    # Thay đổi kích thước ảnh theo tỉ lệ x và y
    resized_img = cv2.resize(img, (0, 0), fx=fx, fy=fy)

    # Hiển thị ảnh đầu ra sau khi zoom
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(img, cmap='gray')

    plt.subplot(1, 2, 2)
    plt.title(f"Zoomed (x={fx}, y={fy})")
    plt.imshow(resized_img, cmap='gray')
    plt.show()

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Zoom Image")

# Nhãn và thanh trượt cho tỉ lệ x và y
scale_x_label = tk.Label(root, text="Tỉ lệ x:")
scale_x_label.pack()
scale_x = tk.Entry(root)
scale_x.pack()

scale_y_label = tk.Label(root, text="Tỉ lệ y:")
scale_y_label.pack()
scale_y = tk.Entry(root)
scale_y.pack()

# Nút để thực hiện zoom ảnh
zoom_button = tk.Button(root, text="Zoom", command=zoom_image)
zoom_button.pack()

root.mainloop()