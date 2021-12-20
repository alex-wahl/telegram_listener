FROM python:3.9

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/
COPY . /usr/src/app/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "main.py"]
CMD ["${i} ${s} ${b} ${l} ${g} ${client_api_id} ${client_api_hash} ${bot_token} ${listening_group} ${target_group}"]