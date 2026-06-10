import click
import os
import json
from google import genai
@click.command("login")
@click.option('-p', '--provider', default='', help='Name of the provider (gemini, claude etc)')
@click.option('-a', '--api_key', default='', help='Your api key')

def login_command(provider, api_key):
    # Step1: Validate the input
    SUPPORTED_PROVIDERS = ['claude', 'gemini', 'openai', 'deepseek']
    #! Step 1 — Validate inputs
    if not provider:
        click.echo("Error:Provider is required")
        return
    if provider not in SUPPORTED_PROVIDERS:
        click.echo(f"Error:Unsupported provider:{provider}. Choose from:{SUPPORTED_PROVIDERS}") 
        return
    if not api_key:
        api_key=click.prompt(f"Enter the apikey for the :{provider}",hide_input=True)

    # Step2: Validate the api_key
    try:
        client = genai.Client(api_key=api_key)
        models = list(client.models.list())
        config_api={"api_key":api_key}
        with open('Config.json','w',encoding='utf-8') as file:
            json.dump(config_api,file,indent=2)
        click.echo(f"Logged in with {provider}. Config saved.")
        return True
    except Exception as e:
        click.echo(f"Validation Error in api_key-{e}")
        return False
    # Step3: store the apikey in a config file 
    # config_api={"api_key":api_key}
    # with open(Confiig.json,'w',encoding='utf-8') as file:
    #     json.dump(config_api,file,indent=2)


if __name__=="__main__":
    login_command()










    






'''

hide_input=True
This masks the input while typing — exactly like a password field.
The user types but nothing appears on screen (no characters, no asterisks).

'''




    # Here what we do is we get the name of provbider and api key 
    # so we just verify both 
    #! Verify the api key
    #! Problem that i m thinking , agar provider doosra hua toh ?? 
    #! Are we going tob use the SDK of all providers in the verification logic ?? 
  














'''

Issue 1: default='' means if user doesn't pass provider or api_key,
you get an empty string silently. You'd want to either use required=True
or validate manually and show a useful error.

Issue 2: Passing API key via -a flag is fine for dev, but it'll show up in
shell history (~/.bash_history). Production CLI tools use click.prompt with
hide_input=True instead. Worth knowing even if you don't fix it now.

'''

