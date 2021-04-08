class CustomObject:
    items = {}
    tracker = []
    idle = False

    def add(self, k, v):
        if self.idle:
            return
        self.items[k] = v
        self._update_tracker(k)

    def remove(self, k):
        if self.idle:
            return
        v = self.get(k)
        try:
            del self.items[k]
        except KeyError:
            pass
        return v

    def get(self, k):
        if self.idle:
            return
        try:
            value = self.items[k]
            self._update_tracker(k)
        except KeyError:
            value = '-1'
        return value

    def evict(self):
        if self.idle:
            return
        if self.tracker:
            self.remove(self.tracker[0])

    def exit(self):
        self.idle = True

    def _update_tracker(self, k):
        try:
            self.tracker.remove(k)
        except ValueError:
            pass
        self.tracker.append(k)


def solution(n):
    result = []
    custom_obj = CustomObject()
    for l in n:
        o_list = l.split(' ')
        params = o_list[1:]
        try:
            f_call = getattr(custom_obj, o_list[0])
            v = f_call(*params)
            if v:
                result.append(v)
        except AttributeError:
            pass
        except TypeError:
            pass
    return result
