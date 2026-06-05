import click
 
@click.command("agent")
@click.option('-p', '--prompt', default='', help='prompt')
def agent_command(prompt):
    """Runs the agent"""
    print("User prompt is ..." + prompt)
 