import click
import json
 
@click.command("set-provider")
@click.option('-p', '--provider', default='', help='Name of the provider (gemini, claude etc)')
def set_provider_command(provider):

    """Lets user set the default provider"""
    PROVIDERS = ["openai", "anthropic", "google", "deepseek", "openrouter", "ollama", "groq", "together", "mistral", "cohere", "xai", "fireworks", "cerebras", "perplexity", "lmstudio"]
    for prov in  PROVIDERS:
        return prov
        print("provider is  " + json.dumps({'provider': provider}))


PROVIDERS = ["openai", "anthropic", "google", "deepseek", "openrouter", "ollama", "groq", "together", "mistral", "cohere", "xai", "fireworks", "cerebras", "perplexity", "lmstudio"]
set_provider_command()





    