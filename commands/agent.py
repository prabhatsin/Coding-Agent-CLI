import click
import json

@click.command("agent")
@click.option('-p', '--prompt', default="Explain how AI works in a few words", help='prompt')
def agent_command(prompt):

    with open ('config.json','r',encoding='utf-8') as file:
        config_json=json.load(file)
    provider=config_json["default_provider"]
    API_KEY=config_json['gemini']['api_key']

    if provider=="Google":
        model1=config_json['gemini']["default_model"]
        from google import genai
        client = genai.Client(api_key=API_KEY)
        response = client.models.generate_content(
            model=model1,
            contents=prompt
        )
        click.echo(response.text)


if __name__=='__main__':
    agent_command()
   
#! TODO : Implement the loop , get the api , and Tool calling part 