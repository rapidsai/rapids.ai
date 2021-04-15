---
title: "RAPIDS + NVIDIA Merlin"
description: "Learn How to Use RAPIDS with Merlin"
tagline: "RAPIDS + NVIDIA Merlin"
button_text: "NVTabular"
button_link: "https://developer.nvidia.com/nvidia-merlin"
layout: default
---

![NVIDIA]({{ site.baseurl }}{% link /assets/images/NVLogo_2D_H.png %}){: .projects-logo}


# Scale and Accelerate <br> Recommender Systems on GPUs
{: .section-title-full}

{% capture intro_content %}

NVIDIA Merlin is an open source library designed to accelerate recommender systems on NVIDIA GPUs. It enables data scientists, machine learning engineers, and researchers to build high-performing recommenders at scale. Merlin includes tools to address common ETL, training, and inference challenges. Each stage of the Merlin pipeline is optimized to support hundreds of terabytes of data, which is all accessible through easy-to-use APIs. With Merlin, better predictions and increased click-through rates are within reach.
{: .subtitle}

{% endcapture %}

{% include section-single.html
    background="background-white" 
    padding-top="0em" padding-bottom="0em" 
    content-single=intro_content
%}

{% capture yd_left %}
## <i class="fas fa-layer-group"></i> Accelerated ETL
As the ETL component of the Merlin ecosystem, NVTabular is a feature engineering and preprocessing library for tabular data. It is designed to quickly and easily manipulate terabyte scale datasets that are used to train deep learning based recommender systems. NVTabular uses RAPIDS’ `dask_cudf` to perform GPU-accelerated transformation.

**[Read more about NVTabular’s  features <i class="fas fa-angle-double-right"></i>](https://nvidia.github.io/NVTabular/main/core_features.html){: target="_blank"}**

{% endcapture %}
{% capture yd_mid %}
## <i class="far fa-chart-network"></i> Accelerated Training
When training deep learning recommender system models, data loading can be a bottleneck. Merlin accelerates the training of deep learning recommender systems using RAPIDS’ cuDF and DaskcuDF to read asynchronous parquet files. This is used to speed-up existing TensorFlow and PyTorch training pipelines **or** used with HugeCTR to train deep learning recommender systems written in CUDA C++. 

**[Read more about accelerated training <i class="fas fa-angle-double-right"></i>](https://nvidia.github.io/NVTabular/main/training/index.html){: target="_blank"}**

{% endcapture %}
{% capture yd_right %}
## <i class="fal fa-waveform-path"></i> Accelerated Inference 
NVTabular and HugeCTR both support the Triton Inference Server to provide GPU-accelerated inference. The Triton Inference Server simplifies the deployment of AI models to production at scale. It is an inference serving software that is open source and lets teams deploy trained AI models from any framework. The NVTabular ETL workflow and trained deep learning models can be easily deployed to production with only a few steps.

**[Read more about inference from examples <i class="fas fa-angle-double-right"></i>](https://github.com/NVIDIA/NVTabular/tree/main/examples/inference_triton){: target="_blank"}**


{% endcapture %}

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

It is easy to get started with Merlin. There are many examples and blog posts to reference.

## <i class="fas fa-bolt"></i> Try Now Online
Try on Kaggle with: 
<br>
**[GPU-accelerated ETL with NVTabular <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://www.kaggle.com/benediktschifferer/faster-etl-for-tabular-data){: target="_blank"}**
<br>
**[Accelerated training pipelines in PyTorch and FastAI <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://www.kaggle.com/benediktschifferer/faster-fastai-tabular-deep-learning){: target="_blank"}**

{% endcapture %}

{% capture start_right %}
## <i class="far fa-bookmark"></i> Try Our Notebook Examples
{: .section-subtitle-top-1}
NVTabular and HugeCTR both provide a collection of examples based on a variety of recommender system datasets that are publicly available. Checkout the **[NVTabular notebooks](https://github.com/NVIDIA/NVTabular/tree/main/examples){: target="_blank"}** and **[HugeCTR notebooks](https://github.com/NVIDIA/HugeCTR/tree/master/notebooks){: target="_blank"}**. 

## <i class="fab fa-docker"></i> Pull Our Docker Container
Merlin published docker containers with pre-installed versions of the latest release on **[NVIDIA's NGC repository](https://ngc.nvidia.com/catalog/containers?orderBy=modifiedDESC&pageNumber=0&query=%20label%3A%22Merlin%22&quickFilter=containers&filters=){: target="_blank"}**. Pull the container and try out Merlin yourself.


## <i class="far fa-file-code"></i> See The Latest Docs
Access our current installations, guides, and tutorials in latest documentations for **[NVTabular](https://nvidia.github.io/NVTabular/main/Introduction.html){: target="_blank"}** and **[HugeCTR](https://github.com/NVIDIA/HugeCTR/blob/master/docs/hugectr_user_guide.md){: target="_blank"}**.

## <i class="fal fa-newspaper"></i> Read Our Blogs
Learn more about recommender systems and Merlin on our **[Blog](https://medium.com/nvidia-merlin){: target="_blank"}**.

{% endcapture %}
{% include slopecap.html 
    background="background-gray" 
    position="top" 
    slope="up" 
%}
{% include section-halfs.html 
    background="background-gray" 
    padding-top="10em" padding-bottom="5em" 
    content-left-half=start_left 
    content-right-half=start_right 
%} 


{% capture nv_l %}
## <i class="fas fa-layer-group"></i> Accelerate ETL <br> with NVTabular <br>

![NVIDIA]({{ site.baseurl }}{% link /assets/images/merlin_tab_chart.png%}){: .full-image-center}

NVTabular is capable of scaling ETL over multiple GPUs and nodes. NVTabular can process the Criteo 1TB Clicks Ads dataset in 13.8 minutes on a GPU and 1.9 minutes on eight GPUs, which is the largest, publicly available recommendation dataset that contains 1.3TB of uncompressed click logs with roughly 4 billion users. NVTabular’s processing time is much faster compared to the original NumPy script that requires 5 days (7200 minutes) and an optimized spark cluster that requires 3 hours (180 minutes). That accounts for a **speedup of 100 times to 3700 times**.

**[Read more in our blogpost <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://developer.nvidia.com/blog/announcing-the-nvtabular-open-beta-with-multi-gpu-support-and-new-data-loaders/){: target="_blank"}**
{% endcapture %}

{% capture nv_r %}
## <i class="fal fa-chart-network"></i> Accelerate DL Training <br> with HugeCTR

![NVIDIA]({{ site.baseurl }}{% link /assets/images/merlin_huge_chart.png %}){: .full-image-center}

MLPerf is a consortium of AI leaders from academia, research labs, and industry whose mission is to “build fair and useful benchmarks” that provide unbiased evaluations of training and inference. HugeCTR on DGX-A100 is the fastest commercial solution available to train Facebook’s Deep Learning Recommender Model on 4TB of data. It finishes the training in 3.33 min and is **13.5x faster** than the best CPU-only solution.

**[Read more in our blogpost <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://developer.nvidia.com/blog/accelerating-recommender-systems-training-with-nvidia-merlin-open-beta/){: target="_blank"}**
{% endcapture %}

{% include section-halfs.html
    background="background-gray" 
    padding-top="3em" padding-bottom="10em" 
    content-left-half=nv_l
    content-right-half=nv_r
%}

{% capture end_bottom %}
# Get Started with NVIDIA Merlin
{: .section-title-full .text-white}

{% endcapture %}
{% include slopecap.html 
    background="background-darkpurple" 
    position="top" 
    slope="down" 
%}
{% include section-single.html
    background="background-darkpurple" 
    padding-top="3em" padding-bottom="0em" 
    content-single=end_bottom
%}

{% include cta-footer-merlin.html 
   background="background-darkpurple" 
%}
