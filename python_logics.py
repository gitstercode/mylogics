#####
## Logic- 1
## If a new file name is given as input 
## Since the file is not yet created in OS. To make perfect validations, the below code is required.

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
##
