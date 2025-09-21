[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AZ3VGVpk)
# LRU Image Cache (DLL + Dict)

## Story (why this matters)
Your app shows lots of thumbnails. Memory is limited, so you cache only the last
**K** items. When the cache is full, you evict the **least-recently used** (LRU).
This pattern powers real systems (browsers, DBs).

## Technical description (what to build)
In `src/lru_cache.py`, implement an **O(1)** LRU using:

- A dict: `key -> node`
- A doubly linked list with **sentinel** head/tail
  - Most-recent near **head**, least-recent near **tail**

APIs:
- `get(key)` → value or `None`; mark as **most-recent**
- `put(key, val)` → insert/update and, if over capacity, **evict LRU**

## Hints
1. Write helpers: `_add_front(node)`, `_remove(node)`, `_move_front(node)`, `_evict()`.
2. Sentinels (dummy head/tail) simplify edge cases.
3. On `get`, **move** the node to the front before returning.

## Run tests locally
```bash
python -m pytest -q

OR

python -m pytest -q tests/test_lru_cache.py
```

## Common problems
- Not moving a key to the front on get.

- Evicting the wrong node (LRU is the one before tail).

- Forgetting to update both prev and next when linking/unlinking.