# commands/models.py
import click
 
@click.commands("models")
@click.option('-m', '--model', default='all', help='name of the model')
def models_command(model):
    """Returns all the supported models"""
    model_list=["Gemini 2.5 Flash","Gemini 3.1","Gemini","Gemini Nano"]
    for mod in model_list:
        return mod
    print("Listing models...")
    print({'model': model})