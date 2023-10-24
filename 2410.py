import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Khởi tạo biến toàn cục để lưu trữ tọa độ của vùng chọn
start_x, start_y, end_x, end_y = -1, -1, -1, -1
is_drawing = False
selected_region = None
img = None  # Thêm biến để lưu trữ ảnh mở lên
smoothing_factor = 0.5  # Giá trị mặc định cho thanh trượt

def select_region(event, x, y, flags, param):
    global start_x, start_y, end_x, end_y, is_drawing, img, selected_region

    if event == cv2.EVENT_LBUTTONDOWN:
        start_x, start_y = x, y
        is_drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if is_drawing:
            end_x, end_y = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        is_drawing = False
        end_x, end_y = x, y

        # Vẽ hình chữ nhật để xác định vùng đã chọn
        cv2.rectangle(img, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

        # Lưu vùng đã chọn
        selected_region = img[start_y:end_y, start_x:end_x]

def open_image():
    global img, selected_region
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tif")])
    if file_path:
        img = cv2.imread(file_path)
        if img is not None:
            cv2.namedWindow('Portrait')
            cv2.setMouseCallback('Portrait', select_region)
            selected_region = None
            cv2.imshow('Portrait', img)

def update_smoothing_factor(*args):
    global smoothing_factor
    smoothing_factor = smoothing_slider.get()
    on_ok_button_click()  # Gọi lại hàm xử lý khi giá trị thanh trượt thay đổi

def on_ok_button_click():
    global img, selected_region, smoothing_factor
    if selected_region is not None and selected_region.shape[0] > 0 and selected_region.shape[1] > 0:
        # Áp dụng bộ lọc trung bình với độ mịn từ thanh trượt
        kernel_size = int(smoothing_factor * 10) + 1
        kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size ** 2)
        smoothed_region = cv2.filter2D(selected_region, -1, kernel)
        img[start_y:end_y, start_x:end_x] = smoothed_region

        # Hiển thị cả ảnh gốc và phần đã làm mịn
        cv2.imshow('Portrait with Smoothing', img)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Image Smoothing")

# Tạo nút "Open Image"
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

# Tạo thanh trượt cho độ mịn
smoothing_slider = ttk.Scale(root, from_=0, to=1, orient="horizontal", length=200, command=update_smoothing_factor)
smoothing_slider.set(smoothing_factor)
smoothing_slider.pack()

# Tạo nút "OK"
ok_button = tk.Button(root, text="Làm Mịn", command=on_ok_button_click)
ok_button.pack()

root.mainloop()
