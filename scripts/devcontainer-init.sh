# SPDX-FileCopyrightText: Copyright (c) 2025, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

#!/bin/bash
set -euo pipefail

case $(arch) in
  "arm64"|"aarch64")
    arch="arm64"
    ;;
  "amd64"|"x86_64")
    arch="amd64"
    ;;
  *)
    echo "Unsupported architecture: $(arch)"
    exit 1
    ;;
esac

# Install Hugo version from `netlify.toml` file
mkdir -p ~/.local/bin
HUGO_VERSION=$(yq -oy '.build.environment.HUGO_VERSION' netlify.toml)
wget "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-${arch}.tar.gz" -O - | \
    tar -xzvf - -C ~/.local/bin hugo

# Install Hugo Modules
hugo config

# Install NodeJS version from `.nvmrc` file
. "${NVM_DIR}/nvm.sh" --install
rm -rf node_modules
npm install

# Install the python libraries for get_medium.py
pip install requests xmltodict pyyaml
