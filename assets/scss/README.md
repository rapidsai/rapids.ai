# scss

This directory contains `.scss` files for the RAPIDS website.

All RAPIDS styles should go in the `rapidsai/` subdirectory.

The `rapidsai/*` subdirectory files can be imported in the `_styles_project.scss` file, which is used for adding additional styles to the Docsy theme as mentioned in their [documentation](https://www.docsy.dev/docs/adding-content/lookandfeel/).

In some cases, it may be necessary to override Docsy's default `.scss` files that are located [here](https://github.com/google/docsy/tree/v0.7.1/assets/scss). In these instances, the Docsy files can be copied directly into the `assets/scss` directory and modified as needed. This should be used as a last resort though, only after adding additional styles to the `rapidsai/` directory has been deemed insufficient.
