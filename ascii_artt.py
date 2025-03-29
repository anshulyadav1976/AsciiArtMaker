from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt  

def ascii_convert(image_path, file_type, output_file, scale, visualize=True):
    """
    Converts an image to ASCII art using K-Means clustering 
    to map pixel brightness to ASCII characters.
    
    Parameters:
      image_path (str): Path to the input image.
      file_type (str): File extension for saving the resized image.
      output_file (str): Output filename for the ASCII art.
      scale (str or int): Factor to downscale the image.
      visualize (bool): If True, plot a histogram of brightness values.
    """
    scale = int(scale)
    # Open image and resize it
    img = Image.open(image_path)
    w, h = img.size
    new_w, new_h = w // scale, h // scale
    img = img.resize((new_w, new_h))
    img.save(f"resized.{file_type}")
    
    # Reload resized image and get pixel data
    img = Image.open(f"resized.{file_type}")
    w, h = img.size
    pix = img.load()
    
    # Extract brightness (sum of RGB channels) for each pixel into a flat array
    brightness = []
    for y in range(h):
        for x in range(w):
            brightness.append(sum(pix[x, y]))
    brightness = np.array(brightness)
    
    # Optional: visualize the brightness histogram to see the distribution
    if visualize:
        plt.hist(brightness, bins=50, color='gray')
        plt.title("Brightness Histogram")
        plt.xlabel("Brightness")
        plt.ylabel("Frequency")
        plt.show()
    
    # Define your ASCII characters from darkest to lightest
    ascii_chars = ['#', 'X', '%', '*', ' ']
    n_chars = len(ascii_chars)
    
    # Prepare a grid for the ASCII art
    grid = [[" "] * w for _ in range(h)]
    
    # K-Means clustering on brightness values
    brightness_reshaped = brightness.reshape(-1, 1)
    kmeans = KMeans(n_clusters=n_chars, random_state=42).fit(brightness_reshaped)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_.flatten()
    
    # Sort cluster indices based on center brightness (from dark to light)
    sorted_indices = np.argsort(centers)
    
    # Create a mapping: each cluster label gets assigned an ASCII char 
    mapping = {}
    for rank, cluster_index in enumerate(sorted_indices):
        mapping[cluster_index] = ascii_chars[rank]
    
    # Assign ASCII characters to each pixel using the mapping from KMeans labels
    label_index = 0
    for y in range(h):
        for x in range(w):
            grid[y][x] = mapping[labels[label_index]]
            label_index += 1
    
    # Write the ASCII art grid to the output file
    with open(output_file, "w") as f:
        for row in grid:
            f.write("".join(row) + "\n")
    
if __name__ == "__main__":
    # Example usage
    ascii_convert("popeye.jpg", "webp", "popeye.txt", scale="3", visualize=True)
