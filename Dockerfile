FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r setup.txt
CMD ["python", "main.py"]