- How do I commit case-sensitive only filename changes in Git?

  ```
  git config core.ignorecase false
  ```
  - [git config documentation](https://jk.gs/git-config.html)
  - [git mv](http://stackoverflow.com/questions/8904327/case-sensitivity-in-git)
  - [How to remove a directory in my GitHub repository?](http://stackoverflow.com/questions/6313126/how-to-remove-a-directory-in-my-github-repository)

- How to solve the problem when you just change the case sensitivity in one folder name, but after push on GitHub you got like 'SQL' and 'sql' at the same time?

  ```
  git mv SQL/ SQL_weird
  git rm -r sql
  git add -A
  git mv SQL_weird/ SQL
  git add -A
  git status
  git commit -a -m "bla bla..."
  ```


  