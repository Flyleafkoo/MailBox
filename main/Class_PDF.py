import fitz
from config import signature1, signature2, signature3, signature4, signature5


class PDF:
    signature_1 = signature1
    signature_2 = signature2
    signature_3 = signature3
    signature_4 = signature4
    signature_5 = signature5
    number = 1

    def __init__(self, file):
        self.file = file

    def signing_1(self):
        input_file = self.file
        output_file = 'input' + str(self.number)
        signature_file = self.signature_1

        image_rectangle = fitz.Rect(0, 0, 50, 50)
        file_handle = fitz.open(input_file)
        first_page = file_handle[0]

        first_page.insertImage(image_rectangle, filename=signature_file)
        file_handle.save(output_file)

        self.number += 1
