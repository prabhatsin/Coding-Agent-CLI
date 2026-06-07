import click
#What’s happening is that the decorator converts the function into a Command
# which then can be invoked:
@click.command()   
# This line makes it a decorator and from  normal function it becomes 
# a command line argument
@click.option('--name',default='world',help='who to greet')
def func_hello(name):
    click.echo(f"Hello {name}")  # echo ???? 
    # echo is just the replacement of print with better
    #  the echo() function applies some error correction in case
    #  the terminal is misconfigured instead of dying with a UnicodeError.
if __name__=='__main__':
    func_hello()

#! Note dont try to do click.echo("Hello",name) just like you do with print 
#! reason being echo only takes one string argument 
'''
click.echo(message=None, file=None, nl=True, err=False, color=None)
'''

'''
@click.command('models')

ye jo command ke andar 'models' hai ye kaha kaam aayega ?? 
this will be used when we run our main script 
 python main.py models  , now the outputv of functions jaha ye models the 
 that will appear 


'''
