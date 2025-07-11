#!/bin/bash
# SPDX-FileCopyrightText: Copyright (c) 2024-2025, NVIDIA CORPORATION & AFFILIATES.
# All rights reserved.
# SPDX-License-Identifier: Apache-2.0

## Usage
# bash ./ci/release/update-version.sh <new_version>

# Format is YY.MM.PP - no leading 'v' or trailing 'a'
NEXT_FULL_VERSION=$1

# Get <major>.<minor> for next version
NEXT_MAJOR=$(echo "$NEXT_FULL_VERSION" | awk '{split($0, a, "."); print a[1]}')
NEXT_MINOR=$(echo "$NEXT_FULL_VERSION" | awk '{split($0, a, "."); print a[2]}')

NEXT_SHORT_VERSION=${NEXT_MAJOR}.${NEXT_MINOR}

if [ "$NEXT_MINOR" -eq "02" ]; then
    CURRENT_MINOR="12"
    CURRENT_MAJOR=$((NEXT_MAJOR - 1))
else
    CURRENT_MINOR=$(printf "%02d" $((10#$NEXT_MINOR - 2)))
    CURRENT_MAJOR=$NEXT_MAJOR
fi

CURRENT_SHORT_VERSION=${CURRENT_MAJOR}.${CURRENT_MINOR}

# Need to distutils-normalize the versions
CURRENT_SHORT_VERSION_PEP440=$(python -c "from packaging.version import Version; print(Version('${CURRENT_SHORT_VERSION}'))")
NEXT_SHORT_VERSION_PEP440=$(python -c "from packaging.version import Version; print(Version('${NEXT_SHORT_VERSION}'))")

# Inplace sed replace; workaround for Linux and Mac
function sed_runner() {
    sed -i.bak ''"$1"'' "$2" && rm -f "${2}".bak
}

sed_runner "s|RAPIDS ${CURRENT_SHORT_VERSION}|RAPIDS ${NEXT_SHORT_VERSION}|g" "layouts/index.html"
sed_runner "s|branch-${CURRENT_SHORT_VERSION}|branch-${NEXT_SHORT_VERSION}|g" "layouts/index.html"
sed_runner "s|rapids-${CURRENT_SHORT_VERSION}|rapids-${NEXT_SHORT_VERSION}|g" "layouts/index.html"
sed_runner "s|rapids=${CURRENT_SHORT_VERSION}|rapids=${NEXT_SHORT_VERSION}|g" "layouts/index.html"
sed_runner "s|==${CURRENT_SHORT_VERSION_PEP440}\.\*|==${NEXT_SHORT_VERSION_PEP440}\.\*|g" "layouts/index.html"
