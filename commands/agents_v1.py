import click
import json
from google.genai import types
from tools import read_file, write_file, bash
from tools.schema import all_tools

def conversation_logic(prompt, messages):
    messages.append(
        types.Content(
            role='user',
            parts=[types.Part(text=prompt)]
        )
    )

    with open('config.json', 'r', encoding='utf-8') as file:
        config_json = json.load(file)
    
    provider = config_json["default_provider"]
    API_KEY = config_json['gemini']['api_key']
    
    if provider == "Google":
        model1 = config_json['gemini']["default_model"]
        from google import genai
        client = genai.Client(api_key=API_KEY)
        
        while True:
            response = client.models.generate_content(
                model=model1,
                contents=messages,
                config=types.GenerateContentConfig(tools=all_tools)
            )

            part = response.candidates[0].content.parts[0]

            if part.function_call:
                name = part.function_call.name
                args = part.function_call.args

                if name == "read_file":
                    result = read_file(args["file_path"])
                elif name == "write_file":
                    result = write_file(args["file_path"], args["content"])
                elif name == "bash":
                    result = bash(args["command"])

                messages.append(types.Content(
                    role='model',
                    parts=[types.Part(function_call=part.function_call)]
                ))
                messages.append(types.Content(
                    role='user',
                    parts=[types.Part(
                        function_response=types.FunctionResponse(
                            name=name,
                            response={"result": result}
                        )
                    )]
                ))

            else:
                messages.append(types.Content(
                    role='model',
                    parts=[types.Part(text=response.text)]
                ))
                return response.text


@click.command("agent")
@click.option('-p', '--prompt', default="Explain how AI works in a few words", help='prompt')
def agent_command(prompt):
    messages = []
    while True:
        prompt = click.prompt("you")
        if prompt == 'exit':
            break
        response = conversation_logic(prompt, messages)
        click.echo(response)


if __name__ == '__main__':
    agent_command()