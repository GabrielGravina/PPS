from abc import ABC, abstractmethod

class Report(ABC):
    def generate(self):
        pass

class HTMLReport(Report):
    def generate(self):
        print("Generating HTML Report")

class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report")

class SimpleReport(Report):
    def generate(self):
        print("Generating Simple Report")

class FullReport(Report):
    def generate(self):
        print("Generating Full Report")

class ReportFactory(ABC):
    def create_report(self):
        pass

class HTMLReportFactory(ReportFactory):
    def create_report(self):
        return HTMLReport()

class PDFReportFactory(ReportFactory):
    def create_report(self):
        return PDFReport()

class SimpleReportFactory(ReportFactory):
    def create_report(self):
        return SimpleReport()

class FullReportFactory(ReportFactory):
    def create_report(self):
        return FullReport()

def generate_report(factory) -> None:
    report = factory.create_report()
    report.generate()

if __name__ == "__main__":
    html_report_factory = HTMLReportFactory()
    pdf_report_factory = PDFReportFactory()
    simple_report_factory = SimpleReportFactory()
    full_report_factory = FullReportFactory()

    generate_report(html_report_factory)
    generate_report(pdf_report_factory)
    generate_report(simple_report_factory)
    generate_report(full_report_factory)