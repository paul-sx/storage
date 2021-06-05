FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY Docker/entrypoint.sh ./
RUN mkdir -p project/static
VOLUME ["/usr/src/app/project", "/usr/src/app/project/static"]

ENV DJANGO_DEBUG_FALSE True
ENV DJANGO_SITENAME localhost
ENV DJANGO_SECRET_KEY definitely-change-me

EXPOSE 8080

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
CMD ["gunicorn", "-b", "0.0.0.0:8080", "storage.wsgi:application"]