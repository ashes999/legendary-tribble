class StringLogger:
    def __init__(self):
        self.messages = ""
        
    def log(self, message):
        self.messages = "{0}{1}".format(self.messages, message)