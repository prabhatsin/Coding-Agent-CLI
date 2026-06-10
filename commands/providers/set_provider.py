import click
import json

@click.command("set-provider")
@click.option('-p', '--provider', default='Google', help='Name of the provider to set as default')
# This function should give the list of providers and set default provider 
def set_provider_command(provider):
    provider = provider.capitalize()
    with open('models.json', 'r', encoding='utf-8') as file:
        object = json.load(file)
        providers_list = list(object["providers"].keys())
    if provider not in providers_list:
        click.echo(f"Unknown provider: {provider}. Available: {providers_list}")
        return
    config = {"default_provider": provider}
    with open('config.json', 'w', encoding='utf-8') as file:
        json.dump(config, file, indent=2)
    click.echo(f"Default provider set to: {provider}")

@click.command("providers list")
def providers_list():
    with open('models.json','r',encoding='utf-8') as file:
        object=json.load(file)
    providers_list=list(object['providers'].keys())
    click.echo(providers_list)

if __name__=='__main__':

    set_provider_command()
    providers_list()





    