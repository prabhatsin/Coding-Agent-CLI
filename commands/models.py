# # # commands/models.py
import click
import json
@click.command('models')
# @click.option('-m', '--model', default='all', help='name of the model')
#! Keerats boiler plate had .option wala part 
#! Get clarity on when to use click.option and when not to 

def models_command():
    all_model_list=[]
    with open('models.json','r',encoding='utf-8') as file:
        object=json.load(file)
        providers_list=list(object["providers"].keys())
        for provider in providers_list:
            all_model_list.extend(object["providers"][provider]['models'])
    click.echo(all_model_list)

if __name__=='__main__':
    models_command()


#?-----------------------------------------------------------------------
# def models_command(provider):
#     """Returns all the supported models"""
#     with open('models.json','r',encoding='utf-8') as file:
#         object=json.load(file)
#         providers_list=list(object["providers"].keys())
#         models_list=object["providers"][provider]['models']
#     # print("Listing models...")
#     # print({'model': models_list})
#     click.echo(models_list)

'''
# # '-m' --> Short flag 
# # '--model' --> Long flag 
# # default='all'  --> the value when user does not give the specific input 
# The equivalent of 'return' and 'print' both in click framework is  cl

'''
#?---------------------------------------------------------------------------














    
     

  