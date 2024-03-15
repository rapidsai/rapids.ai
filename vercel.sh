#!/bin/bash
set -euo pipefail

USAGE="Usage:
  build:           vercel.sh
  install deps:    vercel.sh install
"
if [ $# -eq 0 ]; then
  CMD="build"
elif [ $# -eq 1 ]; then
  CMD="$1"
else
  echo "${USAGE}"
  exit 1
fi

INSTALL_PREFIX="/usr/local"
export PATH="${PATH}:${INSTALL_PREFIX}/go/bin"

install_dependencies() {
  if [ -z "${VERCEL:-}" ]; then
    echo "Not in Vercel, skipping install. Devcontainer already has everything installed."
    return
  fi

  echo "installing npm dependencies"
  npm install

  echo "installing hugo"
  # TODO: move hugo version to its own file so it can be easily parsed by devcontainer
  # init scripts and renovate can update it.
  HUGO_VERSION="0.121.1"
  HUGO_URL="https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz"
  curl -sSL "${HUGO_URL}" | tar -zx -C "${INSTALL_PREFIX}/bin"

  echo "installing golang"
  LATEST_GO_VERSION=$(curl -sSL https://go.dev/VERSION?m=text| head -n 1)
  curl -sSL "https://dl.google.com/go/${LATEST_GO_VERSION}.linux-amd64.tar.gz" | \
    tar -zx -C "${INSTALL_PREFIX}"
  go version
}

build() {
  echo "printing env..."
  env | sort

  echo "building..."
  # TODO: disable draft building
  hugo --gc --minify --buildDrafts
  mkdir -p .vercel/output/
  node scripts/generate-vercel-config.mjs > .vercel/output/config.json
  cp -r public .vercel/output/static
}


case "${CMD}" in
  "install")
    install_dependencies
    ;;
  "build")
    build
    ;;
  *)
    echo "${USAGE}"
    exit 1
    ;;
esac
