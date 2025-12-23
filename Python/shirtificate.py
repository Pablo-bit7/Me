#!/usr/bin/env python3
"""
Program prompts for a name and outputs a PDF of a shirt with text
overlaid on it, as well as a heading. 
"""
from fpdf import FPDF


class PDF():
    """Generate the CS50 shirt certificate PDF for a given name"""


    def __init__(self, name):
        """
        Build the PDF page with heading, shirt image, and overlaid name text
        """
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", style="B", size=50)
        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(r=255, g=255, b=255)
        self._pdf.text(x=38, y=140, text=f"{name} took CS50")


    def save(self, file_name):
        """Write the generated PDF to disk"""
        self._pdf.output(file_name)


if __name__ == "__main__":
    name = input("Name: ").strip()
    pdf = PDF(name)
    pdf.save("shirtificate.pdf")
