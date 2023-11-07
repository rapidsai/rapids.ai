#!/bin/bash
set -euo pipefail
HUGO_ENV=${HUGO_ENV:-staging}

hugo --gc --minify "$@"
cp _redirects public
