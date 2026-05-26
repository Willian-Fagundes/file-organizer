import shutil
from pathlib import Path

import pytest

from organizer import folders_finder, mover


@pytest.fixture
def temp_environment(tmp_path):

    documentos = tmp_path / "Documentos"
    imagens = tmp_path / "Imagens"
    videos = tmp_path / "Videos"

    documentos.mkdir()
    imagens.mkdir()
    videos.mkdir()


    text_file = tmp_path / "test.txt"
    image_file = tmp_path / "photo.jpg"
    video_file = tmp_path / "movie.mp4"

    text_file.write_text("hello")
    image_file.write_text("fake image")
    video_file.write_text("fake video")

    return {
        "root": tmp_path,
        "documentos": documentos,
        "imagens": imagens,
        "videos": videos,
        "text_file": text_file,
        "image_file": image_file,
        "video_file": video_file,
    }


def test_folders_finder(temp_environment):
    root = temp_environment["root"]

    folders = folders_finder(root)

    assert "documentos" in folders
    assert "imagens" in folders
    assert "videos" in folders

    assert folders["documentos"].exists()
    assert folders["imagens"].exists()
    assert folders["videos"].exists()


def test_mover_moves_text_files(temp_environment):
    root = temp_environment["root"]

    mover(root)

    moved_file = temp_environment["documentos"] / "test.txt"

    assert moved_file.exists()
    assert not temp_environment["text_file"].exists()


def test_mover_moves_image_files(temp_environment):
    root = temp_environment["root"]

    mover(root)

    moved_file = temp_environment["imagens"] / "photo.jpg"

    assert moved_file.exists()
    assert not temp_environment["image_file"].exists()


def test_mover_moves_video_files(temp_environment):
    root = temp_environment["root"]

    mover(root)

    moved_file = temp_environment["videos"] / "movie.mp4"

    assert moved_file.exists()
    assert not temp_environment["video_file"].exists()


def test_mover_ignores_directories(tmp_path):

    (tmp_path / "documentos").mkdir()
    (tmp_path / "imagens").mkdir()
    (tmp_path / "Videos").mkdir()

    folder = tmp_path / "random_folder"
    folder.mkdir()

    mover(tmp_path)

    assert folder.exists()
    assert folder.is_dir()