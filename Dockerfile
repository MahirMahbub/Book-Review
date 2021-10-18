FROM python:3.9.0
ENV PYTHONUNBUFFERED 1
RUN mkdir /srv/book_review_backend
WORKDIR /srv/book_review_backend
COPY requirements.txt /srv/book_review_backend/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /srv/book_review_backend/
