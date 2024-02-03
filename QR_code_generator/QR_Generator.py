import qrcode

class MyQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size = size, border = padding)

    def create_qr(self, file_name: str, fg: str, bg: str):
        user_input: str = input("Enter Text")

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(file_color = fg, background_color= bg)
            qr_image.save(file_name)

            print(f"Successfuly created! ({file_name})")
        except Exception as err:
            print(f"Error {err}")



def main():
    myqr = MyQR(size=30, padding=2)
    myqr.create_qr("smaple.png",fg="black", bg="white",)

if __name__ == "__main__":
    main()
