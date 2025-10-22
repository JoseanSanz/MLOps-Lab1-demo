"""
Test goes here

"""

from main import cli
from mylib.calculator import add, subtract, multiply, divide, power
from click.testing import CliRunner


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(6, 3) == 2


def test_power():
    assert power(2, 3) == 8


def test_help():
    """Tests the command-line interface help message."""
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Show this message and exit." in result.output


# Write a test for the add_cli function of the cli group.
def test_add_cli():
    """Tests the command-line interface add command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["add", "1", "2"])
    assert result.exit_code == 0
    assert "3" in result.output


# Write a test for the subtract_cli function of the cli group.
def test_subtract_cli():
    """Tests the command-line interface subtract command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["subtract", "5", "3"])
    assert result.exit_code == 0
    assert "2" in result.output


# Write a test for the multiply_cli function of the cli group.
def test_multiply_cli():
    """Tests the command-line interface multiply command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["multiply", "2", "3"])
    assert result.exit_code == 0
    assert "6" in result.output


# Write a test for the divide_cli function of the cli group.
def test_divide_cli():
    """Tests the command-line interface divide command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["divide", "6", "3"])
    assert result.exit_code == 0
    assert "2" in result.output


# Write a test for the power_cli function of the cli group.
def test_power_cli():
    """Tests the command-line interface power command."""
    runner = CliRunner()
    result = runner.invoke(cli, ["power", "2", "3"])
    assert result.exit_code == 0
    assert "8" in result.output
