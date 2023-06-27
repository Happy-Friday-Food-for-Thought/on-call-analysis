import click

from source.pagerduty import pagerduty

@click.group()
def run():
    pass


run.add_command(pagerduty)
