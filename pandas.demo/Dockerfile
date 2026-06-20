FROM python:slim

WORKDIR /app

COPY requirment.txt .

RUN pip install -r requirment.txt

RUN pip install pandas

COPY pandas-demo.py .

CMD ["python", "pandas-demo.py"]