#
## python --version -> Python 2.7.10
#

#
# Find one possible root node.
#
def find_1_root(A, B):
  for node in A:
    if node not in B:
      return node

#
# Build the initial full multi-way tree.
#
def build_initial_tree(root, A, B):
  tree = {}

  tmp_start_nodes = [root]
  while len(tmp_start_nodes) > 0:

    tmp_end_nodes = []
    tmp_idx = len(A) - 1
    while tmp_idx >= 0:
      if A[tmp_idx] == tmp_start_nodes[0]:
        tmp_end_nodes.append(B[tmp_idx])
        del A[tmp_idx]
        del B[tmp_idx]
      tmp_idx -= 1

    if len(tmp_end_nodes):
      tree[tmp_start_nodes[0]] = tmp_end_nodes

    del tmp_start_nodes[0]
    tmp_start_nodes += tmp_end_nodes

  return tree

#
# Fin one possible longest road in tree.
#
def find_longest_road(tree, root):

  tree_keys = tree.keys()

  #
  # 1. Use recursion strategy to check whether one choice is correct greedily
  # 2. 'res' parameter is quite important, coz you can't use recursion strategy in the 'for loop'.
  # 3. The 'find_n_nodes == 1' check making this method will return 'True' only for checking to get the longest road, that means: if the longest road
  #      is 6, if you try 5, then will return 'False'.
  # 4. But not exactly, if 'find_n_nodes = 3 < length_of_longest_road' but it happen to reach one leaf node, the method still will return 'True',
  #      this is why in the below method 'get_length_of_longest_road' test the value from the possibly greatest value. 
  #
  def greedy_checker(from_node, find_n_nodes, res):
    if from_node in tree_keys:
      find_n_nodes -= 1
      for from_node_item in tree[from_node]:
        greedy_checker(from_node_item, find_n_nodes, res)
    elif find_n_nodes == 1:
      res['is_right_choice'] = True

  #
  # 1. As explained in above '4', here should test from the possibly greatest value.
  # 2. Decided by the storing way, the highest tree is: one element standards for one exclusive level in the tree.
  #
  def get_length_of_longest_road():
    length_of_longest_road = len(tree) + 1
    while True:
      checker_res = {'is_right_choice': False}
      greedy_checker(root, length_of_longest_road, checker_res)
      if checker_res['is_right_choice']:
        break
      length_of_longest_road -= 1
    return length_of_longest_road

  length_of_longest_road = get_length_of_longest_road()

  longest_road = [root]
  while True:
    if longest_road[-1] not in tree_keys:
      return longest_road

    for node in tree[longest_road[-1]]:
      checker_res = {'is_right_choice': False}
      greedy_checker(node, length_of_longest_road - len(longest_road), checker_res)
      if checker_res['is_right_choice']:
        longest_road.append(node)
        if len(longest_road) + 1 == length_of_longest_road:
          longest_road.append(tree[node][0])
          return longest_road

#
# After set one camera the tree will get split, get those split trees.
#
def split_tree(tree, root, road_start, road_end):
  trees = {}
  for key in tree.keys():
    if key == road_start and road_end in tree[key]:
      tree[key].remove(road_end)

    if key == road_end:
      new_tree = {}

      tmp_end_nodes = [key]
      while len(tmp_end_nodes):
        for node in tmp_end_nodes:
          if node in tree.keys():
            new_tree[node] = tree[node]

            del tree[node]

            tmp_end_nodes.remove(node)

            for inner_node in new_tree[node]:
              if inner_node in tree.keys():
                tmp_end_nodes.append(inner_node)


      trees[road_end] = new_tree

  if len(tree) == 1:
    tmp_root, tmp_tree = tree.popitem()
    if len(tmp_tree) == 0:
      return trees

  trees[root] = tree

  return trees



def solution(A, B, K):
  root = find_1_root(A, B)

  initial_tree = build_initial_tree(root, A, B)

  all_trees = {root: initial_tree}

  while K > 0:
    biggest_tree = {}
    for tree_root in all_trees.keys():
      if len(biggest_tree) == 0:
        biggest_tree[tree_root] = all_trees[tree_root]
      else:
        tmp_root, tmp_tree = biggest_tree.popitem()
        if len(all_trees[tree_root]) > len(tmp_tree):
          biggest_tree = {tmp_root: all_trees[tree_root]}
        else:
          biggest_tree = {tmp_root: tmp_tree}

    if biggest_tree:
      tmp_root, tmp_tree = biggest_tree.popitem()
      longest_road = find_longest_road(tmp_tree, tmp_root)

      tmp_middle = int(len(longest_road) / 2)
      trees = split_tree(tmp_tree, tmp_root, longest_road[tmp_middle - 1], longest_road[tmp_middle])

      del all_trees[tmp_root]
      all_trees.update(trees)

    K -= 1

    #
    # Here can check then return earlier:
    #   Lets say:
    #     1. K = 2
    #     2. The left longest road(biggest tree) is 3
    #     3. Have more than 2 trees like I described in '2'
    #     4. Then already can return 3.
    # But too tired, just let the procedure calculate.
    #

  result = 0
  for tree_root in all_trees.keys():
    tmp = len(all_trees[tree_root])
    if tmp and tmp > result:
      result = tmp

  return result


