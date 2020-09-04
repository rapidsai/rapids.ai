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
![spark]({{ site.baseurl }}{% link /assets/images/spark-logo-trademark.png %}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + Spark

NVIDIA will be bringing RAPIDS to Apache Spark.
<br> **[Learn more on our blog post <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://medium.com/rapids-ai/nvidia-gpus-and-apache-spark-one-step-closer-2d99e37ac8fd){: target="_blank"}**

{% endcapture %}


{% capture prj_left %}

{% endcapture %}

{% capture prj_mid %}

{% endcapture %}

{% capture prj_right %}

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

> **<i class="fas fa-download text-purple"></i> 1. Install** RAPIDS using **[Docker or Conda](https://rapids.ai/start.html#get-rapids){: target="_blank"}**, or try it instantly in **[Colabratory](https://colab.research.google.com/drive/1rY7Ln6rEE1pOlfSHCYOVaqt8OvDO35J0#forceEdit=true&offline=true&sandboxMode=true){: target="_blank"}**.

> **<i class="far fa-comments text-purple"></i>  2. Join** our community conversations on **[Twitter](https://twitter.com/rapidsai){: target="_blank"}**, **[Google Groups](https://groups.google.com/forum/#!forum/rapidsai){: target="_blank"}**, and **[Slack](https://join.slack.com/t/rapids-goai/shared_invite/zt-goyqj8pe-MHHggTGmZwiss2qv3KO33g){: target="_blank"}**.

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


