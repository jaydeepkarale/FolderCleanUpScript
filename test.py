from turtledemo.penrose import star

import pytest
from main import (
    start_script,
    read_files_from_download_directory,
    check_if_directory_exists,
    SOURCE_FOLDER,
    DESTINATION_FOLDER
)
from pathlib import Path


def test_start_script():
    assert 0


def test_read_png_files_from_download_directory():
    assert read_files_from_download_directory(extension='png') is not None


def test_read_jpg_files_from_download_directory():
    assert read_files_from_download_directory(extension='jpg') is not None


def test_check_if_dest_directory_exists():
    assert check_if_directory_exists('C:/Users/pc/Downloads/') is True


def test_check_return_false_if_directory_does_not_exists():
    assert check_if_directory_exists('C:/Users/pc/Download') is False


