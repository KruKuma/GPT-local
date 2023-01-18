FROM python:3.8-slim-buster

ENV MODEL_ENGINE "text-davinci-002"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY gpt3_script.py /app/

CMD ["python", "/app/gpt3_script.py"]
