import unittest
from finance_app.pdf_parser.parser import PDFParser

class TestPDFParser(unittest.TestCase):
    def setUp(self):
        self.parser = PDFParser("test_documents")

    def test_parse_pdf(self):
        # Add test cases here
        pass

if __name__ == '__main__':
    unittest.main()
