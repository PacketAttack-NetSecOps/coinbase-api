FROM python:3.12.8


COPY /opt/docker/secrets/cb-api.json ./


RUN git clone https://github.com/PacketAttack-NetSecOps/coinbase-api.git && \
    pip install --no-cache-dir -r /coinbase-api/requirements.txt && \
    python3 /coinbase-api/cb-buy-btc_4-percent_drop_D.py


CMD ["/bin/sh"]