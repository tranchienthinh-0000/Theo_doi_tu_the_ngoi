HƯỚNG DẪN CÀI ĐẶT VÀ SỬ DỤNG HỆ THỐNG THEO DÕI TƯ THẾ NGỒI
I. Giới thiệu
Hệ thống theo dõi tư thế ngồi sử dụng webcam USB và công nghệ xử lý hình ảnh Mediapipe để phát hiện và đánh giá tư thế ngồi đúng/sai theo thời gian thực. Hệ thống hiển thị các góc cơ thể (cổ-vai, lưng-đùi, đầu gối) và phát cảnh báo bằng âm thanh khi tư thế sai. Tài liệu này hướng dẫn chi tiết cách cài đặt các thành phần cần thiết và sử dụng hệ thống.
________________________________________
II. Các thành phần cần chuẩn bị
1. Phần cứng
•	Máy tính: 
o	Cấu hình tối thiểu: CPU i3, RAM 4GB, ổ cứng trống 10GB.
o	Hệ điều hành: Windows 10 hoặc cao hơn (có thể dùng macOS/Linux nhưng cần điều chỉnh mã).
•	Camera: Webcam USB (bất kỳ loại nào hỗ trợ kết nối qua USB, ví dụ: Logitech, webcam tích hợp laptop). 
o	Kết nối qua USB.
•	Loa: Để phát âm thanh cảnh báo (thường có sẵn trên máy tính).
2. Phần mềm và thư viện
•	Python: Phiên bản 3.7 hoặc cao hơn.
•	Thư viện Python: 
o	opencv-python: Xử lý hình ảnh và video.
o	mediapipe: Phát hiện điểm mốc cơ thể.
o	numpy: Tính toán số học.
o	pillow: Vẽ văn bản tiếng Việt.
o	pygame: Phát âm thanh cảnh báo.
•	File âm thanh: 
o	tu_the_dung.mp3: Thông báo tư thế đúng.
o	tu_the_sai.mp3: Thông báo tư thế sai.
•	Font chữ: arial.ttf (để hiển thị tiếng Việt có dấu).
________________________________________
III. Hướng dẫn cài đặt
1. Cài đặt Python
•	Tải Python từ trang chính thức: python.org.
•	Chọn phiên bản mới nhất (ví dụ: 3.11), cài đặt và thêm Python vào PATH khi được hỏi.
•	Kiểm tra cài đặt: Mở Command Prompt (CMD) và gõ: 
text
RéduireEnvelopperCopier
python --version
Nếu hiển thị phiên bản, cài đặt thành công.
2. Cài đặt các thư viện
•	Mở CMD và chạy lần lượt các lệnh sau: 
text
RéduireEnvelopperCopier
pip install opencv-python
pip install mediapipe
pip install numpy
pip install pillow
pip install pygame
•	Nếu gặp lỗi, thử nâng cấp pip: 
text
RéduireEnvelopperCopier
pip install --upgrade pip
3. Chuẩn bị webcam USB
•	Cắm webcam USB vào cổng USB của máy tính.
•	Mở ứng dụng "Camera" trên Windows để kiểm tra xem webcam có hoạt động không. Nếu không, cài đặt driver từ nhà sản xuất (nếu cần).
4. Chuẩn bị file âm thanh và font
•	Tạo thư mục, ví dụ: D:\IOT_BTL\theo_doi_tu_the\.
•	Đặt hai file âm thanh tu_the_dung.mp3 và tu_the_sai.mp3 vào thư mục này.
•	Đảm bảo file arial.ttf có sẵn trong hệ thống (thường nằm ở C:\Windows\Fonts\). Nếu không, tải từ internet và đặt cùng thư mục với mã code.
5. Tải và chỉnh sửa mã nguồn
•	Sao chép mã code từ tài liệu nhóm (đính kèm) và lưu thành file pose_detection.py.
•	Kiểm tra đường dẫn file âm thanh trong mã: 
python
RéduireEnvelopperCopier
CORRECT_SOUND = r"D:\IOT_BTL\theo_doi_tu_the\tu_the_dung.mp3"
INCORRECT_SOUND = r"D:\IOT_BTL\theo_doi_tu_the\tu_the_sai.mp3"
Điều chỉnh nếu thư mục của bạn khác.
•	Nếu webcam USB không phải camera mặc định, thay đổi chỉ số trong: 
python
RéduireEnvelopperCopier
cap = cv2.VideoCapture(0)  # Thử 1, 2 nếu không hoạt động
________________________________________
IV. Cách sử dụng
1. Khởi động hệ thống
•	Mở CMD, di chuyển đến thư mục chứa file pose_detection.py: 
text
RéduireEnvelopperCopier
cd D:\IOT_BTL\theo_doi_tu_the
•	Chạy mã: 
text
RéduireEnvelopperCopier
python pose_detection.py
2. Quan sát và sử dụng
•	Cửa sổ "Pose Detection" sẽ hiện lên, hiển thị hình ảnh từ webcam USB.
•	Ngồi trước webcam sao cho toàn bộ cơ thể (từ đầu đến chân) nằm trong khung hình.
•	Hệ thống sẽ: 
o	Hiển thị các góc: "Góc Cổ - Vai", "Góc Lưng - Đùi", "Góc Đầu gối".
o	Thông báo "Tư thế ngồi đúng" (màu xanh) nếu các góc nằm trong ngưỡng cho phép, kèm âm thanh tích cực.
o	Thông báo "Tư thế ngồi sai" (màu đỏ) nếu tư thế sai, kèm âm thanh cảnh báo.
•	Để dừng chương trình, nhấn phím "q" trên bàn phím.
3. Lưu ý khi sử dụng
•	Đảm bảo ánh sáng tốt để webcam nhận diện chính xác.
•	Ngồi cách webcam khoảng 1-2 mét để toàn thân được ghi lại.
•	Nếu âm thanh không phát, kiểm tra loa và đường dẫn file.
V. Xử lý sự cố
•	Webcam không hoạt động: 
o	Kiểm tra kết nối USB, đảm bảo webcam được cắm chắc chắn.
o	Thử đổi chỉ số camera trong mã (0, 1, 2) tại dòng: 
python
RéduireEnvelopperCopier
cap = cv2.VideoCapture(0)
o	Mở ứng dụng "Camera" trên Windows để kiểm tra webcam có được nhận diện không.
•	Lỗi thư viện: 
o	Nếu gặp thông báo thiếu thư viện, cài lại bằng lệnh: 
text
RéduireEnvelopperCopier
pip install <tên_thư_viện>
Ví dụ: pip install opencv-python.
o	Đảm bảo kết nối internet ổn định khi cài đặt.
•	Hình ảnh nhỏ: 
o	Tăng kích thước FRAME_SIZE trong mã, ví dụ từ (1280, 720) lên (1920, 1080): 
python
RéduireEnvelopperCopier
FRAME_SIZE = (1920, 1080)
o	Điều chỉnh kích thước cửa sổ hiển thị: 
python
RéduireEnvelopperCopier
cv2.resizeWindow('Pose Detection', 1920, 1080)
o	Lưu ý: Tăng kích thước có thể làm chậm chương trình nếu máy tính yếu.
•	Không có âm thanh: 
o	Kiểm tra đường dẫn file .mp3 trong mã có đúng không.
o	Đảm bảo loa máy tính bật và không bị mute.
o	Thử chạy file âm thanh bằng trình phát media để kiểm tra.
________________________________________
VI. Kết luận
Hệ thống theo dõi tư thế ngồi sử dụng webcam USB là một giải pháp đơn giản nhưng hiệu quả để cải thiện tư thế ngồi, giảm nguy cơ đau lưng và cổ do ngồi sai cách. Với các bước cài đặt và sử dụng trên, các bạn có thể dễ dàng triển khai hệ thống trên máy tính cá nhân.
Đây cũng là nền tảng để phát triển thêm các tính năng nâng cao như:
•	Tích hợp với ứng dụng di động để gửi thông báo qua điện thoại.
•	Sử dụng nhiều webcam để quan sát từ nhiều góc độ.
•	Lưu dữ liệu tư thế để phân tích thói quen ngồi lâu dài.
Các bạn khóa dưới có thể tham khảo tài liệu này để chạy thử hệ thống và cải tiến theo ý tưởng của mình. Nếu gặp khó khăn, đừng ngần ngại hỏi lại các anh chị khóa trên hoặc tìm hiểu thêm tài liệu về OpenCV và Mediapipe. Chúc các bạn thành công trong việc học tập và phát triển dự án!

