import os
import subprocess
import shutil

import pytest

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "fixtures")


def _create_minimal_jpeg(path):
    """Create a minimal valid JPEG file using Pillow."""
    from PIL import Image

    os.makedirs(os.path.dirname(path), exist_ok=True)
    img = Image.new("RGB", (10, 10), color="red")
    img.save(path)


def _run_exiftool(args):
    """Run exiftool with the given arguments."""
    subprocess.run(["exiftool"] + args, check=True, capture_output=True)


@pytest.fixture(scope="session", autouse=True)
def create_fixtures():
    """Generate test fixture images before the test session starts."""
    os.makedirs(FIXTURES_DIR, exist_ok=True)

    # 1. Minimal image (no custom EXIF)
    minimal_path = os.path.join(FIXTURES_DIR, "test_minimal.jpg")
    _create_minimal_jpeg(minimal_path)

    # 2. Image with EXIF data (no GPS)
    exif_path = os.path.join(FIXTURES_DIR, "test_with_exif.jpg")
    _create_minimal_jpeg(exif_path)
    _run_exiftool([
        "-Make=CanonTest",
        "-Model=EOS R5",
        "-DateTimeOriginal=2024:06:20 14:00:00",
        "-overwrite_original",
        exif_path,
    ])

    # 3. Image with EXIF + GPS data
    gps_path = os.path.join(FIXTURES_DIR, "test_with_gps.jpg")
    _create_minimal_jpeg(gps_path)
    _run_exiftool([
        "-Make=TestCamera",
        "-Model=TestModel",
        "-DateTimeOriginal=2024:01:15 10:30:00",
        "-GPSLatitude=-23.5505",
        "-GPSLatitudeRef=S",
        "-GPSLongitude=-46.6333",
        "-GPSLongitudeRef=W",
        "-overwrite_original",
        gps_path,
    ])

    yield

    # Cleanup fixtures after test session
    shutil.rmtree(FIXTURES_DIR, ignore_errors=True)


@pytest.fixture
def image_with_gps():
    """Path to a test JPEG image with EXIF data including GPS coordinates."""
    return os.path.join(FIXTURES_DIR, "test_with_gps.jpg")


@pytest.fixture
def image_with_exif():
    """Path to a test JPEG image with EXIF data but no GPS coordinates."""
    return os.path.join(FIXTURES_DIR, "test_with_exif.jpg")


@pytest.fixture
def image_minimal():
    """Path to a minimal JPEG image with no custom EXIF tags."""
    return os.path.join(FIXTURES_DIR, "test_minimal.jpg")


@pytest.fixture
def nonexistent_file():
    """Path to a file that does not exist."""
    return "/tmp/showexif_nonexistent_file_12345.jpg"
