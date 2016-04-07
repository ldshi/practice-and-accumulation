- How the '+, -, *, /' will perform when you try to use them between different types in JavaScript

  ```
  console.log('test' + true)  ->  testtrue

  console.log('test' + 1)  ->  test1

  console.log('test' + true + false)  ->  testtruefalse

  console.log('test' + true - false)  ->  NaN

  console.log(true + true)  ->  2

  console.log(true - true)  ->  0

  console.log(false - false)  ->  0

  console.log(false - true)  ->  -1

  console.log(true * true)  ->  1

  console.log(true / true)  ->  1

  console.log(true / false)  ->  Infinity

  console.log('test')
  console.log('test\n')
  console.log('test\n\n')
  The behaviour of 1st one and 2nd one are same, but the 3rd one do will produce an extra blank line after the 'test'.
  ```


