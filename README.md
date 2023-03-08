# <div align="left"><img src="https://rapids.ai/assets/images/rapids_logo.png" width="90px"/> &nbsp; [RAPIDS.ai](https://rapids.ai.com) Website

Code and content for the [RAPIDS.ai](https://rapids.ai) static public website. This is a refactor from the previous Jekyll backed version. It uses the [Apline.js](https://alpinejs.dev/start-here) and [Bulma](https://bulma.io/) frameworks. No builds necessary. 


## Design and Layout
Use the [Template Design Guide](template.html) and [RAPIDS Brand Guide](brand.html) for reference while updating, and the [Blank Page](blank.html) for starting new pages. Dynamically loaded pages are located in the [Includes Folder](/includes).

Refer to the [Bulma Documentation](https://bulma.io/documentation/) for reference to the CSS class names and components. Note: many css classes are overwritten through `custom.css`. 
- [Column System](https://bulma.io/documentation/columns/basics/)
- [Container Class](https://bulma.io/documentation/layout/container/)
- [Spacing, Margin, and Padding Helpers](https://bulma.io/documentation/helpers/spacing-helpers/)

### Requirements
Each page MUST include the templates for `<nav></nav>` from the [Nav html](includes/nav.html), and `<footer></footer>` from the [Footer html](includes/footer.html). The latter two must be dynamically included via Apline.js as shown in the template. Most pages also should have the 'hero' header section. 

All logos and images are located in the [images](/images) folder. Externally referenced files should be placed in the [assets](/assets) folder.

Font Icons are used from [Font Awesome](https://fontawesome.com/), and include Pro account icons.


## Deployment and Contributions
Hosting is currently done statically with GitHub Pages using the root `gh-pages` branch. To contribute, [fork the repository](https://github.com/rapidsai/rapids.ai/fork) and create a [pull request](https://github.com/rapidsai/rapids.ai/pulls) with the changes. Note, to have a preview of the PR via `https://{username}.github.io/{repository}`, you would need to use the `gh-pages` branch to have it build through GitHub Pages defaults.
