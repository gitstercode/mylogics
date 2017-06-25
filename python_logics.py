#####
## Logic- 1
## If a new file name is given as input 
## Since the file is not yet created in OS. To make perfect validations, the below code is required.
import os

o = "path/to/new/file.txt"
o = os.path.abspath(o)                  # Gets Absolute path if given path is relative
        if os.path.isdir(o):            # If given input is a directory
            output = o
        else:                           # If its a file name 
            parentDir = '/'.join(o.split('/')[0:-1])
            if parentDir:               # If a directory is given along with filename
                if os.path.exists(parentDir):
                    output = os.path.dirname(o)
                    fileNameOut = os.path.basename(o)
                else:
                    click.echo("Given outpath path doesn't exist.")
                    sys.exit()
            else:                       # If only a filename is given
                output = os.getcwd()
                fileNameOut = o
#####                

#####
## Logic -2
## If the Given json file throws error or if any python library(click) not accepting JSON calls
## Below Class can help in converting JSON to dict and then writing back to file

import ast

class Config(object):
    def __init__(self):
        self.contents = None
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                s = f.read()
                self.contents = ast.literal_eval(s)

    def get_config(self):
        return self.contents

    def write(self, key, value):
        self.contents[key] = value
        with open(CONFIG_FILE, 'w') as f:
            f.write(str(self.contents))

    def remove(self, *args):
        for key in args:
            value = self.contents.get(key)
            if value:
                self.contents[key] = ""
                with open(CONFIG_FILE, 'w') as f:
                    f.write(str(self.contents))
config = Config()
some_key = config.get_config().get("some_key")
config.write("some_key1", "some_value1")
config.remove("some_key1", "some_key")

#####

#####
## Logic - 3
## Method Interception

# Methods for Intercepting AClass
    def __getattr__(self, attr):
        try:
            return super(CurrentClass, self).__getattr__(attr)
        except AttributeError:
            return self.__get_global_handler(attr)

    def __get_global_handler(self, name):
        # Do anything that you need to do before simulating the method call
        handler = self.__global_handler
        handler.im_func.func_name = name
        return handler

    def __global_handler(self, *args, **kwargs):
        # Do something with these arguments
        try:
            func = getattr(self.object_of_AClass, self.__global_handler.im_func.func_name)
            if args:
                response = func(args)
            else:
                response = func()
            return response
        except AttributeError:
            print "%s not found" % self.__global_handler.im_func.func_name
#####

#####
## Logic - 4
## Logic to execute a shell command within python

exec_command = subprocess.Popen(cmd_string, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = exec_command.communicate() # exec_command.wait()

#####

#####
## Logic 5
# To Remove a file
os.remove(line)

# To Remove a directory
shutil.rmtree(line)

#####

#####
## Logic - 6
##
