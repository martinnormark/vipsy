import pyvips
import argparse
import os


def main():
    print(pyvips.__version__)
    print(pyvips.API_mode)

    parser = argparse.ArgumentParser(description="Convert PDF to images")
    parser.add_argument("input_pdf", help="Input PDF file")
    parser.add_argument("--output-dir", default=".", help="Output directory")
    parser.add_argument("--dpi", type=int, default=300, help="DPI for conversion")

    args = parser.parse_args()

    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    # Load the PDF
    pdf = pyvips.Image.new_from_file(args.input_pdf, dpi=args.dpi)

    # Get number of pages
    n_pages = pdf.get("n-pages")

    # Extract images from each page
    for i in range(n_pages):
        page = pyvips.Image.new_from_file(args.input_pdf, dpi=args.dpi, page=i)
        output_path = os.path.join(args.output_dir, f"page_{i}.png")
        page.write_to_file(output_path)
        print(f"Converted page {i+1}/{n_pages}")


if __name__ == "__main__":
    main()
