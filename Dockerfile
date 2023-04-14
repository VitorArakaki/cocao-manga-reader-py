FROM python:3.9

ENV PORT=80

WORKDIR /code

RUN apt-get update && apt-get install curl gnupg -y \
  && curl --location --silent https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
  && apt-get update \
  && apt-get install google-chrome-stable -y --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

ENV CHROME_PATH=/usr/bin/google-chrome

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/

EXPOSE ${PORT}

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:80", "--workers=3", "--worker-class=uvicorn.workers.UvicornWorker", "cocao:app"]