class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.next = self.right
        self.map = {}

    def length(self):
        return len(self.map)

    def pushRight(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node

    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            node.prev.next = node.next
            node.next.prev = node.prev
            del self.map[val]

    def popLeft(self):
        if self.length() == 0:
            return None
        leftmost = self.left.next
        self.pop(leftmost.val)
        return leftmost.val

from collections import defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCnt = 0
        self.valMap = {}  # Map key -> val
        self.countMap = defaultdict(int)  # Map key -> count
        # Map count of key -> linkedlist
        self.listMap = defaultdict(LinkedList)
        self.last_operation = f"Set capacity to {capacity}"

    def __repr__(self):
        listMap_repr = {k: [node.val for node in v.map.values()] for k, v in self.listMap.items()}
        return (
            f"LFUCache(\n"
            f"  last_operation = {self.last_operation}\n"
            f"  capacity={self.cap},\n"
            f"  lfuCnt={self.lfuCnt},\n"
            f"  valMap={self.valMap},\n"
            f"  countMap={dict(self.countMap)},\n"
            f"  listMap={listMap_repr},\n"
            
            f")"
        )

    def counter(self, key):
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt + 1].pushRight(key)

        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1

    def get(self, key: int) -> int:
        if key not in self.valMap:
            self.last_operation = f"Get {key} (not found)"
            return -1
        self.counter(key)
        self.last_operation = f"Get {key} (found)"
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            self.last_operation = "Put operation ignored (capacity 0)"
            return

        if key not in self.valMap and len(self.valMap) == self.cap:
            res = self.listMap[self.lfuCnt].popLeft()
            self.valMap.pop(res)
            self.countMap.pop(res)
            self.last_operation = f"Put {key}={value} (evicted {res})"
        else:
            self.last_operation = f"Put {key}={value}"

        self.valMap[key] = value
        if key not in self.countMap:
            self.countMap[key] = 0
        self.counter(key)
        self.lfuCnt = min(self.lfuCnt, self.countMap[key])

# Test cases to demonstrate the usage of LFUCache
def test_lfu_cache():
    cache = LFUCache(2)
    print(cache)

    cache.put(1, 1)
    print(cache)

    cache.put(2, 2)
    print(cache)

    print(cache.get(1))  # returns 1
    print(cache)

    cache.put(3, 3)  # evicts key 2
    print(cache)

    print(cache.get(2))  # returns -1 (not found)
    print(cache)

    print(cache.get(3))  # returns 3
    print(cache)

    cache.put(4, 4)  # evicts key 1
    print(cache)

    print(cache.get(1))  # returns -1 (not found)
    print(cache)

    print(cache.get(3))  # returns 3
    print(cache)

    print(cache.get(4))  # returns 4
    print(cache)

if __name__ == "__main__":
    test_lfu_cache()