# Vipsy

Extract pages from PDF files and convert them to PNG format.

Uses Python bindings for `libvips` via the `pyvips` package.

## How to use

```bash
docker run -v $(pwd):/app vipsy input.pdf --output-dir output --dpi 300
```
