- Browser same origin policy
  - same protocol
  - same domain
  - same port

- Example: http://www.example.com/dir/page.html    is same origin?
  - http://www.example.com/dir2/other.html    YES
  - http://example.com/dir/other.html    NO (domain is different)
  - http://v2.www.example.com/dir/other.html    NO (domain is different)
  - http://www.example.com:81/dir/other.html    NO (port is different)

- Affected resource
  - Cookie, LocalStorage, IndexDB
  - DOM
  - Ajax request

- iframe is in different origin with its parent



- fragment identifier
  - The part in url after the character `#`
  - Example:
    - `http://example.com/x.html#fragment`  ->  #fragment
    - If only change the fragment part, will not cause the page refresh
  - Parent window can write some data into the children iframe window

    ```
    var src = originURL + '#' + data;
    document.getElementById('myIFrame').src = src;
    ```
  - Then children iframe can check the message by listening the `hashchange` event

    ```
    window.onhashchange = checkMessage;

    function checkMessage() {
      var message = window.location.hash;
      // ...
    }
    ```

  - Same to above, the children iframe window also can change the parent's fragment

- window.name

- window.postMessage

- LocalStorage

- AJAX
  - JSONP
  - WebSocket
  - CORS

- [Refer to link](http://mp.weixin.qq.com/s?__biz=MzIyMDEzMTA2MQ==&mid=2651147479&idx=1&sn=b39167f49dfe644a68556cb8238cd455&scene=0#wechat_redirect)


