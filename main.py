#!/usr/bin/env python

"""
Main CLI or app entry point
"""
import click
from mylib.calculator import add, subtract, multiply, divide, power


# Creamos un grupo de comandos
@click.group()
def cli():
    """CLI principal para operaciones matemáticas básicas."""


# Creamos un comando para sumar llamado add, que asociamos al grupo anterior, que recibe dos argumentos a y b de tipo float
@cli.command("add")
@click.argument("a", type=float)
@click.argument("b", type=float)
def add_cli(a, b):
    """Add two numbers together

    Example:
        ./main.py add 1 2
    """

    click.echo(click.style(str(add(a, b)), fg="green"))


# Creamos un comando para restar llamado subtract, que asociamos al grupo anterior, que recibe dos argumentos a y b de tipo float
@cli.command("subtract")
@click.argument("a", type=float)
@click.argument("b", type=float)
def subtract_cli(a, b):
    """Subtract two numbers

    Example:
        ./main.py subtract 5 3
    """

    click.echo(click.style(str(subtract(a, b)), fg="green"))


# Creamos un comando para multiplicar llamado multiply, que asociamos al grupo anterior, que recibe dos argumentos a y b de tipo float
@cli.command("multiply")
@click.argument("a", type=float)
@click.argument("b", type=float)
def multiply_cli(a, b):
    """Multiply two numbers

    Example:
        ./main.py multiply 2 3
    """

    click.echo(click.style(str(multiply(a, b)), fg="green"))


# Creamos un comando para dividir llamado divide, que asociamos al grupo anterior, que recibe dos argumentos a y b de tipo float
@cli.command("divide")
@click.argument("a", type=float)
@click.argument("b", type=float)
def divide_cli(a, b):
    """Divide two numbers

    Example:
        ./main.py divide 6 3
    """

    if b == 0:
        click.echo(click.style("Error: Division by zero", fg="red"))
    else:
        click.echo(click.style(str(divide(a, b)), fg="green"))


# Crea un comando para elevar a la potencia llamado power, que asociamos al grupo anterior, que recibe dos argumentos a y b de tipo float
@cli.command("power")
@click.argument("a", type=float)
@click.argument("b", type=float)
def power_cli(a, b):
    """Raise a number to the power of another

    Example:
        ./main.py power 2 3
    """

    click.echo(click.style(str(power(a, b)), fg="green"))


# Punto de entrada principal
if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    cli()
