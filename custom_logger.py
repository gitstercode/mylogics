class CustomFormatter(Formatter):
    def __init__(self):
        super(CustomFormatter, self).__init__()

    def format(self, record):
        date_string = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
        app_id = "DEP"
        level = record.levelname
        server = record.args[0]
        clientip = record.args[1]
        message = record.msg
        log_messeage = "[%s] APPID=%s TYPE=%s SERVER=%s CLIENT_IP=%s MESSAGE=%s" % (
            date_string, app_id, level, server, clientip, message)

        return log_messeage
        
 def main():
     handler = FileHandler('foo.log')
     handler.setLevel(logging.INFO)
     handler.setFormatter(CustomFormatter())
     app.logger.addHandler(handler)
     
 server = request.host
 client_ip=request.remote_addr
 app.logger.error('An error occurred', server, client_ip)

if __name__ == '__main__':
    main()
