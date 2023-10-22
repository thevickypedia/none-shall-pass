Release Notes
=============

v1.0.4c (10/22/2023)
--------------------
- Suppress warnings from pip when run as root in Dockerfile

v1.0.4b (10/22/2023)
--------------------
- Use requests module to avoid ``forbidden`` errors
- Upgrade ``pip`` and install ``requests`` module in ``Dockerfile``

v1.0.4a (10/22/2023)
--------------------
- Install git in docker to run clone wiki pages successfully

v1.0.3 (10/22/2023)
-------------------
- Get owner and repo information via GitHub env
- Run action without any mandatory args
- Fix order of fail and debug flags during runtime

v1.0.1 (10/22/2023)
-------------------
- Scan for hyperlinks in markdown files and wiki pages
- Fail the action when hyperlink is unreachable
- Ignore hyperlinks that are amazon pages and localhost
