FROM python:3.7

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN mkdir /code
COPY requirements.txt /code

WORKDIR /code
RUN pip install -r requirements.txt

VOLUME /code
ADD . /code

RUN mkdir logs
CMD ["python"]