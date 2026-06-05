import click
 
@click.command("logout")
@click.option('-p', '--provider', default='', help='Name of the provider (gemini, claude etc)')
def logout_command(provider):
    """Lets user logout from the provider"""
    print("logging out for provider " + provider)
 