---
title: Open GPU Data Science | RAPIDS
layout: home
---

<section class="about-rapids">
    <div class="fixed-content">
        <h2>About RAPIDS</h2>
        <p>The RAPIDS suite of open source software libraries gives you the freedom to execute end-to-end data science and analytics
            pipelines entirely on GPUs. It relies on <a href="https://developer.nvidia.com/cuda-toolkit"
                                                        target="_blank">NVIDIA® CUDA® </a> primitives for low-level
            compute optimization, but exposes that GPU parallelism and high-bandwidth memory speed through user-friendly
            Python interfaces. <br> <br> RAPIDS also focuses on common data preparation tasks for analytics and data
            science. This includes a familiar DataFrame API that integrates with a variety of machine learning
            algorithms for end-to-end pipeline accelerations without paying typical serialization costs. RAPIDS also
            includes support for multi-node, multi-GPU deployments, enabling vastly accelerated processing and training
            on much larger dataset sizes. </p>
        <div class="rapids-perfomance">
            <br><br>
            <img src="assets/images/rapids-end-to-end-performance-chart-oss-page-r4.svg" alt="End to end Performance Chat"><br>
            <br>
        </div>
    </div>
</section>

<section class="gpu-pipeline">
    <div class="top-purple-strip"></div>
    <div class="gpu-pipeline-container">
        <div class="fixed-content">
            <h2>The New GPU <br> Data Science Pipeline</h2>
            <div class="Pipeline-Diagram"><img src="assets/images/Pipeline-FPO-Diagram.png" alt="" title=""></div>
            <div class="apache-arrow">
                <!--
                <div class="apache-arrow-inner">
                    <span><img src="assets/images/apache-arrow.svg" alt="" title=""></span>
                    <span>Apache <br> Arrow</span>
                </div>
                -->
            </div>
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

        </div>
    </div>
</section>

<section class="features-main">
    <div class="features-content">
        <div class="fixed-content">
            <h2>Features of RAPIDS </h2>

            <div class="features-row">
                <ul>
                    <li>
                        <img src="assets/images/hassle-free.svg" alt="hassle free">
                        <h3>Hassle-Free Integration</h3>
                        <p>Accelerate your Python data science toolchain with minimal code changes and no new tools to
                            learn.</p>
                    </li>

                    <li>
                        <img src="assets/images/scaling-out.svg" alt="scaling out">
                        <h3>Scaling Out <br> on Any GPU</h3>
                        <p>Seamless scale from GPU workstations to multi-GPU servers and multi-node clusters.</p>
                    </li>

                    <li>
                        <img src="assets/images/top-model.svg" alt="top model">
                        <h3>Top Model Accuracy</h3>
                        <p>Increase machine learning model accuracy by iterating on models faster and deploying them
                            more frequently.</p>
                    </li>
                </ul>
            </div>

            <div class="features-row">
                <ul>


                    <li>
                        <img src="assets/images/reduces.svg" alt="reduces">
                        <h3>Reduced <br> Training Time</h3>
                        <p>Drastically improve your productivity with near-interactive data science.</p>
                    </li>

                    <li>
                        <img src="assets/images/open-source.svg" alt="open source">
                        <h3>Open <br> Source</h3>
                        <p>The open-source software is customizable, extensible, interoperable--supported by NVIDIA and
                            built on Apache Arrow.</p>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <div class="top-gray-strip"></div>
</section>

<section class="community-main">
    <div class="fixed-content">
        <div class="community-content-inner">
            <h2>Community</h2>
            <p>RAPIDS is for everyone--users, adopters, and contributors. If you’re a data scientist, researcher,
                engineer, or developer using pandas, Dask, scikit-learn, or Spark on CPUs and looking for 50X end-to-end
                pipeline speedups at scale, look no further. Downloads RAPIDS and give us a run. RAPIDS is open sourced
                under the Apache 2.0 open source license and intended to be built upon and hardened in the community.
                While significant time and effort has been invested into making the platform usable and relevant, we
                need active contributors to help improve it and build its future.</p>
            <a href="community.html" class="blue-btn">JOIN NOW</a>
        </div>
    </div>
</section>

<section class="contributing-partner">
    <div class="fixed-content">
        <h3>Community Contributors</h3>
        <div class="contributing-logos">
            <div class="contributing-logo">
                <img src="assets/images/anaconda.png" alt="anaconda">
            </div>
            <div class="contributing-logo">
                <img src="assets/images/blazingdb.png" alt="blazingdb">
            </div>
            <div class="contributing-logo">
                <img src="assets/images/Gunrock_Color.png" alt="gunrock">
            </div>
            <div class="contributing-logo">
                <img src="assets/images/NVLogo_2D_H.png" alt="nvidia">
            </div>
            <div class="contributing-logo">
                <img src="assets/images/quansight.png" alt="quantsight">
            </div>
            <div class="contributing-logo">
                <img src="assets/images/scikit-learn_Color.png" alt="scikitlearn">
            </div>
        </div>
    </div>
</section>

<section class="contributing-partner">
    <div class="fixed-content">
        <h3>Ecosystem Partners</h3>
        <div class="contributing-logos">
            
            <div class="contributing-logo">
                <img src="assets/images/Chainer-logo.png" alt="chainer">
            </div>
            
            <div class="contributing-logo">
                <img src="assets/images/databricks-logo.png" alt="databricks">
            </div>
            
            <div class="contributing-logo">
                <img src="assets/images/graphistry.png" alt="graphistry">
            </div>
            
            <div class="contributing-logo">
                <img src="assets/images/gpu-ventures-h2o-ai-logo.png" alt="h20ai">
            </div>
           
            <div class="contributing-logo">
                <img src="assets/images/ibm-logo.png" alt="ibm">
            </div>

            <div class="contributing-logo">
                <img src="assets/images/INRIA_CORPO_SANS_SIGNATURE_RVB.png" alt="inria">
            </div>

            <div class="contributing-logo">
                <img src="assets/images/MapR_Color.png" alt="mapr">
            </div>

            <div class="contributing-logo">
                <img src="assets/images/omni_sci_logo.png" alt="omnisci">
            </div>

            <div class="contributing-logo">
                <img src="assets/images/PyTorch_logo.png" alt="pytorch">
            </div>

            <div class="contributing-logo">
                <img src="assets/images/uber_logo_2018.png" alt="uber">
            </div>

            <div class="contributing-logo">
                <img src="assets/images/ursa_logo.png" alt="ursa">
            </div>

            <div class="contributing-logo">
                <img src="assets/images/walmart_labs.png" alt="walmart">
            </div>

        </div>
    </div>
</section>

<section class="footer-cta-main">
    <div class="fixed-content">
        <h2>Experience Data Science on GPUs with RAPIDS</h2>
        <a href="documentation.html" class="blue-btn">GET STARTED</a>
    </div>
</section>
