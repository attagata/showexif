
# ShowExif

**ShowExif** is a Python tool to extract and display Exif metadata from image and video files.

## Features

- Extract detailed Exif metadata from image and video files.
- Compatible with a wide range of file formats, including MOV and MP4.
- Provides detailed metadata, including file properties, GPS data, and more.

## Requirements

- Python 3.6 or higher
- [ExifTool](https://exiftool.org/), a dependency for extracting metadata.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/attagata/showexif.git
   cd showexif
   ```

2. **Install Required Python Packages**:
   Ensure you have `pip` installed, then install required dependencies (if any). For example:
   ```bash
   pip install -r requirements.txt
   ```

   *(Add a `requirements.txt` file if your script uses specific Python libraries.)*

3. **Install ExifTool**:
   - For **Linux**:
     ```bash
     sudo apt-get install libimage-exiftool-perl
     ```
   - For **MacOS** (via Homebrew):
     ```bash
     brew install exiftool
     ```
   - For **Windows**:
     Download and install [ExifTool](https://exiftool.org/).

## Usage

### Basic Command
Run the script with the path to your image or video file:
```bash
python3 showexif.py --image_path <file_path>
```

### Example
For example, to view metadata for a file `20201115_163714_exif.mov`:
```bash
python3 showexif.py --image_path /path/to/20201115_163714_exif.mov
```

### Sample Output
```
EXIF information:
[ExifTool]      ExifToolVersion: 12.60
[ExifTool]      Warning: [minor] The ExtractEmbedded option may find more tags in the media data
[File]          FileName: 20201115_163714_exif.mov
[File]          Directory: /Volumes/NTFS05TB/System_Files/_ENT/OK/MOV/202011/20201115
[File]          FileSize: 79828861
[File]          FileModifyDate: 2023:07:27 21:36:03-03:00
[File]          FileAccessDate: 2023:07:29 00:53:37-03:00
[File]          FileInodeChangeDate: 2023:07:27 21:36:10-03:00
[File]          FilePermissions: 100600
[File]          FileType: MOV
[File]          FileTypeExtension: MOV
[File]          MIMEType: video/quicktime
[QuickTime]     MajorBrand: qt
[QuickTime]     MinorVersion: 0.0.0
[QuickTime]     CompatibleBrands: qt
[QuickTime]     MediaDataSize: 79794694
[QuickTime]     MediaDataOffset: 36
[QuickTime]     MovieHeaderVersion: 0
[QuickTime]     CreateDate: 2020:11:15 19:37:14
[QuickTime]     ModifyDate: 2020:11:15 19:38:14
[QuickTime]     TimeScale: 600
[QuickTime]     Duration: 59.7516666666667
[QuickTime]     PreferredRate: 1
[QuickTime]     PreferredVolume: 1
[QuickTime]     PreviewTime: 0
[QuickTime]     PreviewDuration: 0
[QuickTime]     PosterTime: 0
[QuickTime]     SelectionTime: 0
[QuickTime]     SelectionDuration: 0
[QuickTime]     CurrentTime: 0
[QuickTime]     NextTrackID: 5
[QuickTime]     TrackHeaderVersion: 0
[QuickTime]     TrackCreateDate: 2020:11:15 19:37:14
[QuickTime]     TrackModifyDate: 2020:11:15 19:38:14
[QuickTime]     TrackID: 1
[QuickTime]     TrackDuration: 59.7516666666667
[QuickTime]     TrackLayer: 0
[QuickTime]     TrackVolume: 1
[QuickTime]     ImageWidth: 1280
[QuickTime]     ImageHeight: 720
[QuickTime]     CleanApertureDimensions: 1280 720
[QuickTime]     ProductionApertureDimensions: 1280 720
[QuickTime]     EncodedPixelsDimensions: 1280 720
[QuickTime]     GraphicsMode: 64
[QuickTime]     OpColor: 32768 32768 32768
[QuickTime]     CompressorID: avc1
[QuickTime]     SourceImageWidth: 1280
[QuickTime]     SourceImageHeight: 720
[QuickTime]     XResolution: 72
[QuickTime]     YResolution: 72
[QuickTime]     CompressorName: H.264
[QuickTime]     BitDepth: 24
[QuickTime]     VideoFrameRate: 30.0242671055201
[QuickTime]     Balance: 0
[QuickTime]     AudioFormat: mp4a
[QuickTime]     AudioBitsPerSample: 16
[QuickTime]     AudioSampleRate: 44100
[QuickTime]     LayoutFlags: 100
[QuickTime]     AudioChannels: 1
[QuickTime]     PurchaseFileFormat: mp4a
[QuickTime]     MatrixStructure: 1 0 0 0 1 0 0 0 1
[QuickTime]     ContentDescribes: 1
[QuickTime]     MediaHeaderVersion: 0
[QuickTime]     MediaCreateDate: 2020:11:15 19:37:14
[QuickTime]     MediaModifyDate: 2020:11:15 19:38:14
[QuickTime]     MediaTimeScale: 600
[QuickTime]     MediaDuration: 59.7516666666667
[QuickTime]     MediaLanguageCode: und
[QuickTime]     GenMediaVersion: 0
[QuickTime]     GenFlags: 0 0 0
[QuickTime]     GenGraphicsMode: 64
[QuickTime]     GenOpColor: 32768 32768 32768
[QuickTime]     GenBalance: 0
[QuickTime]     HandlerClass: dhlr
[QuickTime]     HandlerVendorID: appl
[QuickTime]     HandlerDescription: Core Media Data Handler
[QuickTime]     MetaFormat: mebx
[QuickTime]     HandlerType: mdta
[QuickTime]     GPSCoordinates: -00.2835 -00.6656 000.651
[QuickTime]     Make: Apple
[QuickTime]     Model: iPhone 6
[QuickTime]     Software: 12.4.8
[QuickTime]     CreationDate: 2020:11:15 16:37:14-03:00
[Composite]     ImageSize: 1280 720
[Composite]     Megapixels: 0.9216
[Composite]     AvgBitrate: 10683510
[Composite]     GPSAltitude: 000.651
[Composite]     GPSAltitudeRef: 0
[Composite]     GPSLatitude: -00.2835
[Composite]     GPSLongitude: -00.6656
[Composite]     Rotation: 90
[Composite]     GPSPosition: -00.2835 -00.6656
```

## Contributing

Feel free to open issues or pull requests to improve the tool. Contributions are welcome!

## License

This project is licensed under the [GPL-3.0 License](LICENSE).



