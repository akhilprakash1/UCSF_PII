FROM python:3

WORKDIR .

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN python3 -m textblob.download_corpora
CMD ["brew install ImageMagick@6"]
RUN echo '<policy domain="coder" rights="read | write" pattern="PDF" />' >> /etc/ImageMagick-6/policy.xml
CMD ["python3", "redactor.py", "example1.pdf"]
CMD ["python3", "redactor.py", "example2.pdf"]