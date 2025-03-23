<h1 align="center">ỨNG DỤNG THEO DÕI TƯ THẾ NGỒI</h1> <div align="center"> <p align="center"> <img src="images/logoDaiNam.png" alt="DaiNam University Logo" width="200"/> <img src="images/LogoAIoTLab.png" alt="AIoTLab Logo" width="170"/> </p>




</div> <h2 align="center">Hệ thống theo dõi tư thế ngồi sử dụng thị giác máy tính</h2> <p align="left"> Hệ thống theo dõi tư thế ngồi là một dự án sử dụng công nghệ thị giác máy tính (OpenCV, MediaPipe) để phát hiện và đánh giá tư thế ngồi của người dùng thông qua webcam (Elgato Cam hoặc webcam thông thường). Dự án phân tích các góc cơ thể (cổ-vai, lưng-đùi, đầu gối) để xác định tư thế ngồi đúng hoặc sai, đồng thời cung cấp phản hồi bằng âm thanh và hiển thị trực quan trên giao diện. </p>
<h1 >GIỚI THIỆU 🌟</h1>
📌 Phát hiện tư thế tự động: Hệ thống sử dụng webcam để theo dõi tư thế ngồi theo thời gian thực.
💡 Phản hồi trực quan: Hiển thị góc độ các khớp cơ thể và trạng thái tư thế (đúng/sai) trên giao diện.
🔊 Thông báo âm thanh: Phát âm thanh thông báo khi tư thế đúng (tu_the_dung.mp3) hoặc sai (tu_the_sai.mp3).
📊 Ứng dụng thực tế: Hỗ trợ cải thiện tư thế ngồi, giảm nguy cơ đau lưng hoặc các vấn đề sức khỏe liên quan.
<h1>🏗️ HỆ THỐNG</h1>
<p align="center"> <img src="images/QuytrinhTuThe.png" alt="System Workflow" width="800"/> </p>
📂 Cấu trúc dự án
📦 Project

├── 📂 theo_doi_tu_the

│   ├── tu_the_dung.mp3  # Âm thanh thông báo tư thế đúng

│   ├── tu_the_sai.mp3   # Âm thanh thông báo tư thế sai

├── posture_tracking.py  # Mã nguồn chính xử lý theo dõi tư thế

🛠️ CÔNG NGHỆ SỬ DỤNG
<div align="center">
📡 Phần cứng
🖥️ Phần mềm






</div>
🛠️ Yêu cầu hệ thống
🔌 Phần cứng
Webcam (Elgato Cam hoặc bất kỳ webcam nào tương thích qua USB).
Máy tính có khả năng xử lý video thời gian thực.
💻 Phần mềm
🐍 Python 3+
Font chữ arial.ttf (có sẵn trong hệ điều hành Windows hoặc tải thêm nếu cần).
📦 Các thư viện Python cần thiết
Cài đặt các thư viện bằng lệnh:

pip install opencv-python mediapipe numpy pillow pygame

🚀 Hướng dẫn cài đặt và chạy
1️⃣ Chuẩn bị phần cứng

Kết nối Elgato Cam (hoặc webcam) qua USB.
Kiểm tra chỉ số thiết bị webcam trong mã nguồn (cap = cv2.VideoCapture(0)). Thay đổi số 0 nếu cần (0, 1, 2...).
2️⃣ Cài đặt phần mềm

Cài đặt Python 3 nếu chưa có.
Cài đặt các thư viện cần thiết bằng lệnh pip ở trên.
3️⃣ Chuẩn bị tệp âm thanh

Đảm bảo các tệp tu_the_dung.mp3 và tu_the_sai.mp3 nằm trong thư mục theo_doi_tu_the.
Cập nhật đường dẫn trong mã nguồn nếu cần (mặc định: D:\IOT_BTL\theo_doi_tu_the\).
4️⃣ Chạy chương trình

Mở terminal và chạy:

python posture_tracking.py

Chương trình sẽ:

Mở cửa sổ hiển thị video từ webcam.
Theo dõi tư thế và hiển thị góc độ các khớp cùng trạng thái tư thế.
Phát âm thanh tương ứng khi tư thế thay đổi.
📖 Hướng dẫn sử dụng
1️⃣ Khởi động hệ thống

Chạy file posture_tracking.py.
Đảm bảo webcam đang hoạt động và người dùng nằm trong khung hình.
2️⃣ Theo dõi tư thế

Hệ thống tự động phát hiện các điểm mốc cơ thể (cổ, vai, hông, đầu gối, mắt cá chân).
Tính toán các góc:
Góc cổ-vai: 115°–140°
Góc lưng-đùi: 100°–125°
Góc đầu gối: 110°–135°
Nếu các góc nằm trong khoảng cho phép → "Tư thế ngồi đúng" (màu xanh).
Nếu ngoài khoảng → "Tư thế ngồi sai" (màu đỏ) + âm thanh cảnh báo.
3️⃣ Tắt chương trình

Nhấn phím q để thoát.
⚙️ Cấu hình & Ghi chú
Chỉ số webcam: Nếu webcam không hoạt động với chỉ số 0, thử thay đổi thành 1, 2, v.v.
Độ trễ âm thanh: Thời gian chờ giữa các cảnh báo âm thanh là 3 giây (có thể điều chỉnh trong ALERT_COOLDOWN).
Kích thước khung hình: Mặc định là 1280x720 (có thể chỉnh trong FRAME_SIZE).
FPS mục tiêu: 15 khung hình/giây (có thể chỉnh trong TARGET_FPS).
📰 Poster
<p align="center"> <img src="images/PosterTuThe.PNG" alt="Project Poster" width="800"/> </p>
🤝 Đóng góp
Dự án được phát triển bởi nhóm sinh viên:

Họ và Tên	Vai trò
[Tên bạn]	Phát triển mã nguồn, kiểm thử, triển khai dự án.
[Tên thành viên 2]	Thiết kế tài liệu, poster, hỗ trợ kiểm thử.
[Tên thành viên 3]	Hỗ trợ phát triển, tài liệu hóa.
[Tên thành viên 4]	Hỗ trợ kiểm thử, trình bày.
© 2025 NHÓM [SỐ NHÓM], CNTT16-03, TRƯỜNG ĐẠI HỌC ĐẠI NAM
