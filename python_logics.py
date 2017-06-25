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
