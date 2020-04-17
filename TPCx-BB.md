---
title: "RAPIDS + TPC-XBB"
description: "Learn How RAPIDS Performs on TPCx-BB"
tagline: "Benchmarking RAPIDS with TPCx-BB"
button_text: "TPC.org"
button_link: "http://www.tpc.org/tpcx-bb/default.asp"
layout: default
---
![TPCxbb]({{ site.baseurl }}{% link /assets/images/tpc-reg.gif %}){: .projects-logo}

# TPCx-BB Benchmark Performance of RAPIDS
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

<div id="barChart"></div>


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
## <i class="fas fa-layer-group"></i> Dataframe and ETL Integration
The RAPIDS **[cuDF library](https://github.com/rapidsai/cudf){: target="_blank"}** provides a GPU-backed dataframe class that replicates the popular pandas API. It includes extremely high-performance functions to load CSV, JSON, ORC, Parquet and other file formats directly into GPU memory, eliminating one of the key bottlenecks in many data processing tasks. cuDF includes a variety of other functions supporting GPU-accelerated ETL, such as data subsetting, transformations, one-hot encoding, and more. The RAPIDS team maintains a **[dask-cudf library](https://github.com/rapidsai/cudf/tree/master/python/dask_cudf){: target="_blank"}** that includes helper methods to use Dask and cuDF.
{% endcapture %}

{% capture gpus_xgb %}
## <i class="fas fa-bezier-curve"></i> XGBoost Integration
XGBoost, the popular open source machine learning library for gradient boosting, now includes integrated support for Dask. Users can partition data across nodes using Dask’s standard data structures, build a DMatrix on each GPU using `xgboost.dask.create_worker_dmatrix`, and then launch training through `xgboost.dask.run`. See the **[XGBoost dask documentation](https://ml.dask.org/xgboost.html){: target="_blank"}** or the **[Dask+XGBoost GPU example code](https://github.com/dmlc/xgboost/tree/master/demo/dask){: target="_blank"}** for more details.

New users should check out our **[XGBoost page](https://rapids.ai/xgboost.html){: target="_blank"}** and the **[10 Minutes to Dask-XGBoost guide](https://rapidsai.github.io/projects/cudf/en/{{ site.data.releases.stable-docs }}/dask-xgb-10min.html){: target="_blank"}** to get started quickly.
{% endcapture %}

{% include section-halfs.html
    background="background-gray" 
    padding-top="0em" padding-bottom="5em" 
    content-left-half=gpus_df
    content-right-half=gpus_xgb
%}

{% capture gpus_ml%}
## <i class="fas fa-sliders-h"></i> Integration With Other ML Algorithms 
For other machine learning work on GPU, the **[cuML library](https://github.com/rapidsai/cuml/tree/master/python/cuml/dask){: target="_blank"}** provides a access to the RAPIDS cuML package with Dask. RAPIDS cuML implements popular machine learning algorithms, including clustering, dimensionality reduction, and regression approaches, with high performance GPU-based implementations, offering speedups of up to **100x** over CPU-based approaches. cuML replicates the scikit-learn API, so it integrates well with projects like Dask that include scikit-learn support. Currently, dask-cuml supports distributed clustering and regression algorithms, with new algorithms are being added over time.
{% endcapture %}

{% capture gpus_nb %}
## <i class="far fa-bookmark"></i> Example Notebooks
The RAPIDS Notebooks Extended repository includes several examples with end-to-end examples using Dask for distributed, GPU-accelerated computation. Here’s a few from the collection to get started with. 


<i class="fas fa-caret-right"></i> The Introductino to Dask shows how to get started with Dask using basic Python primitives like integers and strings. **[Go to notebook <i class="fas fa-angle-double-right"></i>](https://github.com/rapidsai/notebooks-contrib/blob/master/getting_started_notebooks/basics/Getting_Started_with_Dask.ipynb){: target="_blank"}**
{: .no-tb-margins }

<i class="fas fa-caret-right"></i> Introduction to XGBoost with RAPIDS shows the acceleration one can gain by using GPUs with XGBoost in RAPIDS. **[Go to notebook <i class="fas fa-angle-double-right"></i>](https://github.com/rapidsai/notebooks/blob/master/xgboost/XGBoost_Demo.ipynb){: target="_blank"}**
{: .no-tb-margins }

<i class="fas fa-caret-right"></i> The Linear Regression with Dask+cuML shows a simple example of how to get started with distributed machine learning. **[Go to notebook <i class="fas fa-angle-double-right"></i>](https://github.com/rapidsai/notebooks-contrib/blob/a236188a08ba7ec77a55ec48e5a5a1d6e81c9895/tutorials/examples/linear_regression_dask_cuml.ipynb){: target="_blank"}**
{: .no-tb-margins }

<i class="fas fa-caret-right"></i> The NYC Taxi End-to-End notebook uses trip data to predict New York City taxi fares (a regression problem). **[Go to notebook <i class="fas fa-angle-double-right"></i>](https://github.com/efajardo-nv/rapids-dataproc/blob/master/notebooks/NYCTaxi-E2E.ipynb){: target="_blank"}**
{: .no-tb-margins }

{% endcapture %}

{% include section-halfs.html
    background="background-gray" 
    padding-top="0em" padding-bottom="10em" 
    content-left-half=gpus_ml
    content-right-half=gpus_nb
%}


{% capture usecase_single %}
# Use Cases

Dask is widely and routinely used, running on everything from laptops to thousand-machine clusters in-house, on the cloud, and on high-performance computing (HPC) supercomputers. Its ability to process hundreds of terabytes of data efficiently makes it a powerful tool in three key areas. See how Dask is being used across industry by reading stories from other **[Dask users](https://stories.dask.org/en/latest/){: target="_blank"}** and see specific examples of how **[people are using Dask](https://stories.dask.org/en/latest/){: target="_blank"}**.
{: .subtitle}

{% endcapture %}

{% capture uc_left %}
## <i class="fas fa-server"></i> HPC

Dask makes it easy to quickly analyze large, multi-dimensional datasets. It provides the same interactivity and ease of development as a system like Spark but is much more aligned to scientific processing, with native code execution, direct integration with systems like SLURM and PBS, and data models that fit multi-dimensional and spatial workloads. It’s also well tuned for high-performance networks and accelerator hardware.

{% endcapture %}
{% capture uc_right %}
## <i class="fas fa-hand-holding-usd"></i> Financial Services
Many financial institutions have large, complex codebases that encode significant business logic, but they now need parallelism. Their systems are more complex than just “a big pandas dataframe” or “a big NumPy array.” These groups use Dask’s lower-level APIs (Delayed, Futures) to add task scheduling and parallelism as a lightweight way to scale out their systems without costly rewrites.

{% endcapture %}
{% capture uc_2_left %}
## <i class="fas fa-store-alt"></i> Retail

Data science and devops teams in the retail industry use Dask to scale their pipelines; taking pandas and machine learning workloads to terabytes of data easily. The Dask interface makes it easy to load in terabytes of tabular data, transform the data with libraries like pandas or RAPIDS cuDF using parallel compute, and pass it off to machine learning–training libraries at scale. One major retailer is using RAPIDS and Dask to generate more accurate forecasting models. **[See how in this video <i class="fas fa-angle-double-right"></i>](https://www.youtube.com/watch?v=OQjko2H7xec&feature=youtu.be){: target="_blank"}**

{% endcapture %}
{% capture uc_2_right %}
## <i class="fas fa-network-wired"></i> Cyber Security
Today’s cybersecurity challenges are data science and engineering challenges. A traditional Security Operations Center (SOC) relies on heuristics and manual triage of alerts, and the amount of logs being generated and kept is increasing while the percentage of those logs used is reducing due to staffing shortages. RAPIDS and CLX provide accelerated workflows and I/O for these use cases, targeting acceleration from the cybersecurity primitive level (e.g., IPv4 and DNS) all the way through end-to-end use case examples and flexible, non-regex log parsing. Learn more about CLX and how to get started with cybersecurity applications of RAPIDS. **[Learn more at this repository <i class="fas fa-angle-double-right"></i>](https://github.com/rapidsai/clx){: target="_blank"}**

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
{% include section-halfs.html 
    background="background-purple" 
    padding-top="0em" padding-bottom="0em" 
    content-left-half=uc_left
    content-right-half=uc_right
%}
{% include section-halfs.html 
    background="background-purple" 
    padding-top="0em" padding-bottom="5em" 
    content-left-half=uc_2_left
    content-right-half=uc_2_right
%}
{% include slopecap.html 
    background="background-purple" 
    position="bottom" 
    slope="down" 
%}

<!-- Query Details Sections 30x -->
<section class="background-white padding-top-2em padding-bottom-2em">
    <div class="pure-g">
       <div class="container-padding">
           <div class="pure-u-1 pure-u-md-1-3">
               <h4 class="query-title">Query 01</h4>
               <div id="Q-1" class="query-num"></div>
                
               <p class="query-desc">To build and train recommender systems, it is typical in retail and eCommerce industries to build data science pipelines for prediction. A workflow may use a basketing technique to determine which products are most frequently to be grouped together in a single sale. To run this query, a data scientist loads structured, transactional data into a table, performs data pre-processing like pairing, sorting, and grouping data to create a report. The pairs can later be grouped into clusters to provide recommendations.  </p>
                
                <p class="query-wf">Reccomenders | Basketing</p>
                <a href="https://github.com/rapidsai/tpcx-bb/blob/master/tpcx-bb1.3.1/rapids-queries/q01/tpcx-bb-query-01.ipynb" taget="_blank" class="query-link">Source Code</a>
           </div>
           <div class="pure-u-1 pure-u-md-1-3">
            <h4 class="query-title">Query 01</h4>
            <div id="Q-1" class="query-num"></div>
             
            <p class="query-desc">When implementing a “viewed together” sort of online store streaming data, a data scientist working in eCommerce may choose to session the dataset to find common product clusters during a given timeframe. This involves reconstructing a user’s browsing session to create a virtual timestamp and determine if the given product was viewed during that session. </p>
             
             <p class="query-wf">Sessioning</p>
             <a href="https://github.com/rapidsai/tpcx-bb/blob/master/tpcx-bb1.3.1/rapids-queries/q02/tpcx-bb-query-02.ipynb" taget="_blank" class="query-link">Source Code</a>
           </div>
           <div class="pure-u-1 pure-u-md-1-3">
            <h4 class="query-title">Query 01</h4>
            <div id="Q-1" class="query-num"></div>
             
            <p class="query-desc">To build and train recommender systems, it is typical in retail and eCommerce industries to build data science pipelines for prediction. A workflow may use a basketing technique to determine which products are most frequently to be grouped together in a single sale. To run this query, a data scientist loads structured, transactional data into a table, performs data pre-processing like pairing, sorting, and grouping data to create a report. The pairs can later be grouped into clusters to provide recommendations.  </p>
             
             <p class="query-wf">Reccomenders | Basketing</p>
             <a href="https://github.com/rapidsai/tpcx-bb/blob/master/tpcx-bb1.3.1/rapids-queries/q01/tpcx-bb-query-01.ipynb" taget="_blank" class="query-link">Source Code</a>
           </div>
       </div>
   </div>

</section>


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


<!-- Bar Chart Results -->
<script src="https://d3js.org/d3.v5.min.js"></script>
<script>
    /* grouped bar chart based on https://observablehq.com/@d3/grouped-bar-chart */
    filepath = 'assets/files/tpcxbb-results.json'
    d3.json(filepath).then(function(data) {
        console.log(data);
        
        buildBar(data.TCB, '#barChart')
        
        /* resize */
        window.addEventListener("resize", ()=>{
            
            buildBar(data.TCB, '#barChart')

        });

    });

    function buildDetails (data){
        // format
    }

    function buildBar (data, id){
       
        width = $(id).width();
        height = 300;
        margin = ({top: 20, right: 60, bottom: 20, left: 60})
    
        keys = ['rapids','huawei']
        groupKey = 'query'

        yAxis = g => g
            .attr("transform", `translate(${margin.left},0)`)
            .call(d3.axisRight(y)
                .tickSize(width - margin.left - margin.right))
            .call(g => g.select(".domain").remove())
            .call(g => g.selectAll(".tick:not(:first-of-type) line")
                .attr("stroke-opacity", 0.15)
                .attr("stroke-dasharray", "2,2"))
            .call(g => g.selectAll(".tick text")
                .attr("x", -20)
                .attr("dy", -4))


        xAxis = g => g
            .attr("transform", `translate(0,${height - margin.bottom})`)
            .call(d3.axisBottom(x0).tickSizeOuter(0))
            .call(g => g.select(".domain").remove())

        color = d3.scaleOrdinal()
            .range(["#98abc5", "#8a89a6"])

        y = d3.scaleLinear()
            .domain([0, d3.max(data, d => d3.max(keys, key => d[key])) + 10]).nice()
            .rangeRound([height - margin.bottom, margin.top])
        
        x0 = d3.scaleBand()
            .domain(data.map(d => d[groupKey]))
            .rangeRound([margin.left, width - margin.right])
            .paddingInner(0.3)

        x1 = d3.scaleBand()
            .domain(keys)
            .rangeRound([0, x0.bandwidth()])
            .padding(0.1)

        legend = svg => {
            const g = svg
                .attr("transform", `translate(${width},0)`)
                .attr("text-anchor", "end")
                .attr("font-family", "sans-serif")
                .attr("font-size", 10)
                .selectAll("g")
                .data(color.domain().slice().reverse())
                .join("g")
                .attr("transform", (d, i) => `translate(0,${i * 20})`);

            g.append("rect")
                .attr("x", -19)
                .attr("width", 19)
                .attr("height", 19)
                .attr("fill", color);

            g.append("text")
                .attr("x", -24)
                .attr("y", 9.5)
                .attr("dy", "0.35em")
                .text(d => d);
            }
            
            /* lazy clear */
            d3.select(id).html("")

            svg = d3.select(id).append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)

            svg.append("g")
                    .selectAll("g")
                    .data(data)
                    .join("g")
                    .attr("transform", d => `translate(${x0(d[groupKey])},0)`)
                    .selectAll("rect")
                    .data(d => keys.map(key => ({key, value: d[key], query: d.query})))
                    .join("rect")
                    .attr("x", d => x1(d.key))
                    .attr("y", d => y(d.value))
                    .attr("width", x1.bandwidth())
                    .attr("height", d => y(0) - y(d.value))
                    .attr("fill", d => color(d.key))
                    .on("click",(d)=>{
                        window.location.href='#'+d.query
                    })

                svg.append("g")
                    .call(xAxis);

                svg.append("g")
                    .call(yAxis); 

                svg.append("g")
                    .call(legend);
        
    }


</script>