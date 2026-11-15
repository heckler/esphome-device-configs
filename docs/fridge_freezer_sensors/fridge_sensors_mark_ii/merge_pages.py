#
# Merge the two PCB pages (front and back) into a single sheet
# CAH 2026-11-15
#


import fitz  # PyMuPDF

MM = 72 / 25.4

# Actual PCB dimensions
BOARD_W_MM = 80
BOARD_H_MM = 50

# Extra margin around the PCB
MARGIN_MM = 2

# Input files
FILES = ["PCB_layout_front.pdf", "PCB_layout_back.pdf"]

# A4 portrait output
A4_W = 210 * MM
A4_H = 297 * MM

# Crop dimensions, including margin
CROP_W = (BOARD_W_MM + 2 * MARGIN_MM) * MM
CROP_H = (BOARD_H_MM + 2 * MARGIN_MM) * MM

# After 90-degree rotation
OUT_W = CROP_W
OUT_H = CROP_H

output = fitz.open()
target = output.new_page(width=A4_W, height=A4_H)

# Center one board in each half of the page
x = (A4_W - OUT_W) / 2
y_top = (A4_H / 2 - OUT_H) / 2
y_bottom = A4_H / 2 + y_top

positions = [y_top, y_bottom]

for filename, y in zip(FILES, positions):
    src = fitz.open(filename)
    page = src[0]

    # Crop around the center of the original A4 landscape page
    r = page.rect
    cx = r.width / 2
    cy = r.height / 2

    clip = fitz.Rect(
        cx - CROP_W / 2,
        cy - CROP_H / 2,
        cx + CROP_W / 2,
        cy + CROP_H / 2
    )

    # Destination rectangle
    dest = fitz.Rect(x, y, x + OUT_W, y + OUT_H)

    # Rotate clockwise, preserving original physical dimensions
    target.show_pdf_page(
        dest,
        src,
        0,
        clip=clip,
        rotate=180,
        keep_proportion=True
    )

    src.close()

output.save("PCB_layout_combined.pdf")
output.close()

print("Created combined.pdf")

