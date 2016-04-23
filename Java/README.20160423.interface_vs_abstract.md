- Interface
  - An interface **is a contract, an empty shell**, there are only the signatures of the methods, which implies that the methods do not have a body. The interface can't do anything. It's just a pattern.

  - Implementing an interface consumes very little CPU, because it's not a class, just a bunch of names, and therefore there is no expensive look-up to do. It's great when it matters such as in embedded devices.

    - On some dynamic languages, if you use an interface, the interpretter will just check if the class complies to the implementation. On abstract classes, it will setup the whole inheritence mecanisme, including what you need to find out the Method Resolution Order. If you create a lot of objects, it's an overhead. Not a bit one, but depending of your requirements, you may want to take it into considerations.

  - A class can implement multiple interfaces.

- Abstract Class
  - Abstract classes, unlike interfaces, are classes. They are more expensive to use because there is a look-up to do when you inherit from them.

  - Abstract classes look a lot like interfaces, but they have something more : you can define a behavior for them. It's more about a guy saying, "these classes should look like that, and they have that in common, so fill in the blanks!".

  - Java single inheritance.

- But
  - With Java 8, you can define default methods in interfaces which is the equivalent of having non-abstract methods in abstract classes. With this addition, I can no longer see the real difference between abstract classes and interface besides the fact that I should use interfaces because classes can implement multiple interfaces but can only inherit one class.

- Implementation
  - ~~While abstract classes and interfaces are supposed to be different concepts, the implementations make that statement sometimes untrue. Sometimes, they are not even what you think they are.~~

  - In Java, this rule is strongly enforced, while in PHP, interfaces are abstract classes with no method declared. 

  - ~~In Python, abstract classes are more a programming trick you can get from the ABC module and is actually using metaclasses, and therefore classes. And interfaces are more related to duck typing in this language and it's a mix between conventions and special methods that call descriptors (the \_\_method\_\_ methods).~~

  - As usual with programming, there is theory, practice, and practice in another language :-)

- [Refer to link](http://stackoverflow.com/questions/1913098/what-is-the-difference-between-an-interface-and-abstract-class)


