import fitz  # PyMuPDF
import os
from typing import List, Dict

class PDFParser:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path
        self.parsed_documents = {}

    def parse_pdf(self, file_path: str) -> Dict[int, str]:
        """
        Parse a single PDF file and return its content as a dictionary.
        
        :param file_path: Path to the PDF file
        :return: Dictionary with page numbers as keys and page content as values
        """
        document = fitz.open(file_path)
        content = {}
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            content[page_num] = page.get_text()
        document.close()
        return content

    def parse_pdfs_in_folder(self) -> None:
        """
        Parse all PDF files in the specified folder.
        """
        for filename in os.listdir(self.folder_path):
            if filename.lower().endswith('.pdf'):
                file_path = os.path.join(self.folder_path, filename)
                self.parsed_documents[filename] = self.parse_pdf(file_path)

    def display_parsed_content(self) -> None:
        """
        Display the content of all parsed documents.
        """
        for file_name, content in self.parsed_documents.items():
            print(f"\n{'='*50}")
            print(f"Content of {file_name}:")
            print(f"{'='*50}")
            for page_num, page_content in content.items():
                print(f"\nPage {page_num + 1}:")
                print(f"{'-'*20}")
                print(page_content[:500] + "..." if len(page_content) > 500 else page_content)

def main():
    user_documents_folder = "user_documents"
    parser = PDFParser(user_documents_folder)
    
    parser.parse_pdfs_in_folder()
    parser.display_parsed_content()

if __name__ == "__main__":
    main()