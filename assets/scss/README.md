# scss

This directory contains SCSS files for the RAPIDS website.

## Special Files

There are two special files in this directory, listed below and described in the Docsy documentation [here](https://www.docsy.dev/docs/adding-content/lookandfeel/):

- `_variables_project.scss` - used for setting SCSS variables _before_ Bootstrap (which is used by Docsy) generates all of its classes. This is useful for modifying Bootstrap's generated classes according to their utility API docs [here](https://getbootstrap.com/docs/5.2/utilities/api/) or setting other customization variables as described [here](https://getbootstrap.com/docs/5.2/customize/overview/)
- `_styles_project.scss` - used for adding additional SCSS styles to the final generated stylesheet. These styles can use the generated Bootstrap styles based on the contents of `_variables_project.scss`

## Other Files

RAPIDS-specific styles should go in the `rapidsai/` subdirectory. These files can then be imported into the `_styles_project.scss` file.

Aside from the special files listed above, the root `assets/scss` directory is reserved for overriding SCSS files from the Docsy theme. In some cases, it may be necessary to override Docsy's default `.scss` files that are located [here](https://github.com/google/docsy/tree/v0.7.1/assets/scss). In these instances, the Docsy files can be copied directly into the `assets/scss` directory and modified as needed. This should be used as a last resort though, only after adding additional styles to the `rapidsai/` directory has been deemed insufficient.

## Conventions

Below is a list of conventions for authoring styles for the site. In the future, we can explore adding [StyleLint](https://stylelint.io/) to our devcontainer to help enforce rules.

- Avoid writing styles. Instead, leverage Bootstrap's utility classes whenever possible. Utility classes are configurable via their [utility API](https://getbootstrap.com/docs/5.2/utilities/api/). Reusable components can be created with Hugo by leveraging its shortcode functionality to avoid needing to repeat utility classes across multiple instances of the same component
- When it is necessary to create custom styles, use the following conventions:
  - Place the related styles in their own `.scss` file in the `rapidsai/*` directory. Import the newly created file in `rapidsai/_index.scss`
  - Use the [BEM](https://getbem.com/) naming convention to avoid naming collisions and promote consistent naming conventions
  - Avoid deep nesting with SCSS. Aim for no more than 1 level of nesting
  - Reserve nesting for pseudo-classes, psuedo-elements, and media query mixins
  - Use Bootstrap's built-in `media-breakpoint-up` ([docs](https://getbootstrap.com/docs/5.2/layout/breakpoints/#min-width)) mixin to generate consistent `min-width` media queries for a [mobile-first](https://zellwk.com/blog/how-to-write-mobile-first-css/) design approach
