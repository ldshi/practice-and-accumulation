'''
  [leonard@Leonards-Air ~/projects/practice-and-accumulation]$ python
  Python 3.5.0 (default, Mar 26 2016, 04:17:19) 
  [GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.29)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>> 
'''

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

def dfs(from_node, visited = []):
  if from_node < 0 or from_node >= len(graph['matrix']):
    return

  node_val = graph['matrix'][from_node][from_node]['val']

  print(node_val)

  visited.append(node_val)

  for idx, val in enumerate(graph['matrix'][from_node]):
    if val == 1 and graph['matrix'][idx][idx]['val'] not in visited:
      dfs(idx, visited)



# dfs(0)

# dfs(7)

# dfs(10)

dfs(3)


