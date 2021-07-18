#!/usr/bin/python

import re
import pdfplumber
import scrubadub
from PyPDF2 import PdfFileMerger
import sys


class Redactor:
    def __init__(self, path):
        self.path = path

    def redaction(self):
        with pdfplumber.open(self.path) as pdf:
            for idx, page in enumerate(pdf.pages):
                text = page.extract_text()
                text_without_pii = scrubadub.clean(text, replace_with='identifier')
                words = page.extract_words()
                img = page.to_image()
                for word in words:
                    if word['text'] not in text_without_pii:
                        # `word` is PII
                        img = img .draw_rect(word, fill='black', stroke='black')
                img.save('redacted_{}.pdf'.format(idx), format="PDF")
        return len(pdf.pages)

    def merge(self, num_pages):
        pdf_merger = PdfFileMerger()
        for i in range(num_pages):
            pdf_merger.append('redacted_{}.pdf'.format(i))
        output_path = self.path.split(".pdf")[0] + "_redacted.pdf"
        with open(output_path, 'wb') as fileobj:
            pdf_merger.write(fileobj)


if __name__ == "__main__":
    # replace it with name of the pdf file
    # path = 'example1.pdf'
    if len(sys.argv) != 2:
        print(
            " ".join(
                [
                    "[USAGE]:",
                    "python",
                    "redactor.py",
                    "<file_name>",
                ]
            )
        )
        sys.exit(1)

    redactor = Redactor(sys.argv[1])
    num_pages = redactor.redaction()
    redactor.merge(num_pages)