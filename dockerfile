FROM python:3.6.8-slim-stretch

#RUN  apt update -y && \
#     apt install gcc -y && \
RUN ln -sf /usr/share/zoneinfo/Asia/ShangHai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

COPY . /app
WORKDIR /app

RUN pip install  --no-cache-dir -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

#CMD ["python", "run.py", "runserver"]
#CMD ["python", "run.py", "runserver"]
