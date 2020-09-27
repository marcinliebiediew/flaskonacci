import cProfile
import timeit

import pyfiglet
import click
from flask.cli import with_appcontext

from src.extensions import db
from src.routes.fibonacci import subset_sum_from_fibonacci_set


@click.command(name='create_database')
@with_appcontext
def create_db():
    db.create_all()


@click.command(name='fib_benchmark')
def benchmark():
    print(pyfiglet.figlet_format("wow"))
    print(pyfiglet.figlet_format("such benchmark"))
    print("\n\n   cProfile")
    command = "from src.routes.fibonacci import subset_sum_from_fibonacci_set as f; f(1234)"
    cProfile.run(command)
    print("\n\n   timeit")
    print("100 executions took {0:.2f} seconds".format(
        timeit.timeit(command, number=100)))
