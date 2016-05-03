```
def manual_iter():
  with open('/etc/passwd') as f:
    try:
      while True:
        line = next(f)
        print(line, end = '')
    except StopIteration:
      pass
```

```
with open('/etc/passwd') as f:
  while True:
    line = next(f, None)
    if line is None:
      break
    print(line, end = '')
```

```
>>> items = [1, 2, 3, 4]
>>> it = iter(items)
>>> next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
4
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> 
```

1. Create iterable object by simply using `iter` to implement the `__iter__` method

  ```
  class Node:
    def __init__(self, value):
      self._value = value
      self._children = []
          
    def __repr__(self):
      return 'Node({!r})'.format(self._value)
      
    def add_child(self, node):
      self._children.append(node)
    
    '''
      If you don't implement this method, and then try to use the `for in` or `iter`,
        you will get the following exception:
        
          Traceback (most recent call last):
          File "python", line 22, in <module>
          TypeError: 'Node' object is not iterable
    '''
    def __iter__(self):
      return iter(self._children)

  root = Node(0)
  child1 = Node(1)
  child2 = Node(2)
  root.add_child(child1)
  root.add_child(child2)

  # Outputs Node(1), Node(2)
  for ch in root:
    print(ch)
    
  it = iter(root)

  print(next(it))
  print(next(it))
  print(next(it))
  ```

2. Create your own generator by using `yield`

  ```
  def frange(start, stop, step):
    x = start
    while x < stop:
      yield x
      x += step

  for n in frange(0, 4, 0.5):
    print(n)

  list(frange(0, 1, 0.125))
  ```

  - More details about how `yield generator` works

    ```
    >>> def countdown(n):
    ...   print('Starting to count from:', n)
    ...   while n > 0:
    ...     yield n
    ...     n -= 1
    ...   print('Done!')
    ... 
    >>> c = countdown(3)
    >>> c
    <generator object countdown at 0x100de3a40>
    >>> next(c)
    Starting to count from: 3
    3
    >>> next(c)
    2
    >>> next(c)
    1
    >>> next(c)
    Done!
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration
    >>> 
    ```

3. Create a depth first travel generator on a tree

  ```
  class Node:
    def __init__(self, value):
      self._value = value
      self._children = []
          
    def __repr__(self):
      return 'Node({!r})'.format(self._value)
      
    def add_child(self, node):
      self._children.append(node)
    
    '''
      If you don't implement this method, and then try to use the `for in` or `iter`,
        you will get the following exception:
        
          Traceback (most recent call last):
          File "python", line 22, in <module>
          TypeError: 'Node' object is not iterable
    '''
    def __iter__(self):
      return iter(self._children)

    def depth_first(self):
      yield self
      for c in self:
        yield from c.depth_first()

  root = Node(0)
  child1 = Node(1)
  child2 = Node(2)
  root.add_child(child1)
  root.add_child(child2)
  child1.add_child(Node(3))
  child1.add_child(Node(4))
  child2.add_child(Node(5))

  for ch in root.depth_first():
    print(ch)

  # output
  Node(0)
  Node(1)
  Node(3)
  Node(4)
  Node(2)
  Node(5)
  ```

  - You also can implement your own `DepthFirstIterator` class(implement the __next__ method), but that will make things quite complex, and it is not necessary, about that details you can refer to page 115, 116 of book Python Cookbook 3rd Edition

4. reversed iterator

  ```
  a = [1, 2, 3, 4]
  for x in reversed(a):
    print(x)
  ```

  ```
  # You must convert it to a list first
  f = open('some_file')
  for line in reversed(list(f)):
    print(line, end = '')
  ```

  - Implement your own iterator by implementing the `__reversed__` method

    ```
    class Countdown:
      def __init__(self, start):
        self.start = start

      # Forward iterator
      def __iter__(self):
        n = self.start
        while n > 0:
          yield n
          n -= 1

      # Reversed iterator
      def __reversed__(self):
        n = 1
        while n <= self.start:
          yield n
          n += 1

    for rr in reversed(Countdown(30)):
      print(rr)

    for rr in Countdown(30):
      print(rr)
    ```

5. Let generator carry some more extra info/status.
  
  ```
  from collections import deque

  class LineHistory:
    def __init__(self, lines, history_len = 3):
      self.lines = lines
      self.history = deque(maxlen = history_len)

    def __iter__(self):
      for line_no, line in enumerate(self.lines, 1):
        self.history.append((line_no, line))
        yield line

    def clear(self):
      self.history.clear()

    with open('/tmp/test.txt') as f:
      lines = LineHistory(f)
      for line in lines:
        if 'Python' in line:
          for line_no, history_line in lines.history:
            print('{}:{}'.format(line_no, history_line), end = '')

    # Content of /tmp/test.txt
      # I am Leonard Shi.
      # I am trying to understand Python's iterator and generator more deeply.
      # I am looking for a new job.
      # I hope myself to be an advanced Python guy.
      # I'd like to do some data analysis or trading job.

  ```

  - Test

    ```
    >>> from collections import deque
    >>> class LineHistory:
    ...   def __init__(self, lines, history_len = 3):
    ...     self.lines = lines
    ...     self.history = deque(maxlen = history_len)
    ...   def __iter__(self):
    ...     for line_no, line in enumerate(self.lines, 1):
    ...       self.history.append((line_no, line))
    ...       yield line
    ...   def clear(self):
    ...     self.history.clear()
    ... 
    >>> with open('/tmp/test.txt') as f:
    ...   lines = LineHistory(f)
    ...   for line in lines:
    ...     if 'Python' in line:
    ...       for line_no, history_line in lines.history:
    ...         print('{}:{}'.format(line_no, history_line), end = '')
    ... 
    1:I am Leonard Shi.
    2:I am trying to understand Python's iterator and generator more deeply.
    2:I am trying to understand Python's iterator and generator more deeply.
    3:I am looking for a new job.
    4:I hope myself to be an advanced Python guy.
    >>> 
    ```


