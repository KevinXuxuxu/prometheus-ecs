FROM prom/alertmanager

COPY alertmanager.yml /etc/alertmanager/

ENTRYPOINT sed -i "s=WEBHOOK_URL=${WEBHOOK_URL}=g" /etc/alertmanager/alertmanager.yml && \
    /bin/alertmanager --config.file=/etc/alertmanager/alertmanager.yml --storage.path=/alertmanager
