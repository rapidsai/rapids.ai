---
title: "RAPIDS + TPC-XBB"
description: "Benchmarking RAPIDS with TPCx-BB"
tagline: "Benchmarking RAPIDS with TPCx-BB"
button_text: "TPC.org"
button_link: "http://www.tpc.org/tpcx-bb/default.asp"
layout: default
---
![TPCxbb]({{ site.baseurl }}{% link /assets/images/tpc-reg.gif %}){: .projects-logo}

# Running TPCx-BB on GPUs
{: .section-title-full}

{% capture total-time %}
## What is TPCx-BB?


TPCx-BB is a Big Data benchmark for enterprises that includes 30 queries representing real-world ETL & ML workflows at various scale factors: SF1000 is 1 TB of data, SF10000 is 10TB. Each “query” is in fact a model workflow that can include SQL, user-defined functions, careful sub-setting and aggregation, and machine learning. To date, these queries have been run using Apache Hive or Apache Spark. **[See the TPC guidelines and past results <i class="fas fa-angle-double-right"></i>](http://www.tpc.org/tpcx-bb/default.asp){: target="_blank"}**  

## Why the Benchmark Matters

This marks the first TPCx-BB benchmark (unofficial) on GPUs. In this run, compute, communication, networking, and storage infrastructure are accelerated by the RAPIDS software ecosystem. This sets a new bar for running data science workloads at scale. **[Read more on this vision <i class="fas fa-angle-double-right"></i>](https://towardsdatascience.com/life-after-hadoop-getting-data-science-to-work-for-your-business-c9ab6605733f){: target="_blank"}**  


## Get dramatic cost and time-savings <br> for both small scale and large-scale data analytics problems

![total rapids vs current leaders]({{ site.baseurl }}{% link /assets/images/TPCx-BB Total Time RAPIDS vs. Current Leaders.png %}){: .center}

{% endcapture %}

{% capture sf1000-left %}
## Scaling Up: <br> 1TB+ on a Single Server
{: .section-title-halfs}

SF1000, with a data size of 1 TB, is the threshold of what used to be “Big Data”, but is now very common.  Many analytics workloads process data at this scale. These tasks take specialized infrastructure to execute, and the ability to draw actionable information out of data sets of this size on demand is relatively recent. It also suggests an organization of a size where data is increasingly critical to operating at optimal capacity. This is often when analysts will begin trading sophistication for performance.

On **two NVIDIA DGX A100 systems (16 GPUs), RAPIDS achieved a 37.1x faster execution time.**

{% endcapture %}

{% capture sf10000-right %}
## Scaling Out: <br> 10TB+ on Distributed Systems
{: .section-title-halfs}

SF10000, with more than 10 TB of data, presents both an opportunity to make data-driven decisions, and a considerable infrastructure challenge. Minor iterations on queries become costly in both execution time and datacenter costs: space, server equipment, power, cooling, and human capital to manage it. Without an efficient solution, many TPCx-BB-style analyses will collapse under their own weight and be infeasible to execute at this scale.

On **sixteen NVIDIA DGX A100 systems (128 GPUs), RAPIDS achieved a 19.5x faster execution time.**

We expect even further improvement as we iterate on RAPIDS, but 19.5x represents a **wall-clock time reduction from 282 minutes to 23 minutes.** **[Read our blog on next steps and plans to improve <i class="fas fa-angle-double-right"></i>](https://medium.com/rapids-ai/no-more-waiting-interactive-big-data-now-32f7b903cf41){: target="_blank"}**

{% endcapture %}

{% include section-single.html
    background="background-white" 
    padding-top="3em" padding-bottom="0em" 
    content-single=total-time
%}
{% include section-halfs.html
    background="background-white" 
    padding-top="0em" padding-bottom="5em" 
    content-left-half=sf1000-left
    content-right-half=sf10000-right
%}

{% capture start_single %}
# RAPIDS TPCxBB Results

Traditionally run on CPU-only servers, the results below represent the first major data analytics  benchmarks (unofficial) run on GPU systems, which would not have been possible without RAPIDS & the Python ecosystem. Using familiar APIs like Pandas and Dask, GPUs can now accelerate these kinds of workloads using user-friendly APIs at both 1TB and 10TB scales at up to 40x faster than the top CPU baseline.

{% endcapture %}

{% capture start_left %}
## <i class="far fa-code"></i> See the Code
Find the documentation, source code, and readme on **[our more on our GitHub Page <i class="fas fa-angle-double-right"></i>](https://github.com/rapidsai/tpcx-bb){: target="_blank"}**  

{% endcapture %}
{% capture start_mid %}
## <i class="fab fa-searchengin"></i> The Query Details
Learn about each query workflow and see how RAPIDS performs **[with each query explained <i class="fas fa-angle-double-right"></i>](#workflow)**  

{% endcapture %}
{% capture start_right %}
## <i class="far fa-file-alt"></i> Next Steps
See the future plans for integrating new technologies for faster results **[with our next steps <i class="fas fa-angle-double-right"></i>](https://medium.com/rapids-ai/no-more-waiting-interactive-big-data-now-32f7b903cf41){: target="_blank"}**  

{% endcapture %}
{% include slopecap.html 
    background="background-gray" 
    position="top" 
    slope="down" 
%}
{% include section-single.html
    background="background-gray" 
    padding-top="3em" padding-bottom="0em" 
    content-single=start_single
%}

<section class="padding-top-0em padding-bottom-3em background-gray">
    <div class="container-padding">
        <h2 class="section-title-full">
            Get Up to 40x Speedups with RAPIDS <br>
            Query in Seconds by Scale Factor 
        </h2>
        <div id="results-sfk" class="full-image-center"></div>
    </div>
</section>

{% include section-thirds.html  
    background="background-gray" 
    padding-top="0em" padding-bottom="10em" 
    content-left-third=start_left
    content-middle-third=start_mid
    content-right-third=start_right
%}



{% capture hardware %}
# Hardware Specifics

At both scales, worker to worker communication is typically a bottleneck for operations like joins. Using the newly released **[UCX-Py library](https://github.com/rapidsai/ucx-py/){: target="_blank"}** with Dask, RAPIDS is able to massively reduce the scale of this problem. Communication is still a bottleneck, but at a fraction of the time cost.


{% endcapture %}

{% capture sf1khw-left %}
## <i class="fal fa-tachometer-alt"></i> SF1000

**GPU Systems:** 
2x **[NVIDIA DGX A100](https://www.nvidia.com/en-us/data-center/dgx-a100/){: target="_blank"}**

**Hardware Detail:**
16 total **[NVIDIA A100](https://www.nvidia.com/en-us/data-center/a100/){: target="_blank"}** GPUs with 640 GBs total GPU memory connected locally over **[NVIDIA NVLink](https://info.nvidianews.com/rs/nvidia/images/NVIDIA%20NVLink%20High-Speed%20Interconnect%20Application%20Performance%20Brief.pdf){: target="_blank"}** and **[NVIDIA NVSwitch](https://images.nvidia.com/content/pdf/nvswitch-technical-overview.pdf){: target="_blank"}** and node-to-node via **[Mellanox InfiniBand](https://www.mellanox.com/pdf/whitepapers/IB_Intro_WP_190.pdf){: target="_blank"}**

Performance Improvement: **37.1x**

{% endcapture %}
{% capture sf10khw-right %}
## <i class="fal fa-tachometer-alt-fastest"></i> SF10000

**GPU Systems:** 
16x **[NVIDIA DGX A100](https://www.nvidia.com/en-us/data-center/dgx-a100/){: target="_blank"}**  

**Hardware Detail:**
128 total **[NVIDIA A100](https://www.nvidia.com/en-us/data-center/a100/){: target="_blank"}** GPUs with 5 TBs total GPU memory connected locally over **[NVIDIA NVLink](https://info.nvidianews.com/rs/nvidia/images/NVIDIA%20NVLink%20High-Speed%20Interconnect%20Application%20Performance%20Brief.pdf){: target="_blank"}** and **[NVIDIA NVSwitch](https://images.nvidia.com/content/pdf/nvswitch-technical-overview.pdf){: target="_blank"}** and node-to-node via **[Mellanox InfiniBand](https://www.mellanox.com/pdf/whitepapers/IB_Intro_WP_190.pdf){: target="_blank"}**

Performance Improvement: **19.5x**

{% endcapture %}
{% include slopecap.html 
    background="background-purple" 
    position="top" 
    slope="up" 
%}
{% include section-single.html
    background="background-purple" 
    padding-top="3em" padding-bottom="0em" 
    content-single=hardware
%}
{% include section-halfs.html
    background="background-purple" 
    padding-top="0em" padding-bottom="10em" 
    content-left-half=sf1khw-left
    content-right-half=sf10khw-right
%}

{% capture wf_single %}
<div id="workflow"></div>
# Detailed Performance Benchmarks <br> by Workflow by Query

The 30 queries represent fundamental data science workflows, in this case for a retailer with a brick and mortar and online presence. Common workflows include Big Data analytics use cases like basketing, sessionizing, inventory management, price analysis, sales analysis, recommendation systems, customer segmentation, and sentiment analysis. **[Get the documentation, code, and readme <i class="fas fa-angle-double-right"></i>](https://github.com/rapidsai/tpcx-bb/tree/master/tpcx-bb1.3.1/rapids-queries){: target="_blank"}**


{% endcapture %}

{% capture wf_left %}
## <i class="far fa-funnel-dollar"></i> Recommenders
Systems that recommend goods to customers that customers are likely to buy, typically on a website:

**[Query 1](#Q1), [Query 5](#Q5), [Query 25](#Q25), [Query 29](#Q29)**

## <i class="far fa-browser"></i> Sessionizing
How a certain kind of customer interacts with a website during a visit; what their browsing/shopping behavior looks like:

**[Query 2](#Q2), [Query 3](#Q3), [Query 4](#Q4)**

## <i class="far fa-cart-arrow-down"></i> Basketing
How are items purchased together, do goods appear in similar “baskets” (customer orders):

**[Query 1](#Q1), [Query 30](#Q30)**

## <i class="far fa-barcode-alt"></i> Price Analysis
How customer behavior changes in response to changes in price:

**[Query 16](#Q16), [Query 17](#Q17), [Query 22](#Q22), [Query 23](#Q23), [Query 24](#Q24)**

{% endcapture %}

{% capture wf_right %}
## <i class="fal fa-analytics"></i> Sales Analysis
Things that impact sales beyond price:

**[Query 8](#Q8), [Query 9](#Q9), [Query 12](#Q12), [Query 13](#Q13), [Query 14](#Q14), [Query 15](#Q15), [Query 21](#Q21)**

## <i class="far fa-chalkboard-teacher"></i> Customer Segmentation
Methods of grouping customers together based on some set of shared characteristics:

**[Query 6](#Q6), [Query 7](#Q7), [Query 20](#Q20), [Query 26](#Q26)**

## <i class="fas fa-warehouse-alt"></i> Competitive Analysis
Identifying weaknesses and strengths of competition to improve efforts within the company:

**[Query 1](#Q1)**

## <i class="far fa-comments"></i> Sentiment Analysis
Methods for analyzing text to predict if the text is positive or negative:

**[Query 10](#Q10), [Query 11](#Q11), [Query 18](#Q18), [Query 19](#Q19), [Query 28](#Q28)**

{% endcapture %}

{% include slopecap.html 
    background="background-gray" 
    position="top" 
    slope="down" 
%}
{% include section-single.html
    background="background-gray" 
    padding-top="5em" padding-bottom="0em" 
    content-single=wf_single
%}
{% include section-halfs.html 
    background="background-gray" 
    padding-top="0em" padding-bottom="5em" 
    content-left-half=wf_left 
    content-right-half=wf_right 
%} 



{% capture key_comp %}
# Key Components of the <br> Technology Stack 

The integration of RAPIDS, BlazingSQL, Dask, CuPy, Numba, and UCX is no easy feat. RAPIDS libraries have previously demonstrated significant speed-ups at small and medium-scale but required significant development to support speed-of-light workflows at scales greater than 10 Terabytes. To address the challenges, core development focused on several key areas: I/O, serialization and spilling, memory interoperability, high-speed networking, and algorithm development.

{% endcapture %}

{% capture key1 %}
## Serialization and Spilling

RAPIDS defined and improved serialization protocols for key GPU data structures like dataframes and series, which enabled the use of NVIDIA NVLink to efficiently transfer these objects over the wire. The set of objects that can be spilled from GPU to main memory through Dask was added to allow the largest ETL workflows to use CPU memory as temporary storage when the GPU would otherwise go out-of-memory.
{% endcapture %}

{% capture key2 %}
## I/O

RAPIDS cuIO, the I/O component of cuDF, added support for reading and writing Apache Parquet formatted data (including splitting Parquet files by row group for enhanced parallelism) and optimized the existing CSV reader implementation.
{% endcapture %}

{% capture key3 %}
## Memory Interoperability

**[RAPIDS Memory Manager](https://github.com/rapidsai/rmm){: target="_blank"}** was enhanced to allow sharing a memory pool between RAPIDS libraries and CuPy. As some RAPIDS TPCx-BB queries rely on CuPy, this change allows use of a single device memory pool on the entire GPU, providing significant performance gains by reducing the cost of dynamically allocating and freeing memory. For more information sharing memory pools, **[check out this blog post](https://medium.com/rapids-ai/using-rapids-memory-manager-with-cupy-8d08fe8f58fa){: target="_blank"}**.
{% endcapture %}

{% capture key4 %}
## High-Speed Networking

RAPIDS developed and released UCX-Py, a Python interface for UCX (a low-level, high-performance networking library) to allow Dask workflows to take advantage of accelerated networking hardware like NVIDIA NVLink and Mellanox InfiniBand (IB). InfiniBand (IB) and GPU RDMA enable a direct path for data exchange between the GPU and a third-party peer device using PCI Express. 

{% endcapture %}

{% capture key5 %}
## Algorithm Development

RAPIDS added and enhanced many single-GPU and distributed algorithms to support the diverse TPCx-BB queries. Key enhancements include new and faster multi-column sort and concatenation, hash-based repartitioning of dataframes, a new join type (left-semi join), a hash-based token-occurrence counter, and a Naive Bayes classifier.

{% endcapture %}

{% include slopecap.html 
    background="background-white" 
    position="top" 
    slope="up" 
%}
{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="3m" 
    content-single=key_comp
%}
{% include section-five-third.html 
    background="background-white" 
    padding-top="0em" padding-bottom="5em" 
    content-left-third=key1
    content-middle-third=key2
    content-right-third=key3
    content-bottom-left=key4
    content-bottom-right=key5
%}
{% include slopecap.html 
    background="background-white" 
    position="bottom" 
    slope="down" 
%}


{% capture contrib_single %}
# It Takes a RAPIDS Ecosystem

The **[RAPIDS TPCx-BB benchmark](https://github.com/rapidsai/tpcx-bb){: target="_blank"}** is an active project with numerous partners and open source communities. We implemented the TPCx-BB queries as a series of Python scripts utilizing the RAPIDS dataframe library, **[cuDF](https://github.com/rapidsai/cudf){: target="_blank"}**, the RAPIDS machine learning library, **[cuML](https://github.com/rapidsai/cuml){: target="_blank"}**, **[CuPy](https://cupy.chainer.org/){: target="_blank"}**, and **[Dask](https://dask.org/){: target="_blank"}** as the primary libraries. We relied on **[Numba](http://numba.pydata.org/){: target="_blank"}** to implement custom-logic in user-defined functions, and we relied on **[spaCy](https://spacy.io/){: target="_blank"}** for named entity recognition. These results would not be possible without the RAPIDS community and the broader PyData ecosystem.


{% endcapture %}
{% include section-single.html
    background="background-gray" 
    padding-top="5em" padding-bottom="5em" 
    content-single=contrib_single
%}

<section class="container-logo-flex padding-top-0em padding-bottom-0em background-gray">
    <div class="logo-flex">
        <a href="https://www.anaconda.com/anaconda-community/" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/anaconda.png %}" alt="anaconda"> </a>
    </div>
        <a href="https://arrow.apache.org/" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/apache-arrow_Color.png %}" alt="Apache Arrow"> </a>
    </div>
    <div class="logo-flex">
        <a href="https://blazingsql.com/" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/blazingsql.png %}" alt="blazingsql"> </a>
    </div>
    <div class="logo-flex">
        <a href="https://github.com/chainer" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/Chainer-logo.png %}" alt="chainer"> </a>
    </div>
    <div class="logo-flex">
        <a href="https://dask.org/" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/dask_logo.png %}" alt="Dask"> </a>
    </div>
    <div class="logo-flex">
        <a href="#" target="_blank"> <img src="#" alt="Pandas"> </a>
    </div>
    <div class="logo-flex">
        <a href="#" target="_blank"> <img src="#" alt="Python"> </a>
    </div>
    <div class="logo-flex">
        <a href="https://developer.nvidia.com/open-source" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/NVLogo_2D_H.png %}" alt="nvidia"> </a>
    </div>
    <div class="logo-flex">
        <a href="https://numba.pydata.org/" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/numba_logo.png %}" alt="Numba"> </a>
    </div>
    <div class="logo-flex">
        <a href="#" target="_blank"> <img src="#" alt="scikit-learn"> </a>
    </div>
    <div class="logo-flex">
        <a href="#" target="_blank"> <img src="#" alt="spaCy"> </a>
    </div>
    <div class="logo-flex">
        <a href="https://www.openucx.org/" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/UCX_Logo.png %}" alt="UCX"> </a>
    </div>
</section>

{% capture next_step %}
# Next Steps and Future Work

While the initial results show significant improvements, there are open GitHub issues for further optimizations, interoperability, and performance improvements.


## BlazingSQL 
BlazingSQL’s high- performance distributed SQL engine provides the opportunity for even better performance. The BlazingSQL team has heavily focused on out-of-core processing and is now able to cache cuDF DataFrames on GPU memory, system memory, or disk during query execution. Out-of-core is still in its infancy, but early testing demonstrates the ability to run over 50% of the TPCx-BB workloads at SF10K on a single NVIDIA DGX A100.

Simultaneously, the team is integrating UCX-Py into BSQL’s communication layer to dramatically improve shuffles, and therefore overall performance.

## Dask
RAPIDS continues to contribute back to the Dask open-source project. Dask will continue to be key to using RAPIDS at scale. As Dask improves, results will improve. There are several ongoing work streams to enhance the Dask scheduler.


## cuStreamz
Reading data from disk also currently requires sequentially doing I/O and compute. With cuStreamz, it will be possible to overlap the I/O and compute tasks involved in reading data, which will bring further performance gains.


## High-Speed Networking

Current SF10K TPCx-BB results use UCX with NVLink, Mellanox InfiniBand, and GPU RDMA. Communicating small data buffers is still slow compared to larger buffers, which reduces performance. There is ongoing work to improve how UCX-Py and InfiniBand transfer small buffers, which should bring performance gains, too.


## GPU Direct Storage

Currently, reading data from disk requires moving the file into host memory and then copying from host memory into GPU memory. This adds latency and increases host memory requirements. The upcoming CUDA cuFile API enables a direct to GPU memory data path between both local and remote NVME storage systems, called GPU Direct Storage. This will greatly increase throughput for I/O heavy workloads.

{% endcapture %}

{% include section-single.html
    background="background-gray" 
    padding-top="5em" padding-bottom="10em" 
    content-single=next_step
%}
{% include slopecap.html 
    background="background-gray" 
    position="bottom" 
    slope="up" 
%}



<!-- Query Details Sections 30x Generated -->
# Detailed Performance Benchmarks by Workflow by Query
{: .section-title-full .padding-top-3em}

<section id="query-details" class="background-white padding-top-3em padding-bottom-10em"></section>

{% capture end_bottom %}
# See the Acceleration Yourself
{: .section-title-full .text-white}

{% endcapture %}

{% include slopecap.html 
    background="background-darkpurple" 
    position="top" 
    slope="down" 
%}
{% include section-single.html
    background="background-darkpurple" 
    padding-top="1em" padding-bottom="0em" 
    content-single=end_bottom
%}
{% include cta-footer.html 
    name="Experience Data Science on GPUs with RAPIDS" 
    tagline=""
    button="GET STARTED"
    link="https://github.com/rapidsai/tpcx-bb"
%}


<!-- Content Build Scripts -->
<script src="https://d3js.org/d3.v5.min.js"></script>
<script>
    /* grouped bar chart based on https://observablehq.com/@d3/grouped-bar-chart */
   
    filepath = 'assets/files/tpcxbb-results.json'
    
    d3.json(filepath).then(function(data) {
        
        buildBar(data.TPCxbb, '#results-sfk')
        buildDetails(data.TPCxbb)
        
        /* resize */
        window.addEventListener("resize", ()=>{
            
            buildBar(data.TPCxbb, '#results-sfk')

        });

    });

    function buildDetails (data){

        /* build query details */
        /* in set of 3 because div tag kept auto closing? */
        var content = []

        for(let i=0; i<=data.length-3; i+=3){
 
            var r1 = data[i]
            var r2 = data[i+1]
            var r3 = data[i+2]  

            content.push(
            '<div class="pure-g"><div class="container-padding">'
            +
            '<div class="pure-u-1 pure-u-md-1-3"> <div id="'+ r1.query +'" class="query-margin"></div> <h3 class="query-title"><i class="fal fa-analytics"></i> '+ r1.query +'</h3> <a href="#workflow" class="query-wf">'+ r1.workflows.toString() +'</a> <div class="query-num-container"> <div class="query-num">'+ r1.sf1kx +'x<div class="query-subtitle-rapids">SF1K</div></div><div class="query-num">'+ r1.sf10kx +'x<div class="query-subtitle-comp">SF10K</div></div></div> <p class="query-desc">'+ r1.description +'</p><a class="query-source" href="'+ r1.link +'">Get Source Code on Github <i class="fas fa-angle-double-right"></i></a></div>'
            +   
            '<div class="pure-u-1 pure-u-md-1-3"> <div id="'+ r2.query +'" class="query-margin"></div> <h3 class="query-title"><i class="fal fa-analytics"></i> '+ r2.query +'</h3> <a href="#workflow" class="query-wf">'+ r2.workflows.toString() +'</a> <div class="query-num-container"> <div class="query-num">'+ r2.sf1kx +'x<div class="query-subtitle-rapids">SF1K</div></div><div class="query-num">'+ r2.sf10kx +'x<div class="query-subtitle-comp">SF10K</div></div></div> <p class="query-desc">'+ r2.description +'</p><a class="query-source" href="'+ r2.link +'">Get Source Code on Github <i class="fas fa-angle-double-right"></i></a></div>'
            +
            '<div class="pure-u-1 pure-u-md-1-3"> <div id="'+ r3.query +'" class="query-margin"></div> <h3 class="query-title"><i class="fal fa-analytics"></i> '+ r3.query +'</h3> <a href="#workflow" class="query-wf">'+ r3.workflows.toString() +'</a> <div class="query-num-container"> <div class="query-num">'+ r3.sf1kx +'x<div class="query-subtitle-rapids">SF1K</div></div><div class="query-num">'+ r3.sf10kx +'x<div class="query-subtitle-comp">SF10K</div></div></div> <p class="query-desc">'+ r3.description +'</p><a class="query-source" href="'+ r3.link +'">Get Source Code on Github <i class="fas fa-angle-double-right"></i></a></div>'
            +
            '</div></div>')
        
        }

        /* append to dom */
        $('#query-details').html(content)

    }

    function buildBar (data, id){
       
        width = $(id).width();
        height = 300;
        margin = ({top: 20, right: 60, bottom: 20, left: 60})
    
        keys = ['sf10k','sf1k']
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
            .call(g => g.selectAll("text")
                .attr("dx", 10)
                .attr("dy", -7)
                .attr("transform", "rotate(90)")
                .style("text-anchor", "start"))

        color = d3.scaleOrdinal()
            .range(["#7306ff", "#d216d2"])

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
            .padding(0.07)

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