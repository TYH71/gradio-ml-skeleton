FROM python:3.10.8-slim

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y \
    ffmpeg libsm6 libxext6
RUN apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

ENV LC_ALL C.UTF-8 
ENV LANG C.UTF-8

# container listens to port 7860
EXPOSE 7860

# Start Gradio application
CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "7860"]