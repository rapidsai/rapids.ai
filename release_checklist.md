# Release Checklist

On release day, the following changes need to be made to the site:

- **Update [\_data/releases.yml](_data/releases.yml)**: Update versions, dates
- **Update [start.md](start.md)**: Verify prerequisites are correct and other information not in selector
- **Update [\_includes/selector.html](_includes/selector.html)**: Update the following:
  - Links to recent & important RAPIDS Notices before selector
  - Selector JS logic to match current release offerings
- **Test site locally**: (from project's root directory) to verify updates and selector is working
```sh
bundle exec jekyll serve
```
- **File PR**: Submit PR with changes to [rapidsai/rapids.ai](https://github.com/rapidsai/rapids.ai) repo and verify/review site preview with Netlify
