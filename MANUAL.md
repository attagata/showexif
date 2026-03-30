# ShowExif - Complete Instruction Manual

## Table of Contents

1. [Introduction](#1-introduction)
2. [System Requirements](#2-system-requirements)
3. [Installation](#3-installation)
   - [3.1 Installing Python](#31-installing-python)
   - [3.2 Installing ExifTool](#32-installing-exiftool)
   - [3.3 Installing ShowExif](#33-installing-showexif)
   - [3.4 Installing the Python Dependency (PyExifTool)](#34-installing-the-python-dependency-pyexiftool)
4. [Usage](#4-usage)
   - [4.1 Basic Command](#41-basic-command)
   - [4.2 Command-Line Arguments](#42-command-line-arguments)
   - [4.3 Examples](#43-examples)
5. [Understanding the Output](#5-understanding-the-output)
   - [5.1 Output Structure](#51-output-structure)
   - [5.2 Metadata Categories](#52-metadata-categories)
   - [5.3 GPS and Google Maps Link](#53-gps-and-google-maps-link)
6. [Supported File Formats](#6-supported-file-formats)
7. [Troubleshooting](#7-troubleshooting)
8. [Frequently Asked Questions (FAQ)](#8-frequently-asked-questions-faq)
9. [Contributing](#9-contributing)
10. [License](#10-license)
11. [Version History](#11-version-history)

---

## 1. Introduction

**ShowExif** is a command-line Python tool that extracts and displays Exif (Exchangeable Image File Format) metadata from image and video files. It leverages the powerful [ExifTool](https://exiftool.org/) engine under the hood via the [PyExifTool](https://pypi.org/project/PyExifTool/) Python library.

### What is EXIF data?

EXIF data is metadata embedded in image and video files by cameras, smartphones, and other recording devices. This metadata can include:

- **Camera settings**: shutter speed, aperture, ISO, focal length
- **Device information**: camera make and model, software version
- **Date and time**: when the photo or video was taken
- **GPS coordinates**: the geographic location where the media was captured
- **File properties**: file size, resolution, format, MIME type

ShowExif reads all of this metadata and presents it in a clear, organized format. When GPS coordinates are available, it also generates a direct Google Maps link so you can view the exact location where the media was captured.

---

## 2. System Requirements

| Requirement | Minimum Version | Notes |
|---|---|---|
| **Python** | 3.6 or higher | Required to run the script |
| **ExifTool** | Any recent version | System-level tool for metadata extraction |
| **PyExifTool** | Any recent version | Python wrapper for ExifTool |
| **Operating System** | Linux, macOS, or Windows | Cross-platform support |

### Checking Your Python Version

Open a terminal and run:

```bash
python3 --version
```

You should see output like `Python 3.x.x`. If Python is not installed or the version is below 3.6, see [Section 3.1](#31-installing-python).

### Checking if ExifTool is Installed

```bash
exiftool -ver
```

If this command outputs a version number (e.g., `12.60`), ExifTool is installed. Otherwise, see [Section 3.2](#32-installing-exiftool).

---

## 3. Installation

### 3.1 Installing Python

#### Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### Linux (Fedora/RHEL)

```bash
sudo dnf install python3 python3-pip
```

#### macOS

Python 3 can be installed via [Homebrew](https://brew.sh/):

```bash
brew install python
```

Alternatively, download the installer from [python.org](https://www.python.org/downloads/).

#### Windows

Download and install Python from [python.org](https://www.python.org/downloads/). During installation, make sure to check **"Add Python to PATH"**.

---

### 3.2 Installing ExifTool

ExifTool is a platform-independent command-line application for reading, writing, and editing metadata. ShowExif requires it to be installed on your system.

#### Linux (Debian/Ubuntu)

```bash
sudo apt-get install libimage-exiftool-perl
```

#### Linux (Fedora/RHEL)

```bash
sudo dnf install perl-Image-ExifTool
```

#### Linux (Arch)

```bash
sudo pacman -S perl-image-exiftool
```

#### macOS (via Homebrew)

```bash
brew install exiftool
```

#### Windows

1. Download ExifTool from [https://exiftool.org/](https://exiftool.org/).
2. Extract the downloaded archive.
3. Rename `exiftool(-k).exe` to `exiftool.exe`.
4. Move `exiftool.exe` to a directory in your system PATH (e.g., `C:\Windows`), or add its location to the PATH environment variable.

#### Verify Installation

After installation, verify that ExifTool is accessible:

```bash
exiftool -ver
```

---

### 3.3 Installing ShowExif

Clone the repository from GitHub:

```bash
git clone https://github.com/attagata/showexif.git
cd showexif
```

Alternatively, you can download the source code as a ZIP file from the [GitHub releases page](https://github.com/attagata/showexif/releases) and extract it.

---

### 3.4 Installing the Python Dependency (PyExifTool)

ShowExif uses the `PyExifTool` library to interface with ExifTool from Python. Install it with pip:

```bash
pip install PyExifTool
```

Or, if the repository includes a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

> **Note**: Depending on your system, you may need to use `pip3` instead of `pip`.

---

## 4. Usage

### 4.1 Basic Command

Run ShowExif by providing the path to an image or video file using the `--image_path` argument:

```bash
python3 showexif.py --image_path <file_path>
```

Replace `<file_path>` with the absolute or relative path to the file you want to inspect.

---

### 4.2 Command-Line Arguments

| Argument | Required | Description |
|---|---|---|
| `--image_path` | Yes | The path to the image or video file to analyze |
| `-h`, `--help` | No | Show the help message and exit |

#### Viewing Help

To see all available options:

```bash
python3 showexif.py --help
```

Output:

```
usage: showexif.py [-h] --image_path IMAGE_PATH

Exibir informacoes EXIF de uma imagem.

options:
  -h, --help            show this help message and exit
  --image_path IMAGE_PATH
                        Caminho para o arquivo de imagem
```

> **Note**: The help text is displayed in Portuguese, as the tool's user-facing messages are localized to Brazilian Portuguese.

---

### 4.3 Examples

#### Analyzing a JPEG Image

```bash
python3 showexif.py --image_path /home/user/photos/vacation.jpg
```

#### Analyzing a MOV Video

```bash
python3 showexif.py --image_path /path/to/20201115_163714_exif.mov
```

#### Analyzing a PNG Image

```bash
python3 showexif.py --image_path ./screenshot.png
```

#### Analyzing an MP4 Video

```bash
python3 showexif.py --image_path /videos/recording.mp4
```

#### Using a Relative Path

```bash
python3 showexif.py --image_path ../images/photo.jpg
```

---

## 5. Understanding the Output

### 5.1 Output Structure

When ShowExif successfully extracts metadata, the output begins with the header:

```
Informacoes EXIF:
```

*(Portuguese for "EXIF Information")*

Each subsequent line displays a metadata tag and its value in the format:

```
[Category]      TagName: Value
```

- **Category** (in square brackets): The metadata group the tag belongs to (e.g., `[ExifTool]`, `[File]`, `[QuickTime]`, `[EXIF]`, `[Composite]`).
- **TagName**: The specific metadata field name.
- **Value**: The value of that field.

#### No EXIF Data

If the file contains no EXIF metadata, the output will be:

```
Nenhuma informacao EXIF encontrada na imagem.
```

*(Portuguese for "No EXIF information found in the image.")*

#### File Not Found

If the specified file does not exist:

```
Erro: Arquivo nao encontrado: '<file_path>'
```

*(Portuguese for "Error: File not found: '<file_path>'")*

---

### 5.2 Metadata Categories

Below is a description of the most common metadata categories and their fields:

#### `[ExifTool]` - ExifTool Information

| Field | Description |
|---|---|
| `ExifToolVersion` | The version of ExifTool used to extract the data |
| `Warning` | Any warnings encountered during extraction |

#### `[File]` - File Properties

| Field | Description |
|---|---|
| `FileName` | The name of the file |
| `Directory` | The directory path where the file is located |
| `FileSize` | The file size in bytes |
| `FileModifyDate` | The date the file was last modified |
| `FileAccessDate` | The date the file was last accessed |
| `FileInodeChangeDate` | The date the file's inode was last changed |
| `FilePermissions` | Unix-style file permissions |
| `FileType` | The file type (e.g., JPEG, MOV, MP4, PNG) |
| `FileTypeExtension` | The file extension |
| `MIMEType` | The MIME type of the file (e.g., `image/jpeg`, `video/quicktime`) |

#### `[EXIF]` - Camera/Image EXIF Data (common in JPEG/TIFF)

| Field | Description |
|---|---|
| `Make` | Camera manufacturer (e.g., Apple, Canon, Nikon) |
| `Model` | Camera model (e.g., iPhone 6, EOS R5) |
| `ExposureTime` | Shutter speed (e.g., `1/125`) |
| `FNumber` | Aperture f-stop value (e.g., `2.2`) |
| `ISO` | ISO sensitivity |
| `FocalLength` | Focal length of the lens in mm |
| `DateTimeOriginal` | Date and time when the image was originally taken |
| `ImageWidth` | Image width in pixels |
| `ImageHeight` | Image height in pixels |
| `Software` | Software used to process the image |
| `Orientation` | Image orientation |

#### `[QuickTime]` - Video Metadata (common in MOV/MP4)

| Field | Description |
|---|---|
| `MajorBrand` | The major brand of the file format |
| `CreateDate` | The creation date of the video |
| `ModifyDate` | The date the video was last modified |
| `Duration` | Duration of the video in seconds |
| `ImageWidth` | Video width in pixels |
| `ImageHeight` | Video height in pixels |
| `CompressorName` | Video codec used (e.g., `H.264`) |
| `BitDepth` | Color bit depth |
| `VideoFrameRate` | Frames per second |
| `AudioFormat` | Audio codec |
| `AudioSampleRate` | Audio sample rate in Hz |
| `AudioChannels` | Number of audio channels |
| `GPSCoordinates` | GPS coordinates (latitude, longitude, altitude) |
| `Make` | Device manufacturer |
| `Model` | Device model |
| `Software` | Firmware or software version |
| `CreationDate` | Creation date with timezone |

#### `[Composite]` - Computed/Derived Fields

| Field | Description |
|---|---|
| `ImageSize` | Image dimensions (width x height) |
| `Megapixels` | Total megapixels |
| `AvgBitrate` | Average bitrate for video files |
| `GPSAltitude` | Altitude above sea level in meters |
| `GPSAltitudeRef` | Altitude reference (`0` = above sea level, `1` = below sea level) |
| `GPSLatitude` | Latitude coordinate (negative = south) |
| `GPSLongitude` | Longitude coordinate (negative = west) |
| `GPSPosition` | Combined latitude and longitude |
| `Rotation` | Image/video rotation in degrees |

---

### 5.3 GPS and Google Maps Link

When the image or video contains GPS coordinates, ShowExif automatically generates a Google Maps link at the end of the output:

```
Localizacao no Google Maps:
https://www.google.com/maps?q=-23.5505,-46.6333
```

*(Portuguese for "Location on Google Maps")*

Click the link (or copy and paste it into a browser) to open Google Maps centered on the exact location where the media was captured.

> **Note**: GPS data is only available if the device that captured the media had location services enabled at the time of capture.

---

## 6. Supported File Formats

ShowExif supports any file format recognized by ExifTool. Below are the most common formats:

### Images

| Format | Extension(s) | Notes |
|---|---|---|
| JPEG | `.jpg`, `.jpeg` | Most common image format with EXIF support |
| PNG | `.png` | Limited EXIF support; may contain text metadata |
| TIFF | `.tif`, `.tiff` | Full EXIF support |
| RAW formats | `.cr2`, `.nef`, `.arw`, `.dng`, `.orf`, `.rw2` | Camera-specific RAW formats |
| HEIF/HEIC | `.heif`, `.heic` | Modern Apple format |
| WebP | `.webp` | Web-optimized format |
| BMP | `.bmp` | Limited metadata |
| GIF | `.gif` | Limited metadata |

### Videos

| Format | Extension(s) | Notes |
|---|---|---|
| QuickTime | `.mov` | Apple video format; rich metadata support |
| MPEG-4 | `.mp4`, `.m4v` | Common video format |
| AVI | `.avi` | Microsoft video format |
| MKV | `.mkv` | Matroska video |
| 3GP | `.3gp` | Mobile video format |

### Audio

| Format | Extension(s) | Notes |
|---|---|---|
| MP3 | `.mp3` | ID3 tag metadata |
| WAV | `.wav` | RIFF metadata |
| FLAC | `.flac` | Vorbis comment metadata |
| M4A | `.m4a` | AAC audio with metadata |

> **Note**: The metadata fields available vary by file format. Image files captured by digital cameras and smartphones typically contain the richest EXIF data.

---

## 7. Troubleshooting

### "Erro: Arquivo nao encontrado"

**Cause**: The file path provided to `--image_path` is incorrect or the file does not exist.

**Solution**:
- Verify the file path is correct and the file exists.
- Use the absolute path to avoid issues with relative paths.
- Check for typos in the file name or path.
- On Linux/macOS, remember that file names are case-sensitive.

```bash
# Verify the file exists
ls -la /path/to/your/file.jpg
```

---

### "exiftool: command not found" or "FileNotFoundError"

**Cause**: ExifTool is not installed or not in the system PATH.

**Solution**:
- Install ExifTool following the instructions in [Section 3.2](#32-installing-exiftool).
- On Windows, ensure `exiftool.exe` is in a directory listed in your PATH environment variable.
- Verify the installation: `exiftool -ver`

---

### "ModuleNotFoundError: No module named 'exiftool'"

**Cause**: The PyExifTool Python library is not installed.

**Solution**:

```bash
pip install PyExifTool
```

Or with `pip3`:

```bash
pip3 install PyExifTool
```

---

### "Nenhuma informacao EXIF encontrada na imagem"

**Cause**: The file does not contain EXIF metadata.

**Possible reasons**:
- The file was created by software that does not embed EXIF data.
- The EXIF data was stripped (some social media platforms and messaging apps remove EXIF data for privacy).
- The file format does not support EXIF metadata.

**Solution**:
- Try analyzing the original, unprocessed file from the camera or device.
- Verify that the file format supports EXIF data (see [Section 6](#6-supported-file-formats)).

---

### No Google Maps Link in the Output

**Cause**: The file does not contain GPS coordinate metadata.

**Possible reasons**:
- Location services were disabled on the device when the media was captured.
- The GPS data was stripped from the file.
- The device does not have GPS hardware.

**Solution**:
- Ensure location services are enabled on the device before capturing media.
- Use the original, unprocessed file.

---

### Permission Denied Errors

**Cause**: The current user does not have read permissions for the file.

**Solution**:

```bash
# Check file permissions
ls -la /path/to/your/file.jpg

# Grant read permission if needed
chmod +r /path/to/your/file.jpg
```

---

### Python Version Error

**Cause**: You are using a Python version older than 3.6.

**Solution**:
- Upgrade Python to version 3.6 or higher (see [Section 3.1](#31-installing-python)).
- Explicitly use `python3` to run the script:

```bash
python3 showexif.py --image_path /path/to/file.jpg
```

---

## 8. Frequently Asked Questions (FAQ)

### Q: Can I analyze multiple files at once?

**A**: The current version of ShowExif processes one file at a time. To analyze multiple files, you can use a shell loop:

```bash
for file in /path/to/photos/*.jpg; do
    echo "=== $file ==="
    python3 showexif.py --image_path "$file"
    echo ""
done
```

---

### Q: Why are the messages in Portuguese?

**A**: ShowExif's user-facing messages are localized to Brazilian Portuguese as of version 1.1.0. The EXIF tag names and values remain in their standard English format.

---

### Q: Can ShowExif modify or remove EXIF data?

**A**: No. ShowExif is a read-only tool. It only displays metadata and does not modify, write, or remove any data from your files.

---

### Q: Does ShowExif work with RAW camera files?

**A**: Yes. ShowExif works with any file format supported by ExifTool, which includes all major RAW formats such as Canon CR2/CR3, Nikon NEF, Sony ARW, Adobe DNG, and many more.

---

### Q: Is my GPS location data safe?

**A**: ShowExif only reads and displays the metadata on your local machine. It does not transmit any data over the network. The Google Maps link is generated locally; no data is sent to Google until you choose to open the link in your browser.

---

### Q: Can I use ShowExif in a script or pipeline?

**A**: Yes. ShowExif outputs plain text to standard output (stdout), so you can pipe its output to other commands:

```bash
# Save output to a file
python3 showexif.py --image_path photo.jpg > metadata.txt

# Search for specific tags
python3 showexif.py --image_path photo.jpg | grep "Model"

# Extract just the Google Maps link
python3 showexif.py --image_path video.mov | grep "google.com/maps"
```

---

### Q: What is the difference between ShowExif and running ExifTool directly?

**A**: ShowExif provides a simplified, user-friendly interface on top of ExifTool. Key differences:
- ShowExif automatically generates a Google Maps link when GPS data is available.
- ShowExif provides user-friendly error messages (in Portuguese).
- ShowExif uses a curated set of ExifTool flags (`-G -s -n`) for clean, structured output.
- ExifTool has hundreds of options for reading, writing, and editing metadata; ShowExif focuses specifically on reading and displaying metadata.

---

## 9. Contributing

Contributions to ShowExif are welcome! Here's how you can contribute:

1. **Fork** the repository on GitHub.
2. **Create a branch** for your feature or bug fix:
   ```bash
   git checkout -b feature/my-new-feature
   ```
3. **Make your changes** and commit them:
   ```bash
   git commit -m "Add my new feature"
   ```
4. **Push** to your fork:
   ```bash
   git push origin feature/my-new-feature
   ```
5. **Open a Pull Request** on the [GitHub repository](https://github.com/attagata/showexif).

### Reporting Issues

If you find a bug or have a feature request, please [open an issue](https://github.com/attagata/showexif/issues) on GitHub.

---

## 10. License

ShowExif is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

This means you are free to:
- **Use** the software for any purpose.
- **Study** how the software works and modify it.
- **Distribute** copies of the software.
- **Improve** the software and release your improvements to the public.

The full license text is available in the [LICENSE](LICENSE) file.

---

## 11. Version History

### v1.1.0

- User-facing messages translated to Brazilian Portuguese.
- Added Google Maps URL generation when GPS location data is present in the EXIF metadata.

### v1.0.0

- Initial release.
- Extract detailed EXIF metadata from image and video files.
- Compatible with a wide range of file formats, including MOV and MP4.
- Provides detailed metadata, including file properties, GPS data, and more.
