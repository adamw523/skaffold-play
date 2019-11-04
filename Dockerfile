FROM python:3

ADD requirements.txt /
RUN pip install -r requirements.txt

ADD start.sh .
RUN chmod +x start.sh
ADD app /app

CMD ["sh", "start.sh"]