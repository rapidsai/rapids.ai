# Contributing

## Development Environment

Use the included devcontainer for local development.

Start the container and run `hugo serve` to start a development server.

To view draft files, run `hugo serve -D`.

The development server can be viewed in a browser at <http://localhost:1313>.

## Project Layout

This repository uses the [standard Hugo directory structure](https://gohugo.io/getting-started/directory-structure/).

Here are some general guidelines to follow:

- Site content should go in [content](./content/)
- HTML layouts (e.g. for landing pages) should go in [layouts](./layouts/)
- Section content (e.g. partners, announcements, docs, etc.) should include an archetype template in [archetypes](./archetypes/) (see section on archetypes below)
- Global assets (e.g. CSS, JavaScript, images used in more than one location, etc.) should go in [assets](./assets/)
  - Page-specific assets should be alongside the page itself in the [content](./content/) directory

## Using Archetypes to Generate New Content

Hugo [archetypes](https://gohugo.io/content-management/archetypes/) provide a template for creating new content.

Once an archetype template is created, it can be used like this:

```sh
# Create a new partner
hugo new _partners/dask

# Create a new announcement
hugo new announcements/cuda-12-deprecation
```

## Pull Request Previews

[Netlify](https://www.netlify.com/) will create a preview environment when PRs are opened.

## Using pre-commit hooks

This repository uses [pre-commit](https://pre-commit.com/) to execute all code linters and
formatters. These tools ensure a consistent code format throughout the project. Using pre-commit
ensures that linter versions and options are aligned for all developers. Additionally, there is a CI
check in place to enforce that committed code follows our standards.

To use `pre-commit`, install via `conda` or `pip`:

```bash
conda install -c conda-forge pre-commit
```

```bash
pip install pre-commit
```

Then run pre-commit hooks before committing code:

```bash
pre-commit run
```

By default, pre-commit runs on staged files (only changes and additions that will be committed).
To run pre-commit checks on all files, execute:

```bash
pre-commit run --all-files
```

Optionally, you may set up the pre-commit hooks to run automatically when you make a git commit. This can be done by running:

```bash
pre-commit install
```

Now code linters and formatters will be run each time you commit changes.

You can skip these checks with `git commit --no-verify` or with the short version `git commit -n`.
