[![made-with-gha](https://img.shields.io/badge/Made%20with-Github_Actions-black?style=for-the-badge&logo=GitHub)][marketplace]

# None Shall Pass

`none-shall-pass` is a GitHub action designed to identify and flag any broken links
within markdown files in your repository and wiki pages.

## Install Guide

### Add `none-shall-pass` action to your build workflow

- In your GitHub repository, select the Actions tab and either add or edit a workflow.
- Search for `none-shall-pass` from the [Marketplace][marketplace] tab on the right.
- Copy and paste the yaml into your workflow.

![marketplace][screenshot]

Copy & paste the following workflow definition into your project `.github/workflows/none-shall-pass.yml`

```yaml
# This workflow checks out code and scans the hyperlinks in 
# markdown files for broken links

name: Validate hyperlinks in markdown files

on:
  push:
  workflow_dispatch:

jobs:
  none-shall-pass:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: thevickypedia/none-shall-pass@v1.0.6
```

- Commit your changes to trigger the workflow or run the workflow manually.

### Action configuration options

Use the options below to configure debug and fail state when broken links are found in the repository/wiki pages.

| option  | requirement | description                                                                                                                                              |
|---------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `owner` | optional    | Owner/Organization of the repository - Defaults to current owner/org name                                                                                |
| `repo`  | optional    | Name of the repository - Defaults to current repository's name                                                                                           |
| `fail`  | optional    | If `true` (Default) the build is failed if broken links are found.<br/>If `false` the build completes successfully and warnings are provided in the logs |
| `debug` | optional    | If `true` (Default is `false`) debug level logging is enabled                                                                                            |


## [Release Notes][release-notes]
**Requirement**
```shell
python -m pip install gitverse
```

**Usage**
```shell
gitverse-release reverse -f release_notes.rst -t 'Release Notes'
```

## License & copyright

&copy; Vignesh Rao

Licensed under the [MIT License][license]

[marketplace]: https://github.com/marketplace/actions/none-shall-pass
[screenshot]: https://raw.githubusercontent.com/thevickypedia/none-shall-pass/main/images/marketplace.png
[license]: https://github.com/thevickypedia/none-shall-pass/blob/main/LICENSE
[release-notes]: https://github.com/thevickypedia/none-shall-pass/blob/main/release_notes.rst
