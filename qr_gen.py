import os
from io import BytesIO
import qrcode


class QRCodeGenerator:
    def __init__(
        self,
        data,
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    ):
        self.data = data
        self.version = version
        self.error_correction = error_correction
        self.box_size = box_size
        self.border = border

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=self.version,
            error_correction=self.error_correction,
            box_size=self.box_size,
            border=self.border,
        )

        qr.add_data(self.data)
        image = qr.make_image(fill_color="black", back_color="white")
        return image

    def get_qr_code_bytes(self, image_format="PNG") -> bytes:
        image = self.generate_qr_code()
        byte_stream = BytesIO()
        image.save(byte_stream)
        return byte_stream.getvalue()

    # def save_qr_code(self, file_path="qrcode.png"):
    #     image = self.generate_qr_code()
    #     image.save(file_path)


if __name__ == "__main__":
    qr = QRCodeGenerator("https://www.google.com")
    qr_bytes = qr.get_qr_code_bytes()

    # Save the QR code as a file
    # cur_dir = os.path.dirname(os.path.realpath(__file__))
    # file_path = os.path.join(cur_dir, "qrcode.png")

    # with open(file_path, "wb") as f:
    #     f.write(qr_bytes)
    # qr.save_qr_code(file_path)
