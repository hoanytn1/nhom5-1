import math
import sympy as sp
from sympy import Point, Triangle
import tkinter as tk
from tkinter import ttk, messagebox

def is_triangle(a, b, c):
    # Tạo các điểm từ các đoạn
    point_a = Point(a[0], a[1])
    point_b = Point(b[0], b[1])
    point_c = Point(c[0], c[1])

    # Tạo tam giác từ các điểm
    triangle = Triangle(point_a, point_b, point_c)

    # Kiểm tra xem tam giác có hợp lệ không
    if triangle.is_real:
        return True
    else:
        return False

def clear_entries():
    entry_Ax.delete(0, tk.END)
    entry_Ay.delete(0, tk.END)
    entry_Bx.delete(0, tk.END)
    entry_By.delete(0, tk.END)
    entry_Cx.delete(0, tk.END)
    entry_Cy.delete(0, tk.END)

def check_triangle():
    try:
        A = (float(entry_Ax.get()), float(entry_Ay.get()))
        B = (float(entry_Bx.get()), float(entry_By.get()))
        C = (float(entry_Cx.get()), float(entry_Cy.get()))
        AB = math.sqrt(((A[0]-B[0])**2)+((A[1]-B[1])**2))
        BC = math.sqrt(((B[0] - C[0]) ** 2) + ((B[1] - C[1]) ** 2))
        AC = math.sqrt(((A[0] - C[0]) ** 2) + ((A[1] - C[1]) ** 2))

        if (AB + BC > AC) and (AB + AC > BC) and (AC + BC > AB):
            messagebox.showinfo("Kết quả", "Ba đoạn tạo thành một tam giác.")
            if (AC*AC==AB*AB+BC*BC)or(BC*BC==AC*AC+AB*AB)or(AB*AB==BC*BC+AC*AC):
                messagebox.showinfo("Kết quả", "Ba đoạn tạo thành tam giác vuông")
                if AB == BC == AC:
                    messagebox.showinfo("Kết quả", "Ba đoạn tạo thành tam giác vuông đều")
                else:
                    messagebox.showinfo("Kết quả", "Ba đoạn tạo thành tam giác vuông cân")
            elif (AB == BC == AC):
                messagebox.showinfo("Kết quả", "Ba đoạn tạo thành tam giác đều")
            elif (AB == BC) or (AB == AC) or (BC == AC):
                messagebox.showinfo("Kết quả", "Ba đoạn tạo thành tam giác cân")
        else:
            messagebox.showerror("Kết quả", "Ba đoạn không tạo thành một tam giác.")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Kiểm tra tam giác")



# Tạo các nhãn và ô nhập liệu cho các điểm A, B, C
label_A = ttk.Label(root, text="Điểm A (Ax, Ay):")
label_A.grid(row=0, column=0, padx=10, pady=(10, 5))
entry_Ax = ttk.Entry(root)
entry_Ax.grid(row=0, column=1, padx=10, pady=(10, 5))
entry_Ay = ttk.Entry(root)
entry_Ay.grid(row=0, column=2, padx=10, pady=(10, 5))

label_B = ttk.Label(root, text="Điểm B (Bx, By):")
label_B.grid(row=1, column=0, padx=10, pady=5)
entry_Bx = ttk.Entry(root)
entry_Bx.grid(row=1, column=1, padx=10, pady=5)
entry_By = ttk.Entry(root)
entry_By.grid(row=1, column=2, padx=10, pady=5)

label_C = ttk.Label(root, text="Điểm C (Cx, Cy):")
label_C.grid(row=2, column=0, padx=10, pady=5)
entry_Cx = ttk.Entry(root)
entry_Cx.grid(row=2, column=1, padx=10, pady=5)
entry_Cy = ttk.Entry(root)
entry_Cy.grid(row=2, column=2, padx=10, pady=5)

# Tạo nút Kiểm Tra và nút Xóa
check_button = ttk.Button(root, text="Kiểm Tra", command=check_triangle, padding=(20, 10))
check_button.grid(row=3, column=0, columnspan=3, pady=10)

clear_button = ttk.Button(root, text="Xóa", command=clear_entries, padding=(20, 10))
clear_button.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
