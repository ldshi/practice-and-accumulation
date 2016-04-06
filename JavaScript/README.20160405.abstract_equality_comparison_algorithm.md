- Implicit data type conversion in JavaScript when comparing integer with string using ==
  ```
  console.log('1' == 1)  ->  true
  console.log('2' == 2)  ->  true
  console.log('' == 0)   ->  true
  console.log(1 == {toString: null})  ->  TypeError!
  ```
  - [Implicit data type conversion in JavaScript when comparing integer with string using ==](http://stackoverflow.com/questions/7625144/implicit-data-type-conversion-in-javascript-when-comparing-integer-with-string-u)

  - [11.9.3 The Abstract Equality Comparison Algorithm # Ⓣ ](http://es5.github.io/#x11.9.3)

- What is the difference between "==" and "==="
  - The only difference between them is that == will do type coercion to try to get the values to match, and === won't. So for instance "1" == 1 is true, because "1" coerces to 1. But "1" === 1 is false, because the types don't match. ("1" !== 1 is true.) The first (real) step of === is "Are the types of the operands the same?" and if the answer is "no", the result is false. If the types are the same, it does exactly what == does.
  - For type coercion, refer to:
    - [Abstract Equality Comparison(==, also called "loose" equality)](http://www.ecma-international.org/ecma-262/6.0/index.html#sec-abstract-equality-comparison)
    - [Strict Equality Comparison(===)](http://www.ecma-international.org/ecma-262/6.0/index.html#sec-strict-equality-comparison)


