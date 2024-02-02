from abc import ABC

class Document(ABC):
    def load(self):
        pass

class PDFDocument(Document):
    def load(self):
        print("Carregando documento PDF")

class WordDocument(Document):
    def load(self):
        print("Carregando documento Word")

class HTMLDocument(Document):
    def load(self):
        print("Carregando documento HTML")

class DocumentLoader(ABC):
    @abstractmethod
    def create_document(self):
        pass

class PDFDocumentLoader(DocumentLoader):
    def create_document(self):
        return PDFDocument()

class WordDocumentLoader(DocumentLoader):
    def create_document(self):
        return WordDocument()

class HTMLDocumentLoader(DocumentLoader):
    def create_document(self):
        return HTMLDocument()

class DocumentReader:
    def __init__(self, document_loader):
        self.document = document_loader.create_document()

    def read_document(self):
        self.document.load()

if __name__ == "__main__":
    pdf_loader = PDFDocumentLoader()
    word_loader = WordDocumentLoader()
    html_loader = HTMLDocumentLoader()

    pdf_reader = DocumentReader(pdf_loader)
    word_reader = DocumentReader(word_loader)
    html_reader = DocumentReader(html_loader)

    pdf_reader.read_document()
    word_reader.read_document()
    html_reader.read_document()
