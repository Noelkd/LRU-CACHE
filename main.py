
class LRUCACHE:
    def __init__(self, capacity) -> None:
        self.queue = []
        self.look_up = {}
        self.que_len = 0
        self.capacity = capacity
   
    def set(self, key, value):
        if self.que_len >= self.capacity:
            rkey, rvalue = self.queue.pop(0)
            self.look_up.pop(rkey, None)
            self.que_len -= 1
        self.look_up[key] = value
        self.queue.append((key, value))
        self.que_len += 1
        return self.queue
    
    def get(self, key):
        try:
            return self.look_up[key]
        except KeyError:
            return None





if __name__ == "__main__":
    cache = LRUCACHE(2)
    print(cache.set(1,2))
    print(cache.set(2,3))
    print(cache.set(1,5))
    print(cache.set(4,5))
    print(cache.set(6,7))
    print(cache.get(4))
    print(cache.set(1,4))
    print(cache.get(3))