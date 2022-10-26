---
title: "RAPIDS Developer and Contributor Community"
description: "Learn how to become a RAPIDS adopter, contributor and more. Start contributing today!"
tagline: "Learn How To Contribute To RAPIDS"
button_text: "CONTRIBUTE"
button_link: "https://github.com/rapidsai"
layout: default
---
{% capture com_content %}
# Community and Projects
{: .section-title-full }

The RAPIDS team is developing, contributing, and collaborating closely with numerous open-source projects including Apache Arrow, Numba, XGBoost, Apache Spark, scikit-learn, and more. Our goal is to upstream all code contributions to ensure that all the components of the GPU-accelerated data science ecosystem work smoothly together.
{: .subtitle}

{% endcapture %}

{% include section-single.html
    background="white"
    padding-top="0em" padding-bottom="5em"
    content-single=com_content
%}

{% capture com_left_top %}
![RAPIDS+SQL]({{ site.baseurl }}{% link /assets/images/RAPIDS-SQL.png %}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + SQL

RAPIDS integrates with Spark SQL and Dask-SQL to accelerate your SQL queries at scale and make GPU acceleration available to an even broader set of users.
<br> **[Learn more about RAPIDS + Spark SQL <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://developer.nvidia.com/blog/accelerating-apache-spark-3-0-with-gpus-and-rapids/)**
<br> **[Learn more about RAPIDS + Dask SQL <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://dask-sql.readthedocs.io/en/latest/)**

{% endcapture %}
{% capture com_mid_top %}
![Dask]({{ site.baseurl }}{% link /assets/images/dask_logo.png%}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + Dask

Dask is an open source project providing advanced parallelism for analytics that enables performance at scale. RAPIDS is actively contributing to Dask, and it integrates with both RAPIDS cuDF, XGBoost, and RAPIDS cuML for GPU-accelerated data analytics and machine learning. <br> **[Learn more on our Dask page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](dask.html)**

{% endcapture %}
{% capture com_right_top %}
![xgboost]({{ site.baseurl }}{% link /assets/images/xgboost_logo.png %}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + XGBoost

XGBoost is a well-known gradient boosted decision trees (GBDT) machine learning package used to tackle regression, classification, and ranking problems. The RAPIDS team works closely with the Distributed Machine Learning Common (DMLC) XGBoost organization to upstream code and ensure that all components of the GPU-accelerated analytics ecosystem work smoothly together. <br> **[Learn more on our XGBoost page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](xgboost.html)**

{% endcapture %}

{% capture com_left_bottom %}
![Plotly]({{ site.baseurl }}{% link /assets/images/Plotly_Dash_logo.png %}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + Plotly Dash

Plotly’s Dash enables Data Science teams to focus on the data and models, while producing and sharing enterprise-ready analytic apps that sit on top of RAPIDS-accelerated Python dataframes. <br> **[Learn more on our Plotly page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](plotly.html)**

{% endcapture %}

{% capture com_mid_bottom %}
![HPO]({{ site.baseurl }}{% link /assets/images/csp+hpo.png %}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + HPO

Accelerate Hyperparameter Optimization (HPO) in the Cloud. The RAPIDS team works closely with major cloud providers and open source hyperparameter optimization solutions to ensure smooth integration and high performance, regardless of your deployment platform. <br> **[Learn more on our HPO page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](hpo.html)**

{% endcapture %}
{% capture com_right_bottom %}
![cloud]({{ site.baseurl }}{% link /assets/images/RAPIDS-cloud.png %}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + Cloud

RAPIDS’ GPU accelerated data science tools can be deployed on all of the major clouds, allowing anyone to take advantage of the speed increases and TCO reductions that RAPIDS enables.
<br>
**[Learn more on our cloud page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](cloud.html)**
{% endcapture %}

{% capture prj_left_top %}
![merlin]({{ site.baseurl }}{% link /assets/images/NVLogo_2D_H.png%}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + NVIDIA MERLIN

NVIDIA Merlin is an open source library providing end-to-end GPU-accelerated recommender systems. Merlin leverages RAPIDS cuDF and Dask cuDF for dataframe transformation during ETL and inference, as well as for the optimized dataloaders in TensorFlow, PyTorch or HugeCTR to accelerate deep learning training. <br> **[Learn more on our Merlin page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](merlin.html)**
{% endcapture %}

{% capture prj_mid_top %}
![slurm]({{ site.baseurl }}{% link /assets/images/slurm-logo.png%}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + HPC

RAPIDS works extremely well in traditional HPC environments where GPUs are often co-located with accelerated networking hardware such as InfiniBand.
<br> **[Learn more on our HPC page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](/hpc)**
{% endcapture %}

{% capture prj_right_top %}
![spark]({{ site.baseurl }}{% link /assets/images/spark-logo-trademark.png %}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + Spark

NVIDIA is bringing RAPIDS to Apache Spark to accelerate ETL workflows with GPUs.
<br> **[Learn more on the RAPIDS for Apache Spark page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://nvidia.github.io/spark-rapids/){: target="_blank"}**
{% endcapture %}

{% capture prj_left_bottom %}
![monai]({{ site.baseurl }}{% link /assets/images/MONAI-logo_color.png%}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + MONAI

The Medical Open Network for AI ([MONAI](https://monai.io/)) has been named by some the PyTorch of healthcare.
RAPIDS cuCIM has been integrated into the MONAI Transforms component to accelerate the data pathology training pipeline on GPU.
<br> **[Learn more on MONAI latest highlights <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://docs.monai.io/en/latest/highlights.html)**
{% endcapture %}



{% include section-double-thirds.html
    background="background-white"
    padding-top="1em" padding-bottom="0em"
    content-top-left-third=com_left_top
    content-top-middle-third=com_mid_top
    content-top-right-third=com_right_top
    content-bottom-left-third=com_left_bottom
    content-bottom-middle-third=com_mid_bottom
    content-bottom-right-third=com_right_bottom
%}

{% include section-double-thirds.html
    background="background-white"
    padding-top="1em" padding-bottom="0em"
    content-top-left-third=prj_left_top
    content-top-middle-third=prj_mid_top
    content-top-right-third=prj_right_top
    content-bottom-left-third=prj_left_bottom
    content-bottom-middle-third=prj_mid_bottom
    content-bottom-right-third=prj_right_bottom
%}


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
{: .section-subtitle-top-1}

Anyone can join our community and contribute to to RAPIDS in a five step onboarding process:

> **<i class="fas fa-download text-purple"></i> 1. Install** RAPIDS using **[Docker or Conda](https://rapids.ai/start.html#get-rapids){: target="_blank"}**. Or try RAPIDSAI with **[SageMaker Studio Lab](smsl.html){: target="_blank"}** (free account required).

> **<i class="far fa-comments text-purple"></i>  2. Join** our community conversations on **[Twitter](https://twitter.com/rapidsai){: target="_blank"}** and **[Slack]({{ site.slack_invite }}){: target="_blank"}**.

> **<i class="fas fa-search text-purple"></i> 3. Explore** our **[docs](https://docs.rapids.ai/){: target="_blank"}**, **[walk through videos](https://www.youtube.com/channel/UCsoi4wfweA3I5FsPgyQnnqw?view_as=subscriber){: target="_blank"}**, **[blog posts](https://medium.com/rapids-ai){: target="_blank"}**, **[tutorial notebooks](https://github.com/rapidsai/notebooks-contrib#getting-started-notebooks){: target="_blank"}**, and our **[examples workflows](https://github.com/rapidsai/notebooks-contrib#intermediate-notebooks){: target="_blank"}**.

> **<i class="fas fa-hammer text-purple"></i> 4. Build** your own RAPIDS powered data science workflows.

> **<i class="fab fa-github text-purple"></i> 5. Contribute** back by **[reviewing our contribution guidelines](https://docs.rapids.ai/contributing)**, **[filing issues or submitting pull requests](https://github.com/rapidsai){: target="_blank"}**, and don't forget to ask and answer questions on **[Stack Overflow](https://stackoverflow.com/tags/rapids){: target="_blank"}**.

{% endcapture %}

{% include section-halfs.html
    background="background-white"
    padding-top="1em" padding-bottom="5em"
    content-left-half=com_left
    content-right-half=com_right
%}


# Contributors
{: .section-title-full}
{% include contributing-logos.html
    padding-top="0em" padding-bottom="5em"
%}


# Adopters
{: .section-title-full}
{% include adopter-logos.html
    padding-top="0em" padding-bottom="5em"
%}


# Open Source
{: .section-title-full}
{% include open-source-logos.html
    padding-top="0em" padding-bottom="10em"
%}

{% include slopecap.html
    background="background-darkpurple"
    position="top"
    slope="down"
%}
{% include cta-footer-help.html
   background="background-darkpurple"
%}
