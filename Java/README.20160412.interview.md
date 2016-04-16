1. Compare keyword 'final', 'finally' and 'finalize' in Java
  - final
    - _final_ can be used to mark a variable "unchangeable".
    - _final_ can also make a method not "overrideable".
    - _final_ can also make a class not "inheritable". i.e. the class can not be subclassed.

  - finally
    - _finally_ is used in a try/catch statement to [execute code "always"](http://docs.oracle.com/javase/tutorial/essential/exceptions/finally.html)

        ```
        lock.lock();
        try {
          //do stuff
        } catch (SomeException se) {
          //handle se
        } finally {
          lock.unlock(); //always executed, even if Exception or Error or se
        }
        ```
      - Java 7 has a [new try with resources statement](http://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html) that you can use to automatically close resources that explicitly or implicitly implement [java.io.Closeable](http://docs.oracle.com/javase/7/docs/api/java/io/Closeable.html) or [java.lang.AutoCloseable](http://docs.oracle.com/javase/7/docs/api/java/lang/AutoCloseable.html)

  - finalize
    - _finalize_ is called when an object is garbage collected. You rarely need to override it. An example:

      ```
      protected void finalize() {
        //free resources (e.g. unallocate memory)
        super.finalize();
      }
      ```

2. What is variable, what is pointer?

3. Object vs Class

4. Programming skills test on paper.... then on a hard to use HP laptop in Ubuntu, fortunately I am quite familiar with nearly all kinds of Linux distributions.


