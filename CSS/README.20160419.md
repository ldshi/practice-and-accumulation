- Use `:not()` to Apply/Unapply Borders on Navigation

  ```
  .nav li:not(:last-child) {
    border-right: 1px solid #666;
  }
  ```

- Vertically-Center Anything

  ```
  html, body {
    height: 100%;
    margin: 0;
  }

  body {
    -webkit-align-items: center;  
    -ms-flex-align: center;  
    align-items: center;
    display: -webkit-flex;
    display: flex;
  }
  ```

- Comma-Separated Lists

  ```
  ul > li:not(:last-child)::after {
    content: ",";
  }
  ```

- Select Items Using Negative `nth-child`

  ```
  li {
    display: none;
  }

  /* select items 1 through 3 and display them */
  li:nth-child(-n+3) {
    display: block;
  }

  /* select items 1 through 3 and display them */
  li:not(:nth-child(-n+3)) {
    display: none;
  }
  ```

- Equal Width Table Cells
  - Tables can be a pain to work with so try using `table-layout: fixed` to keep cells at equal width:

    ```
    .calendar {
      table-layout: fixed;
    }
    ```

- Get Rid of Margin Hacks With Flexbox
  - When working with column gutters you can get rid of `nth-`, `first-`, and `last-child` hacks by using flexbox's `space-between` property:

    ```
    .list {
      display: flex;
      justify-content: space-between;
    }

    .list .person {
      flex-basis: 23%;
    }
    ```

- Use Attribute Selectors with Empty Links
  - Display links when the `<a>` element has no text value but the `href` attribute has a link:

    ```
    a[href^="http"]:empty::before {
      content: attr(href);
    }
    ```

- Style Broken Images
  - Make broken images more aesthetically-pleasing with a little bit of CSS:

    ```
    img {  
      display: block;
      font-family: Helvetica, Arial, sans-serif;
      font-weight: 300;
      height: auto;
      line-height: 2;
      position: relative;
      text-align: center;
      width: 100%;
    }
    ```
  - Now add pseudo-elements rules to display a user message and URL reference of the broken image:

    ```
    img:before {  
      content: "We're sorry, the image below is broken :(";
      display: block;
      margin-bottom: 10px;
    }

    img:after {  
      content: "(url: " attr(src) ")";
      display: block;
      font-size: 12px;
    }
    ```

- Use `rem` for Global Sizing; Use `em` for Local Sizing
  - After setting the base font size at the root (`html {font-size: 16px;}`), set the font size for textual elements to `em`:

    ```
    h2 { 
      font-size: 2em;
    }

    p {
      font-size: 1em;
    }
    ```
  - Then set the font-size for modules to `rem`:

    ```
    article {
      font-size: 1.25rem;
    }

    aside .module {
      font-size: .9rem;
    }
    ```

  - Now each module becomes compartmentalized and easier to style, more maintainable, and flexible.

- [Original source](https://github.com/AllThingsSmitty/css-protips)


