#!/bin/bash

# SPDX-FileCopyrightText: Copyright (c) 2025-2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

set -euo pipefail
HUGO_ENV=${HUGO_ENV:-staging}

hugo --gc --minify "$@"
cp _redirects public
