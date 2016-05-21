1. Convert to `Boolean` type

  ```
  !!'foo'
  ```

2. Convert `String` to `Number`

  ```
  +'45'           -> 45
  + '45'          -> 45
  +-'45'          -> -45
  + - '45'        -> -45
  2 + +'45'       -> 47
  2 + + '45'      -> 47
  2 + + - '45'    -> -43
  2 + + - + '45'  -> -43
  2 + + - - '45'  -> 47
  2 + + --'45'    -> VM442:1 Uncaught ReferenceError: Invalid left-hand side expression in prefix operation
  2 + + -- '45'   -> VM442:1 Uncaught ReferenceError: Invalid left-hand side expression in prefix operation
  ```

3. parseInt

  ```
  ~~4.98709898  -> 4
  ~4.98709898   -> -5
  ~~~4.98709898 -> -5
  +new Date()
  ```

  - How it works?
    - `~`: Binary Ones Complement Operator is unary and has the effect of 'flipping' bits.

4. Random color str

  ```
  (~~(Math.random() * (1 << 24))).toString(16);
  ```

  - But above code have flaws:
    - It has the chance to get the output like this: `c63f9` whent the Math.random gets `0 < result < 0.1`
    - How to fix?

      ```
      ('00000' + (0 | Math.random() * (1 << 24)).toString(16)).slice(-6);
      ```

      ```
      /**
       * Get a random floating point number between `min` and `max`.
       * 
       * @param {number} min - min number
       * @param {number} max - max number
       * @return {float} a random floating point number
       */
      function getRandom(min, max) {
        return Math.random() * (max - min) + min;
      }

      (~~(getRandom(0.1, 1) * (1 << 24))).toString(16);
      ```

- [1 - 4 come from this link](https://annatarhe.github.io/2016/04/19/hack-js-code.html)


