import click
import json
@click.command("logout")
@click.option('-p', '--provider', default='', help='Name of the provider (gemini, claude etc)')
def logout_command(provider):
    # Step1: check if config file exist or not 
    try:
        with open('/home/prabhat/Desktop/TUI/config.json','r',encoding='utf-8')as file:
            object=json.load(file)
            # Check if the provider asked for exist in the config file
        if provider not in object:
            click.echo(f"The {provider} is not logged in")
            # stop here, don't reach the save
            return # ! # ← function exits HERE 
            # this emty return makes sure that if provider not in the confif file so
            # it should not be saved 
        
        elif object["default_provider"]==provider:
            object.pop("default_provider")
            object.pop(provider)
            print(f"The {provider} is logged out .The default provider which is :{provider} is removed")

        else:
            object.pop(provider)
            print(f"The :{provider} is logged out")
        # Save the updated config back to file     
        with open('/home/prabhat/Desktop/TUI/config.json','w',encoding='utf-8')as file:
                json.dump(object,file)
    except FileNotFoundError:
          print("File does not exist")
    except PermissionError:
        print("The file exists, but you do not have permission to read it.")


if __name__=="__main__":
     
     logout_command()
     

'''
Not a bug but worth noting ->

object is a built-in Python type name. Using it as a variable name shadows the built-in.
Not dangerous here but bad habit — name it config instead.

'''



    






   