---
title: Gradio ML Skeleton
emoji: 💀
colorFrom: red
colorTo: pink
sdk: gradio
sdk_version: 3.8.2
app_file: app.py
pinned: false
---

# Gradio Model Server Skeleton

This repository contains a Gradio skeleton application which can be used to rapid prototype a demonstration app for your next machine learning/deep learning model.

To experiment and get a feeling on how to use this skeleton, a sample YOLOv5 object detection model is included in this proejct. Follow the installation and setup instructions to run the deep learning application.

## Pre-requisite & Setup

Ensure to have a Python environment before setting up, preferably Python 3.8+.

```sh
apt-get update
apt-get install ffmpeg libsm6 libxext6  -y
```

```sh
pip install -r requirements.txt
```

```sh
# for dev env, hot-reloading is enabled
gradio app.py

# for testing/UAT/prod env, ensure port number is cleared
python app.py --host 0.0.0.0 --port 7860
```

## Docker alternative

Alternatively, you can use docker to containerize the Gradio application.

```sh
# REQUIRED
export docker_repo_name=gradio-ml-skeleton
export docker_tag=dev_latest

# build an image from Dockerfile
sh build_docker.sh
```

```sh
# creates a container layer over the image
sh launch_docker.sh
```

## Application Preview

<img src="assets/Web%20capture_2-12-2022_17491_tyh71-miniature-memory.jpeg" alt="Preview">
