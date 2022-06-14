FROM python:3.9

RUN pip3 install --upgrade pip; mkdir -p /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "main.py"]