---
title: Forward Mergers
linkTitle: Forward Mergers
description: Gateway to Questions
type: docs
weight: 10
---


## Overview

The forward mergers are automated pull requests to merge a branch in burndown into the next versioned branch. For example merging `branch-{{< rapids_version "stable" >}}` into `{{< rapids_version "nightly" >}}`. This ensures all changes to the current branch are reflected in the next version.

The forward merger jobs are located here: [https://gpuci.gpuopenanalytics.com/job/rapidsai/job/forward-mergers/](https://gpuci.gpuopenanalytics.com/job/rapidsai/job/forward-mergers/)

## Forward Mergers

During the release process, the branch for the next release is created and set as default. Once this happens, the forward-merger branch jobs are activated. Forward-mergers automatically merge any commits made to the release branch to the latest default branch during burn down.

**When Forward Merging Fails**

It is important to note that the forward-merge jobs will sometimes fail due to merge conflicts, and will request a manual merge to be done. *Never* use the GitHub Web UI to fix the merge conflicts as it will cause changes in the default branch to be merged into the release branch. Please use the following steps to fix the merge conflicts manually:

Using the example of `branch-{{< rapids_version "stable" >}}` release branch and a new default `branch-{{< rapids_version "nightly" >}}`.

```sh
git checkout branch-{{< rapids_version "stable" >}}
git pull <rapidsai remote>
git checkout branch-{{< rapids_version "nightly" >}}
git pull <rapidsai remote>
git checkout -b branch-{{< rapids_version "nightly" >}}-merge-{{< rapids_version "stable" >}}
git merge --no-squash branch-{{< rapids_version "stable" >}}
# Fix any merge conflicts caused by this merge
git commit -am "Merge branch-{{< rapids_version "stable" >}} into branch-{{< rapids_version "nightly" >}}"
git push <personal fork> branch-{{< rapids_version "nightly" >}}-merge-{{< rapids_version "stable" >}}
```

Once this is done, open a PR that targets the new default branch (`branch-{{< rapids_version "nightly" >}}` in this example) with your changes.

**IMPORTANT**: When merging this PR, do not use the [auto-merger]({{< relref "auto-merger.md" >}}) (i.e. the `/merge` comment). Instead, an admin must manually merge by changing the merging strategy to `Create a Merge Commit`. Otherwise, history will be lost and the branches become incompatible.

Once this PR is approved and merged, the original forward-merger PR should automatically be merged since it will contain the same commit hashes.
