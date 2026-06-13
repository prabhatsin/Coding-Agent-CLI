from google.genai import types

read_file_schema = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="read_file",
            description="Reads the content of a file and returns it as a string",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="The path to the file to read"
                    )
                    
                },
                required=["file_path"]
            )
        )
    ]
)


write_file_schema = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="write_file",
            description="Write  the content to the file ",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="The path to the file to write"
                    ),

                    "content":types.Schema(
                        type=types.Type.STRING,
                        description="The content to be written"
                    )
                },
                required=["file_path","content"]
            )
        )
    ]
)


bash_schema = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="bash",
            description="pass the command line arguments as a string",
            parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "command": types.Schema(
                        type=types.Type.STRING,
                        description="The Command to be passed "
                    )
                },
                required=["command"]
            )
        )
    ]
)

all_tools = [read_file_schema, write_file_schema, bash_schema]