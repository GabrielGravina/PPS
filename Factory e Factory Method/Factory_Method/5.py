from abc import ABC

class Report(ABC):
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        print(f"Generating PDF Report: {self.title}\n{self.content}")

class CSVReport(Report):
    def generate(self):
        print(f"Generating CSV Report: {self.title}\n{self.content}")

class HTMLReport(Report):
    def generate(self):
        print(f"Generating HTML Report: {self.title}\n{self.content}")

class ReportFactory(ABC):
    def create_report(self, title, content):
        pass

class PDFReportFactory(ReportFactory):
    def create_report(self, title, content):
        return PDFReport(title, content)

class CSVReportFactory(ReportFactory):
    def create_report(self, title, content):
        return CSVReport(title, content)

class HTMLReportFactory(ReportFactory):
    def create_report(self, title, content):
        return HTMLReport(title, content)

class ReportGenerator:
    def __init__(self, report_factory):
        self.report_factory = report_factory

    def generate_report(self, title, content):
        report = self.report_factory.create_report(title, content)
        report.generate()

if __name__ == "__main__":
    pdf_report_factory = PDFReportFactory()
    csv_report_factory = CSVReportFactory()
    html_report_factory = HTMLReportFactory()

    report_generator_pdf = ReportGenerator(pdf_report_factory)
    report_generator_csv = ReportGenerator(csv_report_factory)
    report_generator_html = ReportGenerator(html_report_factory)

    report_generator_pdf.generate_report("Monthly Report", "Sales data and trends")
    report_generator_csv.generate_report("Quarterly Report", "Financial summary")
    report_generator_html.generate_report("Yearly Report", "Company performance metrics")
