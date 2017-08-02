class EntityList:
    def __init__(self, obj=None):
        self._objects = []
        if isinstance(obj, list):
            for innerObj in obj:
                self._objects.append(innerObj)
        elif obj is not None:
            self._objects.append(obj)

    def __len__(self):
        return self._objects.__len__()

    def __getitem__(self, item):
        return self._objects[item]

    def send_to_back(self, entity):
        self._objects.remove(entity)
        self._objects.insert(0, entity)

    def append(self, entity):
        self._objects.append(entity)

    def remove(self, entity):
        self._objects.remove(entity)
