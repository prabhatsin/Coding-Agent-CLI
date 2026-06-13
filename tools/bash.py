
import subprocess


def bash(command):
        result=subprocess.run(command,shell=True ,capture_output=True,text=True)
        # shell=True. ??? 
        # tells subprocess to pass the command string to your system shell
        '''
        capture_output=True — instead of printing stdout/stderr directly
        to your terminal, capture them into result.stdout and result.
        stderr as strings. This is what lets you return the output back to the LLM.
        
        '''

        if result.returncode !=0:
            return result.stderr
        return result.stdout

        

