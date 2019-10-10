class Preparer:
    def __init__(self, obj, prefix: str = ""):
        self.obj = obj
        self.prefix = prefix

    def append_prefix(self, val) -> str:
        prefix = val

        if not isinstance(prefix, str):
            prefix = str(prefix)

        if len(self.prefix) > 0:
            prefix = f'{self.prefix}[{prefix}]'
        return prefix

    def parse(self) -> str:
        pass

class DictPreparer(Preparer):
    def parse(self) -> str:

        payload = ""
        for k, v in sorted(self.obj.items()):
            payload += "&" + PreparerFactory(). \
                get_preparer(v, self.append_prefix(k)).parse()

        payload = payload[1:]

        return payload

class ListPreparer(Preparer):
    def parse(self) -> str:

        payload = ""
        for i, v in enumerate(self.obj):
            payload += "&" + PreparerFactory(). \
                get_preparer(v, self.append_prefix(i)).parse()
        payload = payload[1:]

        return payload

class StrPreparer(Preparer):
    def parse(self) -> str:
        return self.prefix + "=" + self.obj

class IntPreparer(Preparer):
    def parse(self) -> str:
        return self.prefix + "=" + str(self.obj)

class PreparerFactory:
    def get_preparer(self, obj, prefix: str = "") -> Preparer:
        if isinstance(obj, dict):
            return DictPreparer(obj, prefix)
        elif isinstance(obj, list):
            return ListPreparer(obj, prefix)
        elif isinstance(obj, str):
            return StrPreparer(obj, prefix)
        elif isinstance(obj, int):
            return IntPreparer(obj, prefix)

        raise Exception(f"type {type(obj)} have not been supported yet")