'''custom error handlers'''

class Error(Exception):
    '''default exception handler'''
    def __init__(self, msg):
        self.msg = msg

class CustomError(Error):
    '''example handle for custom error type'''
    pass
