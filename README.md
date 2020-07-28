# [PROD] RAPIDS.ai Jekyll Site

## Overview

This is the PROD repo for all changes for the https://rapids.ai

**All changes** go through this repo and the [deployment process](#deployment-process) outlined below

### Jekyll Markup

The content of this site is written in .md files and converted to html. Try to avoid using raw html and rely on the templates described below. Note, any css updates should use the `custom.css` and any code highlight updates should use the `highlight.css` files. 

### Templates, Includes, and Styles

Most content should use the `default` layout and include the top line page variables (an example can be see on index.md). Layouts use templates in the `_includes` folder. The default layout already includes the nav, header and footer. Using the templates will ensure that your content is **responsive** to various screen sizes and follows the **site design**.

Depending on the desired layout, a section heading may be outside or inside of the layout content. Refer to `index/about/start/community.md` for reference examples. The most useful templates are:

* section-single: 1x1 Row by Cols
* section-halfs: 1x2 Row by Cols
* section-double-halfs: 2x2 Row by Cols
* section-thirds: 1x3 Row by Cols
* section-double-thirds: 2x3 Row by Cols
* section-onethird-twothird: 1x2 Row by Cols (1/3 2/3)
* section-twothird-onethird: 1x2 Row by Cols (2/3 1/3)

#### Sections
Section content is generally formatted as follows, but be sure to view the html file for the exact capture variable names to pass to the include. Background can be: `background-white / background-gray / background-purple / background-darkpurple.` Padding-top and padding-bottom can be: `0 / 1 / 2`. To get the diagonal background effect, you must include `slopecap`, for both the top and bottom of a section. Position can be `top / bottom` and slope can be `up / down`. Section-thirds has a Banner option that can be: blank or `banner-row`. Exact formatting might require some tinkering...

```
{% capture name_left %}

CONTENT

{% endcapture %}
{% capture name_right %}

CONTENT

{% endcapture %}
{% include slopecap.html 
    background="background-purple" 
    position="top" 
    slope="up" 
%}
{% include section-halfs.html 
    background="background-purple" 
    padding-top="1" padding-bottom="1" 
    content-left-half=name_left 
    content-right-half=name_right 
%} 
{% include slopecap.html 
    background="background-purple" 
    position="bottom" 
    slope="up" 
%}

```
#### Links
Links should use the following format, with `_target` being unnecessary if the link is within rapids.ai: 
```
**[NAME <i FONT-AWEOME-ICON"></i>](LINK){: target="_blank"}**
```

#### Font Icons
Font Awesome Icons are fun, but use them accordingly. They are one of the few exceptions to including in line HTML. See the [free gallery here](https://fontawesome.com/icons?d=gallery&m=free).

#### Twitter and Medium 
Twitter and Medium sections content are updated from the `post.json` file posted the `postsurl` repo specified in `_config.yml`, which is updated a few times a day with an external job. 


### Experimental feature examples

These examples are made possible by the new Jekyll site and can either be used in the production site or not.

>**NOTE:** With the merge of PROD & STAGING the links below do not work as they have been hidden.

- [Job Board](https://rapidsai.github.io/rapids.ai/jobs.html) - [raw Markdown file](/jobs.md) (uses new short header)
  - [Job Post](https://rapidsai.github.io/rapids.ai/job/2019/01/01/c-developers.html) - [raw Markdown file](/_posts/2019-01-01-c-developers.md)
- [Site Blog](https://rapidsai.github.io/rapids.ai/blog.html) - [raw Markdown file](/blog.md) (uses new short header)
  - [Jiwei's Converted Medium Post to Markdown](https://rapidsai.github.io/rapids.ai/blog/2019/01/15/make-sense-of-the-universe-with-rapids-ai.html) - [raw Markdown file](/_posts/2019-01-15-make-sense-of-the-universe-with-rapids-ai.md)

### TODO

Will create these as issues in the future, but wanted to capture where we are at the moment.

- [ ] Add featured section in blogs
- [ ] Add pagination to blogs
- [ ] Port over blogs


## Contributing

To submit changes to the site use the guide below.

### Fork this repo

First thing is to fork this repo to your own userspace on GitHub. This will allow you to deploy the site and host a personal version as you work through the changes. In addition, this is how we accept PRs from you.

### Setting up local development

Follow the [guide](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/) to setup a local Jekyll environment that will build and host the site locally. This is especially useful in debugging issues as GitHub will not give details when a deployment fails, only that it has.

This is also helpful as you're able to spot errors and issues more easily.

### Submitting PRs

Once your changes are ready in your fork, create a [new pull request](https://github.com/rapidsai/rapids.ai/compare) to start the [deployment process](#deployment-process).

### Other resources

- [Jekyll Tutorial](https://jekyllrb.com/docs/step-by-step/01-setup/) - shows core componets that we use in the site
- [Jekyll Cheatsheet](https://learn.cloudcannon.com/jekyll-cheat-sheet/)

## Deployment process

1. Submit proposed changes as a PR to this repo from the contributor's fork, targetting the `gh-pages` branch
2. Review PR providing feedback and request any necessary changes
3. Use the Netlify preview to test and verify the changes in the PR
4. Approve and merge PR into `gh-pages` of this repo
4. Verify site updated by visiting https://rapids.ai
