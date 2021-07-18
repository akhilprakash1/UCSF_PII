import unittest

from diff_pdf_visually import pdfdiff


class Test(unittest.TestCase):

    def test_redaction(self):
        redactor = Redactor('example1.pdf')
        num_pages = redactor.redaction()
        redactor.merge(num_pages)
        redactor = Redactor('example1_redaction.pdf')
        redactor.redaction()
        redactor.merge(num_pages)
        assert pdfdiff("example1_redaction.pdf", "example1_redaction_redaction.pdf")


if __name__ == '__main__':
    unittest.main()