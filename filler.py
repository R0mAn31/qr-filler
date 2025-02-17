from PIL import Image, ImageDraw
import os

def create_a4_with_qr(qr_code_path, output_path):
    # Constants
    A4_SIZE = (2480, 3508)  # A4 size in pixels at 300 DPI
    QR_SIZE = 550  # Size of each QR code (300x300 pixels)
    MARGIN = 50  # Margin between QR codes
    ROWS = 6
    COLUMNS = 4

    # Open the QR code image
    qr_code = Image.open(qr_code_path).convert("RGBA")
    qr_code = qr_code.resize((QR_SIZE, QR_SIZE))

    # Create an A4 blank canvas
    a4_canvas = Image.new("RGBA", A4_SIZE, "white")
    draw = ImageDraw.Draw(a4_canvas)

    # Calculate initial position to center grid on page
    start_x = (A4_SIZE[0] - (COLUMNS * QR_SIZE + (COLUMNS - 1) * MARGIN)) // 2
    start_y = (A4_SIZE[1] - (ROWS * QR_SIZE + (ROWS - 1) * MARGIN)) // 2

    # Paste QR codes in grid layout
    for row in range(ROWS):
        for col in range(COLUMNS):
            x = start_x + col * (QR_SIZE + MARGIN)
            y = start_y + row * (QR_SIZE + MARGIN)
            a4_canvas.paste(qr_code, (x, y), qr_code)

    # Save the output as PNG
    a4_canvas.save(output_path, "PNG")

# Usage example
qr_code_path = "../qr.jpg"  # Replace with the path to your QR code image
output_path = "output_a4_qr_codes.png"  # Replace with the desired output file path

if os.path.exists(qr_code_path):
    create_a4_with_qr(qr_code_path, output_path)
    print(f"A4 page with QR codes saved at: {output_path}")
else:
    print("QR code image not found. Please check the file path.")
