import simplejson as json

class LookupModule(object):
    def __init__(self, basedir=None, **kwargs):
        pass

    def run(self, terms, inject=None, **kwargs):
        with open(terms, 'r') as f:
            json_obj = json.load(f)

        return json_obj

