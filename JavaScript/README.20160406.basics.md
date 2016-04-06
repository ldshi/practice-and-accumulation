- Primitive value
  - Member of one of the types **Undefined**, **Null**, **Boolean**, **Number**, or **String**
  - A primitive value is a datum that is represented directly at the lowest level of the language implementation.

- undefined value
  - primitive value used when a variable has not been assigned a value.
- Undefined type
  - type whose sole value is the undefined value.

- null value
  - primitive value that represents the intentional absence of any object value.
- Null type
  - type whose sole value is the null value.

- **[What is the difference between the null and undefined?](http://stackoverflow.com/questions/5101948/javascript-checking-for-null-vs-undefined-and-difference-between-and)**
  - They're both values usually used to indicate the absence of something. undefined is the more generic one, used as the default value of variables until they're assigned some other value, as the value of function arguments that weren't provided when the function was called, and as the value you get when you ask an object for a property it doesn't have. But it can also be explicitly used in all of those situations.
  - There's a difference between an object not having a property, and having the property with the value undefined.
  - There's also a difference between calling a function with the value undefined for an argument, and leaving that argument off entirely.

  - **null is slightly more specific than undefined: It's a blank object reference.**
  - JavaScript is loosely typed, of course, but not all of the things JavaScript interacts with are loosely typed. If an API like the DOM in browsers needs an object reference that's blank, we use null, not undefined. 
  - And similarly, the DOM's getElementById operation returns an object reference — either a valid one (if it found the DOM element), or null (if it didn't).

    ```
    var test = document.getElementById('not_unexisting_dom_id')
    then test will be null
    ```

- Boolean value
  - member of the Boolean type.
- Boolean type
  - type consisting of the primitive values true and false.
- Boolean object
  - member of the Object type that is an instance of the standard built-in Boolean constructor.
  - A Boolean object is created by using the Boolean constructor in a new expression, supplying a Boolean value as an argument. The resulting object has an internal property whose value is the Boolean value. A Boolean object can be coerced to a Boolean value.

    ```
    var test = new Boolean(true);
    test
    Boolean {[[PrimitiveValue]]: true}
    ```

- String value
  - primitive value that is a finite ordered sequence of zero or more 16-bit unsigned integer.
- String type
  - set of all possible String values.
- String object
  - member of the Object type that is an instance of the standard built-in String constructor.

    ```
    var test = new String('Singapore')
    test
    String {0: "S", 1: "i", 2: "n", 3: "g", 4: "a", 5: "p", 6: "o", 7: "r", 8: "e", length: 9, [[PrimitiveValue]]: "Singapore"}
    ```

- Number value
  - primitive value corresponding to a double-precision 64-bit binary format IEEE 754 value.
- Number type
  - set of all possible Number values including the special “Not-a-Number” (NaN) values, positive infinity, and negative infinity.
- Number object
  - member of the Object type that is an instance of the standard built-in Number constructor.
- Infinity
  - Number value that is the positive infinite Number value.
- NaN
  - Number value that is a IEEE 754 “Not-a-Number” value.


