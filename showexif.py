import os
import argparse
import exiftool

def print_exif_info(image_path):
    if not os.path.exists(image_path):
        print("Error: File not found.")
        return

    with exiftool.ExifTool() as et:
        output = et.execute("-G", "-s", "-n", image_path)
    
    if output:
        print("EXIF information:")
        for line in output.splitlines():
            tag, value = line.split(":", 1)
            print(f"{tag.strip()}: {value.strip()}")
    else:
        print("No EXIF information found in the image.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Display EXIF information for an image.')
    parser.add_argument('--image_path', required=True, help='Path to the image file')
    args = parser.parse_args()

    image_path = args.image_path
    print_exif_info(image_path)
