
# Framework_structure.md

Tài liệu này liệt kê rõ ràng, dễ đọc các thành phần chính trong repo ViT-CoMer, giúp người phân tích nhanh chóng nắm bắt cấu trúc, mục đích và mối liên hệ giữa các file/thư mục.

## 1. detection/

- **configs/**: Chứa các file cấu hình cho mô hình detection/instance segmentation.
	- `_base_/`:
		- `datasets/`: Định nghĩa dataset (ví dụ: coco_detection.py, coco_instance.py).
		- `models/`: Định nghĩa kiến trúc cơ bản (ví dụ: mask_rcnn_r50_fpn.py).
		- `schedules/`: Lịch huấn luyện (schedule_1x.py, schedule_2x.py).
		- `default_runtime.py`: Cấu hình runtime mặc định.
	- `mask_rcnn/`, `dinov2/`, ...: Các file cấu hình cụ thể cho từng mô hình (ví dụ: mask_rcnn_dinov2_comer_base_fpn_1x_coco.py).
	- **Liên hệ:** Các file này được import vào script train/test để build mô hình, dataset, optimizer.

- **mmcv_custom/**: Module mở rộng cho MMCV.
	- Ví dụ: checkpoint.py, my_checkpoint.py (lưu/tải checkpoint), customized_text.py (xử lý text), layer_decay_optimizer_constructor.py (tối ưu hóa), uniperceiver_converter.py (chuyển đổi mô hình).
	- **Liên hệ:** Được import trong file cấu hình hoặc script chính để thay thế/tăng cường chức năng MMCV mặc định.

- **mmdet_custom/**: Module mở rộng cho MMDetection.
	- `models/`: Custom backbone, head, neck (ví dụ: backbones/comer_modules.py, roi_heads/custom_roi_head.py).
	- `ops/`: Các phép toán đặc biệt (ví dụ: attention), có thể có file C++/CUDA, make.sh để build.
	- **Liên hệ:** Được sử dụng trong file cấu hình để build mô hình với các thành phần custom.

- **ops/**: Chứa các phép toán đặc biệt, có thể cần build thêm (ví dụ: Multi-Scale Deformable Attention, make.sh).
	- **Liên hệ:** Được gọi trong các module custom hoặc trực tiếp trong mô hình.

- **train.py**: Script huấn luyện mô hình (đọc config, build mô hình, dataset, optimizer, logger, checkpoint, gọi train_detector).

- **test.py**: Script đánh giá mô hình (đọc config, load checkpoint, build mô hình, dataset test, chạy single/multi_gpu_test).

- **visualization.py**: Script trực quan hóa kết quả (vẽ bounding box, mask lên ảnh).

- **dist_train.sh, dist_test.sh, train.sh, test.sh**: Script shell hỗ trợ chạy train/test nhanh, phân tán hoặc trên nhiều GPU.

- **README.md**: Hướng dẫn sử dụng detection: cài đặt, chuẩn bị dữ liệu, train/test, giải thích các file cấu hình, ví dụ lệnh chạy.

---

## 2. segmentation/

- **configs/**: Cấu hình cho segmentation.
	- `ade20k/`, `coco_stuff164k/`: Các file cấu hình cho từng dataset (ví dụ: upernet_vit-b16_512x512_160k_ade20k.py).
	- `_base_/`: Cấu hình cơ sở cho dataset, model, schedule, runtime.
	- **Liên hệ:** Được import vào các script train/test segmentation.

- **mmcv_custom/**, **mmseg_custom/**: Module mở rộng cho segmentation.
	- core/, datasets/, models/: Custom dataset, loss, head, backbone cho segmentation.
	- **Liên hệ:** Được sử dụng trong file cấu hình segmentation để build các thành phần custom.

- **train.py, test.py**: Script huấn luyện, đánh giá segmentation (đọc config, build mô hình, dataset, optimizer, logger, checkpoint, gọi train/test).

- **image_demo.py, video_demo.py**: Demo kết quả segmentation trên ảnh/video thực tế (đọc checkpoint đã huấn luyện, chạy inference trên ảnh/video).

- **dist_train.sh, dist_test.sh, train.sh, test.sh, slurm_train.sh, slurm_test.sh**: Script shell hỗ trợ chạy nhanh, phân tán hoặc trên hệ thống SLURM.

- **README.md**: Hướng dẫn sử dụng segmentation: cài đặt, chuẩn bị dữ liệu, train/test, giải thích các file cấu hình, ví dụ lệnh chạy.

---

## 3. README.md

- **detection/README.md**: Hướng dẫn sử dụng, cài đặt, mô tả pipeline detection, các lưu ý khi huấn luyện/đánh giá, ví dụ: cách chuẩn bị dữ liệu COCO, lệnh train/test mẫu, giải thích các file cấu hình detection.

- **segmentation/README.md**: Hướng dẫn sử dụng, cài đặt, mô tả pipeline segmentation, các lưu ý khi huấn luyện/đánh giá, ví dụ: cách chuẩn bị dữ liệu ADE20K, lệnh train/test mẫu, giải thích các file cấu hình segmentation.

- **README.md (root)**: Tổng quan dự án, hướng dẫn cài đặt, sử dụng, các thông tin chung, ví dụ: giới thiệu mục tiêu dự án, các tính năng nổi bật, hướng dẫn cài đặt nhanh, các repo liên quan.

---

## 4. File ở root

- **check_params.py**: Script kiểm tra số lượng tham số của mô hình (đọc file config, build mô hình, in số lượng tham số tổng, backbone, neck, head).

- **Framework_structure.md**: Tài liệu mô tả cấu trúc framework (file này).

- **LICENSE**: Bản quyền dự án, quy định về việc sử dụng, phân phối mã nguồn.

- **Xia_ViT-CoMer_Feature_fusion_for_Dense_Prediction_CVPR_2024_paper.pdf**: Bản PDF bài báo liên quan, trình bày chi tiết về phương pháp và kết quả nghiên cứu.

---

## 5. Mối liên hệ tổng thể

- File cấu hình là trung tâm, quyết định mọi thành phần sẽ được build và sử dụng trong pipeline.
- Các module custom (mmcv_custom, mmdet_custom, mmseg_custom) giúp mở rộng, tùy biến framework gốc (MMDetection/MMCV/MMsegmentation) để phù hợp với ý tưởng mới của nhóm tác giả.
- Script shell giúp tự động hóa, đơn giản hóa việc chạy lệnh phức tạp, đặc biệt khi huấn luyện phân tán hoặc trên nhiều GPU.
- Các script Python (train.py, test.py, ...) là nơi thực thi chính, phối hợp đọc config, build mô hình, huấn luyện, đánh giá, lưu checkpoint, log kết quả.
- Các file README.md cung cấp hướng dẫn chi tiết, giúp người dùng mới dễ dàng tiếp cận và sử dụng repo.
- Các file PDF, LICENSE cung cấp thông tin pháp lý và học thuật liên quan.