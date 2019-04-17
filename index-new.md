---
title: "Open GPU Data Science | RAPIDS"
og_title: "RAPIDS: A Data Science & Analytics Pipeline Accelerator"
og_description: "A suite of software libraries for executing end-to-end data science completely on GPUs"
brand_name: ""
brand_tagline: "Open GPU Data Science"
brand_button: "GET STARTED"
brand_link: "start.html"
layout: default
---
# Gpu data Science
{: .section-title-thirds}

{% capture about_top_left %}
<img class="intro-icons" src="{{ site.baseurl }}{% link /assets/images/info.svg %}" alt="about">
## About RAPIDS
The RAPIDS suite of open source software libraries gives you the freedom to execute end-to-end data science and analytics pipelines entirely on GPUs. <a href="https://rapids.ai/about.html" class="bold">Learn more <i class="fa fa-angle-double-right" aria-hidden="true"></i></a>
{% endcapture %}

{% capture about_top_middle %}
<img class="intro-icons" src="{{ site.baseurl }}{% link /assets/images/scaling-out.svg %}" alt="scaling out">
## Scale Out on GPUS
Seamless scale from GPU workstations to multi-GPU servers and multi-node clusters.
{% endcapture %}

{% capture about_top_right %}
<img class="intro-icons" src="{{ site.baseurl }}{% link /assets/images/hassle-free.svg %}" alt="hassle free">
## Hassle Free Integration
Accelerate your Python data science toolchain with minimal code changes and no new tools to learn.
{% endcapture %}

{% capture about_bottom_left %}
<img class="intro-icons" src="{{ site.baseurl }}{% link /assets/images/top-model.svg %}" alt="top model">
## Top Model Accuracy
Increase machine learning model accuracy by iterating on models faster and deploying them more frequently.
{% endcapture %}

{% capture about_bottom_middle %}
<img class="intro-icons" src="{{ site.baseurl }}{% link /assets/images/reduces.svg %}" alt="reduces">
## Reduced Training Time
Drastically improve your productivity with near-interactive data science.
{% endcapture %}

{% capture about_bottom_right %}
<img class="intro-icons" src="{{ site.baseurl }}{% link /assets/images/open-source.svg %}" alt="open source">
## Open Source
The open-source software is customizable, extensible, interoperable--supported by NVIDIA and built on Apache Arrow.
{% endcapture %}

{% include section-double-thirds.html background="background-white" content-top-left-third=about_top_left content-top-middle-third=about_top_middle content-top-right-third=about_top_right content-bottom-left-third=about_bottom_left content-bottom-middle-third=about_bottom_middle content-bottom-right-third=about_bottom_right %}



{% capture start_left %}
# Getting Started
{: .section-title-halfs}

The RAPIDS data science framework is designed to have a familiar look and feel to data scientists working in Python. Here’s a code snippet where we read in a CSV file and output some descriptive statistics. You can find more on our <a class="bold" href="https://rapids.ai/start.html">Get started section <i class="fa fa-angle-double-right" aria-hidden="true"></i></a>

```python
import cudf
gdf = cudf.read_csv('path/to/file.csv')
for column in gdf.columns:
    print(gdf[column].mean())
```
{% endcapture %}

{% capture start_right %}
## 10 Minutes to cuDF
Modeled after 10 Minutes to Pandas, this is a short introduction to cuDF that is geared mainly for new users. <a class="bold" href="https://rapidsai.github.io/projects/cudf/en/latest/10min.html">Go to guide <i class="fa fa-angle-double-right" aria-hidden="true"></i></a>

## GDF Cheat Sheet
Handy PDF reference guide for handling GPU Data Frames (GDF) with cuDF. <a class="bold" href="https://rapids.ai/assets/files/cheatsheet.pdf">Download PDF <i class="fa fa-angle-double-right" aria-hidden="true"></i></a>

## Example Notebooks
Github repository with examples of cuML using knn, dbscan, pca and tsvd, the End-to-End Mortgage demo, cuGraph demos, and more. <a class="bold" href="https://github.com/rapidsai/notebooks">Go to repo <i class="fa fa-angle-double-right" aria-hidden="true"></i></a>

{% endcapture %}
{% include section-halfs.html background="background-gray" content-left-half=start_left content-right-half=start_right %} 



# Featured News and Posts
{: .section-title-thirds}
{% include medium-thirds.html
    link1="https://medium.com/rapids-ai/the-road-to-1-0-building-for-the-long-haul-657ae1afdfd6"
    image1="https://cdn-images-1.medium.com/max/800/1*GxaubH_8eZTsNRV7FBhiyw.png"
    title1="The Road to 1.0 — Building for the Long Haul"
    desc1="RAPIDS was everywhere at NVIDIA’s GTC 2019 in Silicon Valley. It was great to see so many vendors, partners, and customers showcasing RAPIDS in their booths and presentations. Even the RAPIDS press coverage blew me away..."
    link2="https://medium.com/rapids-ai/rapids-cugraph-1ab2d9a39ec6"
    image2="https://cdn-images-1.medium.com/max/800/1*pXa2tr1z-op8xWhMuQ67-g.jpeg"
    title2="RAPIDS cuGraph "
    desc2="The Data Scientist has a collection of techniques within their proverbial toolbox. Data engineering, statistical analysis, and machine learning are among the most commonly known..."
    link3="https://medium.com/rapids-ai/rapids-can-now-be-accessed-on-databricks-unified-analytics-platform-666e42284bd1"
    image3="https://cdn-images-1.medium.com/max/800/1*QOhZrlj6IcRCuETYMmRpiA.png"
    title3="RAPIDS can now be accessed on Databricks Unified Analytics Platform "
    desc3="NVIDIA RAPIDS can now be accessed on Databricks Unified Analytics Platform, making it easy for data scientists to leverage RAPIDS for their end-to-end data science workflows... "
%}



{% include tweet-thirds.html
    tweetlink1="https://twitter.com/rapidsai/status/1113184332988997634"
    poster1="@rapidsai"
    text1="Check out the NEW RAPIDS 0.6 release with cleaner docs, feature improvements, more functionality, a new graph library, and so much more for #datascience -  https://nvda.ws/2WMsC1H "
    action1="posted by @rapidsai"
    tweetlink2="https://twitter.com/TalkPython/status/1117288613153255424"
    poster2="@TalkPython"
    text2="Make your Python zing with parallel computation using Dask. That's our topic on this week's episode of @talkpython with @mrocklin"
    action2="retweeted by @rapidsai"    
    tweetlink3="https://twitter.com/blazingdb/status/1115680801494974464"
    poster3="@blazingdb"
    text3="With #BlazingSQL + @Graphistry: Analyze log data 100x faster than comparable #ApacheSpark cluster at price parity on @rapidsai . Check out the new #blog post to  learn more, see the #code, and a #demo."
    action3="retweeted by @rapidsai"
%}



{% capture com_left %}
# RAPIDS Community
{: .section-title-halfs}
We strive for a major release every 6 weeks, give or take. Below is a general release schedule. You can also learn more on <a class="bold" href="https://medium.com/rapids-ai/the-road-to-1-0-building-for-the-long-haul-657ae1afdfd6"> our road to 1.0 post<i class="fa fa-angle-double-right" aria-hidden="true"></i></a>

## <span class="text-gray"> Previous Release: 0.5 | Jan.2019 </span>
## Current Release: 0.6 | March.2019
## <span class="text-gray"> Next Release: 0.7 | May.2019 </span>
{% endcapture %}

{% capture com_right %}
## RAPIDS APIS and Libraries
RAPIDS is open sourced under the Apache 2.0 open-source license, spanning multiple projects that range from GPU dataframes to GPU accelerated ML algoritms. Its also provides native array_interface support, allowing Apache Arrow stored data to be pushed to deep learning frameworks such as PyTorch and Chainer. Learn more on the<a class="bold" href="https://rapids.ai/about.html">about page <i class="fa fa-angle-double-right" aria-hidden="true"></i></a>

## Contributing
Whether you are new to RAPIDS, looking to help, or are part of the team, learn about our contributiong guidelines on our <a class="bold" href="https://docs.rapids.ai/contributing"> docs page<i class="fa fa-angle-double-right" aria-hidden="true"></i></a>
{% endcapture %}
{% include section-halfs.html background="background-purple" content-left-half=com_left content-right-half=com_right %} 



{% capture lib_top_left %}
## cuDF
cuDF is a Python GPU DataFrame library (built on the <a href="http://arrow.apache.org/" target="_blank">Apache Arrow</a> columnar memory format) for loading, joining, aggregating, filtering, and otherwise manipulating data.
<br>
<a href="" class="lib-link">GitHub</a> | <a href="" class="lib-link">Docs</a> | <a href="" class="lib-link">Change Log</a> | <a href="" class="lib-link">Roadmap</a>
{% endcapture %}

{% capture lib_top_middle %}
## cuML
cuML is a suite of libraries that implement machine learning algorithms and mathematical primitives functions that share compatible APIs with other RAPIDS projects.
<br>
<a href="" class="lib-link">GitHub</a> | <a href="" class="lib-link">Docs</a> | <a href="" class="lib-link">Change Log</a> | <a href="" class="lib-link">Roadmap</a>
{% endcapture %}

{% capture lib_top_right %}
## cuGraph
cuGraph is a collection of graph analytics that process data found in a GPU Dataframe. cuGraph aims at provides a NetworkX-like API that will be familiar to data scientists, so they can now build GPU-accelerated workflows more easily.
<br>
<a href="" class="lib-link">GitHub</a> | <a href="" class="lib-link">Docs</a> | <a href="" class="lib-link">Change Log</a> | <a href="" class="lib-link">Roadmap</a>
{% endcapture %}

{% capture lib_bottom_left %}
## nvStrings
nvStrings (the Python bindings for <a href="https://github.com/rapidsai/custrings" target="_blank"> cuStrings</a>), provides a pandas-like API that will be familiar to data engineers & data scientists, so they can use it to easily accelerate their workflows without going into the details of CUDA programming.
<br>
<a href="" class="lib-link">GitHub</a> | <a href="" class="lib-link">Docs</a> | <a href="" class="lib-link">Change Log</a> | <a href="" class="lib-link">Roadmap</a>
{% endcapture %}

{% capture lib_bottom_middle %}
## libcudf
libcudf is a C/C++ CUDA library for implementing standard dataframe operations.
<br>
<a href="" class="lib-link">GitHub</a> | <a href="" class="lib-link">Docs</a> | <a href="" class="lib-link">Change Log</a> | <a href="" class="lib-link">Roadmap</a>
{% endcapture %}

{% capture lib_bottom_right %}
## RMM 
RAPIDS Memory Manager (RMM) is a central place for all device memory allocations in cuDF (C++ and Python) and other RAPIDS libraries. In addition, it is a replacement allocator for CUDA Device Memory (and CUDA Managed Memory) and a pool allocator to make CUDA device memory allocation / deallocation faster and asynchronous.
<br>
<a href="" class="lib-link">GitHub</a> | <a href="" class="lib-link">Docs</a> | <a href="" class="lib-link">Change Log</a> | <a href="" class="lib-link">Roadmap</a>
{% endcapture %}

{% include section-double-thirds.html background="background-purple" content-top-left-third=lib_top_left content-top-middle-third=lib_top_middle content-top-right-third=lib_top_right content-bottom-left-third=lib_bottom_left content-bottom-middle-third=lib_bottom_middle content-bottom-right-third=lib_bottom_right %}



# Contributors
{: .section-title-full}
{% include contributing-logos.html %}



# Adopters
{: .section-title-full}
{% include adopter-logos.html %}



# Open Source
{: .section-title-full}
{% include open-source-logos.html %}


{% include cta-footer.html 
name="Experience Data Science on GPUs with RAPIDS" 
tagline=""
button="GET STARTED"
link="start.html"
%}

