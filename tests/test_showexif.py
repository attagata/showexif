"""Tests for showexif.py - EXIF metadata extraction tool."""

import os
import sys
import subprocess

import pytest

# Add parent directory to path so we can import showexif
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from showexif import print_exif_info


class TestFileNotFound:
    """Tests for when the specified file does not exist."""

    def test_prints_error_message(self, nonexistent_file, capsys):
        """Should print a Portuguese error message when file does not exist."""
        print_exif_info(nonexistent_file)
        captured = capsys.readouterr()
        assert "Erro" in captured.out
        assert "não encontrado" in captured.out

    def test_includes_file_path_in_error(self, nonexistent_file, capsys):
        """Should include the file path in the error message."""
        print_exif_info(nonexistent_file)
        captured = capsys.readouterr()
        assert nonexistent_file in captured.out

    def test_does_not_crash(self, nonexistent_file):
        """Should return gracefully without raising an exception."""
        # Should not raise any exception
        print_exif_info(nonexistent_file)


class TestExifExtraction:
    """Tests for EXIF metadata extraction from valid image files."""

    def test_prints_exif_header(self, image_with_exif, capsys):
        """Should print the EXIF information header in Portuguese."""
        print_exif_info(image_with_exif)
        captured = capsys.readouterr()
        assert "Informações EXIF:" in captured.out

    def test_extracts_camera_make(self, image_with_exif, capsys):
        """Should extract and display the camera Make tag."""
        print_exif_info(image_with_exif)
        captured = capsys.readouterr()
        assert "CanonTest" in captured.out

    def test_extracts_camera_model(self, image_with_exif, capsys):
        """Should extract and display the camera Model tag."""
        print_exif_info(image_with_exif)
        captured = capsys.readouterr()
        assert "EOS R5" in captured.out

    def test_extracts_date_time_original(self, image_with_exif, capsys):
        """Should extract and display the DateTimeOriginal tag."""
        print_exif_info(image_with_exif)
        captured = capsys.readouterr()
        assert "2024:06:20 14:00:00" in captured.out

    def test_extracts_file_type(self, image_with_exif, capsys):
        """Should extract and display the file type."""
        print_exif_info(image_with_exif)
        captured = capsys.readouterr()
        assert "JPEG" in captured.out

    def test_extracts_mime_type(self, image_with_exif, capsys):
        """Should extract and display the MIME type."""
        print_exif_info(image_with_exif)
        captured = capsys.readouterr()
        assert "image/jpeg" in captured.out

    def test_extracts_image_dimensions(self, image_with_exif, capsys):
        """Should extract and display image width and height."""
        print_exif_info(image_with_exif)
        captured = capsys.readouterr()
        # The test image is 10x10 pixels
        assert "10" in captured.out

    def test_output_contains_tag_group_format(self, image_with_exif, capsys):
        """Should display tags in [Group] TagName: Value format."""
        print_exif_info(image_with_exif)
        captured = capsys.readouterr()
        lines = captured.out.strip().split("\n")
        # Skip the header line and check that data lines contain the expected format
        data_lines = [l for l in lines[1:] if l.strip()]
        assert len(data_lines) > 0
        for line in data_lines:
            assert ":" in line, f"Expected ':' in line: {line}"


class TestGPSExtraction:
    """Tests for GPS coordinate extraction and Google Maps link generation."""

    def test_prints_google_maps_header(self, image_with_gps, capsys):
        """Should print the Google Maps header in Portuguese when GPS data exists."""
        print_exif_info(image_with_gps)
        captured = capsys.readouterr()
        assert "Localização no Google Maps:" in captured.out

    def test_generates_google_maps_link(self, image_with_gps, capsys):
        """Should generate a valid Google Maps URL with lat/lon coordinates."""
        print_exif_info(image_with_gps)
        captured = capsys.readouterr()
        assert "https://www.google.com/maps?q=" in captured.out

    def test_maps_link_contains_correct_latitude(self, image_with_gps, capsys):
        """Should include the correct latitude in the Maps link."""
        print_exif_info(image_with_gps)
        captured = capsys.readouterr()
        assert "-23.5505" in captured.out

    def test_maps_link_contains_correct_longitude(self, image_with_gps, capsys):
        """Should include the correct longitude in the Maps link."""
        print_exif_info(image_with_gps)
        captured = capsys.readouterr()
        assert "-46.6333" in captured.out

    def test_no_maps_link_without_gps(self, image_with_exif, capsys):
        """Should NOT print a Google Maps link when GPS data is absent."""
        print_exif_info(image_with_exif)
        captured = capsys.readouterr()
        assert "google.com/maps" not in captured.out
        assert "Localização no Google Maps:" not in captured.out


class TestMinimalImage:
    """Tests for a minimal image without custom EXIF tags."""

    def test_still_extracts_file_metadata(self, image_minimal, capsys):
        """Should still extract basic file metadata even without camera EXIF tags."""
        print_exif_info(image_minimal)
        captured = capsys.readouterr()
        assert "Informações EXIF:" in captured.out
        assert "FileName" in captured.out
        assert "FileType" in captured.out

    def test_no_maps_link_for_minimal_image(self, image_minimal, capsys):
        """Should NOT generate a Google Maps link for an image without GPS data."""
        print_exif_info(image_minimal)
        captured = capsys.readouterr()
        assert "google.com/maps" not in captured.out


class TestCLI:
    """Tests for the command-line interface."""

    def test_help_flag(self):
        """Should display help message with --help flag."""
        result = subprocess.run(
            [sys.executable, "showexif.py", "--help"],
            capture_output=True,
            text=True,
            cwd=os.path.join(os.path.dirname(__file__), ".."),
        )
        assert result.returncode == 0
        assert "--image_path" in result.stdout
        assert "EXIF" in result.stdout or "imagem" in result.stdout

    def test_missing_required_argument(self):
        """Should exit with error when --image_path is not provided."""
        result = subprocess.run(
            [sys.executable, "showexif.py"],
            capture_output=True,
            text=True,
            cwd=os.path.join(os.path.dirname(__file__), ".."),
        )
        assert result.returncode != 0
        assert "required" in result.stderr.lower() or "error" in result.stderr.lower()

    def test_cli_with_valid_file(self, image_with_exif):
        """Should display EXIF data when run from the command line with a valid file."""
        result = subprocess.run(
            [sys.executable, "showexif.py", "--image_path", image_with_exif],
            capture_output=True,
            text=True,
            cwd=os.path.join(os.path.dirname(__file__), ".."),
        )
        assert result.returncode == 0
        assert "Informações EXIF:" in result.stdout
        assert "CanonTest" in result.stdout

    def test_cli_with_nonexistent_file(self, nonexistent_file):
        """Should print error message when run with a nonexistent file."""
        result = subprocess.run(
            [sys.executable, "showexif.py", "--image_path", nonexistent_file],
            capture_output=True,
            text=True,
            cwd=os.path.join(os.path.dirname(__file__), ".."),
        )
        assert "Erro" in result.stdout
        assert nonexistent_file in result.stdout

    def test_cli_with_gps_image(self, image_with_gps):
        """Should display Google Maps link when run with an image containing GPS data."""
        result = subprocess.run(
            [sys.executable, "showexif.py", "--image_path", image_with_gps],
            capture_output=True,
            text=True,
            cwd=os.path.join(os.path.dirname(__file__), ".."),
        )
        assert result.returncode == 0
        assert "google.com/maps" in result.stdout


class TestOutputFormat:
    """Tests for the output format structure."""

    def test_output_lines_have_group_prefix(self, image_with_exif, capsys):
        """Should prefix metadata lines with group name in brackets."""
        print_exif_info(image_with_exif)
        captured = capsys.readouterr()
        lines = captured.out.strip().split("\n")
        # Find lines that contain EXIF data (skip header and empty lines)
        data_lines = [l for l in lines[1:] if l.strip() and ":" in l]
        # Check that at least some lines contain group prefixes
        lines_with_groups = [l for l in data_lines if "[" in l and "]" in l]
        assert len(lines_with_groups) > 0, "Expected lines with [Group] prefix"

    def test_multiple_metadata_lines(self, image_with_exif, capsys):
        """Should output multiple lines of metadata."""
        print_exif_info(image_with_exif)
        captured = capsys.readouterr()
        lines = [l for l in captured.out.strip().split("\n") if l.strip()]
        # A JPEG with EXIF data should produce at least 10 lines of metadata
        assert len(lines) >= 10, f"Expected at least 10 lines, got {len(lines)}"

    def test_exif_tags_are_present(self, image_with_exif, capsys):
        """Should include standard EXIF group tags in the output."""
        print_exif_info(image_with_exif)
        captured = capsys.readouterr()
        assert "[EXIF]" in captured.out
        assert "[File]" in captured.out
