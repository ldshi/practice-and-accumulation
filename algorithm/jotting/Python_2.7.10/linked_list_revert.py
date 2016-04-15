class Node(object):
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next

linked_list_0 = Node(0, Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9))))))))))

def revert(head):
  if not head or not head.next:
    return head

  pre_node = None
  next_node = None

  while head:
    next_node = head.next
    head.next = pre_node
    pre_node = head
    head = next_node

  return pre_node

def recursively_revert(head):
  if not head or not head.next:
    return head

  new_head = recursively_revert(head.next)

  head.next.next = head
  head.next = None

  return new_head

def print_linked_list(head):
  tmp_node = head

  while tmp_node:
      print tmp_node.data

      tmp_node = tmp_node.next



print_linked_list(linked_list_0)

reverted_linked_list_0 = revert(linked_list_0)

print_linked_list(reverted_linked_list_0)

reverted_reverted_linked_list_0 = recursively_revert(reverted_linked_list_0)

print_linked_list(reverted_reverted_linked_list_0)


