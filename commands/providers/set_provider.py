import click
import json
 
@click.command("set-provider")
# @click.option('-p', '--provider', default='', help='Name of the provider (gemini, claude etc)')
def set_provider_command():
    """Lets user set the default provider"""
    with open ('/home/prabhat/Desktop/TUI/models.json','r',encoding='utf-8') as file:
        object=json.load(file)
        providers=list(object["providers"].keys())
        for i,provider in enumerate(providers,start=1):
            click.echo(f"{i}.{provider}")

        choice=input("Enter the number: ",)
        choice=int(choice)
        selected=providers[choice-1]

        config={"default provider":selected}

    with open('Config.json','w',encoding='utf-8') as file:
        json.dump(config,file,indent=2)

    print("The defualt provider set to :",selected)
        



    
    # print("provider is  " + json.dumps({'provider': provider}))

if __name__=='__main__':

    set_provider_command()





    