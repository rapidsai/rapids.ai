---
title: "RAPIDS + XGBoost"
description: "Learn How to Deploy XGBoost on GPUs"
tagline: "Deploy XGBoost on GPUs"
button_text: "XGBOOST.IO"
button_link: "https://xgboost.readthedocs.io"
layout: default
---

![xgboost]({{ site.baseurl }}{% link /assets/images/xgboost_logo.png %}){: .projects-logo}

# Seamless Acceleration at Scale
{: .section-title-full}

{% capture intro_content %}

XGBoost is a well-known gradient boosted decision trees (GBDT) machine learning package used to tackle regression, classification, and ranking problems. It’s written in C++ and NVIDIA CUDA® with wrappers for Python, R, Java, Julia, and several other popular languages. XGBoost now includes seamless, drop-in GPU acceleration, which significantly speeds up model training and improves accuracy for better predictions.
{: .subtitle}

The RAPIDS team works closely with the Distributed Machine Learning Common (DMLC) XGBoost organization to upstream code and ensure that all components of the GPU-accelerated analytics ecosystem work smoothly together. 
{: .subtitle}

{% endcapture %}

{% include section-single.html
    background="background-white"
    padding-top="0em" padding-bottom="1em" 
    content-single=intro_content
%}


{% capture start_left %}
# Getting Started
{: .section-title-halfs}
The project is well supported and documented by many tutorials, quick-start guides, and papers.

## <i class="fas fa-bolt"></i> Try It Now in CoLab
Try out XGBoost now, with the basics of cuDF and other RAPIDS libraries, in our online **[XGBoost Colaboratory notebook](https://colab.research.google.com/drive/1xnTpVS194BJ0pOPuxN4GOmypdu2RvwdH){: target="_blank"}**.

## <i class="far fa-bookmark"></i> Notebook Examples
To see how XGBoost integrates with cuDF, Dask, and the entire RAPIDS ecosystem, check out these **[RAPIDS notebooks](https://github.com/rapidsai/notebooks-contrib){: target="_blank"}** which walk through classification and regression examples.

{% endcapture %}
{% capture start_right %}
## <i class="far fa-file-code"></i> See the Latest Docs 
{: .section-subtitle-top-1}
Access current installation instructions, guides, FAQs, and more in the **[latest documentation](https://xgboost.readthedocs.io/en/latest/){: target="_blank"}**. 

## <i class="far fa-file-alt"></i> Read the original XGBoost paper
Take a deep dive into XGBoost’s algorithms with Tianqi Chen and Carlos Guestrin in their **[XGBoost Paper](https://arxiv.org/abs/1603.02754){: target="_blank"}**. 

## <i class="fas fa-wave-square"></i> Dive into the XGBoost Algorithm

Learn about the XGBoost algorithms used on GPUs in these blogs from Rory Mitchell, a RAPIDS team member and core XGBoost contributor. <br>
<i class="fas fa-caret-right"></i> **[Gradient Boosting, Decision Trees and XGBoost with CUDA](https://devblogs.nvidia.com/gradient-boosting-decision-trees-xgboost-cuda/){: target="_blank"}** <br>
<i class="fas fa-caret-right"></i> **[Updates to the XGBoost GPU algorithms](https://xgboost.ai/2018/07/04/gpu-xgboost-update.html){: target="_blank"}** <br>
<i class="fas fa-caret-right"></i> **[Bias Variance Decompositions using XGBoost](https://devblogs.nvidia.com/bias-variance-decompositions-using-xgboost/){: target="_blank"}** <br>


{% endcapture %}
{% include section-halfs.html 
    background="background-white" 
    padding-top="3em" padding-bottom="10em" 
    content-left-half=start_left 
    content-right-half=start_right 
%} 

{% capture metric_title%}
# Maximize XGBoost Performance on GPUs

{% endcapture %}
{% capture metric_left %}
![xgboost]({{ site.baseurl }}{% link /assets/images/XGboost-benchmark.png %}){: .full-image-center}
{% endcapture %}
{% capture metric_right %}
## <i class="fas fa-microchip"></i> Benchmarks Comparing CPUs and GPUs

XGBoost has integrated support to run across multiple GPUs, which can deliver even more significant performance improvements. For the 113-million-row airline dataset used in the gradient boosting machines (GBM) benchmarks suite, eight NVIDIA® Tesla® V100 GPUs completed training in 42.6 seconds, compared to over 39 minutes on eight CPUs—a 54.9X speedup.

## <i class="far fa-chart-bar"></i> Measure Your Performance

You can run GBM benchmarking scripts from this **[GitHub repository](https://github.com/RAMitchell/GBM-Benchmarks){: target="_blank"}** to measure performance on your own system and compare it to various GBM/GBDT implementations.

{% endcapture %}
{% include slopecap.html 
    background="background-gray" 
    position="top" 
    slope="down" 
%}
{% include section-single.html
    background="background-gray" 
    padding-top="5em" padding-bottom="1em" 
    content-single=metric_title
%}
{% include section-halfs.html 
    background="background-gray" 
    padding-top="0em" padding-bottom="10em" 
    content-left-half=metric_left
    content-right-half=metric_right 
%} 



{% capture deploy_single %}
# Deploying Distributed XGBoost at Scale

It’s easy to work across multiple GPUs and multiple nodes with distributed Dask and Apache Spark. 
{: .subtitle}


{% endcapture %}
{% capture deploy_left %}
## <i class="fas fa-expand-arrows-alt"></i> Scale Out with Dask

To take advantage of multiple GPU-accelerated nodes, you can use XGBoost’s native Dask integration. This distributes data, builds DMatrix objects, and sets up cross-node communication to run XGBoost training on a cluster.  This **[blog post](https://medium.com/rapids-ai/a-new-official-dask-api-for-xgboost-e8b10f3d1eb7)** covers the XGBoost Dask API in more detail, including usage and performance. The **[official XGBoost repository](https://github.com/dmlc/xgboost/tree/master/demo/dask){: target="_blank"}** includes simple examples with distributed Dask and also more detailed **[API documentation](https://xgboost.readthedocs.io/en/latest/python/python_api.html#dask-api){: target="_blank"}**.
{% endcapture %}
{% capture deploy_mid %}
## <i class="fas fa-expand-arrows-alt"></i> Scale Out with Spark

XGBoost supports a Java API, called **[XGBoost4J](https://xgboost.readthedocs.io/en/latest/jvm/index.html){: target="_blank"}**. As of release 1.2, the XGBoost4J JARs include GPU support in the pre-built xgboost4j-spark-gpu JARs.

The team is continuing to work on deeper integration into the Spark ecosystem - learn more in this **[devblog post](link to: https://news.developer.nvidia.com/gpu-accelerated-spark-xgboost/){: target="_blank"}**.

{% endcapture %}
{% capture deploy_right %}
## <i class="fas fa-desktop"></i> Use a Single Machine

With **[Dask-CUDA](https://github.com/rapidsai/dask-cuda){: target="_blank"}**, running across multiple GPUs on a single machine is easy. Two lines of code can spin up a LocalCUDACluster and parallelize ETL as well as training. See the **[Dask-CUDA docs](https://github.com/rapidsai/dask-cuda){: target="_blank"}** for more details.

**NOTE:** Older versions of XGBoost supported a thread-based "single-node, multi-GPU" pattern with the `n_gpus` parameters. This parameter is now deprecated, and we encourage all users to shift to Dask or Spark for more scalable and maintainable multi-GPU training.


{% endcapture %}
{% include slopecap.html 
    background="background-purple" 
    position="top" 
    slope="up" 
%}
{% include section-single.html
    background="background-purple" 
    padding-top="5em" padding-bottom="0em" 
    content-single=deploy_single
%}
{% include section-thirds.html
    background="background-purple" 
    padding-top="0em" padding-bottom="10em"
    content-left-third=deploy_left
    content-middle-third=deploy_mid
    content-right-third=deploy_right
%}
{% include slopecap.html 
    background="background-purple" 
    position="bottom"
    slope="down" 
%}



{% capture download_single %}
# Download the Software

The RAPIDS team is developing GPU enhancements to open-source XGBoost, working closely with the DCML/XGBoost organization to improve the larger ecosystem. Since RAPIDS is iterating ahead of upstream XGBoost releases, some enhancements will be available earlier from the **[RAPIDS branch](https://github.com/rapidsai/xgboost){: target="_blank"}**, or from RAPIDS-provided installers.
{: .subtitle}

## <i class="fas fa-box-open"></i> Prerequisites for RAPIDS + XGBoost
For the latest prerequisites and supported versions, check out our **[Getting Started page](https://rapids.ai/start.html#req){: target="_blank"}**.

{% endcapture %}
{% capture download_left %}
## <i class="fas fa-laptop-code"></i> Conda Install

The default RAPIDS conda metapackage includes a recent snapshot of XGBoost by default. This package is released on the same schedule as other RAPIDS packages and tested for full compatibility. You can find the latest install options with our **[RAPIDS Release Selector](https://rapids.ai/start.html#get-rapids){: target="_blank"}**.


## <i class="fab fa-docker"></i> Docker Container
{: .section-subtitle-top-2}

Install using Docker (the latest RAPIDS release). RAPIDS provides Docker images that include a recent version of GPU-accelerated XGBoost. Just follow the Docker installation instructions with our **[RAPIDS Release Selector](https://rapids.ai/start.html#get-rapids)** page and you can start using XGBoost right away from a notebook or the command line.


{% endcapture %}
{% capture download_right %}
## <i class="fas fa-laptop-code"></i> PIP Install or Other Methods

Install using pip or other methods (the default upstream version). The default open-source XGBoost packages already include GPU support, Dask integration, and the ability to load data from a cuDF DataFrame. Follow the XGBoost instructions to install from source or use:

```bash
pip install xgboost
```

**NOTE:** Full RAPIDS integration first appeared in release 1.0 of XGBoost. Older pip packages will not include cuDF support.

{% endcapture %}
{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="0em" 
    content-single=download_single
%}
{% include section-halfs.html
    background="background-white" 
    padding-top="3em" padding-bottom="2em"
    content-left-half=download_left
    content-right-half=download_right
%}

{% capture config_single %}
# Configuring Your Code for GPUs

With only a few minor code changes, you’ll be training models on a supercharged XGBoost.
{: .subtitle}

{% endcapture %}
{% capture config_left %}
## <i class="fas fa-play"></i> The Best Place to Start

If you haven’t developed your model yet, the best place to start is **[XGBoost's Getting Started documentation](https://xgboost.readthedocs.io/en/latest/get_started.html){: target="_blank"}**. If you have an existing code to train models on CPU, converting it to run on GPUs is simple.

## <i class="far fa-file-code"></i> More Reference Materials
{: .section-subtitle-top-2}

Similar configuration options apply to R, Java, and Julia wrappers. The **[XGBoost Documentation](https://xgboost.readthedocs.io/en/latest/index.html){: target="_blank"}** and **[XGBoost GPU Support](https://xgboost.readthedocs.io/en/latest/gpu/index.html){: target="_blank"}** pages contain much more information on configuring and running models and on GPU-specific options and algorithms.

{% endcapture %}

{% capture config_right %}
## <i class="fas fa-cogs"></i> Training a Model

When training a model with XGBoost, you have to specify a dictionary of training parameters. If you set the `tree_method` parameter to `gpu_hist`, XGBoost will run on your GPU.

For example, if your old code in Python looks like:
```bash
params = {'max_depth': 3, 'learning_rate': 0.1}
dtrain = xgb.DMatrix(X, y)
xgb.train(params, dtrain)
```
Change it to:
```bash
params = {‘tree_method’: ‘gpu_hist’, 'max_depth': 3, 
'learning_rate': 0.1}
dtrain = xgb.DMatrix(X, y)
xgb.train(params, dtrain)
```

{% endcapture %}

{% include section-single.html
    background="background-white" 
    padding-top="2em" padding-bottom="0em" 
    content-single=config_single
%}
{% include section-halfs.html 
    background="background-white" 
    padding-top="0em" padding-bottom="5em" 
    content-left-half=config_left 
    content-right-half=config_right 
%} 


{% capture df_single %}
# Bridging DataFrames with XGBoost DMatrix

The RAPIDS team is contributing to the XGBoost project and integrating new features to better optimize GPU performance. 
{: .subtitle}

{% endcapture %}
{% capture df_left %}
## <i class="fas fa-border-none"></i> XGBoost DMatrix

The RAPIDS project has developed a seamless bridge between cuDF DataFrames, the primary data structure in RAPIDS, and DMatrix, XGBoost’s data structure. The DMatrix will be built from the GPU dataframe with no need to copy data through host memory. Starting in XGBoost 1.0, GPU data from cuPy and any other GPU array library with support for the `__cuda_array_interface__ API` can also be used directly to build a DMatrix.

{% endcapture %}
{% capture df_right %}
## <i class="fas fa-border-none"></i> How to Create a DMatrix

To create a DMatrix from a cuDF DataFrame, just pass the data frames to the constructor:
```bash
import xgboost as xgb
train_X_cudf = cudf.DataFrame(...)
train_y_cudf = cudf.Series(...)
dmatrix = xgb.DMatrix(train_X_cudf, label=train_y_cudf)
```

The package will automatically convert from cuDF’s format to XGBoost’s DMatrix format, keeping the data on GPU memory.

{% endcapture %}
{% include section-single.html
    background="background-white" 
    padding-top="2em" padding-bottom="0em" 
    content-single=df_single
%}
{% include section-halfs.html
    background="background-white" 
    padding-top="0sem" padding-bottom="10em"
    content-left-half=df_left
    content-right-half=df_right
%}



{% capture end_bottom %}
# Get Started with XGBoost
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

{% include cta-footer-xgboost.html 
   background="background-darkpurple" 
%}




