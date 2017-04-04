from erlport import Atom


class BtlBase(object):
    def __init__(self, tag):
        self.tag = tag


class BtlOk(BtlBase):
    def __init__(self, message):
        super(BtlOk, self).__init__("ok")
        self.message = message

class BtlRequest(BtlBase):
    def __init__(self, handler, necessary_fields, context):
        super(BtlRequest, self).__init__("request")
        self.request = "request"
        self.handler = handler
        self.necessary_fields = necessary_fields
        self.context = context


class BtlResult():
    def __init__(self, values):
        self.values = values
        self.btl_result = {
            "ok" : lambda result: (Atom(result.tag), result.message, self.values),
            "request" : lambda result: (Atom(result.tag), Atom(result.handler), result.necessary_fields, result.context, self.values)
        }
    def get_result(self, result):
        return self.btl_result[result.tag](result)
