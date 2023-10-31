import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('diemPython.csv', index_col=0, header=0)
in_data = np.array(df.iloc[:, :])

tongsv = in_data[:, 1]
print('Tổng số sinh viên đi thi:', np.sum(tongsv))

diemA = in_data[:, 3]
diemBc = in_data[:, 4]

diemA_count = np.sum(diemA >= 8)  # Điểm A: >= 8
diemBc_count = np.sum((diemBc >= 6) & (diemBc < 8))  # Điểm B: 6 <= B < 8
diemC_count = np.sum(diemBc < 6)  # Điểm C: < 6

print('Số sinh viên đạt điểm A:', diemA_count)
print('Số sinh viên đạt điểm B:', diemBc_count)
print('Số sinh viên đạt điểm C:', diemC_count)

total_students = diemA_count + diemBc_count + diemC_count
print('Tổng số sinh viên:', total_students)

plt.bar(['Điểm A', 'Điểm B', 'Điểm C'], [diemA_count, diemBc_count, diemC_count])
plt.xlabel('Phân loại điểm')
plt.ylabel('Số Sinh Viên')
plt.title('Thống kê điểm theo phân loại A, B, C')
plt.show()
