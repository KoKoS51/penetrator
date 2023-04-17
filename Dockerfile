FROM python:3.7-stretch

ENV TZ='Europe/Moscow'

COPY requirements.txt requirements.txt

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc telnet tcpdump tcpflow mc nano vim && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org cryptography && \
    pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org --upgrade pip && \
    pip3 install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org -r requirements.txt && \
    apt-get purge -y --auto-remove gcc

COPY bot2.py /bot2.py
COPY settings.ini /settings.ini

ENTRYPOINT ["python", "bot2.py"]