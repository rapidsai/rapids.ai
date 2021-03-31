---
title: "RAPIDS + HPO"
description: "Learn How to Use RAPIDS with HPO in the Cloud"
tagline: "Use RAPIDS with Hyper Parameter Optimization"
button_text: "Get Started"
button_link: "https://github.com/rapidsai/cloud-ml-examples/"
layout: default
---

![RAPIDS CSP HPO]({{ site.baseurl }}{% link /assets/images/csp+hpo.png %}){: .projects-logo}


# Accelerate Hyperparameter Optimization <br> in the Cloud
{: .section-title-full}

{% capture intro_content %}

Machine learning models can have dozens of options, or “hyperparameters,” that make the difference between a great model and an inaccurate one. Accelerated machine learning models in RAPIDS give you the flexibility to use hyperparameter optimization (HPO) experiments to explore all of these options to find the most accurate possible model for your problem. The acceleration of GPUs lets data scientists iterate through hundreds or thousands of variants over a lunch break, even for complex models and large datasets.
{: .subtitle}

## RAPIDS Integration into Cloud / Distributed Frameworks
{: .section-title-full}

![RAPIDS CSP HPO]({{ site.baseurl }}{% link /assets/images/HPO-space-2.png %}){: .center}
{% endcapture %}

{% include section-single.html
    background="background-white" 
    padding-top="3em" padding-bottom="1em" 
    content-single=intro_content
%}

<section class="container-logo-flex padding-top-1em padding-bottom-5em">
    <div class="logo-flex">
        <a href="https://dask.org/" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/dask_stacked.png %}" alt="Dask"> </a>
    </div>
    <div class="logo-flex">
        <a href="https://databricks.com/product/enterprise-cloud-service" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/databricks-logo.png %}" alt="Databricks"> </a>
    </div>
    <div class="logo-flex">
       <a href="https://mlflow.org/" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/MLflow-logo.png %}" alt="MLflow"> </a>
    </div>
    <div class="logo-flex">
       <a href="https://optuna.org/" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/Optuna-logo.png %}" alt="Optuna"> </a>
    </div>
    <div class="logo-flex">
       <a href="https://epistasislab.github.io/tpot/" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/tpot-logo.png %}" alt="TPOT"> </a>
    </div>
    <div class="logo-flex">
       <a href="https://docs.ray.io/en/latest/tune.html" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/ray-tune.png %}" alt="ray tune"> </a>
    </div>

</section>

{% capture yd_header %}
# Benefits With RAPIDS
{: .section-title-full}

{% endcapture %}
{% capture yd_left %}
## <i class="fal fa-boxes-alt"></i> Smooth Integration
RAPIDS matches popular PyData APIs, making it an easy drop-in for existing workloads built on Pandas and scikit-learn.

{% endcapture %}
{% capture yd_mid %}
## <i class="fal fa-tachometer-fast"></i> High Performance
With GPU acceleration, RAPIDS models can train 40x faster than CPU equivalents, enabling more experimentation in less time.

{% endcapture %}
{% capture yd_right %}
## <i class="fal fa-cloud-upload"></i> Deploy on Any Platform
The RAPIDS team works closely with major cloud providers and open source hyperparameter optimization solutions to provide code samples so you can get started with HPO in minutes on the cloud of your choice.

{% endcapture %}

{% include section-single.html
    background="background-white" 
    padding-top="2em" padding-bottom="0em" 
    content-single=yd_header
%}
{% include section-thirds.html 
    background="background-white" 
    padding-top="0em" padding-bottom="10em" 
    content-left-third=yd_left
    content-middle-third=yd_mid
    content-right-third=yd_right
%}



{% capture start_left %}
# Getting Started
{: .section-title-halfs}

RAPIDS supports hyperparameter optimization and AutoML solutions based on AWS SageMaker, Azure ML, Google Cloud AI, Dask ML, Optuna, Ray Tune and TPOT frameworks, so you can easily integrate with whichever framework you use today. RAPIDS also integrates easily with MLflow to track and orchestrate experiments from any of these frameworks.

## <i class="fad fa-terminal"></i> Get the HPO example code

Our GitHub repo contains helper code, sample notebooks, and step-by-step instructions to get you up and running on each HPO platform. **[See our README <i class="fas fa-angle-double-right"></i>](https://github.com/rapidsai/cloud-ml-examples){: target="_blank"}**

## <i class="far fa-code-merge"></i> Clone the Repo

Start by cloning the open-source cloud-ml-examples repository from RAPIDSai GitHub.
 **[See our Repo <i class="fas fa-angle-double-right"></i>](https://github.com/rapidsai/cloud-ml-examples){: target="_blank"}**

{% endcapture %}

{% capture start_right %}
## <i class="far fa-bookmark"></i> Notebook examples
{: .section-subtitle-top-1}

The repo will walk you through step-by-step instructions for a sample hyperparameter optimization job. To start running your experiments with HPO, navigate to the directory for your framework or CSP, and check out the README.md file there.  **[Walk Through The Notebooks <i class="fas fa-angle-double-right"></i>](https://github.com/rapidsai/cloud-ml-examples){: target="_blank"}**

## <i class="fab fa-youtube"></i> Video Tutorials

Watch tutorials of accelerated HPO examples on **[Amazon SageMaker](https://www.youtube.com/watch?v=BtE4d0v6Css){: target="_blank"}** and **[Azure ML](https://www.youtube.com/watch?v=aqTmVVFnEwI&t=3s){: target="_blank"}** from the RAPIDSAI YouTube Channel, and **[Optuna+MLflow](https://cfp.jupytercon.com/2020/schedule/presentation/139/optimizing-model-performance-with-feature-engineering-and-hyperparameter-optimisation/){: target="_blank"}** from JupyterCon 2020.

## <i class="far fa-bookmark"></i> Blog Posts

<i class="fas fa-caret-right"></i> **[RAPIDS and Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/rapids-and-amazon-sagemaker-scale-up-and-scale-out-to-tackle-ml-challenges/){: target="_blank"}**: Scale up and scale out to tackle ML challenges
{: .no-tb-margins }

<i class="fas fa-caret-right"></i> An End to End Guide to Hyperparameter Optimization using **[RAPIDS and MLflow on Google’s Kubernetes Engine (GKE)](https://medium.com/rapids-ai/an-end-to-end-guide-to-hyperparameter-optimization-using-rapids-and-mlflow-on-gke-8c07596cfff5){: target="_blank"}**
{: .no-tb-margins }

<i class="fas fa-caret-right"></i> Hyperparameter Optimization with **[Optuna and RAPIDS](https://medium.com/rapids-ai/hyper-parameter-optimization-with-optuna-and-rapids-467fc8189962){: target="_blank"}**
{: .no-tb-margins }

<i class="fas fa-caret-right"></i> Faster AutoML with **[TPOT and RAPIDS](https://medium.com/rapids-ai/faster-automl-with-tpot-and-rapids-758455cd89e5){: target="_blank"}**
{: .no-tb-margins }

<i class="fas fa-caret-right"></i> Optimizing Machine Learning Models with Hyperopt and **[RAPIDS on Databricks Cloud](https://medium.com/rapids-ai/optimizing-machine-learning-models-with-hyperopt-and-rapids-on-databricks-cloud-fdac9154e3e4){: target="_blank"}**  
{: .no-tb-margins }

<i class="fas fa-caret-right"></i> Managing and Deploying High-Performance Machine Learning Models on GPUs with **[RAPIDS and MLFlow](https://medium.com/rapids-ai/managing-and-deploying-high-performance-machine-learning-models-on-gpus-with-rapids-and-mlflow-753b6fcaf75a){: target="_blank"}**
{: .no-tb-margins }

<i class="fas fa-caret-right"></i> 30x Faster Hyperparameter Search with **[Ray Tune and RAPIDS](https://medium.com/rapids-ai/30x-faster-hyperparameter-search-with-raytune-and-rapids-403013fbefc5){: target="_blank"}**

{% endcapture %}

{% capture chart_single %}
# Minimize Cost, Accelerate Turnaround
{: .section-title-full}

![100 job cost]({{ site.baseurl }}{% link /assets/images/100-Job HPO.png %}){: .full-image-center}

{% endcapture %}

{% include slopecap.html 
    background="background-purple" 
    position="top" 
    slope="down" 
%}
{% include section-halfs.html 
    background="background-purple" 
    padding-top="5em" padding-bottom="0em" 
    content-left-half=start_left 
    content-right-half=start_right 
%} 
{% include section-single.html
    background="background-purple" 
    padding-top="0em" padding-bottom="10em" 
    content-single=chart_single
%}



{% capture cl_single%}
# Run your experiments with HPO
 
It’s easy to work in the cloud of your choice to find the best quality model.
{: .subtitle}

{% endcapture %}
{% capture cl_left_top %}
## <i class="fas fa-cloud"></i> RAPIDS on Cloud <br> Machine Learning Services
Azure ML, AWS SageMaker, and Google Cloud AI hyperparameter optimization services free users from the details of managing their own infrastructure. Launch a job from a RAPIDS sample notebook, and the platform will automatically scale up and launch as many instances as you need to complete the experiments quickly. From a centralized interface, you can manage your jobs, view results, and find the best model to deploy. For various deployment options and instructions, check out our **[Deploying RAPIDS in the Cloud page](https://rapids.ai/cloud){: target="_blank"}**.

{% endcapture %}

{% capture cl_right_top %}
## <i class="fas fa-clouds"></i> Bring Your Own Cloud <br> On-Prem or Public
Whether running a cluster on-prem, or managing instances in a public cloud, RAPIDS integrates with HPO platforms that can run on your infrastructure. RayTune and Dask-ML both provide cloud-neutral platforms for hyperparameter optimization. RayTune combines the scalable Ray platform with state-of-the-art HPO algorithms, including PBT, Vizier’s stopping rule, and more. Dask-ML HPO offers GPU-aware caching of intermediate datasets and a familiar, Pythonic API. Both can benefit from high-performance estimators from RAPIDS.

{% endcapture %}

{% include slopecap.html 
    background="background-white" 
    position="top" 
    slope="up" 
%}
{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="0em" 
    content-single=cl_single
%}
{% include section-halfs.html 
    background="background-white" 
    padding-top="0em" padding-bottom="10em" 
    content-left-half=cl_left_top
    content-right-half=cl_right_top
%}



{% capture end_bottom %}
# Get Started with Hyperopt
{: .section-title-full .text-white}

{% endcapture %}
{% include slopecap.html 
    background="background-darkpurple" 
    position="top" 
    slope="down" 
%}
{% include section-single.html
    background="background-darkpurple" 
    padding-top="0em" padding-bottom="0em" 
    content-single=end_bottom
%}
{% include cta-footer-hpo.html 
   background="background-darkpurple" 
%}
