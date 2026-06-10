# # # commands/models.py
import click
import json
@click.command('models')
@click.option('-p', '--provider', default='all', help='name of the model')
def models_command(provider):
    # This line handles the part when user throws provider name in
    # small letters like google or anthropic instead of Google / Anthropic
    all_model_list=[]
    with open('models.json','r',encoding='utf-8') as file:
        object=json.load(file)
        providers_list=list(object["providers"].keys())

        if provider=='all':
            for each_provider in providers_list:
                all_model_list.extend(object["providers"][each_provider]['models'])
            click.echo(all_model_list)
        else:
            provider=provider.capitalize()
            if provider not in providers_list:
                click.echo(f"Unknown provider :{provider}. Providers list is :{providers_list}")
            else:
                provider_model_list=object['providers'][provider]['models']
                click.echo(provider_model_list)

if __name__=='__main__':

    print("This part only executes itself  when we directly run this script ")
    models_command()


'''
if we import the script (models.py) anywhere else the part below 'if __name__=='__main__':
' does not execute becase then 
__name__ is "myscript", not "__main__".

'''
'''
# click.echo — prints to the terminal. That's it. Function keeps running after it.
'''














    
     

  