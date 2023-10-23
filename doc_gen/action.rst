GitHub Action
=============

Configuration MetaData
----------------------
- ``none-shall-pass`` includes a GitHub action config metadata, that includes various input parameters that allow users to customize the behavior of the action according to their needs.
- The ``owner`` and ``repo`` inputs are optional and can be used to specify the owner/organization and repository name.
- The ``fail`` input is optional and controls whether the action will fail if broken links are found.
- The ``debug`` input is also optional and can be used to enable debugging, providing more detailed information about the validation process.
- Default values are provided for all the inputs, allowing the action to work seamlessly in common use cases.

Docker Setup
------------
- Containerization enhances the action's portability and isolates it from external dependencies.
- The ``Dockerfile`` sets up the container environment for the GitHub Action.
- It uses the python 3.11-alpine base image.

Validator
---------
- ``validator.py``, is responsible for hyperlink validation in Markdown files.
- It accepts inputs provided as command-line arguments.
- The script extracts hyperlinks from Markdown content, validates them concurrently using multithreading, and logs the validation results.
- It can differentiate between local Markdown files and Wiki pages within the repository, expanding its validation scope.
