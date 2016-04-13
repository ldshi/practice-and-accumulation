- **FIRST**
  - **Don't always think it is 'parent class' when 'super' is mentioned!!!**
  - **Actually 'super' is refered to the next class in the MRO(Method Resolution Order)**
  - **MRO: Method Resolution Order, it standards for the order how the classes are inherited.**

- What does 'super' in Python do?

  ```
    def super(cls, inst):
      mro = inst.__class__.mro()
      return mro[mro.index(cls) + 1]
  ```
  - The **inst** takes in charge of generating the MRO list
  - The cls locates where it is in the MRO, then return mro[index + 1]

  - Take the following code as example:

    ```
      class Root(object):
        def __init__(self):
          print('this is root')

      class B(Root):
        def __init__(self):
          print('enter B')
          super(B, self).__init__()
          print('leave B')

      class C(Root):
        def __init__(self):
          print('enter C')
          super(C, self).__init__()
          print('leave C')

      class D(B, C):
        pass

      d = D()

      print(d.__class__.__mro__)
    ```
  - The output will be:

    ```
      enter B
      enter C
      this is root
      leave C
      leave B
      (<class 'D'>, <class 'B'>, <class 'C'>, <class 'Root'>, <class 'object'>)
    ```

  - **Think about the above output order very carefully**


