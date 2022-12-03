'''
module to load yolov5* model from the ultralytics/yolov5 repo
'''
import torch


def load_model():
    """
    It loads the YOLOv5s model from the PyTorch Hub
    :return: A model
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    _model = torch.hub.load("ultralytics/yolov5", "yolov5m6", device=device)
    _model_agnostic = True  # NMS class-agnostic
    _model.amp = True  # enable Automatic Mixed Precision (NMS) for inference
    return _model


model = load_model()
