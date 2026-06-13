


def read_file(file_path):
    try:
        with open(file_path,'r',encoding='utf-8') as f:
            obj=f.read()
            return str(obj)
    except FileNotFoundError:
        return('The file does not exist ')








# file_path='/home/prabhat/Desktop/TUI/commands/providers/set_provider.py'
# read_file(file_path)