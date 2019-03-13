# [STAGING] RAPIDS.ai Jekyll Site

## Overview

This is a STAGING repo for all changes that will push to PROD aka https://rapids.ai

**All changes for PROD** go through this repo and the [deployment process](#deployment-process) outlined below.

### Jekyll conversion

This is a conversion of the original rapids.ai site to use Jekyll allowing for use of Markdown instead of all HTML. With Jekyll we can make posts and also mix HTML and Markdown with eachother. In addition, we can template and reuse a lot of the coding and formatting of elements as snippets. This will make things much easier to change and add in the future.


### Setting up local development

Follow the [guide](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/) to setup a local Jekyll environment that will build and host the site locally. This is especially useful in debugging issues as GitHub will not give details when a deployment fails, only that it has.

This is also helpful as you're able to spot errors and issues more easily.

### Submitting PRs

Once your changes are ready in your fork, create a [new pull request](https://github.com/rapidsai/rapidsai-staging/compare) to start the [deployment process](#deployment-process).

### Other resources

- [Jekyll Tutorial](https://jekyllrb.com/docs/step-by-step/01-setup/) - shows core componets that we use in the site
- [Jekyll Cheatsheet](https://learn.cloudcannon.com/jekyll-cheat-sheet/)

## Deployment process

1. Submit proposed changes as a PR to this repo from the contributor's fork
2. Review PR providing feedback and request any necessary changes
3. Approve PR merging into `master` of this repo
4. Verify the staging site https://rapidsai.github.io/rapidsai-staging/ to ensure there are no errors or issues after merge
5. Approve promotion to PROD 
   - This is done through a CI process that merges `master` of this repo into the PROD repo and updates the `_config.yml` to match PROD
6. Verify PROD site updated
