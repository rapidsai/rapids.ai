#!/bin/bash
set -euo pipefail

# Install Hugo version from `netlify.toml` file
mkdir -p ~/.local/bin
HUGO_VERSION=$(yq -oy '.build.environment.HUGO_VERSION' netlify.toml)
wget "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz" -O - | \
tar -xzvf - -C ~/.local/bin hugo
