'''
main script for gradio application
'''
import argparse
import gradio as gr
from src.core.logger import logger
from src.interface.yolov5 import yolov5_demo

demo = gr.TabbedInterface(
    [yolov5_demo],
    ["YOLOv5 Demo"]
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="0.0.0.0", type=str)
    parser.add_argument(
        "--port", help="will start gradio app on this port (if available)", default=7860, type=int)
    args_all = parser.parse_args()
    logger.info("Gradio Application live and running !")
    demo.queue().launch(share=False, server_name=args_all.host, server_port=args_all.port)
