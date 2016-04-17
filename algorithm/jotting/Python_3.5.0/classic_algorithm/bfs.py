'''
  [leonard@Leonards-Air ~/projects/practice-and-accumulation]$ python
  Python 3.5.0 (default, Mar 26 2016, 04:17:19) 
  [GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.29)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>> 
'''
import queue

graph = {
  'is_directed': False,
  'matrix': [
    [{'key': 0, 'val': 'V00'}, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, {'key': 1, 'val': 'V01'}, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, {'key': 2, 'val': 'V02'}, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, {'key': 3, 'val': 'V03'}, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, {'key': 4, 'val': 'V04'}, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, {'key': 5, 'val': 'V05'}, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, {'key': 6, 'val': 'V06'}, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, {'key': 7, 'val': 'V07'}, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, {'key': 8, 'val': 'V08'}, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, {'key': 9, 'val': 'V09'}, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, {'key': 10, 'val': 'V10'}]
  ]
}

def bfs(from_node):
  if from_node < 0 or from_node >= len(graph['matrix']):
    return

  q = queue.Queue()

  q.put(from_node)

  print(from_node)

  visited = [from_node]

  while not q.empty():
    node_key = q.get()
    for idx, val in enumerate(graph['matrix'][node_key]):
      if val == 1 and idx not in visited:
        q.put(idx)

        print(idx)

        visited.append(idx)



# bfs(0)

# bfs(4)

bfs(1)


