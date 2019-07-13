---
title: "RAPIDS Developer and Contributor Community | RAPIDS"
og_title: "RAPIDS Developer and Contributor Community"
og_description: "Learn how to become a RAPIDS adopter, contributor and more. Start contributing today!"
brand_name: ""
brand_tagline: "Learn How To Contribute To RAPIDS"
brand_button: "CONTRIBUTE"
brand_link: "https://github.com/rapidsai"
layout: default
---

{% capture com_left %}
# RAPIDS Community
{: .section-title-halfs}

RAPIDS is for everyone: users, adopters, and contributors. If you’re a data scientist, researcher, engineer, or developer using pandas, Dask, scikit-learn, or Spark on CPUs, our **[RAPIDS projects](https://github.com/rapidsai){: target="_blank"}** are almost drop in replacements that can speed up your end-to-end workflow up to 50x.

## <i class="fas fa-code"></i> Open Source
{: .section-subtitle-top-1}
RAPIDS is open sourced under the Apache 2.0 license and is intended to be improved and extended upon by help from the community. While significant time and effort have been invested into making the platform to date, we need active contributors to help build its future.
{% endcapture %}

{% capture com_right %}
## <i class="fas fa-users"></i> Community Onboarding
Anyone can join our community and contribute to to RAPIDS in a five step onboarding process:

> **<i class="fas fa-download text-purple"></i> Install** RAPIDS using **[Docker or Conda](https://rapids.ai/start.html#get-rapids){: target="_blank"}**, or try it instantly in **[Colabratory](https://colab.research.google.com/drive/1XTKHiIcvyL5nuldx0HSL_dUa8yopzy_Y#forceEdit=true&offline=true&sandboxMode=true){: target="_blank"}**.

> **<i class="far fa-comments text-purple"></i> Join** our community conversations on **[Twitter](https://twitter.com/rapidsai){: target="_blank"}**, **[Google Groups](https://groups.google.com/forum/#!forum/rapidsai){: target="_blank"}**, and **[Slack](https://join.slack.com/t/rapids-goai/shared_invite/enQtMjE0Njg5NDQ1MDQxLTViZWFiYTY5MDA4NWY3OWViODg0YWM1MGQ1NzgzNTQwOWI1YjE3NGFlOTVhYjQzYWQ4YjI4NzljYzhiOGZmMGM){: target="_blank"}**.

> **<i class="fas fa-search text-purple"></i> Explore** our **[walk through videos](https://www.youtube.com/channel/UCsoi4wfweA3I5FsPgyQnnqw?view_as=subscriber){: target="_blank"}**, **[blog posts](https://medium.com/rapids-ai){: target="_blank"}**, **[tutorial notebooks](https://github.com/rapidsai/notebooks-extended#getting-started-notebooks){: target="_blank"}**, and our **[examples workflows](https://github.com/rapidsai/notebooks-extended#intermediate-notebooks){: target="_blank"}**.

> **<i class="fas fa-hammer text-purple"></i> Build** your own RAPIDS powered data science workflows.

> **<i class="fab fa-github text-purple"></i> Contribute** back by **[reviewing our contribution guidelines](https://docs.rapids.ai/contributing)**, **[filing issues or submitting pull requests](https://github.com/rapidsai){: target="_blank"}**, and don't forget to ask and answer questions on **[Stack Overflow](https://stackoverflow.com/tags/rapids){: target="_blank"}**.

{% endcapture %}

{% include section-halfs.html
    background="background-white" 
    padding-top="1em" padding-bottom="5em" 
    content-left-half=com_left 
    content-right-half=com_right
%} 

{% capture proj_left %}
# Community Projects
{: .section-title-halfs}

The RAPIDS team is developing, contributing, and collaborating closely with numerous open-source projects including Apache Arrow, Numba, XGBoost, Apache Spark, sci-kit learn, and more. Our goal is to upstream all code contributions to ensure that all the components of the GPU-accelerated data science ecosystem work smoothly together.
{% endcapture %}

{% capture proj_right %}
## <i class="fas fa-code-branch"></i> RAPIDS + Dask
{: .section-subtitle-top-1}

Dask is an open source project providing advanced parallelism for analytics that enables performance at scale. RAPIDS is actively contributing to Dask, and it integrates with both RAPIDS cuDF, XGBoost, and RAPIDS cuML for GPU-accelerated data analytics and machine learning. <br> **[Learn more on our Dask page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](dask.html)**


## <i class="fas fa-code-branch"></i> RAPIDS + XGBoost

XGBoost is a well-known gradient boosted decision trees (GBDT) machine learning package used to tackle regression, classification, and ranking problems. The RAPIDS team works closely with the Distributed Machine Learning Common (DMLC) XGBoost organization to upstream code and ensure that all components of the GPU-accelerated analytics ecosystem work smoothly together. <br> **[Learn more on our XGBoost page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](xgboost.html)**


## <i class="fas fa-code-branch"></i> RAPIDS + Spark

The RAPIDS team is working with the community to build a distributed, open source XGBoost4J-Spark + RAPIDS package. More details coming soon. 

{% endcapture %}

{% include section-halfs.html
    background="background-white" 
    padding-top="1em" padding-bottom="5em" 
    content-left-half=proj_left 
    content-right-half=proj_right
%} 


# Contributors
{: .section-title-full}
{% include contributing-logos.html 
    padding-top="1em" padding-bottom="5em" 
%}

# Open Source
{: .section-title-full}
{% include open-source-logos.html 
    padding-top="1em" padding-bottom="10em" 
%}

{% include slopecap.html 
    background="background-darkpurple" 
    position="top" 
    slope="down"
%}
{% include cta-footer-help.html 
   background="background-darkpurple" 
%}


