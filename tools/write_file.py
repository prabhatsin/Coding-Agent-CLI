
def write_file(file_path,content):
    try:
        with open(file_path,'w',encoding='utf-8') as f:
            f.write(content)   
            return "File written successfully"
    except FileNotFoundError:
        return('The file does not exist ')



# write_file('/home/prabhat/Desktop/TUI/test.txt')