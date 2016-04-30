- Expires(Response Headers)
  - An absolute expiration time
- Cache-Control(Response Headers)
  - A relative period to the client time
  - Cache-Control: 3600


- Last-Modify(Response Headers)
  - The first time the browser requests this resource
- If-Modify-Since(Request Headers)
  - From 2nd request onwards to the same resource, this option will be included in the Request Headers
  - Server will check whether can use the cache according to this option
    - If can use cache, then return http304, and no `Last-Modify` option in the `Response Headers`



- Etag(Response Headers)
  - It is a validation code
- If-None-Match(Request Headers)
- ETag is generated according to the following factors:
  - i-node
  - file last modified time on server
  - file size

- Use resource version to control the browser cache behaviour


