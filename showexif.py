import os
import argparse
import exiftool

def print_exif_info(image_path):
    if not os.path.exists(image_path):
        print(f"Erro: Arquivo não encontrado: '{image_path}'")
        return

    with exiftool.ExifTool() as et:
        output = et.execute("-G", "-s", "-n", image_path)
        # Get GPS coordinates specifically
        gps_data = et.execute("-n", "-Composite:GPSLatitude", "-Composite:GPSLongitude", image_path)
    
    if output:
        print("Informações EXIF:")
        for line in output.splitlines():
            tag, value = line.split(":", 1)
            print(f"{tag.strip()}: {value.strip()}")
        
        # Extract GPS coordinates if available
        if gps_data:
            try:
                gps_lines = gps_data.splitlines()
                if len(gps_lines) == 2:  # Make sure we have both latitude and longitude
                    lat = float(gps_lines[0].split(": ")[1])
                    lon = float(gps_lines[1].split(": ")[1])
                    maps_link = f"https://www.google.com/maps?q={lat},{lon}"
                    print("\nLocalização no Google Maps:")
                    print(maps_link)
            except (ValueError, IndexError):
                pass  # Skip if GPS data is not in expected format
    else:
        print("Nenhuma informação EXIF encontrada na imagem.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Exibir informações EXIF de uma imagem.')
    parser.add_argument('--image_path', required=True, help='Caminho para o arquivo de imagem')
    args = parser.parse_args()

    image_path = args.image_path
    print_exif_info(image_path)
