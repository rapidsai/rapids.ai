---
title: "Open GPU Data Science | RAPID"
og_title: "RAPIDS: A Data Science & Analytics Pipeline Accelerator"
og_description: "A suite of software libraries for executing end-to-end data science completely on GPUs"
brand_name: ""
brand_tagline: "Open GPU Data Science"
brand_button: "GET STARTED"
brand_link: "documentation.html"
layout: default
---
{% capture section_intro %}
## About RAPIDS

The RAPIDS suite of open source software libraries gives you the freedom to execute end-to-end data science and analytics pipelines entirely on GPUs. RAPIDS is incubated by [NVIDIA&reg;](https://nvidia.com) based on years of accelerated data science experience, it relies on [NVIDIA CUDA&reg;](https://developer.nvidia.com/cuda-toolkit) primitives for low-level compute optimization. RAPIDS exposes GPU parallelism and high-bandwidth memory speed through user-friendly Python interfaces.
{: .h5 }

RAPIDS also focuses on common data preparation tasks for analytics and data science. This includes a familiar DataFrame API that integrates with a variety of machine learning algorithms for end-to-end pipeline accelerations without paying typical serialization costs. RAPIDS also includes support for multi-node, multi-GPU deployments, enabling vastly accelerated processing and training on much larger dataset sizes.
{: .h5 }

![End to end Performance Chat]({{ site.baseurl }}{% link /assets/images/rapids-end-to-end-performance-chart-oss-page-r4.svg %})
{: .rapids-perfomance .text-center .pad-top-40 }

{% endcapture %}
{% include sec-white.html content=section_intro %}

{% capture section_pipeline %}
## The New GPU <br> Data Science Pipeline

![RAPIDS Pipeline Diagram]({{ site.baseurl }}{% link /assets/images/Pipeline-FPO-Diagram.png %})
{: .Pipeline-Diagram .text-center }

<div class="gpu-list">
    <ul>
        <li>Apache Arrow <span>This is a columnar, in-memory data structure that delivers efficient and fast data interchange with flexibility to support complex data models.</span>
        </li>
        <li>cuDF<span>The RAPIDS cuDF library is a DataFrame manipulation library based on Apache Arrow that accelerates loading, filtering, and manipulation of data for model training data preparation. The Python bindings of the core-accelerated CUDA DataFrame manipulation primitives mirror the pandas interface for seamless onboarding of pandas users.</span>
        </li>
        <li>cuML<span>RAPIDS cuML is a collection of GPU-accelerated machine learning libraries that will provide GPU versions of all machine learning algorithms available in scikit-learn.</span>
        </li>
    </ul>
    <ul>
        <li>cuGRAPH<span>This is a framework and collection of graph analytics libraries that seamlessly integrate into the RAPIDS data science platform.</span>
        </li>
        <li>Deep Learning Libraries<span>RAPIDS provides native array_interface support. This means data stored in Apache Arrow can be seamlessly pushed to deep learning frameworks that accept array_interface such as PyTorch and Chainer.</span>
        </li>
        <li>Visualization Libraries Coming Soon<span>RAPIDS will include tightly integrated data visualization libraries based on Apache Arrow. Native GPU in-memory data format provides high-performance, high-FPS data visualization, even with very large datasets.</span>
        </li>
    </ul>
</div>
{% endcapture %}
{% include sec-left-purple.html content=section_pipeline %}

{% capture section_features %}
## Features of RAPIDS

<div class="features-row">
    <ul>
        <li>
            <img src="{{ site.baseurl }}{% link /assets/images/hassle-free.svg %}" alt="hassle free">
            <h3>Hassle-Free Integration</h3>
            <p>Accelerate your Python data science toolchain with minimal code changes and no new tools to
                learn.</p>
        </li>
        <li>
            <img src="{{ site.baseurl }}{% link /assets/images/scaling-out.svg %}" alt="scaling out">
            <h3>Scaling Out <br> on Any GPU</h3>
            <p>Seamless scale from GPU workstations to multi-GPU servers and multi-node clusters.</p>
        </li>
        <li>
            <img src="{{ site.baseurl }}{% link /assets/images/top-model.svg %}" alt="top model">
            <h3>Top Model Accuracy</h3>
            <p>Increase machine learning model accuracy by iterating on models faster and deploying them
                more frequently.</p>
        </li>
    </ul>
</div>

<div class="features-row">
    <ul>
        <li>
            <img src="{{ site.baseurl }}{% link /assets/images/reduces.svg %}" alt="reduces">
            <h3>Reduced <br> Training Time</h3>
            <p>Drastically improve your productivity with near-interactive data science.</p>
        </li>
        <li>
            <img src="{{ site.baseurl }}{% link /assets/images/open-source.svg %}" alt="open source">
            <h3>Open <br> Source</h3>
            <p>The open-source software is customizable, extensible, interoperable--supported by NVIDIA and
                built on Apache Arrow.</p>
        </li>
    </ul>
</div>
{% endcapture %}
{% include sec-right-gray.html content=section_features %}

{% capture section_community %}
## Community

RAPIDS is for everyone--users, adopters, and contributors. If you’re a data scientist, researcher, engineer, or developer using pandas, Dask, scikit-learn, or Spark on CPUs and looking for 50X end-to-end pipeline speedups at scale, look no further. Downloads RAPIDS and give us a run. RAPIDS is open sourced under the Apache 2.0 open source license and intended to be built upon and hardened in the community. While significant time and effort has been invested into making the platform usable and relevant, we need active contributors to help improve it and build its future.
{: .h5 }

[JOIN NOW](community.html){: .blue-btn }
{: .text-center }

### Community Contributors
{: .text-center .pad-btm-40 }

<div class="contributing-logos">
    <div class="contributing-logo">
        <img src="{{ site.baseurl }}{% link /assets/images/anaconda.png %}" alt="anaconda">
    </div>
    <div class="contributing-logo">
        <img src="{{ site.baseurl }}{% link /assets/images/blazingdb.png %}" alt="blazingdb">
    </div>
    <div class="contributing-logo">
        <img src="{{ site.baseurl }}{% link /assets/images/Gunrock_Color.png %}" alt="gunrock">
    </div>
    <div class="contributing-logo">
        <img src="{{ site.baseurl }}{% link /assets/images/NVLogo_2D_H.png %}" alt="nvidia">
    </div>
    <div class="contributing-logo">
        <img src="{{ site.baseurl }}{% link /assets/images/quansight.png %}" alt="quantsight">
    </div>
    <div class="contributing-logo">
        <img src="{{ site.baseurl }}{% link /assets/images/scikit-learn_Color.png %}" alt="scikitlearn">
    </div>
</div>

### Ecosystem Partners
{: .text-center .pad-btm-40 }

<div class="contributing-logos">
    <div class="contributing-logo">
        <img src="{{ site.baseurl }}{% link /assets/images/Chainer-logo.png %}" alt="chainer">
    </div>
    <div class="contributing-logo">
        <img src="{{ site.baseurl }}{% link /assets/images/databricks-logo.png %}" alt="databricks">
    </div>
    <div class="contributing-logo">
        <img src="{{ site.baseurl }}{% link /assets/images/graphistry.png %}" alt="graphistry">
    </div>
    <div class="contributing-logo">
        <img src="{{ site.baseurl }}{% link /assets/images/gpu-ventures-h2o-ai-logo.png %}" alt="h20ai">
    </div>
    <div class="contributing-logo">
        <img src="{{ site.baseurl }}{% link /assets/images/ibm-logo.png %}" alt="ibm">
    </div>
    <div class="contributing-logo">
        <img src="{{ site.baseurl }}{% link /assets/images/INRIA_CORPO_SANS_SIGNATURE_RVB.png %}" alt="inria">
    </div>
    <div class="contributing-logo">
        <img src="{{ site.baseurl }}{% link /assets/images/MapR_Color.png %}" alt="mapr">
    </div>
    <div class="contributing-logo">
        <img src="{{ site.baseurl }}{% link /assets/images/omni_sci_logo.png %}" alt="omnisci">
    </div>
    <div class="contributing-logo">
        <img src="{{ site.baseurl }}{% link /assets/images/PyTorch_logo.png %}" alt="pytorch">
    </div>
    <div class="contributing-logo">
        <img src="{{ site.baseurl }}{% link /assets/images/uber_logo_2018.png %}" alt="uber">
    </div>
    <div class="contributing-logo">
        <img src="{{ site.baseurl }}{% link /assets/images/ursa_logo.png %}" alt="ursa">
    </div>
    <div class="contributing-logo">
        <img src="{{ site.baseurl }}{% link /assets/images/walmart_labs.png %}" alt="walmart">
    </div>
</div>
{% endcapture %}
{% include sec-white.html content=section_community %}


{% include cta-footer.html 
name="Experience Data Science on GPUs with RAPIDS" 
tagline=""
button="GET STARTED"
link="documentation.html"
%}

