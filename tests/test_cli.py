"""Tests for cli."""
import pytest

from py_organizer.cli import cli


def test_cli_without_arg():
    """Test without arguments."""
    with pytest.raises(SystemExit):
        cli.parse_arguments()
        pytest.fail()
