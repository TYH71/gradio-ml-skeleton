'''
YOLOv5 Interface Module
'''
# packages
from typing import Tuple, Optional
import glob
import numpy as np
import torch
import gradio as gr
import pandas as pd
import PIL


# modules
from src.core.logger import logger
from src.core.utils import current_sg_time
from src.model.yolov5 import model


def yolov5_demo_fn(
    image: np.array,
    nms_threshold: Optional[float] = 0.25,
    conf_threshold: Optional[float] = 0.3
) -> Tuple[PIL.Image.Image, pd.DataFrame]:
    """
    It takes an image as input, runs it through a model, and returns the rendered image
    and the bounding box coordinates

    :param image: np.array
    :type image: np.array
    :return: The first return value is a PIL image, the second is a pandas dataframe.
    """
    try:
        logger.info("\nYOLOv5 demo function invoked\ndate/time: %s",
                    current_sg_time())

        # model config
        model.conf = conf_threshold
        model.iou = nms_threshold

        # disables automatic differential gradients during inference
        with torch.inference_mode(True):
            results = model(image)
        return results.render()[0], results.pandas().xyxy[0].round(decimals=2)
    except Exception as e:
        logger.error("Error Caught: %s", e)
    finally:
        logger.info("YOLOv5 demo function complete")

DESCRIPTION = """
You can use YOLOv5 to run object detection on common objects of interests (based on COCO classes). To use it, simply uplaod an image and click submit.
You can also use the confidence threshold slider to set a threshold to filter out low probability predictions 
and Non-Maximum Suppression (NMS) to set a threshold to filter out duplicate predictions.
"""

ARTICLE = """
#### License
YOLOv5 is open-sourced by Ultralytics for open source and academic proejcts under a **GPL 3.0 License**.
"""

examples = [
    ["./examples/ash_ketchum_world_champion_screenshot_3.webp", 0.25, 0.3]
]

yolov5_demo = gr.Interface(
    fn=yolov5_demo_fn,
    inputs=[
        gr.Image(type="pil", label="Input Image"),
        gr.Slider(0, 1, value=0.25,
                  label="Non-Maximum Suppression (NMS) Threshold"),
        gr.Slider(0, 1, value=0.3, label="Confidence Threshold")
    ],
    outputs=[gr.Image(type="numpy", label="Render"),
             gr.Dataframe(label="BBox (COCO), Confidence, Class")],
    title="YOLOv5 Object Detection",
    description=DESCRIPTION,
    article=ARTICLE,
    # examples=examples,
    allow_flagging="never"
)
logger.info("YOLOv5 Interface Built")
