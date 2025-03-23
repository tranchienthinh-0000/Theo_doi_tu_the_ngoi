ỨNG DỤNG THEO DÕI TƯ THẾ NGỒI

  

Giới thiệu

Hệ thống theo dõi tư thế ngồi là một ứng dụng sử dụng Python và MediaPipe để phát hiện tư thế ngồi của người dùng. Dựa trên góc đo của các bộ phận cơ thể, hệ thống có thể cảnh báo khi phát hiện tư thế sai bằng âm thanh.

🏗️ HỆ THỐNG

📂 Cấu trúc dự án

📦 Project  
├── 📂 Model  # Chứa mô hình MediaPipe  
├── 📂 Sounds  # Chứa âm thanh cảnh báo  
│   ├── tu_the_dung.mp3  # Âm thanh tư thế đúng  
│   ├── tu_the_sai.mp3  # Âm thanh tư thế sai  
├── 📂 utils  # Chứa các hàm hỗ trợ  
├── main.py  # Chương trình chính  

🛠️ CÔNG NGHỆ SỬ DỤNG

📡 Phần cứng



🖥️ Phần mềm

    

🛠️ Yêu cầu hệ thống

🔌 Phần cứng

Máy tính có cài đặt Python

Camera hỗ trợ video streaming

💻 Phần mềm

🐍 Python 3+

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

1️⃣ Người dùng ngồi trước camera. 2️⃣ Hệ thống sẽ phân tích tư thế dựa trên các góc đo. 3️⃣ Nếu tư thế đúng, hệ thống sẽ hiển thị thông báo xanh. 4️⃣ Nếu tư thế sai, hệ thống sẽ phát cảnh báo bằng âm thanh và hiển thị thông báo đỏ. 5️⃣ Nhấn phím 'q' để thoát ứng dụng.

⚙️ Cấu hình & Ghi chú

Camera: Mặc định sử dụng chỉ số 0, nếu không nhận diện được có thể thử 1 hoặc 2.

Độ trễ xử lý video: Có thể được điều chỉnh bằng cách thay đổi TARGET_FPS trong code.

Âm thanh cảnh báo: Để tắt âm thanh, có thể xóa hoặc thay đổi đường dẫn file âm thanh trong main.py.

📰 Poster

🤝 Đóng góp

Dự án được phát triển bởi 4 thành viên:

Họ và Tên

Vai trò

Nguyễn Nam Hưng

Phát triển toàn bộ mã nguồn, thiết kế cơ sở dữ liệu, kiểm thử, triển khai dự án và thực hiện video giới thiệu.

Hoàng Mạnh Linh

Biên soạn tài liệu Overleaf, Poster, Powerpoint, thuyết trình, đề xuất cải tiến, và hỗ trợ bài tập lớn.

Đào Đức Mạnh

Thiết kế slide PowerPoint, hỗ trợ bài tập lớn.

Cao Văn Huy

Hỗ trợ bài tập lớn

© 2025 NHÓM 1, CNTT16-03, TRƯỜNG ĐẠI HỌC ĐẠI NAM

