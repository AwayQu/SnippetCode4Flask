# python==3.5
# flask==0.12
# Flask-RESTful==0.3.5

from flask_restful import Api

class AlertMessageException(Exception):
    def __init__(self, msg=None, code=None):
        self.msg = msg
        self.http_code = 400
        if not code:
            self.code = 1002
        else:
            self.code = code

    @property
    def data(self):
        return {
            'msg': self.msg,
            'code': self.code
        }

class ExceptionAwareApi(Api):
    def handle_error(self, e):
        if isinstance(e, AlertMessageException):
            code = e.http_code
            data = e.data
        else:
            # Did not match a custom exception, continue normally
            return super(ExceptionAwareApi, self).handle_error(e)
        return self.make_response(data, code)
