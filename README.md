# ASCII Art Generator using K-Means Clustering

This project is a modern take on converting images to ASCII art. Instead of using lengthy `if-else` statements to map brightness values to characters, it leverages **K-Means Clustering** to intelligently group pixel brightness into character buckets.

## 🧠 Why K-Means?
Traditional approaches use hardcoded brightness ranges to map pixels to ASCII characters. While that works, it's rigid and often inefficient. With **K-Means**, the algorithm dynamically learns brightness clusters based on the image itself — giving a cleaner, smarter, and more adaptive result.

## 📸 How It Works
1. The image is resized based on a scale factor to reduce processing load.
2. Brightness of each pixel is calculated using the sum of its RGB values.
3. K-Means clustering groups brightness values into `k` clusters (`k` = number of ASCII characters).
4. Cluster centers are sorted and mapped to ASCII characters from darkest to lightest.
5. The ASCII characters are written to a `.txt` file, reconstructing the image in text form.

## 🧾 Requirements
- Python 3
- Pillow
- NumPy
- scikit-learn
- matplotlib (optional for brightness histogram)

Install dependencies:
```bash
pip install pillow numpy scikit-learn matplotlib
```

## 🚀 Usage
```python
ascii_convert(image_path="your_image.jpg", file_type="jpg", output_file="output.txt", scale=3, visualize=True)
```

- `image_path`: Path to the image you want to convert.
- `file_type`: Image file extension (e.g., jpg, png).
- `output_file`: Name of the ASCII output text file.
- `scale`: Downscaling factor for the image.
- `visualize`: (Optional) Show brightness histogram for analysis.

## 🧪 Example
```python
ascii_convert("bill_gates.jpg", "jpg", "bill_gates_ascii.txt", scale=3, visualize=True)
```

## 🖼️ Sample Output
The result is a `.txt` file with characters like `#`, `%`, `*`, and ` ` that visually represent your image.

---

Feel free to explore and modify the character set or clustering method to create your own artistic variations!

Happy Hacking 🎨
