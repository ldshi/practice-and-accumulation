### The steps of a full OAuth_2.0 authentication process will be(take the Google Servers as the authentication servers):
  1. User try to login your server

  2. In this step
    - Your server send getting token request to Google(**the URL includes query parameters that indicate the type of access being requested**)
    - And at the same time redirect user to 'Google authentication page'(**Google handles the user authentication, session selection, and user consent**)
    - The result is an authorization code, which the application can exchange for an access token and a refresh token.
    - The application should store the refresh token for future use and use the access token to access a Google API. Once the access token expires, the application uses the refresh token to obtain a new one. 

  3. If the user grants the permission, the Google Authorization Server sends your application an access token (or an authorization code that your application can use to obtain an access token) with the **redirect_uri**. If the user does not grant the permission, the server returns an error.

  4. In this step
    - Then your server decide whether let the user go into the system
    - And at the same time use the **Authentication code** to exchange the access token and refresh token.

  5. In this step
    - Then your server can use the access token to access the corresponding resources
    - When the access token is expired, then use the refresh token to echange the new valid access token

  6. In this step
    - <img src="images/OAuth_2.0.png"/>


