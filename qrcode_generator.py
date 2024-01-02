import qrcode
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from qrcode.main import QRCode
import argparse


def parse_arguments() -> argparse.Namespace:
    """
    parse_arguments Parsing arguments into flags

    Returns:
            argparse.Namespace: contains all the flags
    """
    parser = argparse.ArgumentParser(
        prog="QR code generator",
        description='Generates code, example use: # python qrcode_generator.py --content "Participant-01"',
    )
    parser.add_argument(
        "--content",
        help="Enter the information to be encoded into the QR code.",
    )
    parser.add_argument(
        "--path",
        default="qrcode_img/",
        help="Specify where to save the generated QR code.",
    )
    flags = parser.parse_args()
    return flags


def gen_qrcode(qrcode_content: str, save_path: str = "qrcode_img/") -> str:
    """
    gen_qrcode Generates QR code based on the content provided, with annotations of the content0


    Args:
            qrcode_content (str): The content to be embedded in the QR Code
            save_path (str, optional): specify where QR Code is saved. Defaults to "qrcode_img/".

    Returns:
            str: passing out the input
    """
    qr = qrcode.QRCode(box_size=15)
    qr.add_data(qrcode_content)
    img = qr.make_image()
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype("open-sans/OpenSans-Regular.ttf", 35)
    font = ImageFont.truetype(
        "atkinson-hyperlegible/Atkinson-Hyperlegible-Regular-102.otf", 40
    )
    draw.text((12, 0), qrcode_content, font=font)
    img.save(f"{save_path+qrcode_content}.png")
    return qrcode_content


if __name__ == "__main__":
    # python qrcode_generator.py --content "Participant-01"
    flags = parse_arguments()
    _ = gen_qrcode(qrcode_content=flags.content, save_path=flags.path)
    print("done!")
