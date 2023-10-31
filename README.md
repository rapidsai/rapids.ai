# <div align="left"><img src="https://rapids.ai/assets/images/rapids_logo.png" width="90px"/> &nbsp; [RAPIDS.ai](https://rapids.ai.com) Website

This repository contains the source code and content for the [RAPIDS.ai](https://rapids.ai) website. The site uses [Hugo](https://gohugo.io/about/) for generating static HTML and [Bulma](https://bulma.io/) as a CSS framework. On occasion it uses [Apline.js](https://alpinejs.dev/start-here).


## Design and Layout

Refer to the [Bulma Documentation](https://bulma.io/documentation/) for reference to the CSS class names and components. Note: many CSS classes are overwritten through `custom.css`.
- [Column System](https://bulma.io/documentation/columns/basics/)
- [Container Class](https://bulma.io/documentation/layout/container/)
- [Spacing, Margin, and Padding Helpers](https://bulma.io/documentation/helpers/spacing-helpers/)

Hugo uses templates, layouts, and directories to build pages. The `/layouts/_defaults` folder contains `Baseof.html` for the root page chrome layout, followed by `section.html` for directory `_index.html` files, then `single.html` for sub pages. The `/layout/index.html` page is for the `/content/_index.html` page only, but still uses `Baseof.html` for chrome. Note: `partials` can only be used as part of template `layouts`, and `shortcodes` can only be used as part of `content` sections/pages. All in all, more complicated than it needs to be...


## Requirements

All logos and images are located in the [images](/static/images) folder. Externally (no website) referenced files should be placed in the [assets](/assets) folder.

Font Icons are used from [Font Awesome](https://fontawesome.com/), and include Pro account icons.

In the future it will employ the more optimized assets and Hugo pipe features.

## Pull Request Previews

[Netlify](https://www.netlify.com/) will create a preview environment when PRs are opened.

## Contributing

You can use the included devcontainer for local development.

Start the container and run `hugo serve` to start a development server.

The development server can be viewed in a browser at <http://localhost:1313>.