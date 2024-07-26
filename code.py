import qrcode
from svglib.svglib import svg2rlg
from PIL import Image, ImageDraw

# Cargar el SVG del logo y convertirlo a un objeto Drawing
svg_file = "logo-sena.svg"  # Ajusta el nombre y la ubicación de tu archivo SVG
drawing = svg2rlg(svg_file)

# Obtener el tamaño del SVG y convertirlo a enteros
svg_width = int(drawing.width)
svg_height = int(drawing.height)

# Crear una imagen de Pillow (RGBA) para el SVG
svg_img = Image.new('RGBA', (svg_width, svg_height), (0, 0, 0, 0))

# Crear un objeto ImageDraw para dibujar en svg_img
draw = ImageDraw.Draw(svg_img)

# Dibujar el SVG en la imagen de Pillow utilizando ImageDraw
drawing.draw(svg_img)

# Datos para el código QR
data = "https://raw.githubusercontent.com/JuanPabloLeonF/pdf-informacion/main/requisitos-certificados.pdf"

# Configuración del código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Generar la imagen del código QR (blanco sobre negro)
img = qr.make_image(fill_color="black", back_color="white")

# Obtener el tamaño del código QR
img_width, img_height = img.size

# Calcular el tamaño y posición del logo (ajustado más pequeño)
logo_size = (img_width // 6, img_height // 6)  # Tamaño del logo más pequeño
logo_position = ((img_width - logo_size[0]) // 2, (img_height - logo_size[1]) // 2)  # Centrado

# Redimensionar el SVG según el tamaño calculado
svg_img_resized = svg_img.resize(logo_size)

# Superponer el SVG en el código QR
img.paste(svg_img_resized, logo_position, svg_img_resized)

# Guardar el código QR con el SVG superpuesto
img.save("codigoQr_con_logo.svg")

# Mostrar la imagen (opcional)
img.show()
