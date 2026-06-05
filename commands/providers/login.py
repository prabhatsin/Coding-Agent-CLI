import click
 
@click.command("login")
@click.option('-p', '--provider', default='', help='Name of the provider (gemini, claude etc)')
@click.option('-a', '--api_key', default='', help='Your api key')
def login_command(provider, api_key):
    """Lets user login into the provider (use it as default)"""
    print("logging into " + provider)



'''
def login(username, password):
    """Simple program that authenticates a user."""
    # Place your credential validation or API logic here
    if username == "admin" and password == "secret":
        click.echo(f"Access granted. Welcome, {username}!")
    else:
        click.echo("Access denied. Invalid credentials.")

if __name__ == '__main__':
    login()




'''