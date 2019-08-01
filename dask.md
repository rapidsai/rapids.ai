---
title: "RAPIDS + Dask | RAPIDS"
og_title: "RAPIDS + Dask"
og_description: "Learn How to Use Dask with GPUs"
brand_name: ""
brand_tagline: "Scale Python with Dask on GPUs"
brand_button: "DASK.ORG"
brand_link: "https://dask.org/"
layout: default
---

![Dask]({{ site.baseurl }}{% link /assets/images/dask.svg %}){: .projects-logo}


# Scale Python with Ease 
{: .section-title-full}

{% capture intro_content %}

Pandas, Numpy, and scikit-learn packages are efficient, intuitive, and widely trusted—but they weren’t designed to scale. **[Dask](https://dask.org){: target="_blank"}** is an open-source tool that can scale Python packages to multiple machines. Developed by core NumPy, pandas, scikit-learn, Jupyter, Dask is freely available and deployed in production across numerous Fortune 500 companies.
{: .subtitle}

{% endcapture %}

{% include section-single.html
    background="background-white" 
    padding-top="0em" padding-bottom="1em" 
    content-single=intro_content
%}


{% capture yd_header %}
# Why Use Dask?
{: .section-title-full}

{% endcapture %}
{% capture yd_left %}
## <i class="fas fa-expand-arrows-alt"></i> Scalable
Code only needs to be written once and then can be deployed locally or to a multi-node cluster using a comfortable Pythonic syntax. No need for code rewrites or retraining.

{% endcapture %}
{% capture yd_mid %}
## <i class="far fa-hand-rock"></i> Resilient
It’s resilient, handling the failure of worker nodes gracefully, and elastic, able to take advantage of new nodes added on the fly.

{% endcapture %}
{% capture yd_right %}
## <i class="far fa-check-square"></i> Simple to Implement
Dask requires no configuration and no setup. Adding even a single machine to computation adds very little cognitive overhead.

{% endcapture %}

{% include section-single.html
    background="background-white" 
    padding-top="2em" padding-bottom="0em" 
    content-single=yd_header
%}
{% include section-thirds.html 
    background="background-white" 
    padding-top="0em" padding-bottom="5em" 
    content-left-third=yd_left
    content-middle-third=yd_mid
    content-right-third=yd_right
%}



{% capture start_left %}
# Getting Started
{: .section-title-halfs}

It’s easy to get started with Dask quickly. The project is well supported by many tutorials, quick-start guides, and cheat sheets.

## <i class="far fa-star"></i> Working with Apache Spark?
Dask collaborates with Apache Spark and its ecosystem. However, there are **[some basic differences](https://docs.dask.org/en/latest/spark.html){: target="_blank"}**.

{% endcapture %}

{% capture start_right %}
## <i class="fas fa-microphone-alt"></i> Get an Overview
{: .section-subtitle-top-1}
Listen to the TalkPython podcast **“[Parallelizing Computation with Dask](https://talkpython.fm/episodes/show/207/parallelizing-computation-with-dask){: target="_blank"}.”**

## <i class="fab fa-youtube"></i> See How Dask Works
Watch presentations from the **[Dask Youtube channel](https://www.youtube.com/playlist?list=PLRtz5iA93T4PQvWuoMnIyEIz1fXiJ5Pri){: target="_blank"}**.

## <i class="far fa-file-code"></i> Access Dask Docs 
See the latest **[documentation from Dask](https://docs.dask.org/en/latest/){: target="_blank"}**.

## <i class="far fa-file-code"></i> Check Out Dask Tutorials
Explore Dask tutorials on **[Github](https://github.com/dask/dask-tutorial){: target="_blank"}**, see Dask code examples on **[dask.org](https://examples.dask.org){: target="_blank"}** and **[Binder](https://mybinder.org/v2/gh/dask/dask-examples/master?urlpath=lab){: target="_blank"}**.

{% endcapture %}
{% include section-halfs.html 
    background="background-white" 
    padding-top="1em" padding-bottom="10em" 
    content-left-half=start_left 
    content-right-half=start_right 
%} 


{% capture gpus_single %}
# Dask on GPUs

Dask can distribute data and computation over multiple GPUs, either in the same system or in a multi-node cluster. Dask integrates with both RAPIDS cuDF, XGBoost, and RAPIDS cuML for GPU-accelerated data analytics and machine learning.
{: .subtitle}

{% endcapture %}
{% include slopecap.html 
    background="background-gray" 
    position="top" 
    slope="down" 
%}
{% include section-single.html
    background="background-gray" 
    padding-top="5em" padding-bottom="0em" 
    content-single=gpus_single
%}


{% capture gpus_df %}
## Dataframe and ETL Integration
The RAPIDS **[cuDF library](https://github.com/rapidsai/cudf){: target="_blank"}** provides a GPU-backed dataframe class that replicates the popular pandas API. It includes extremely high-performance functions to load CSV, JSON, ORC, Parquet and other file formats directly into GPU memory, eliminating one of the key bottlenecks in many data processing tasks. cuDF includes a variety of other functions supporting GPU-accelerated ETL, such as data subsetting, transformations, one-hot encoding, and more. The RAPIDS team maintains a **[dask-cudf library](https://github.com/rapidsai/dask-cudf){: target="_blank"}** that includes helper methods to integrate Dask and cuDF.

{% endcapture %}
{% capture gpus_df_img %}
<i class="fas fa-layer-group"></i>{: .dask-icon }

{% endcapture %}
{% include section-onethird-twothird.html
    background="background-gray" 
    padding-top="0em" padding-bottom="0em" 
    content-one-third=gpus_df_img
    content-two-third=gpus_df
%}

{% capture gpus_xgb %}
## XGBoost Integration
XGBoost, the popular open source machine learning library for gradient boosting, now includes integrated support for Dask. Users can partition data across nodes using Dask’s standard data structures, build a DMatrix on each GPU using `xgboost.dask.create_worker_dmatrix`, and then launch training through `xgboost.dask.run`. See the xgboost.dask documentation or the **[Dask+XGBoost GPU example code](https://github.com/dmlc/xgboost/blob/master/demo/dask/dask_gpu_demo.py){: target="_blank"}** for more details.

**Note**: This support is currently available in custom builds, and it is expected to be included in the next official release of XGBoost **after 0.90**. New users should check out the **[10 Minutes to Dask-XGBoost guide](https://rapidsai.github.io/projects/cudf/en/latest/dask-xgb-10min.html){: target="_blank"}** to get started quickly.

{% endcapture %}
{% capture gpus_xgb_img %}
<i class="fas fa-bezier-curve"></i>{: .dask-icon }

{% endcapture %}
{% include section-onethird-twothird.html
    background="background-gray" 
    padding-top="0em" padding-bottom="0em" 
    content-one-third=gpus_xgb_img
    content-two-third=gpus_xgb
%}
{% capture gpus_ml%}
## Integration With Other Machine Learning Algorithms 
For other machine learning work on GPU, the **[dask-cuml library](https://github.com/rapidsai/dask-cuml){: target="_blank"}** provides a bridge to the RAPIDS cuML package. RAPIDS cuML implements popular machine learning algorithms, including clustering, dimensionality reduction, and regression approaches, with high performance GPU-based implementations, offering speedups of up to **100x** over CPU-based approaches. cuML replicates the scikit-learn API, so it integrates well with projects like Dask that include scikit-learn support. Currently, dask-cuml supports distributed clustering and regression algorithms, with new algorithms are being added over time.

{% endcapture %}
{% capture gpus_ml_img %}
<i class="fas fa-sliders-h"></i>{: .dask-icon }

{% endcapture %}
{% include section-onethird-twothird.html
    background="background-gray" 
    padding-top="0em" padding-bottom="0em" 
    content-one-third=gpus_ml_img
    content-two-third=gpus_ml
%}

{% capture gpus_nb %}
## Example Notebooks
The RAPIDS Notebooks Extended repository includes several examples with end-to-end examples using Dask for distributed, GPU-accelerated computation. Here’s a few from the collection to get started with. 

<i class="fas fa-caret-right"></i> The Linear Regression with Dask+cuML shows a simple example of how to get started with distributed machine learning. **[Go to notebook <i class="fas fa-angle-double-right"></i>](https://github.com/rapidsai/notebooks-extended/blob/a236188a08ba7ec77a55ec48e5a5a1d6e81c9895/tutorials/examples/linear_regression_dask_cuml.ipynb){: target="_blank"}**
{: .no-tb-margins }

<i class="fas fa-caret-right"></i> The end-to-end mortgage example notebook uses Fannie Mae data to predict mortgage delinquency (a classification problem). **[Go to notebook <i class="fas fa-angle-double-right"></i>](https://github.com/rapidsai/notebooks-extended/blob/master/intermediate_notebooks/E2E/mortgage/mortgage_e2e.ipynb){: target="_blank"}**
{: .no-tb-margins }

<i class="fas fa-caret-right"></i> The NYC Taxi End-to-End notebook uses trip data to predict New York City taxi fares (a regression problem). **[Go to notebook <i class="fas fa-angle-double-right"></i>](https://github.com/efajardo-nv/rapids-dataproc/blob/master/notebooks/NYCTaxi-E2E.ipynb){: target="_blank"}**
{: .no-tb-margins }

{% endcapture %}
{% capture gpus_nb_img %}
<i class="far fa-bookmark"></i>{: .dask-icon }

{% endcapture %}
{% include section-onethird-twothird.html
    background="background-gray" 
    padding-top="0em" padding-bottom="10em" 
    content-one-third=gpus_nb_img
    content-two-third=gpus_nb
%}


{% capture usecase_single %}
# Use Cases

Dask is widely and routinely used, running on everything from laptops to thousand-machine clusters in-house, on the cloud, and on high-performance computing (HPC) supercomputers. Its ability to process hundreds of terabytes of data efficiently makes it a powerful tool in three key areas. See how Dask is being used across industry by reading stories from other **[Dask users](https://stories.dask.org/en/latest/){: target="_blank"}** and see specific examples of how **[people are using Dask](http://docs.dask.org/en/latest/use-cases.html){: target="_blank"}**.
{: .subtitle}

{% endcapture %}
{% capture uc_left %}
## <i class="fas fa-store-alt"></i> Retail

Data science and devops teams in the retail industry use Dask to scale their pipelines; taking pandas and machine learning workloads to terabytes of data easily. The Dask interface makes it easy to load in terabytes of tabular data, transform the data with libraries like pandas or RAPIDS cuDF using parallel compute, and pass it off to machine learning–training libraries at scale. See how **[one major retailer](https://www.youtube.com/watch?v=OQjko2H7xec&feature=youtu.be){: target="_blank"}** is using RAPIDS and Dask to generate more accurate forecasting models.

{% endcapture %}
{% capture uc_mid %}
## <i class="fas fa-server"></i> HPC

Dask makes it easy to quickly analyze large, multi-dimensional datasets. It provides the same interactivity and ease of development as a system like Spark but is much more aligned to scientific processing, with native code execution, direct integration with systems like SLURM and PBS, and data models that fit multi-dimensional and spatial workloads. It’s also well tuned for high-performance networks and accelerator hardware.

{% endcapture %}
{% capture uc_right %}
## <i class="fas fa-hand-holding-usd"></i> Financial Services
Many financial institutions have large, complex codebases that encode significant business logic, but they now need parallelism. Their systems are more complex than just “a big pandas dataframe” or “a big NumPy array.” These groups use Dask’s lower-level APIs (Delayed, Futures) to add task scheduling and parallelism as a lightweight way to scale out their systems without costly rewrites.

{% endcapture %}
{% include slopecap.html 
    background="background-purple" 
    position="top" 
    slope="up" 
%}
{% include section-single.html
    background="background-purple" 
    padding-top="5em" padding-bottom="0em" 
    content-single=usecase_single
%}
{% include section-thirds.html 
    background="background-purple" 
    padding-top="0em" padding-bottom="5em" 
    content-left-third=uc_left
    content-middle-third=uc_mid
    content-right-third=uc_right
%}
{% include slopecap.html 
    background="background-purple" 
    position="bottom" 
    slope="down" 
%}



{% capture tik_single%}
# Dask Libraries

Dask provides advanced parallelism for data science, enabling performance at scale for popular Python tools. Below are the key libraries of Dask that make it unique. 
{: .subtitle}

{% endcapture %}
{% capture tik_top_left %}
## <i class="fas fa-dice-d20"></i> User Interfaces

Dask collections, including DataFrame, Array, Delayed, and Futures, provide underlying parallel computing machinery to scale workloads. All come with a purpose-built set of parallel algorithms and programming style. <br> **[Learn more <i class="fas fa-angle-double-right"></i>](https://docs.dask.org/en/latest/user-interfaces.html){: target="_blank"}** 

{% endcapture %}

{% capture tik_top_mid %}
## <i class="fas fa-wave-square"></i>  Machine Learning

Dask-ML provides scalable machine learning in Python using Dask with popular machine learning libraries, such as scikit-learn. <br> **[Learn more <i class="fas fa-angle-double-right"></i>](https://ml.dask.org){: target="_blank"}** 
{% endcapture %}
{% capture tik_top_right %}
## <i class="fas fa-random"></i> Parallel Execution

Dask uses task graphs to optimize and execute work in parallel. After Dask generates task graphs, it executes them on parallel hardware with a distributed task scheduler. <br> **[Learn more <i class="fas fa-angle-double-right"></i>](https://docs.dask.org/en/latest/scheduling.html){: target="_blank"}** 

{% endcapture %}

{% capture tik_bottom_left %}
## <i class="fas fa-cloud-upload-alt"></i> Deployment

Dask integrates into existing cluster management tooling like Kubernetes and YARN (Hadoop/Spark) and HPC schedulers like SLURM, PBS, and LSF to enable scalable workloads to evolve, reducing the burst workloads of computations by 10X.<br> **[Learn more <i class="fas fa-angle-double-right"></i>](http://docs.dask.org/en/latest/setup.html){: target="_blank"}** 

{% endcapture %}

{% capture tik_bottom_mid %}
## <i class="fas fa-chart-line"></i> Visual Interactivity
The Dask interactive dashboard gives real-time feedback during computations, pointing users to hot spots in their code. This helps them use their hardware more effectively to customize load balancing, communications, thread-level profiling, and more. <br> **[Learn more <i class="fas fa-angle-double-right"></i>](http://docs.dask.org/en/latest/understanding-performance.html){: target="_blank"}** 

{% endcapture %}
{% capture tik_bottom_right %}
 
{% endcapture %}
{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="0em" 
    content-single=tik_single
%}
{% include section-double-thirds.html 
    background="background-white" 
    padding-top="0em" padding-bottom="10em" 
    content-top-left-third=tik_top_left 
    content-top-middle-third=tik_top_mid
    content-top-right-third=tik_top_right 
    content-bottom-left-third=tik_bottom_left 
    content-bottom-middle-third=tik_bottom_mid
    content-bottom-right-third=tik_bottom_right 
%}

{% capture end_bottom %}
# Get Started with Dask
{: .section-title-full .text-white}

{% endcapture %}
{% include slopecap.html 
    background="background-darkpurple" 
    position="top" 
    slope="up" 
%}
{% include section-single.html
    background="background-darkpurple" 
    padding-top="1em" padding-bottom="0em" 
    content-single=end_bottom
%}

{% include cta-footer-dask.html 
   background="background-darkpurple" 
%}

