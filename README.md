# [STAGING] RAPIDS.ai Jekyll Site

## Overview

This is a STAGING repo for all changes that will push to PROD aka https://rapids.ai

**All changes for PROD** go through this repo and the [deployment process](#deployment-process) outlined below.

### Jekyll conversion

This is a conversion of the original rapids.ai site to use Jekyll allowing for use of Markdown instead of all HTML. With Jekyll we can make posts and also mix HTML and Markdown with eachother. In addition, we can template and reuse a lot of the coding and formatting of elements as snippets. This will make things much easier to change and add in the future.

### Core site improvements

With the Jekyll change the following areas have been updated:

- [Home](https://rapidsai.github.io/rapidsai-staging/index.html) - [raw Markdown file](/index.md)
  - WIP on conversion to Markdown and templates
- [Documentation](https://rapidsai.github.io/rapidsai-staging/documentation.html) - [raw Markdown file](/documentation.md)
  - Fully converted to Markdown with code highlighting and sections mimicing original site design
- [Community](https://rapidsai.github.io/rapidsai-staging/community.html) - [raw Markdown file](/community.md)
  - WIP on conversion to Markdown and templates
  - Updated footer CTA boxes
  - Added new footer CTA boxes for Stack Overflow and Join RAPIDS with link to job board
- Site Footer - [html template](/_includes/footer.html)
  - Added icon and link for Stack Overflow

### Experimental feature examples

These examples are made possible by the new Jekyll site and can either be used in the production site or not.

- [Job Board](https://rapidsai.github.io/rapidsai-staging/jobs.html) - [raw Markdown file](/jobs.md) (uses new short header)
  - [Job Post](https://rapidsai.github.io/rapidsai-staging/job/2019/01/01/c-developers.html) - [raw Markdown file](/_posts/2019-01-01-c-developers.md)
- [Site Blog](https://rapidsai.github.io/rapidsai-staging/blog.html) - [raw Markdown file](/blog.md) (uses new short header)
  - [Jiwei's Converted Medium Post to Markdown](https://rapidsai.github.io/rapidsai-staging/blog/2019/01/15/make-sense-of-the-universe-with-rapids-ai.html) - [raw Markdown file](/_posts/2019-01-15-make-sense-of-the-universe-with-rapids-ai.md)

### TODO

Will create these as issues in the future, but wanted to capture where we are at the moment.

- [ ] - Finish converting elements of home page from HTML to Markdown and templates
- [ ] - Finish converting elements of community page from HTML to Markdown and templates
- [ ] - Condense CSS formatting
  - Original CSS was copy/pasted & customized for each page, with the templates we need to standardize this for consistency

## Contributing

To submit changes to the site use the guide below.

### Fork this repo

First thing is to fork this repo to your own userspace on GitHub. This will allow you to deploy the site and host a personal version as you work through the changes. In addition, this is how we accept PRs from you.

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
