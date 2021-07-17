import re
import pdfplumber
import scrubadub


class Redactor:
    def __init__(self, path):
        self.path = path

    # static methods work independent of class object
    @staticmethod
    def get_sensitive_data(lines):

        """ Function to get all the lines """

        # email regex
        EMAIL_REG = r"([\w\.\d]+\@[\w\d]+\.[\w\d]+)"
        for line in lines:

            # matching the regex to each line
            if re.search(EMAIL_REG, line, re.IGNORECASE):
                search = re.search(EMAIL_REG, line, re.IGNORECASE)

                # yields creates a generator
                # generator is used to return
                # values in between function iterations
                yield search.group(1)

    def redaction(self):

        """ main redactor code """
        with pdfplumber.open(self.path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                print(text)
                print("\n\n")
                print(scrubadub.clean(text, replace_with='identifier'))
                print("\n\n\n")
                print(page.extract_words())
                # extract_words
                # draw_rect



if __name__ == "__main__":
    # replace it with name of the pdf file
    path = 'example1.pdf'
    redactor = Redactor(path)
    redactor.redaction()