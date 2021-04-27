FROM ubuntu

RUN apt-get update \
    && apt-get install -y python3 \
    python3-pip 

RUN pip3 install \
    discord \
    python-dotenv

COPY bot.py /opt/bot.py
COPY .env /opt/.env

ENTRYPOINT python3 /opt/bot.py