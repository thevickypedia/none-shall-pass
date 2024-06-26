[![made-with-gha](https://img.shields.io/badge/Made%20with-Github_Actions-black?style=for-the-badge&logo=GitHub)][marketplace]

[![pages](https://github.com/thevickypedia/none-shall-pass/actions/workflows/pages/pages-build-deployment/badge.svg)][pages]

# None Shall Pass

`none-shall-pass` is a GitHub action designed to identify and flag any broken links
within markdown files in your repository and wiki pages.

## Install Guide

#### Add `none-shall-pass` action to your build workflow

- In your GitHub repository, select the Actions tab and either add or edit a workflow.
- Search for `none-shall-pass` from the [Marketplace][marketplace] tab on the right.
- Copy and paste the yaml into your workflow.

**[OR]**

Copy & paste the following workflow definition into your project `.github/workflows/none-shall-pass.yml`

```yaml
name: Validate hyperlinks in markdown files

on:
  push:
  workflow_dispatch:

jobs:
  none-shall-pass:
    runs-on: ubuntu-latest  # Can run on multiple operating systems
    steps:
      - uses: thevickypedia/none-shall-pass@v5
```

- Commit your changes to trigger the workflow or run the workflow manually.

### Action configuration options

Use the options below to configure debug and fail state when broken links are found in the repository/wiki pages.

- `debug` - If `true` debug level logging is enabled. _Defaults to `false`_
- `owner` - Owner/Organization of the repository. _Defaults to current owner/org name_
- `repo` - Name of the repository. _Defaults to current repository's name_
- `excludeHostnames` - Space separated list of hostnames to ignore when failed. _Defaults to `""`_
- `failOnError` - If `true` (Default is `false`) the action will fail if broken links are found. _Defaults to `false`_

> `excludeHostnames` will perform a regex like lookup, so wildcards (*) are not required<br>

> To exclude any URL with `amazon`/`amzn` in it simply specify,<br>`excludeHostnames: "amazon amzn"`

## [Release Notes][release-notes]
**Requirement**
```shell
python -m pip install gitverse
```

**Usage**
```shell
gitverse-release reverse -f release_notes.rst -t 'Release Notes'
```

## [Docs][docs]
**Requirement**
```shell
pip install sphinx==5.1.1 sphinx-rtd-theme recommonmark requests
```

**Usage**
```shell
bash pre_commit.sh
```

## License & copyright

&copy; Vignesh Rao

Licensed under the [MIT License][license]

[marketplace]: https://github.com/marketplace/actions/none-shall-pass
[license]: https://github.com/thevickypedia/none-shall-pass/blob/main/LICENSE
[release-notes]: https://github.com/thevickypedia/none-shall-pass/blob/main/release_notes.rst
[docs]: https://thevickypedia.github.io/none-shall-pass/
[pages]: https://github.com/thevickypedia/none-shall-pass/actions/workflows/pages/pages-build-deployment
