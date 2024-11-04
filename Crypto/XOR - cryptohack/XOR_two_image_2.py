from PIL import Image

def xor_images(image_path1, image_path2, output_path):
    # Open the two images
    img1 = Image.open(image_path1)
    img2 = Image.open(image_path2)

    # Ensure both images are the same size
    if img1.size != img2.size:
        raise ValueError("Images must be the same size for XOR operation")

    # Create a new image to hold the XOR result
    xor_image = Image.new("RGB", img1.size)

    # Perform XOR operation on each pixel
    for x in range(img1.width):
        for y in range(img1.height):
            # Get the pixel values
            pixel1 = img1.getpixel((x, y))
            pixel2 = img2.getpixel((x, y))
            # XOR each channel (R, G, B)
            xor_pixel = tuple(a ^ b for a, b in zip(pixel1, pixel2))
            xor_image.putpixel((x, y), xor_pixel)

    # Save the resulting image
    xor_image.save(output_path)
    print(f"XOR image saved as: {output_path}")

# Example usage
print("Give the full path of the images like : /home/devil/CTF Istruction Files/CRYPTO/XOR/image_name")
print("For output image in image_name just give a new name for output. It will creat automatically ")
image_path1 = input("Enter the path for the first image: ")
image_path2 = input("Enter the path for the second image: ")
output_path = input("Enter the output path for the XOR image: ")

xor_images(image_path1, image_path2, output_path)
