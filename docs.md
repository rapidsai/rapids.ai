---
title: "Technical Documentation, Docker Container | RAPIDS"
og_title: "RAPIDS Technical Documentation"
og_description: "Get started with RAPIDS. Find docker container details, download and installation details, and more."
brand_name: "DOCUMENTATION"
brand_tagline: "Getting started with RAPIDS"
brand_button: "DOWNLOAD CHEAT SHEET"
brand_link: "assets/files/cheatsheet.pdf"
layout: short
---
{% capture section_docs %}
## Contributing Guidelines

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg .tg-5ztr{font-weight:bold;background-color:#cbcefb;border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-c4ww{background-color:#cbcefb;border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-baqh{text-align:center;vertical-align:top}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-zv36{font-weight:bold;background-color:#ffffff;border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-fymr{font-weight:bold;border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-7btt{font-weight:bold;border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-3xi5{background-color:#ffffff;border-color:inherit;text-align:center;vertical-align:top}
</style>
[Dev Docs Home Page](https://rapidsai.github.io/devdocs/)<br><br>

<table class="tg">
  <tr>
    <th class="tg-5ztr">Community/Project Guidelines</th>
    <th class="tg-5ztr">Contributing Guidelines</th>
  </tr>
  <tr>
    <td class="tg-baqh">
      <ul>
        <li><a href="https://rapidsai.github.io/devdocs/docs/resources/conduct/">Code of Conduct</a><br></li>
        <li><a href="https://rapidsai.github.io/devdocs/docs/resources/changelog/">Changelog Format</a><br></li>
        <li><a href="https://rapidsai.github.io/devdocs/docs/resources/git/">Git Methodology</a><br></li>
        <li><a href="https://rapidsai.github.io/devdocs/docs/resources/style/">Style Guide</a><br></li>
        <li><a href="https://rapidsai.github.io/devdocs/docs/resources/versions/">Verisons and Tags</a></li>
      </ul>
    </td>
    <td class="tg-baqh">
      <ul>
        <li><a href="https://rapidsai.github.io/devdocs/docs/contributing/issues/">Issues</a><br></li>
        <li><a href="https://rapidsai.github.io/devdocs/docs/contributing/code/">Code Contributions</a><br></li>
        <li><a href="https://rapidsai.github.io/devdocs/docs/contributing/prs/">Pull Requests</a><br></li>
      </ul>
    </td>
  </tr>
</table>

## Useful Docs and Resources
<table class="tg">
  <tr>
    <th class="tg-5ztr"></th>
    <th class="tg-5ztr">cuML</th>
    <th class="tg-5ztr">cuDF</th>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:bold">Documentation</span></td>
    <td class="tg-baqh"><a href="https://rapidsai.github.io/projects/cuml/en/latest/api.html">cuML API Docs</a></td>
    <td class="tg-baqh"><a href="https://rapidsai.github.io/projects/cudf/en/latest/api.html">cuDF API Docs</a></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:bold">Getting Started</span></td>
    <td class="tg-0lax"></td>
    <td class="tg-baqh"><a href="https://github.com/rapidsai/notebooks/tree/master/samples">Getting Started with cuDF Demo and Data</a></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:700">Related How To's</span></td>
    <td class="tg-0lax"></td>
    <td class="tg-baqh"><a href="https://rapidsai.github.io/projects/cudf/en/latest/10min.html">10 Minutes to cuDF</a></td>
  </tr>
  <tr>
    <td class="tg-fymr">Demos to Try</td>
    <td colspan="2" class="tg-0pky">
      <ul>
        <li><a href="https://github.com/rapidsai/notebooks/blob/0a3ec4feb5778ecc33db39b89ea918df9871cdb2/cuml/XGBoost_Demo.ipynb">XGBoost Demo</a><br>
          This notebook shows the acceleration one can gain by using GPUs with XGBoost in RAPIDS.<br></li>
        <li><a href="https://github.com/rapidsai/notebooks/blob/master/cuml/dbscan_demo.ipynb">dbscan_demo</a>: <br>
          This notebook showcases density-based spatial clustering of applications with noise (dbscan) algorithm comparison between cuML and scikit-learn.<br></li>
        <li><a href="https://github.com/rapidsai/notebooks/blob/master/cuml/knn_demo.ipynb">knn_demo</a><br>
          This notebook showcases k-nearest neighbors (knn) algorithm comparison between cuML and scikit-learn.<br></li>
        <li><a href="https://github.com/rapidsai/notebooks/blob/master/cuml/linear_regression_demo.ipynb">Linear Regression Demo</a><br>
          This notebook includes code example linear regression using RAPIDS cuDF and cuML.<br></li>
        <li><a href="https://github.com/rapidsai/notebooks/blob/master/cuml/pca_demo.ipynb">pca_demo</a><br>
          This notebook showcases principal component analysis (PCA) algorithm comparison between cuML and scikit-learn.<br></li>
        <li><a href="https://github.com/rapidsai/notebooks/blob/master/cuml/ridge.ipynb">Ridge Regression Demo</a> <br>
          This notebook includes code examples of ridge regression using RAPIDS cuDF and cuML.<br></li>
        <li><a href="https://github.com/rapidsai/notebooks/blob/master/cuml/tsvd_demo.ipynb">tsvd_demo</a><br>
          This notebook showcases truncated singular value decomposition (tsvd) algorithm comparison between cuML and scikit-learn.<br></li>
        <li><a href="https://github.com/rapidsai/notebooks/blob/master/mortgage/E2E.ipynb">Mortgage Workflow</a><br>
          Dataset driven notebook that has a workflow that is derived from <a href="http://www.fanniemae.com/portal/funding-the-market/data/loan-performance-data.html">Fannie Mae’s Single-Family Loan Performance Data</a><br></li>
        </ul>
      </td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:bold">Useful scripts</span></td>
    <td colspan="2" class="tg-0pky">
      <a href="https://github.com/rapidsai/notebooks/tree/master/utils">Utility Scripts</a><br>
      <ul>
        <li>start-jupyter.sh: starts a JupyterLab environment for interacting with, and running, notebooks<br></li>
        <li>stop-jupyter.sh: identifies all process IDs associated with Jupyter and kills them<br></li>
        <li>dask-cluster.py: launches a configured Dask cluster (a set of nodes) for use within a notebook<br></li>
        <li>dask-setup.sh: a low-level script for constructing a set of Dask workers on a single node<br></li>
        <li>split-data-mortgage.sh: splits mortgage data files into smaller parts, and saves them for use with the mortgage notebook</li>
      </ul>
    </td>
    <td class="tg-0lax"></td>
  </tr>
  <tr>
    <td class="tg-zv36">Related Blogs</td>
    <td class="tg-3xi5"><a href="https://medium.com/rapids-ai/make-sense-of-the-universe-with-rapids-ai-d105b0e5ec95">Making Sense of the Universe with RAPIDS</a></td>
    <td class="tg-3xi5"><a href="https://medium.com/rapids-ai/accelerating-cross-filtering-with-cudf-3b4c29c89292">Accelerating Cross Filtering with cuDF</a><br>Using cuDF to speed up a data scientist's visual workflow</td>
  </tr>
</table>
<br>
<br>
{% endcapture %}
{% include sec-white.html content=section_docs %}

{% include cta-footer.html 
name="Join the Community" 
tagline="Learn how you can be an adopter, contributor, and more."
button="Join Today"
link="community.html"
%}
