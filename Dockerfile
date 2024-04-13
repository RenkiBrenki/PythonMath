FROM python:3.9
LABEL authors="renki"
ADD . /code
WORKDIR .
RUN pip install pytest
CMD ["python3", "main.py"]
