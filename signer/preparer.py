class Preparer:
    def __init__(self, obj, prefix: str = ""):
        self.obj = obj
        self.prefix = prefix

    def parse(self) -> str:
        pass

class DictPreparer(Preparer):
    def parse(self) -> str:

        payload = ""
        for k, v in sorted(self.obj.items()):
            payload += "&" + k + "=" + v
        payload = payload[1:]

        return payload

class ListPreparer(Preparer):
    def parse(self) -> str:

        payload = ""
        for i, v in enumerate(self.obj):
            payload += '&' + f'[{i}]={v}'
        payload = payload[1:]

        return payload

class PreparerFactory:
    def get_preparer(self, obj, prefix: str = "") -> Preparer:
        if isinstance(obj, dict):
            return DictPreparer(obj, prefix)
        elif isinstance(obj, list):
            return ListPreparer(obj, prefix)

        return None