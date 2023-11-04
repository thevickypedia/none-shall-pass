#!/usr/bin/env bash
# 'set -e' stops the execution of a script if a command or pipeline has an error.
# This is the opposite of the default shell behaviour, which is to ignore errors in scripts.
set -e

docs_dir="docs"

mkdir -p $docs_dir  # Create a docs directory if unavailable

clean_docs() {
  local file_to_keep="CNAME"
  if [ -d "${docs_dir}" ]; then
    cd "${docs_dir}"
    if [ -e "${file_to_keep}" ]; then
      # Delete all files and directories except the file_to_keep
      for entry in *; do
        if [ "${entry}" != "${file_to_keep}" ]; then
          if [ -d "${entry}" ]; then
            rm -r "${entry}"
          else
            rm "${entry}"
          fi
        fi
      done
    else
      # If the file_to_keep doesn't exist, remove everything
      rm -rf *
    fi
    cd ../
  else
    echo "Docs directory not found: ${docs_dir}"
  fi
}

update_release_notes() {
  # Update release notes
  gitverse-release reverse -f release_notes.rst -t 'Release Notes'
}

gen_docs() {
  # Generate sphinx docs
  mkdir -p doc_gen/_static  # Create a _static directory if unavailable
  cp README.md doc_gen/
  cd doc_gen && make clean html  # cd into doc_gen and create the runbook
  mv _build/html/* ../docs  # Move the runbook
  cp theme.css ../docs/_static/theme.css  # Copy the theme.css file
  cd ../
}

clean_docs
gen_docs
update_release_notes

# The existence of this file tells GitHub Pages not to run the published files through Jekyll.
# This is important since Jekyll will discard any files that begin with _
touch docs/.nojekyll
