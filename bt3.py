import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

# Hàm chuẩn hóa ảnh
def normalize_image(image):
    if len(image.shape) == 2:  # Nếu ảnh đen trắng
        normalized_image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
    else:  # Nếu ảnh màu
        normalized_image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
    return normalized_image

# Hàm chuyển ảnh màu thành ảnh đen trắng
def convert_to_grayscale(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

# Hàm xử lý nút mở tệp và hiển thị ảnh
def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        original_image = cv2.imread(file_path, cv2.IMREAD_COLOR)
        if original_image is not None:
            # Điều chỉnh kích thước ảnh ban đầu để phù hợp với Label
            h, w, _ = original_image.shape
            max_label_width = 400  # Đặt kích thước tối đa cho Label
            if w > max_label_width:
                scale = max_label_width / w
                original_image = cv2.resize(original_image, (max_label_width, int(h * scale)))

            # Hiển thị ảnh ban đầu
            original_image_pil = Image.fromarray(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
            root.original_photo = ImageTk.PhotoImage(image=original_image_pil)
            original_image_label.config(image=root.original_photo)
            original_image_label.image = root.original_photo

            # Chuyển ảnh sang đen trắng
            gray_image = convert_to_grayscale(original_image)

            # Hiển thị ảnh đen trắng của ảnh gốc
            gray_image_pil = Image.fromarray(gray_image, 'L')
            root.gray_photo = ImageTk.PhotoImage(image=gray_image_pil)
            gray_image_label.config(image=root.gray_photo)
            gray_image_label.image = root.gray_photo

            # Chuẩn hóa ảnh đen trắng
            normalized_gray_image = normalize_image(gray_image)

            # Hiển thị ảnh đen trắng sau khi chuẩn hóa
            normalized_gray_image_pil = Image.fromarray(normalized_gray_image, 'L')
            root.normalized_gray_photo = ImageTk.PhotoImage(image=normalized_gray_image_pil)
            normalized_gray_image_label.config(image=root.normalized_gray_photo)
            normalized_gray_image_label.image = root.normalized_gray_photo

            # Chuẩn hóa ảnh gốc
            normalized_original_image = normalize_image(original_image)

            # Hiển thị ảnh gốc sau khi chuẩn hóa
            normalized_original_image_pil = Image.fromarray(cv2.cvtColor(normalized_original_image, cv2.COLOR_BGR2RGB))
            root.normalized_original_photo = ImageTk.PhotoImage(image=normalized_original_image_pil)
            normalized_original_image_label.config(image=root.normalized_original_photo)
            normalized_original_image_label.image = root.normalized_original_photo
        else:
            print("Không thể đọc ảnh từ đường dẫn được chỉ định.")

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Chuẩn hóa ảnh")

# Tạo nút mở tệp
open_button = ttk.Button(root, text="Mở ảnh", command=open_image)
open_button.pack()

# Tạo Label để hiển thị ảnh ban đầu
original_image_label = ttk.Label(root)
original_image_label.pack()

# Tạo Label để hiển thị ảnh gốc sau khi chuẩn hóa
normalized_original_image_label = ttk.Label(root)
normalized_original_image_label.pack()

# Tạo Label để hiển thị ảnh đen trắng của ảnh gốc
gray_image_label = ttk.Label(root)
gray_image_label.pack()

# Tạo Label để hiển thị ảnh chuẩn hóa ảnh đen trắng của ảnh gốc
normalized_gray_image_label = ttk.Label(root)
normalized_gray_image_label.pack()

root.mainloop()
