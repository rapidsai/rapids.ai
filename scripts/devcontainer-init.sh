#!/bin/bash
set -euo pipefail

# Install Hugo version from `netlify.toml` file
mkdir -p ~/.local/bin
HUGO_VERSION=$(yq -oy '.build.environment.HUGO_VERSION' netlify.toml)
wget "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz" -O - | \
tar -xzvf - -C ~/.local/bin hugo

# Install Hugo/Go Modules
# Dependency versions repeated here due to: https://github.com/gohugoio/hugo/issues/11857.
# Once that is resolved, this command can be simplified to just:
# hugo mod get
hugo mod get github.com/google/docsy@v0.8.0

# Install NodeJS version from `.nvmrc` file
. "${NVM_DIR}/nvm.sh" --install
rm -rf node_modules
npm install
