FROM tiangolo/uwsgi-nginx:python2.7


RUN pip install flask
RUN pip install pymongo

ENV NGINX_MAX_UPLOAD 0

ENV UWSGI_INI /app/uwsgi.ini

COPY ./app /app
WORKDIR /app

ENV PYTHONPATH=/app

COPY start.sh /start.sh
RUN chmod +x /start.sh

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/start.sh"]
