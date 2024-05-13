Release Notes
=============

v4 (05/13/2024)
---------------
- Onboard command line interface creation kit in `none-shall-pass-rustic`

v3 (05/13/2024)
---------------
- Onboard none-shall-pass-rustic
- Remove Dockerfile and python dependencies
- Run scans via executable directly to reduce runtime
- Improves speed and accuracy

v2.0-prerelease-1698262793 (10/25/2023)
---------------------------------------
- Release v2.0
- Update docs

v2.0 (10/25/2023)
-----------------
- Includes option to allow users to specify the hostnames to be excluded despite broken links
- Includes bug fix for empty home page in GitHub wiki

v2.0a-prerelease-1698262370 (10/25/2023)
----------------------------------------
- Move argument assignment to main method

v2.0a-prerelease-1698261829 (10/25/2023)
----------------------------------------
- Get exclude hostnames as user input
- Handle an edge case scenario in subprocess errors
- Update README.md

v1.0.8-prerelease-1698201597 (10/24/2023)
-----------------------------------------
- Set commit message to prerelease notes
- Create steps for dedicated action in workflow
- Use a token identifier for exit code
- Bump version

v1.0.8 (10/24/2023)
-------------------
- Includes minor updates to prerelease
- Adds clear description on prerelease notes

v1.0.7-prerelease-1698176010 (10/24/2023)
-----------------------------------------
- Creating a pre-release [v1.0.7-prerelease-1698176010] for 1.0.7

v1.0.7 (10/24/2023)
-------------------
- Split validator into multiple modules
- Setup automatic prerelease

v1.0.6 (10/22/2023)
-------------------
- Improve logging

v1.0.5 (10/22/2023)
-------------------
- Includes bug fix for failing ``wiki`` scans
- Stability improvements by using ``requests`` module

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
