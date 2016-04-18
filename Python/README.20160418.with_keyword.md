- Python's **with** statement is handy when you have two related operations which you’d like to execute as a pair, with a block of code in between. The classic example is opening a file, manipulating the file, then closing it:

  ```
  with open('output.txt', 'w') as f:
    f.write('Hi there!')
  ```

  - The above _with_ statement will automatically close the file after the nested block of code.
  - The advantage of using a _with_ statement is that it is guaranteed to close the file no matter how the nested block exits.
  - If an exception occurs before the end of the block, it will close the file before the exception is caught by an outer exception handler.
  - If the nested block were to contain a _return_ statement, or a _continue_ or _break_ statement, the _with_ statement would automatically close the file in those cases, too.


- [Example of implementing the Context Manager as a Class](http://preshing.com/20110920/the-python-with-statement-by-example/)

- [Example of implementing the Context Manager as a Generator](http://preshing.com/20110920/the-python-with-statement-by-example/)


