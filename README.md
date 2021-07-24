# UCSF_PII

This is a Python app that draws black boxes around PII. The intput pdf is passed in as a command line argument. The output pdf is written to the local working directory. THe file name has "_redacted" appended to it.
For example, if the input file name is "example1.pdf", then the output file name is "example1_redacted.pdf".

I used pdfplumber to read the pdf. scrubadub is used to detect PII. However, there are a lot of false positives. One improvement could be to find a better library to use.
I used PyPDF2 to mrege multiple pdfs into one pdf. This accounts for the case where the input pdf has multiple pages.

It is hard to write a correct unit test because I am just calling other library functions. Also, no PII detector will have 100% accuracy. In my unit test, I basically tested if the app is idempotent.

To run things locally, you can `pip install --no-cache-dir -r requirements.txt` and then run `python3 redactor.py example1.pdf`.

To run things with docker, `docker build .`. Run `docker image ls` and find the image id of the recently created image. The repository and tag should be `<none>`. `docker tag <imageId> redactor`. `docker run redactor`.

Follow these commands to copy the output from the docker container (example1_redacted.pdf and example2_redacted.pdf) to the Downloads folder on the local file system.

```
docker create -ti --name dummy redactor bash
docker cp dummy:example1_redacted.pdf ~/Downloads/
docker cp dummy:example2_redacted.pdf ~/Downloads/
```
