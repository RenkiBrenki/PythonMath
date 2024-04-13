FROM python:3.9
WORKDIR .
RUN pip install pytest
CMD ["python3", "main.py"]
