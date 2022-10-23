import PyPDF2
from config import signature1, signature2, signature3, signature4, signature5


class PDF:

    def __init__(self, file):
        self.file = file
        self.number = 0

    def signing_file_1(self):
        input_file = self.file
        output_file = 'in' + '' + str(self.number) + '.pdf'

        with open(input_file, 'rb') as filehandle_input:
            pdf = PyPDF2.PdfFileReader(filehandle_input)
            first_page = pdf.getPage(0)

            with open(signature1, 'rb') as filehandle_watermark:
                watermark = PyPDF2.PdfFileReader(filehandle_watermark)
                first_page_watermark = watermark.getPage(0)

                first_page.mergePage(first_page_watermark)

                pdf_writer = PyPDF2.PdfFileWriter()
                pdf_writer.addPage(first_page)

                with open(output_file, "wb"):
                    pdf_writer.write(output_file)


