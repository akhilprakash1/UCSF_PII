FROM python:3

WORKDIR .

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["/python3", "Redactor.py", "example1.pdf"]
CMD ["/python3", "Redactor.py", "example2.pdf"]