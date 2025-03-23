THEO DÕI TƯ THẾ NGỒI
![image](https://github.com/user-attachments/assets/27128c24-0c6b-4593-97c4-9a77c11d9643)
Giới thiệu
Hệ thống theo dõi tư thế ngồi là một ứng dụng sử dụng Python và MediaPipe để phát hiện tư thế ngồi của người dùng. Dựa trên góc đo của các bộ phận cơ thể, hệ thống có thể cảnh báo khi phát hiện tư thế sai bằng âm thanh.

🏗️ HỆ THỐNG

📂 Cấu trúc dự án

📦 Project
├── 📂 Model # Chứa mô hình MediaPipe
├── 📂 Sounds # Chứa âm thanh cảnh báo
│ ├── tu_the_dung.mp3 # Âm thanh tư thế đúng
│ ├── tu_the_sai.mp3 # Âm thanh tư thế sai
├── 📂 utils # Chứa các hàm hỗ trợ
├── main.py # Chương trình chính

🛠️ CÔNG NGHỆ SỬ DỤNG

📡 Phần cứng

Camera (Elgato Cam hoặc webcam khác)

🖥️ Phần mềm

Python

OpenCV

MediaPipe

NumPy

Pygame

🛠️ Yêu cầu hệ thống

🔌 Phần cứng

Máy tính có cài đặt Python

Camera hỗ trợ video streaming

💻 Phần mềm

Python 3+

Các thư viện cần thiết:

pip install opencv-python mediapipe numpy pygame pillow

🚀 Hướng dẫn cài đặt và chạy

1️⃣ Chuẩn bị phần cứng

Kết nối camera với máy tính

Kiểm tra nhận diện camera bằng lệnh:

python -c "import cv2; print(cv2.VideoCapture(0).isOpened())"

2️⃣ Chạy chương trình

Mở terminal và chạy lệnh:

python main.py

Ứng dụng sẽ hiển thị hình ảnh từ camera và kiểm tra tư thế ngồi.

📖 Hướng dẫn sử dụng

1️⃣ Người dùng ngồi trước camera.
2️⃣ Hệ thống sẽ phân tích tư thế dựa trên các góc đo.
3️⃣ Nếu tư thế đúng, hệ thống sẽ hiển thị thông báo xanh.
4️⃣ Nếu tư thế sai, hệ thống sẽ phát cảnh báo bằng âm thanh và hiển thị thông báo đỏ.
5️⃣ Nhấn phím 'q' để thoát ứng dụng.

⚙️ Cấu hình & Ghi chú

Camera mặc định sử dụng chỉ số 0, nếu không nhận diện được có thể thử 1 hoặc 2.

Độ trễ xử lý video có thể được điều chỉnh bằng cách thay đổi TARGET_FPS trong code.

Để tắt âm thanh cảnh báo, có thể xóa hoặc thay đổi đường dẫn file âm thanh trong main.py.

© 2025 NHÓM 1, CNTT16-03, TRƯỜNG ĐẠI HỌC ĐẠI NAM

