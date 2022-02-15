"""Tests for mover functions."""

import pytest

from py_organizer.organizer.mover import get_file_and_destination

TEST_TEMPLATE = [
    (
        '/test_img/',
        'test.jpg',
        '/test_img/test.jpg',
        '/test_img/images',
    ),
    (
        '/test_vid/',
        'test.mkv',
        '/test_vid/test.mkv',
        '/test_vid/videos',
    ),
    (
        '/test_doc/',
        'test.pdf',
        '/test_doc/test.pdf',
        '/test_doc/documents',
    ),
    (
        '/test_arch/',
        'test.zip',
        '/test_arch/test.zip',
        '/test_arch/archives',
    ),
    (
        '/test_misc/',
        'test.exe',
        '/test_misc/test.exe',
        '/test_misc/other',
    ),
]


@pytest.mark.parametrize(
    'source_folder, file_in_dir, exp_file, exp_dest',
    TEST_TEMPLATE,
    )
def test_get_file_and_destination(
    source_folder,
    file_in_dir,
    exp_file,
    exp_dest,
):
    """Tests different extensions.

    Args:
        source_folder: test folder
        file_in_dir: test file name
        exp_file: expected result for file_to_move
        exp_dest: expected result for destination
    """
    test_case = get_file_and_destination(source_folder, file_in_dir)
    assert test_case == (exp_file, exp_dest)
