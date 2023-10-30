FROM node:16 AS build
WORKDIR /app
ENV VUE_APP_SERVER http://170.64.132.129/api/
RUN apt-get update && apt-get install git
RUN git clone -b hao/bugfix/deployment https://hche8093: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@github.sydney.edu.au/hche8093/CS74-1-2023S1.git
RUN cd /app/CS74-1-2023S1/frontend && npm install --legacy-peer-deps && npm run build

FROM nikolaik/python-nodejs:python3.8-nodejs16

ENV EMAIL_BACKEND=django_smtp_ssl.SSLEmailBackend \
    EMAIL_HOST=smtp.qiye.aliyun.com \
    EMAIL_PORT=465 \
    EMAIL_HOST_USER=cs63-1@mineserver.top \
    EMAIL_HOST_PASSWORD=CS63-1-mail \
    EMAIL_USE_TLS=True \
    DEFAULT_FROM_EMAIL=cs63-1@mineserver.top \
    SITE_ID=1 \
    ACCOUNT_EMAIL_VERIFICATION=mandatory \
    ACCOUNT_EMAIL_REQUIRED=True \
    PYTHONUNBUFFERED=1 

RUN apt-get update && apt-get install git libpq-dev nginx vim net-tools -y
COPY --from=build /app/CS74-1-2023S1 /home/CS74-1-2023S1

ADD run.sh /home/CS74-1-2023S1/
ADD nginx.conf /etc/nginx/sites-available/default
#ADD settings.py /home/CS06-1/backend/django_core/settings.py
RUN pip3 install -r /home/CS74-1-2023S1/backend/requirements.txt
WORKDIR /home/CS74-1-2023S1
RUN chmod 777 /home/CS74-1-2023S1/backend/static/upload -R

CMD ["bash","run.sh"]