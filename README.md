# 🎓 Hệ Thống Ôn Tập Cấp Tốc MLN111 • Triết Học Mác - Lênin

[![GitHub Pages](https://img.shields.io/badge/Live_Demo-GitHub_Pages-2ea44f?style=for-the-badge&logo=github)](https://ciculs.github.io/MLN111/)
[![Questions](https://img.shields.io/badge/Ng%C3%A2n_h%C3%A0ng-598_C%C3%A2u_chu%E1%BA%A9n-blue?style=for-the-badge)](https://ciculs.github.io/MLN111/)
[![Offline First](https://img.shields.io/badge/Offline-100%25_No_Server-orange?style=for-the-badge)](https://ciculs.github.io/MLN111/)

> Ứng dụng web ôn tập thông minh, thi thử trắc nghiệm và tra cứu lý thuyết toàn diện cho học phần **Triết học Mác - Lênin (MLN111)** với chuẩn 598 câu hỏi trắc nghiệm chia theo 3 chương.

🌐 **Trải nghiệm trực tiếp trên web:** [https://ciculs.github.io/MLN111/](https://ciculs.github.io/MLN111/)

---

## ✨ Tính Năng Nổi Bật

### 1. 🎯 Chế Độ Luyện Thi Theo Batch (10 câu / Batch)
- **Chia nhỏ kiến thức**: 598 câu được chia thành 60 micro-batches (10 câu/batch) giúp học nhanh, tránh quá tải não bộ.
- **🚀 Nhảy câu linh hoạt**: Nhập số thứ tự câu hỏi bất kỳ (`1 - 598`) hoặc chọn từ menu 60 batches để học ngay từ giữa.
- **Thanh 10 Dots Tracker**: Trực quan hóa trạng thái từng câu (Đang làm, Đúng xanh, Sai đỏ, Đã sửa sai tím).
- **Tự động chuyển câu khi sai**: Thông báo và tự động chuyển câu tiếp theo sau 0.9s (kèm nút *Bỏ qua ngay ⏩*) để giữ nhịp học liền mạch.
- **🔄 Vòng lặp sửa sai (Retry Loop)**: Cuối mỗi batch, hệ thống tự động lọc các câu sai và cho phép làm lại với các đáp án được reset sạch để kích hoạt *active recall* (hồi tưởng chủ động) cho đến khi làm chủ 100%.
- **🏆 Hiệu ứng chúc mừng 10/10**: Pháo hoa giấy toàn màn hình (Canvas Confetti), âm thanh kèn chiến thắng (Web Audio Fanfare) và ghi nhận huy hiệu vàng vào `localStorage`.

### 2. 📝 Thi Thử Cấp Tốc (Exam Simulation)
- Tạo đề thi ngẫu nhiên 40 câu trong 30 phút mô phỏng sát format thi thật.
- Đồng hồ đếm ngược, tự động nộp bài khi hết giờ và chấm điểm chi tiết kèm phân tích tỷ lệ theo từng chương.

### 3. 🃏 3D Flashcards Tương Tác
- Lật thẻ 3D trực quan, ẩn/hiện đáp án, ghi nhớ các cặp khái niệm kinh điển.

### 4. 📚 Sổ Tay Lý Thuyết Chi Tiết (20 Chủ Đề Trọng Tâm)
- Hệ thống hóa toàn bộ kiến thức 3 chương thành 20 chủ đề lý thuyết sâu sắc.
- 44 cặp phản xạ nhanh "Gặp từ khóa này ➡ Chọn ngay đáp án kia".
- 7 bảng so sánh các cặp phạm trù và quy luật dễ nhầm lẫn.
- 15 cạm bẫy phòng thi thường gặp nhất.
- Bộ lọc theo chương và tìm kiếm từ khóa thời gian thực.

### 5. 🔍 Tra Cứu & Đánh Dấu (Bookmark)
- Tra cứu nhanh 598 câu hỏi theo từ khóa trong đề hoặc đáp án.
- Đánh dấu ⭐ câu hỏi quan trọng để luyện tập riêng.
- Lọc danh sách câu hỏi từng làm sai để khắc phục điểm yếu.

---

## ⌨️ Phím Tắt Tiện Dụng

| Phím tắt | Tác vụ |
| :--- | :--- |
| **A / B / C / D** hoặc **1 / 2 / 3 / 4** | Chọn nhanh đáp án tương ứng |
| **Space** hoặc **Alt + →** | Chuyển sang câu tiếp theo |
| **Alt + ←** | Lùi về câu trước đó |
| **Alt + PageDown** / **Alt + PageUp** | Chuyển nhanh giữa các Batch |
| **Enter** | Kích hoạt nhảy câu hoặc tiếp tục sang batch mới trên modal vinh danh |

---

## 🚀 Hướng Dẫn Tự Chạy Offline (Không Cần Internet)

1. Tải file [`index.html`](./index.html) về máy tính hoặc điện thoại.
2. Mở trực tiếp bằng bất kỳ trình duyệt nào (Chrome, Edge, Safari, Firefox).
3. Toàn bộ âm thanh, câu hỏi và dữ liệu đều chạy 100% offline không cần kết nối mạng hay cài đặt thêm phần mềm nào khác.

---

## 📁 Cấu Trúc Dự Án

```
├── index.html                                  # Ứng dụng web chạy chính (dành cho GitHub Pages)
├── MLN111_On_Tap_Thong_Minh.html               # Bản sao ứng dụng web offline
├── MLN111_Tong_Hop_Kien_Thuc_On_Thi_Nhanh.md   # Sổ tay tổng hợp kiến thức ôn thi đầy đủ
├── MLN111_598_Cau_Hoi_Va_Dap_An.json           # Dữ liệu 598 câu hỏi chuẩn dạng JSON
└── MLN111_598_Cau_Hoi_Va_Dap_An.md             # Toàn văn 598 câu hỏi & đáp án dạng Markdown
```

---

*Chúc các bạn ôn tập tốt và đạt kết quả cao nhất trong kỳ thi Triết học Mác - Lênin!* 🎓
