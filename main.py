import click
from commands.models import models_command
from commands.agent import agent_command
from commands.providers import set_provider_command

@click.group()
@click.version_option(version='0.1.0')
def cli():
    """Coding agent cli"""
    pass

cli.add_command(models_command)
cli.add_command(agent_command)
cli.add_command(set_provider_command)

if __name__ == '__main__':
    cli()



