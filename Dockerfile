FROM python:alpine3.10
WORKDIR /webapp
COPY . /webapp
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python","./launch.py" ]