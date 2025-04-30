
#py -m pip install Pillow   (INSTALA ESTA WEA AWEONAO COMO SOY TAN IDIOTA POR LA CTM)
from PIL import Image


ASCII_CHARS = "@%#*+=-:. "


def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)  

    return image.resize((new_width, new_height))

# COMO QUERIAS QUE TUVIESE ESCALA DE GRISES SI NO LO ESCRIBISTE AWEONAO EL PROGRAMA NO ADIVINA
def grayify(image):
    return image.convert("L")


def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join(ASCII_CHARS[min(pixel // 25, len(ASCII_CHARS) - 1)] for pixel in pixels) 
    return ascii_str


def image_to_ascii(path, new_width=100):
    try:
        image = Image.open(path)
    except Exception as e:
        print("No se pudo abrir la imagen:", e)
        return

    image = resize_image(image, new_width)
    gray_image = grayify(image)
    ascii_str = pixels_to_ascii(gray_image)

    pixel_count = len(ascii_str)
    ascii_image = "\n".join(
        ascii_str[i:(i + new_width)] for i in range(0, pixel_count, new_width)
    )

    print(ascii_image)  
    return ascii_image


image_path = "C:/Users/juanj/Downloads/Nico.png"  
ascii_result = image_to_ascii(image_path, new_width=480)


if ascii_result:
    with open("imagen_ascii.txt", "w") as f:
        f.write(ascii_result)