---
title: "Open GPU Data Science | RAPIDS"
og_title: "RAPIDS: A Data Science & Analytics Pipeline Accelerator"
og_description: "A suite of software libraries for executing end-to-end data science completely on GPUs"
brand_name: ""
brand_tagline: "More About RAPIDS"
brand_button: "LEARN MORE"
brand_link: "https://medium.com/rapids-ai"
layout: default
---

{% capture about_top_left %}
# About RAPIDS 
{: .section-title-halfs}

The RAPIDS suite of open source software libraries and APIs gives you the ability to execute end-to-end data science and analytics pipelines entirely on GPUs. RAPIDS is incubated by <strong>[NVIDIA®](https://developer.nvidia.com/open-source){: target="_blank"}</strong> based on extensive hardware and data science science experience. RAPIDS utilizes <strong>[NVIDIA CUDA®](https://developer.nvidia.com/cuda-toolkit){: target="_blank"}</strong> primitives for low-level compute optimization, and exposes GPU parallelism and high-bandwidth memory speed through user-friendly Python interfaces.

RAPIDS also focuses on common data preparation tasks for analytics and data science. This includes a familiar DataFrame API that integrates with a variety of machine learning algorithms for end-to-end pipeline accelerations without paying typical serialization costs. RAPIDS also includes support for multi-node, multi-GPU deployments, enabling vastly accelerated processing and training on much larger dataset sizes.

## Apache Arrow
RAPIDS had its start from the <a href="https://arrow.apache.org/" class="bold" target="_blank">Apache Arrow</a> and <a href="http://gpuopenanalytics.com/#/f" class="bold" target="_blank">GoAi</a> projects based on a columnar, in-memory data structure that delivers efficient and fast data interchange with flexibility to support complex data models.

{% endcapture %}

{% capture about_top_right %}
## Libraries and APIs Overview
{: .section-subtitle-top}

Some RAPIDS projects include <a href="https://github.com/rapidsai/cudf" class="bold" target="_blank">cuDF</a>, a DataFrame manipulation library; <a href="https://github.com/rapidsai/cuml" class="bold" target="_blank">cuML</a>, a collection of machine learning libraries that will provide GPU versions of algorithms available in scikit-learn; <a href="https://github.com/rapidsai/cugraph" class="bold" target="_blank">cuGraph</a>, a collection of graph analytics libraries that seamlessly integrate into the RAPIDS data science platform. Development follows a 6 week release schedule, so new features and libraries are always on the way. 

## Integration With Deep Learning Libraries
RAPIDS provides native array_interface support. This means data stored in Apache Arrow can be seamlessly pushed to deep learning frameworks that accept array_interface such as PyTorch and Chainer. 

## Visualization
Our focus on Python allows RAPIDS to play well with most data science visualization libraries. For even greater performance, we are working towards deeper integration with these libraries since a native GPU in-memory data format provides high-performance, high-FPS data visualization capabilities, even with very large datasets.
{% endcapture %}

{% capture about_bottom_left %}
<img class="half-image" src="{{ site.baseurl }}{% link /assets/images/EaseVsPerformance.svg %}" alt="ease">
{: .flex-center}
{% endcapture %}

{% capture about_bottom_right %}
<img class="full-image" src="{{ site.baseurl }}{% link /assets/images/rapids-end-to-end-performance-chart-oss-page-r4.svg %}" alt="performance">
{: .flex-center}
{% endcapture %}

{% include section-double-halfs.html
    background="background-white" 
    padding-top="0" padding-bottom="2" 
    content-top-left-half =about_top_left 
    content-top-right-half=about_top_right
    content-bottom-left-half =about_bottom_left
    content-bottom-right-half =about_bottom_right 
%} 

{% include slopecap.html 
    background="background-darkpurple" 
    position="top" 
    slope="up"
%}
{% include cta-footer.html 
name="Learn more about Data Science on GPUs with RAPIDS" 
tagline=""
button="LEARN MORE"
link="https://medium.com/rapids-ai"
%}

