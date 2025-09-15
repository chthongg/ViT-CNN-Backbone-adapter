import sys
sys.path.insert(0, 'detection')

from mmcv import Config
from mmdet.models import build_detector

def main():
    config_path = 'detection/configs/mask_rcnn/dinov2/mask_rcnn_dinov2_comer_base_fpn_1x_coco.py'
    cfg = Config.fromfile(config_path)
    cfg.model.backbone.pretrained = None
    model = build_detector(cfg.model)
    total = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f'Total params: {total}')
    print(f'Trainable params: {trainable}')
    print(f'Backbone params: {sum(p.numel() for p in model.backbone.parameters())}')
    if hasattr(model, "neck"):
        print(f'Neck params: {sum(p.numel() for p in model.neck.parameters())}')
    if hasattr(model, "rpn_head"):
        print(f'RPN head params: {sum(p.numel() for p in model.rpn_head.parameters())}')
    if hasattr(model, "roi_head"):
        print(f'ROI head params: {sum(p.numel() for p in model.roi_head.parameters())}')

if __name__ == "__main__":
    main()