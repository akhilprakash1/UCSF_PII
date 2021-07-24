FROM python:3

WORKDIR .

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN python3 -m textblob.download_corpora
CMD ["brew install ImageMagick@6"]
CMD ["brew install ghostscript@9.22.0"]
RUN ln -s /usr/local/bin/gs /usr/bin/gs
ENV MAGICK_GHOSTSCRIPT_PATH=/usr/local/Cellar/ghostscript/9.22.0/bin:/usr/bin/gs:/usr/local/bin/gs:$MAGICK_GHOSTSCRIPT_PATH
RUN echo '<policy domain="coder" rights="read | write" pattern="PDF" />' >> /etc/ImageMagick-6/policy.xml
RUN apt-get update && apt-get install -y ghostscript-x
CMD ["python3", "redactor.py", "example1.pdf"]
CMD ["python3", "redactor.py", "example2.pdf"]