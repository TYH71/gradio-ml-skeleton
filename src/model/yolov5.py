'''
module to load yolov5* model from the ultralytics/yolov5 repo
'''
import torch
from src.core.logger import logger


def load_model(model_repo: str = "ultralytics/yolov5", model_name: str = "yolov5s6"):
    """
    It loads the YOLOv5s model from the PyTorch Hub
    :return: A model
    """
    try:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        _model = torch.hub.load(model_repo, model_name, device=device)
        _model_agnostic = True  # NMS class-agnostic
        _model.amp = True  # enable Automatic Mixed Precision (NMS) for inference
        return _model
    except Exception as e:
        logger.debug("Exception Caught: {}".format(e))
    finally:
        logger.info(f"[{model_repo}] {model_name} loaded with AMP [Device: {device}]")

model = load_model()
