# Release Checklist

On release day, the following changes need to be made to the site:

- **Update [\_data/releases.yml](_data/releases.yml)**: Update versions, dates
- **Update [start.md](start.md)**: Verify prerequisites are correct and other information not in "selector"
- **Update [generate_selector.py](generate_selector.py)**: Update config settings for releases to generate new selector files
- **Update [\_includes/selector.html](_includes/selector.html)**: Update logic for "selector" to match current release offerings
- **Run codeblock below**: (from project's root directory) to update selector files
```sh
python generate_selector.py
```
- **Test site locally**: (from project's root directory) to verify updates and selector is working
```sh
bundle exec jekyll serve
```
- **File PR**: Submit PR with changes to [rapidsai/rapids.ai](https://github.com/rapidsai/rapids.ai) repo and verify/review site preview with Netlify
