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
### Documentation
[cuML API Docs](https://rapidsai.github.io/projects/cuml/en/latest/api.html){: .blue-btn }
[cuDF API Docs](https://rapidsai.github.io/projects/cudf/en/latest/api.html){: .blue-btn }
[Cheat Sheet](assets/files/cheatsheet.pdf){: .blue-btn }
{: .text-center }

### Community/Project Guidelines
<p>RAPIDS projects use an established set of guidelines and procedures for all projects. These are available for the community to review and provide feedback on.</p>
[Code of Conduct](https://rapidsai.github.io/devdocs/docs/resources/conduct/){: .blue-btn }
[Changelog Format](https://rapidsai.github.io/devdocs/docs/resources/changelog/){: .blue-btn }
[Git Methodology](https://rapidsai.github.io/devdocs/docs/resources/git/){: .blue-btn }
[Style Guide](https://rapidsai.github.io/devdocs/docs/resources/style/){: .blue-btn }
[Verisons and Tags](https://rapidsai.github.io/devdocs/docs/resources/versions/){: .blue-btn }
{: .text-center }

### Contributing Guidelines
<p>RAPIDS can only grow with community support and it is vital to include developers at all levels. Reporting bugs, fixing them, and/or creating new features are all vital for the success of RAPIDS. The following pages outline our approach for contributing to RAPIDS.</p>
[Issues](https://rapidsai.github.io/devdocs/docs/contributing/issues/){: .blue-btn }
[Code Contributions](https://rapidsai.github.io/devdocs/docs/contributing/code/){: .blue-btn }
[Pull Requests](https://rapidsai.github.io/devdocs/docs/contributing/prs/){: .blue-btn }
{: .text-center }

{% endcapture %}
{% include sec-white.html content=section_docs %}


{% capture section_demos %}
#### Beginner Guides and Scripts
[Getting Started with cuDF Demo and Data](https://github.com/rapidsai/notebooks/tree/master/samples){: .blue-btn }
[10 Minutes to cuDF](https://rapidsai.github.io/projects/cudf/en/latest/10min.html){: .blue-btn }
[Utility Scripts](https://github.com/rapidsai/notebooks/tree/master/utils){: .blue-btn }
{: .text-center }


#### Notebook Demos 
<div class="boxContent">
    <a href="https://github.com/rapidsai/notebooks/blob/0a3ec4feb5778ecc33db39b89ea918df9871cdb2/cuml/XGBoost_Demo.ipynb">
        <div class="box" style="cursor: pointer;" onclick="window.location='https://github.com/rapidsai/notebooks/blob/0a3ec4feb5778ecc33db39b89ea918df9871cdb2/cuml/XGBoost_Demo.ipynb';">
            <h4>XGBoost Demo</h4>
            <p>This notebook shows the acceleration one can gain by using GPUs with XGBoost in RAPIDS.</p>
        </div>
    </a>
    <a href="https://github.com/rapidsai/notebooks/blob/master/cuml/dbscan_demo.ipynb">
        <div class="box">
            <h4>DBScan Demo</h4>
            <p>This notebook showcases density-based spatial clustering of applications with noise (dbscan) algorithm comparison between cuML and scikit-learn.</p>
        </div>
    </a>
    <a href="https://github.com/rapidsai/notebooks/blob/master/cuml/knn_demo.ipynb">
        <div class="box">
            <h4>KNN Demo</h4>
            <p>This notebook showcases k-nearest neighbors (knn) algorithm comparison between cuML and scikit-learn.</p>
        </div>
    </a>
    <a href="https://github.com/rapidsai/notebooks/blob/master/cuml/linear_regression_demo.ipynb">
        <div class="box">
            <h4>Linear Regression Demo</h4>
            <p>This notebook includes code example linear regression using RAPIDS cuDF and cuML.</p>
        </div>
    </a>
    <a href="https://github.com/rapidsai/notebooks/blob/master/cuml/pca_demo.ipynb">
        <div class="box">
            <h4>PCA Demo</h4>
            <p>This notebook showcases principal component analysis (PCA) algorithm comparison between cuML and scikit-learn.</p>
        </div>
    </a>
    <a href="https://github.com/rapidsai/notebooks/blob/master/cuml/ridge.ipynb">
        <div class="box">
            <h4>Ridge Regression Demo</h4>
            <p>This notebook includes code examples of ridge regression using RAPIDS cuDF and cuML.</p>
        </div>
    </a>
    <a href="https://github.com/rapidsai/notebooks/blob/master/cuml/tsvd_demo.ipynb">
        <div class="box">
            <h4>TSVD Demo</h4>
            <p>This notebook showcases truncated singular value decomposition (tsvd) algorithm comparison between cuML and scikit-learn.</p>
        </div>
    </a>
    <a href="https://github.com/rapidsai/notebooks/blob/master/mortgage/E2E.ipynb">
        <div class="box">
            <h4>Mortgage Workflow</h4>
            <p>Dataset driven notebook that has a workflow that is derived from Fannie Mae’s Single-Family Loan Performance Data</p>
        </div>
    </a>
</div>

{% endcapture %}
{% include sec-left-purple.html content=section_demos %}

{% capture section_blogs %}
### Teaching Blogs
<div class="boxContent">
    <a href="https://medium.com/rapids-ai/make-sense-of-the-universe-with-rapids-ai-d105b0e5ec95">
        <div class="box">
            <h4 style="color:#FFFFFF">Making Sense of the Universe with RAPIDS</h4>
            <p style="color:rgb(211, 211, 211)">By Jiwei Liu.  Code won 8th Place in Kaggle Competition</p>
        </div>
    </a>
    <a href="https://medium.com/rapids-ai/accelerating-cross-filtering-with-cudf-3b4c29c89292">
        <div class="box">
            <h4 style="color:#FFFFFF">Accelerating Cross Filtering with cuDF</h4>
            <p style="color:rgb(211, 211, 211)">By Allan Enermark.  How to use cuDF to speed up a data scientist's visual workflow</p>
        </div>
    </a>
</div>
{% endcapture %}
{% include sec-right-gray.html content=section_blogs %}

{% include cta-footer.html 
name="Join the Community" 
tagline="Learn how you can be an adopter, contributor, and more."
button="Join Today"
link="community.html"
%}
