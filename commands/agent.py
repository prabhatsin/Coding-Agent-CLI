import click
import json

# @click.command("agent")
# @click.option('-p', '--prompt', default="Explain how AI works in a few words", help='prompt')

# 
from google.genai import types
def conversation_logic(prompt,messages):

    #! todo: whats the optimal way to do this ?
    #! Is it reading the data from a config file or (THIS ONE IS IMPLEMENTED here)
    #! Calling the functions directly in the script ?? 
    # messages=[]
    # messages.append(
    #     {'role':'user',
    #     'parts':prompt}
    # )

    # do this
    messages.append(
        types.Content(
            role='user',
            parts=[types.Part(text=prompt)]
        )
    )

    with open ('config.json','r',encoding='utf-8') as file:
        config_json=json.load(file)
    provider=config_json["default_provider"]
    API_KEY=config_json['gemini']['api_key']
    if provider=="Google":
        model1=config_json['gemini']["default_model"]
        print('The model used in this loop is',model1)
        from google import genai
        client = genai.Client(api_key=API_KEY)
        response = client.models.generate_content(
            model=model1,
            contents=messages
        )
        # click.echo(response.text)
        # click.echo(response)
    messages.append(
    types.Content(
        role='model',
        parts=[types.Part(text=response.text)]
    )
)

    # messages.append(
    #     {'role':'model',
    #     'parts':response.text}
    # )
    return response.text 

@click.command("agent")
@click.option('-p', '--prompt', default="Explain how AI works in a few words", help='prompt')
def agent_command(prompt):
    messages=[]
    while True:
        prompt=click.prompt("you")
        if prompt=='exit':
            break
        response=conversation_logic(prompt,messages)
        # click.echo(messages[-1]['content'])
        click.echo(response)
        # Why not response.text ?






if __name__=='__main__':
    agent_command()
   
#! TODO : Implement the loop , get the api , and Tool calling part 