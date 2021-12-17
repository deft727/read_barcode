from pyzbar import pyzbar
import cv2


def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    # print(decoded_objects)
    if not decoded_objects:
        print('баркод код не обнаружен')
    for obj in decoded_objects:
        print("Тип:", obj.type)
        print("Данные:", obj.data)
    return image


if __name__ == "__main__":
    im = cv2.imread('02.png')
    decode(im)
