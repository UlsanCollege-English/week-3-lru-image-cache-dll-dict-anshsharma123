# src/lru_cache.py

class _Node:
    __slots__ = ("key", "val", "prev", "next")
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        assert capacity > 0
        self.cap = capacity
        self.map = {}
        # sentinels: head <-> ... <-> tail
        self.head = _Node("__H__", None)  # MRU side
        self.tail = _Node("__T__", None)  # LRU side
        self.head.next = self.tail
        self.tail.prev = self.head

    # --- internal helpers ---
    def _add_front(self, node):
        """Insert node right after head (most recent position)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node):
        """Unlink node from the list."""
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None

    def _move_front(self, node):
        """Move an existing node to most recent position."""
        self._remove(node)
        self._add_front(node)

    def _evict(self):
        """Remove least recently used node (before tail)."""
        lru = self.tail.prev
        if lru is self.head:
            return
        self._remove(lru)
        del self.map[lru.key]

    # --- public API ---
    def get(self, key):
        if key not in self.map:
            return None
        node = self.map[key]
        self._move_front(node)
        return node.val

    def put(self, key, val):
        if key in self.map:
            node = self.map[key]
            node.val = val
            self._move_front(node)
        else:
            node = _Node(key, val)
            self.map[key] = node
            self._add_front(node)
            if len(self.map) > self.cap:
                self._evict()
