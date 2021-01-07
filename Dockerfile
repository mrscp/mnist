FROM tensorflow/tensorflow:2.2.2-gpu-py3

WORKDIR /mnist

#RUN apt-get update && apt-get install -y python3 python3-pip sudo python-scipy
RUN pip3 install --upgrade pip

COPY requirements.txt /mnist/
RUN pip3 install -r requirements.txt

COPY . /mnist/
