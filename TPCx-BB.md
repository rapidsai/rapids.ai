---
title: "RAPIDS + TPC-XBB"
description: "Learn How RAPIDS Performs on TPCx-BB"
tagline: "Benchmarking RAPIDS with TPCx-BB"
button_text: "TPC.org"
button_link: "http://www.tpc.org/tpcx-bb/default.asp"
layout: default
---
![TPCxbb]({{ site.baseurl }}{% link /assets/images/tpc-reg.gif %}){: .projects-logo}

# Running TPCx-BB on GPUs
{: .section-title-full}


{% capture intro_content-left %}
## What is TPCx-BB?
{: .section-title-halfs}

**[TPCx-BB](http://www.tpc.org/tpcx-bb/default.asp){: target="_blank"}** is 30 queries representing real-world ETL & ML workflows and provides TCO performance benchmark for enterprises. Queries combine SQL statements (run on Apache Hive or Apache Spark) and machine learning algorithms (using ML libraries, user-defined functions, and procedural code) to cover typical analytics workflows. 

{% endcapture %}

{% capture intro-content-right %}
## Why the Benchmark Matters

A modern data center also requires an investment in state-of-the-art storage, networking, orchestration, and accelerated software to meet the future demands of AI. Read about this vision here: **[Life After Hadoop blog.](https://towardsdatascience.com/life-after-hadoop-getting-data-science-to-work-for-your-business-c9ab6605733f){: target="_blank"}**

{% endcapture %}

{% capture in_left %}
## <i class="fal fa-elephant"></i> Hadoop is <br> Inefficient
Scaling production level data science in enterprises is evolving yet again. No longer can enterprises rely on inefficient systems like Hadoop. 

{% endcapture %}
{% capture in_mid %}
## <i class="fal fa-sparkles"></i> Spark on CPUS is <br> Bottlenecked
Moving to an in-system-memory like Apache Spark delivers more flexible and complex workflows, however, slow CPU processing represents a significant bottleneck. Analyzing even a few hundred gigabytes of data takes days on Spark clusters using hundreds of CPU nodes. 

{% endcapture %}
{% capture in_right %}
## <i class="far fa-bolt"></i> Supercharging <br> Data Centers
More efficient compute is required for at-scale data science in the enterprise. NVIDIA GPUs are the core compute building block for modern AI data centers - supercharging servers across numerous applications and providing 10-1000X improvement over CPUs. 

{% endcapture %}

{% include section-halfs.html
    background="background-white" 
    padding-top="0em" padding-bottom="3em" 
    content-left-half=intro_content-left
    content-right-half=intro-content-right
%}
{% include section-thirds.html 
    background="background-white" 
    padding-top="0em" padding-bottom="10em" 
    content-left-third=in_left
    content-middle-third=in_mid
    content-right-third=in_right
%}


{% capture start_single %}
# RAPIDS TPCxBB Results

Get 25x with a RAPIDS optimal setup. See what it takes.
{: .subtitle}

{% endcapture %}

{% capture start_left %}
## <i class="far fa-code"></i> Get the Code
Learn how to execute the TPCx-BB benchmarks on a GPU-cluster running RAPIDS. **[Learn more on our GitHub Page <i class="fas fa-angle-double-right"></i>](#){: target="_blank"}**  

{% endcapture %}
{% capture start_mid %}
## <i class="fab fa-searchengin"></i> See the Queries
Scaling production level data. **[Learn more about the queries <i class="fas fa-angle-double-right"></i>](#){: target="_blank"}**  

{% endcapture %}
{% capture start_right %}
## <i class="far fa-file-alt"></i>  Learn the Details
Scaling production level data. **[Learn more with our whitepaper <i class="fas fa-angle-double-right"></i>](#){: target="_blank"}**  

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
{% include section-thirds.html 
    background="background-white" 
    padding-top="0em" padding-bottom="0em" 
    content-left-third=start_left
    content-middle-third=start_mid
    content-right-third=start_right
%}

{% capture contrib_single %}
# Help Contribute

The RAPIDS TPCx-BB benchmark is an active project and open collaboration with numerous RAPIDS community partners. These results are not possible without the RAPIDS ecosystem. While the initial results show significant improvements across all 30 queries, there are further optimizations and performance improvements to address **[Find out more about open issues <i class="fas fa-angle-double-right"></i>](#){: target="_blank"}** 
{: .subtitle}

{% endcapture %}
{% include section-single.html
    background="background-gray" 
    padding-top="5em" padding-bottom="0em" 
    content-single=contrib_single
%}

<section class="container-logo-flex padding-top-0em padding-bottom-10em">
    <div class="logo-flex">
        <a href="https://arrow.apache.org/" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/apache-arrow_Color.png %}" alt="Apache Arrow"> </a>
    </div>
    <div class="logo-flex">
        <a href="https://www.anaconda.com/anaconda-community/" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/anaconda.png %}" alt="anaconda"> </a>
    </div>
    <div class="logo-flex">
        <a href="https://blazingsql.com/" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/blazingsql.png %}" alt="blazingsql"> </a>
    </div>
    <div class="logo-flex">
        <a href="https://dask.org/" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/dask_logo.png %}" alt="Dask"> </a>
    </div>
    <div class="logo-flex">
        <a href="https://developer.nvidia.com/open-source" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/NVLogo_2D_H.png %}" alt="nvidia"> </a>
    </div>
    <div class="logo-flex">
        <a href="https://numba.pydata.org/" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/numba_logo.png %}" alt="Numba"> </a>
    </div>
    <div class="logo-flex">
        <a href="https://www.openucx.org/" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/UCX_Logo.png %}" alt="UCX"> </a>
    </div>
</section>


{% capture dc_single %}
# Data Center TCO 

Multiple compute, communication, networking, and storage accelerated hardware and software are integrated and optimized to achieve top benchmark performance. This combination of massively parallel compute ability, paired with lightning fast IO, network capabilities, and storage make the solution ideal for scale-out data science workloads.
{: .subtitle}

[ TCO graphic? ]

{% endcapture %}

{% capture dc_left %}
## <i class="far fa-microchip"></i> Compute
The benchmark was run on a cluster of **[18 NVIDIA DGX-1s](https://www.nvidia.com/en-us/data-center/dgx-1/){: target="_blank"}** , each with **[8 NVIDIA V100 32GB GPUs](https://www.nvidia.com/en-us/data-center/v100/){: target="_blank"}**  with **[NVLink interconnect](https://www.nvidia.com/en-us/data-center/nvlink/){: target="_blank"}** .

{% endcapture %}

{% capture dc_mid %}
## <i class="far fa-network-wired"></i> Networking
The massive compute ability of these nodes necessitated a high speed network and IO solution to keep data fed to each GPU and maximize GPU utilization. This was accomplished via 4x Infiniband 100Gb/s adapters per node connected through a **[Mellanox CS7520 switch](https://www.mellanox.com/products/infiniband-switches/CS7500){: target="_blank"}**.

{% endcapture %}

{% capture dc_right %}
## <i class="fal fa-database"></i> Storage
High speed storage provided by [DESCRIBE WEKA] and MAGNUM GPU Direct storage.

{% endcapture %}

{% capture table_single %}

| System Information                          | Dell PowerEdge R730/R730xd | NVIDIA DGX-1 (Max P)|
|:--------------------------------------------|:-------------------|:-------------------|
| Total System Cost                           | 439,187 USD       |
| Performance                                 | 495.28 BBQpm@SF10000 |
| Price/Performance                           | 886.75 USD per BBQpm@SF10000 |
| TPC-Energy Metric                           | Not reported |
| Availability Date                           | 05/13/17 |
| DBMS Software (Big Data Software Framework) | Cloudera for Apache Hadoop (CDH) 5.9.0 |
| Operating System                            | Red Hat Enterprise Linux Server 7.2 |
| **Server Specific Information**             | Dell              | NVIDIA            |
| CPU Type                                    | Intel Xeon E5 - 2690 v4 - 2.6 GHz |
| Node Count                                  | 13 |
| Total # of Processors                       | 26 |
| Total # of Cores                            | 360 |                  
| Total # of Threads                          |     |           
| Cluster                                     | yes |           
| Concurrent Streams                          | 2   |               
| Storage Ratio                               | 36.08 |               
| Memory Ratio                                | 3     |    
| Load Test Time                              | 1.10 Hours  |                 
| Power Test Time                             | 14.75 Hours |                  
| Throughput Test Time                        | 24.64 Hours |             

{% endcapture %}

{% include slopecap.html 
    background="background-purple" 
    position="top" 
    slope="up" 
%}
{% include section-single.html
    background="background-purple" 
    padding-top="5em" padding-bottom="0em" 
    content-single=dc_single
%}
{% include section-thirds.html 
    background="background-purple" 
    padding-top="0em" padding-bottom="0em" 
    content-left-third=dc_left
    content-middle-third=dc_mid
    content-right-third=dc_right
%}
{% include section-single.html
    background="background-purple" 
    padding-top="5em" padding-bottom="10em" 
    content-single=table_single
%}
{% include slopecap.html 
    background="background-purple" 
    position="bottom" 
    slope="down" 
%}

<!-- compute -->
{% capture comp_single %}
# Squeezing Every Last Drop of Perf

## COMPUTE
RAPIDS running on 18 NVIDIA DGX (144 GPUs) achieve a XX performance speedup across all TPCxBB queries over the top benchmark submission from Dell running Hortonworks on a cluster with 19 CPU-based nodes. This is one reason why Fortune 500s (including Walmart, Capital One, and Best Buy) are using the RAPIDS accelerator stack in at-scale production today. The RAPIDS accelerator software stack looks something like this

[ Graphic ] 

{% endcapture %}
{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="5em" 
    content-single=comp_single
%}

<!-- network results -->
{% capture net_single %}
## Networking 
Infiniband and Remote Direct Memory Access (RDMA) allow GPUs to communicate directly with each other, across nodes, at up to 100Gb/s. The benefits of RDMA is critical for large, complex ETL workloads and ML training, providing up to a 20x benefit for distributed joins over PCIe GPU on systems without it. The RAPIDS TPCx-BB submission uses the latest compute and networking advances, including: 

{% endcapture %}

{% capture net_left %}
## RDMA
RDMA in Mellanox NICs

{% endcapture %}

{% capture net_mid %}
## NCCL2
NCCL2 (NVIDIA collective communication library)

{% endcapture %}

{% capture net_right %}
## OpenUCX
OpenUCX (an open-source point to point communication framework)

{% endcapture %}

{% capture netmore_single %}
This improved networking and communication helps achieve an XXX performance increase over CPU-based communications with XXX networking.

{% endcapture %}
{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="0em" 
    content-single=net_single
%}

<section class="container-logo-flex padding-top-5em padding-bottom-5em">
    <div id="results-1" class="full-image-center"></div>
</section>

{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="0em" 
    content-single=netmore_single
%}
<section class="container-logo-flex padding-top-5em padding-bottom-5em">
    <div id="results-2" class="full-image-center"></div>
</section>

{% include section-thirds.html 
    background="background-white" 
    padding-top="5em" padding-bottom="5em" 
    content-left-third=net_left
    content-middle-third=net_mid
    content-right-third=net_right
%}

<!-- storage results -->
{% capture store_single %}
#  Storage

Legacy architectures placed a “bounce buffer” in the CPU’s system memory between storage and GPU computing, where copies of data would be used to keep applications on GPUs fed. GPUDirect Storage allows both NVMe and NVMe over Fabric (NVMe-oF) to read and write data directly to the GPU, bypassing the CPU and system memory. 
{: .subtitle}

{% endcapture %}

{% capture store_left %}
## Fully Utilizes GPU
With GPUDirect Storage, the GPU not only becomes the fastest computing element, but also the one with the highest I/O bandwidth.

{% endcapture %}

{% capture store_mid %}
## Free System Resources
Now that all of the computation happens on the GPU, this frees up the CPU and system memory for other tasks.
{% endcapture %}

{% capture store_right %}
## Improves System Capacity
GPU Direct Storage unifies GPUs and NVMe to improve system capacity to petabyte scale and achieves a TPCx-BB benchmark result of XXX.

{% endcapture %}

{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="0em" 
    content-single=store_single
%}

<section class="container-logo-flex padding-top-5em padding-bottom-5em">
    <div id="results-3" class="full-image-center"></div>
</section>

{% include section-thirds.html 
    background="background-white" 
    padding-top="5em" padding-bottom="5em" 
    content-left-third=store_left
    content-middle-third=store_mid
    content-right-third=store_right
%}


<!-- workflows -->
{% capture wf_single %}
# Detailed Performance Benchmarks by Workflow by Query

The 30 queries represent fundamental data science workflows, in this case for a retailer with a brick and mortar and online presence. Common workflows include Big Data analytics use cases like basketing, sessionizing, inventory management, price analysis, sales analysis, recommendation systems, customer segmentation, and sentiment analysis. 
{: .subtitle}

{% endcapture %}

{% capture wf_left %}
## <i class="far fa-funnel-dollar"></i> Recommenders
[Query 1](#Q-1), [Query 20](#Q-20), [Query 30](#Q-30)

## <i class="far fa-browser"></i> Sessionizing
[Query 1](#Q-1), [Query 20](#Q-20), [Query 30](#Q-30)

## <i class="far fa-cart-arrow-down"></i> Basketing
[Query 1](#Q-1), [Query 20](#Q-20), [Query 30](#Q-30)

## <i class="far fa-barcode-alt"></i> Price Analysis
[Query 1](#Q-1), [Query 20](#Q-20), [Query 30](#Q-30)

{% endcapture %}

{% capture wf_right %}
## <i class="fal fa-analytics"></i> Sales Analysis
[Query 1](#Q-1), [Query 20](#Q-20), [Query 30](#Q-30)

## <i class="far fa-chalkboard-teacher"></i> Customer Segmentation
[Query 1](#Q-1), [Query 20](#Q-20), [Query 30](#Q-30)

## <i class="fas fa-warehouse-alt"></i> Inventory Management
[Query 1](#Q-1), [Query 20](#Q-20), [Query 30](#Q-30)

## <i class="far fa-comments"></i> Sentiment Analysis
[Query 1](#Q-1), [Query 20](#Q-20), [Query 30](#Q-30)

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
    padding-top="5em" padding-bottom="10em" 
    content-left-half=wf_left 
    content-right-half=wf_right 
%} 
{% include slopecap.html 
    background="background-gray" 
    position="bottom" 
    slope="up" 
%}

<!-- Query Details Sections 30x -->
<section class="background-white padding-top-10em padding-bottom-10em">
    <div class="pure-g">
       <div class="container-padding">
           <div class="pure-u-1 pure-u-md-1-3">
               <h3 class="query-title">Query 01</h3>
               <div id="Q-10" class="query-num">100 | 50</div>
                
               <p class="query-desc">To build and train recommender systems, it is typical in retail and eCommerce industries to build data science pipelines for prediction. A workflow may use a basketing technique to determine which products are most frequently to be grouped together in a single sale. To run this query, a data scientist loads structured, transactional data into a table, performs data pre-processing like pairing, sorting, and grouping data to create a report. The pairs can later be grouped into clusters to provide recommendations.  </p>
                
                <p class="query-wf">Reccomenders | Basketing</p>
                <a href="https://github.com/rapidsai/tpcx-bb/blob/master/tpcx-bb1.3.1/rapids-queries/q01/tpcx-bb-query-01.ipynb" taget="_blank" class="query-link">Source Code</a>
           </div>
           <div class="pure-u-1 pure-u-md-1-3">
            <h3 class="query-title">Query 01</h3>
            <div id="Q-20" class="query-num">100 | 50</div>
             
            <p class="query-desc">When implementing a “viewed together” sort of online store streaming data, a data scientist working in eCommerce may choose to session the dataset to find common product clusters during a given timeframe. This involves reconstructing a user’s browsing session to create a virtual timestamp and determine if the given product was viewed during that session. </p>
             
             <p class="query-wf">Sessioning</p>
             <a href="https://github.com/rapidsai/tpcx-bb/blob/master/tpcx-bb1.3.1/rapids-queries/q02/tpcx-bb-query-02.ipynb" taget="_blank" class="query-link">Source Code</a>
           </div>
           <div class="pure-u-1 pure-u-md-1-3">
            <h3 class="query-title">Query 01</h3>
            <div id="Q-30" class="query-num">100 | 50</div>
             
            <p class="query-desc">To build and train recommender systems, it is typical in retail and eCommerce industries to build data science pipelines for prediction. A workflow may use a basketing technique to determine which products are most frequently to be grouped together in a single sale. To run this query, a data scientist loads structured, transactional data into a table, performs data pre-processing like pairing, sorting, and grouping data to create a report. The pairs can later be grouped into clusters to provide recommendations.  </p>
             
             <p class="query-wf">Reccomenders | Basketing</p>
             <a href="https://github.com/rapidsai/tpcx-bb/blob/master/tpcx-bb1.3.1/rapids-queries/q01/tpcx-bb-query-01.ipynb" taget="_blank" class="query-link">Source Code</a>
           </div>
       </div>
   </div>

</section>

{% capture end_bottom %}
# See the Acceleration Yourself
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
{% include cta-footer.html 
    name="Experience Data Science on GPUs with RAPIDS" 
    tagline=""
    button="GET STARTED"
    link="start.html"
%}


<!-- Content Build Scripts -->
<script src="https://d3js.org/d3.v5.min.js"></script>
<script>
    /* grouped bar chart based on https://observablehq.com/@d3/grouped-bar-chart */
    filepath = 'assets/files/tpcxbb-results.json'
    d3.json(filepath).then(function(data) {
        console.log(data);
        
        buildBar(data.TCB, '#results-1')
        buildBar(data.TCB, '#results-2')
        buildBar(data.TCB, '#results-3')
        
        /* resize */
        window.addEventListener("resize", ()=>{
            
            buildBar(data.TCB, '#results-1')
            buildBar(data.TCB, '#results-2')
            buildBar(data.TCB, '#results-3')

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