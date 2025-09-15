# Framework Structure

Nhóm tác giả tổ chức chương trình cho các tác vụ deep learning (object detection, instance segmentation) dựa trên framework [MMDetection](https://github.com/open-mmlab/mmdetection). Dưới đây là cách hệ thống hóa và tổ chức code của họ:

---

### 1. **Cấu trúc thư mục**

- **detection/**: Chứa toàn bộ code liên quan đến object detection/instance segmentation.
  - `configs/`: Các file cấu hình mô hình, dataset, pipeline huấn luyện/đánh giá.
  - `mmcv_custom/`, `mmdet_custom/`: Các module mở rộng hoặc custom dựa trên MMDetection.
  - `ops/`: Các phép toán đặc biệt (ví dụ: Multi-Scale Deformable Attention).
  - `train.py`, `test.py`, `visualization.py`: Script huấn luyện, đánh giá, trực quan hóa kết quả.
  - `README.md`: Hướng dẫn sử dụng, kết quả, cách chạy.

---

### 2. **Luồng chạy chính**

- **Huấn luyện**:  
  - Sử dụng script `train.py`  
  - Đọc cấu hình từ file `.py` trong `configs/` (ví dụ: `mask_rcnn_dinov2_comer_base_fpn_1x_coco.py`)
  - Xây dựng mô hình qua `build_detector`, khởi tạo dataset, seed, logger, v.v.
  - Gọi hàm `train_detector` để bắt đầu huấn luyện.

- **Đánh giá**:  
  - Sử dụng script `test.py`  
  - Đọc cấu hình, load checkpoint, xây dựng mô hình và dataset.
  - Chạy đánh giá qua `single_gpu_test` hoặc `multi_gpu_test`.

- **Trực quan hóa**:  
  - Sử dụng `visualization.py` để trực quan hóa kết quả trên ảnh.

---

### 3. **Cấu hình mô hình**

- Các file cấu hình trong `configs/` định nghĩa:
  - Kiến trúc mô hình (backbone, neck, head, ...).
  - Dataset, pipeline tiền xử lý.
  - Tham số huấn luyện, optimizer, scheduler, v.v.
- Có thể kế thừa, ghi đè các cấu hình cơ sở (`_base_`).

---

### 4. **Mở rộng/custom**

- Các module custom được đặt trong `mmcv_custom/`, `mmdet_custom/` để mở rộng hoặc thay đổi hành vi mặc định của MMDetection.
- Các phép toán đặc biệt (ví dụ: Multi-Scale Deformable Attention) được cài đặt trong `ops/` và build qua script `make.sh`.

---

### 5. **Cách sử dụng**

- Cài đặt môi trường theo hướng dẫn trong `README.md`.
- Chạy huấn luyện/đánh giá bằng các script shell (`train.sh`, `test.sh`) hoặc trực tiếp qua Python.

---

**Tóm lại:**  
Nhóm tác giả tận dụng tối đa cấu trúc module hóa, cấu hình động và khả năng mở rộng của MMDetection để tổ chức code, giúp dễ dàng thêm mới mô hình, thay đổi pipeline, và tái sử dụng các thành phần cho các tác vụ deep learning khác nhau.