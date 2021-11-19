---
title: "RAPIDS Partners"
description: "Join other companies in using and contributing to RAPIDS and its Partner Ecosystem"
tagline: "Who is using RAPIDS"
button_text: "JOIN THE COMMUNITY"
button_link: "https://github.com/rapidsai"
layout: default
---
{% capture com_content %}

# Corporate Adopters
{: .section-title-full}
{% include adopter-logos.html
    padding-top="0em" padding-bottom="5em"
%}

# Integrated Solutions
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
![BLAZINGSQL]({{ site.baseurl }}{% link /assets/images/blazingsql.png %}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + BlazingSQL

BlazingSQL is an open source project providing distributed SQL for analytics that enables the integration of enterprise data at scale. RAPIDS is actively contributing to BlazingSQL, and it integrates with RAPIDS cuDF, XGBoost, and RAPIDS cuML for GPU-accelerated data analytics and machine learning. <br> **[Learn more on our BlazingSQL page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](blazingsql.html)**

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
![cloud]({{ site.baseurl }}{% link /assets/images/RAPIDs-cloud.png %}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + Cloud

RAPIDS’s GPU accelerated data science tools can be deployed on all of the major clouds, allowing anyone to take advantage of the speed increases and TCO reductions that RAPIDS enables.
<br>
**[Learn more on our cloud page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](cloud.html)**
{% endcapture %}

{% capture prj_left %}
![merlin]({{ site.baseurl }}{% link /assets/images/NVLogo_2D_H.png%}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + NVIDIA MERLIN

NVIDIA Merlin is an open source library providing end-to-end GPU-accelerated recommender systems. Merlin leverages RAPIDs cuDF and Dask cuDF for dataframe transformation during ETL and inference, as well as for the optimized dataloaders in TensorFlow, PyTorch or HugeCTR to accelerate deep learning training. <br> **[Learn more on our Merlin page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](merlin.html)**
{% endcapture %}

{% capture prj_mid %}
![slurm]({{ site.baseurl }}{% link /assets/images/slurm-logo.png%}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + HPC

RAPIDS works extremely well in traditional HPC environments where GPUs are often co-located with accelerated networking hardware such as InfiniBand.
<br> **[Learn more on our HPC page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](/hpc)**
{% endcapture %}

{% capture prj_right %}
![spark]({{ site.baseurl }}{% link /assets/images/spark-logo-trademark.png %}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + Spark

NVIDIA is bringing RAPIDS to Apache Spark to accelerate ETL workflows with GPUs.
<br> **[Learn more on the RAPIDS for Apache Spark page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://nvidia.github.io/spark-rapids/){: target="_blank"}**
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
{% include section-thirds.html
    background="background-white"
    padding-top="1em" padding-bottom="5em"
    content-left-third=prj_left
    content-middle-third=prj_mid
    content-right-third=prj_right
%}
# Partner Ecosystem
{: .section-title-full }
{% capture com_left %}
## <i class="fas fa-map"></i> Ecosystem Map
{: .section-subtitle-top-1}
![Map]({{ site.baseurl }}{% link /assets/images/ecosystem.png%}){: .third-image-center}
{% endcapture %}

{% capture com_right %}
## <i class="fas fa-oss"></i> Open Source
{: .section-subtitle-top-1}

{% include open-source-logos.html
    padding-top="0em" padding-bottom="10em"
%}
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


{% include slopecap.html
    background="background-darkpurple"
    position="top"
    slope="down"
%}
{% include cta-footer-help.html
   background="background-darkpurple"
%}


