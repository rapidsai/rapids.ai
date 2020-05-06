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
{: .section-title-halfs}

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

{% capture sf1000-left %}
## Why SF1000 Matters
{: .section-title-halfs}

SF1000 marks crossing over to what was once called “Big Data,” with a total data size of 1 TB.  These are tasks that take specialized infrastructure to execute, and the ability to draw actionable information out of data sets of this size on demand is relatively recent. It also suggests an organization of a size where data is increasingly critical to operating at optimal capacity. This is often when analysts will begin trading sophistication for performance. 

{% endcapture %}

{% capture sf10000-right %}
## Why SF10000 Matters More
{: .section-title-halfs}

SF10000, a total data size of 10 TB, will present a considerable infrastructure challenge. Organizations with analytics tasks so large will also critically need to make data-driven decisions. However, minor iterations on queries become costly. Many analyses will collapse under their own weight and be infeasible to execute. And data this large will represent substantial investments in human capital and infrastructure to manage. 

{% endcapture %}

{% include section-halfs.html
    background="background-white" 
    padding-top="0em" padding-bottom="3em" 
    content-left-half=intro_content-left
    content-right-half=intro-content-right
%}
{% include section-thirds.html 
    background="background-white" 
    padding-top="0em" padding-bottom="3em" 
    content-left-third=in_left
    content-middle-third=in_mid
    content-right-third=in_right
%}
{% include section-halfs.html
    background="background-white" 
    padding-top="0em" padding-bottom="5em" 
    content-left-half=sf1000-left
    content-right-half=sf10000-right
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

<section class="padding-top-5em padding-bottom-5em background-gray">
    <div class="container-padding">
        <div id="results-1" class="full-image-center"></div>
    </div>
</section>

{% include section-thirds.html  
    background="background-gray" 
    padding-top="0em" padding-bottom="0em" 
    content-left-third=start_left
    content-middle-third=start_mid
    content-right-third=start_right
%}

{% capture contrib_single %}
# Help Contribute

The RAPIDS TPCx-BB benchmark is an active project and open collaboration with numerous RAPIDS community partners. These results are not possible without the RAPIDS ecosystem.
{: .subtitle} 

{% endcapture %}
{% include section-single.html
    background="background-gray" 
    padding-top="3em" padding-bottom="0em" 
    content-single=contrib_single
%}

<section class="container-logo-flex padding-top-0em padding-bottom-0em background-gray">
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

{% capture contribers_single %}
While the initial results show significant improvements across all 30 queries, there are further optimizations and performance improvements to address.
{: .subtitle} 

{% endcapture %}
{% capture contrib_left %}
## BlazingSQL

The team at BSQL has made monumental efforts to build out the SQL portions of the TPCxBB workflows involving SQL.

Help Contribute **[Learn more on GitHub <i class="fas fa-angle-double-right"></i>](#){: target="_blank"}**  
Help Contribute **[Learn more on GitHub <i class="fas fa-angle-double-right"></i>](#){: target="_blank"}**  

{% endcapture %}

{% capture contrib_mid %}
## Dask

There are numerous open issues and requests to the Dask community to help speed up scheduling overhead and improve latencies. 

Help Contribute **[Learn more on GitHub <i class="fas fa-angle-double-right"></i>](#){: target="_blank"}**  
Help Contribute **[Learn more on GitHub <i class="fas fa-angle-double-right"></i>](#){: target="_blank"}**  

{% endcapture %}

{% capture contrib_right %}
## UCX 

Content content content.

Help Contribute **[Learn more on GitHub <i class="fas fa-angle-double-right"></i>](#){: target="_blank"}**  
Help Contribute **[Learn more on GitHub <i class="fas fa-angle-double-right"></i>](#){: target="_blank"}**  

{% endcapture %}

{% include section-single.html
    background="background-gray" 
    padding-top="0em" padding-bottom="0em" 
    content-single=contribers_single
%}
{% include section-thirds.html 
    background="background-gray" 
    padding-top="0em" padding-bottom="5em" 
    content-left-third=contrib_left
    content-middle-third=contrib_mid
    content-right-third=contrib_right
%}
{% include slopecap.html 
    background="background-gray" 
    position="bottom" 
    slope="up" 
%}


{% capture perf_single %}
# Squeezing Every Last Drop of Perf

RAPIDS running on 18 NVIDIA DGX (144 GPUs) achieve a XX performance speedup across all TPCxBB queries over the top benchmark submission from Dell running Hortonworks on a cluster with 19 CPU-based nodes. This is one reason why Fortune 500s (including Walmart, Capital One, and Best Buy) are using the RAPIDS accelerator stack in at-scale production today. The RAPIDS accelerator software stack looks something like this

[ Network Arch Graphic ] 

{% endcapture %}
{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="10em" 
    content-single=perf_single
%}


{% capture next_single %}
# Next Steps and Future Work 

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua

{% endcapture %}

{% capture next_left %}
## IB, RDMA in Mellanox NICs

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat

{% endcapture %}

{% capture next_mid %}
## Ampere
NCCL2 (NVIDIA collective communication library)

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat

{% endcapture %}

{% capture next_right %}
## Magnum I/O, GDS
OpenUCX (an open-source point to point communication framework)

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat

{% endcapture %}

{% include slopecap.html 
    background="background-purple" 
    position="top" 
    slope="down" 
%}
{% include section-single.html
    background="background-purple" 
    padding-top="5em" padding-bottom="0em" 
    content-single=next_single
%}
{% include section-thirds.html 
    background="background-purple" 
    padding-top="5em" padding-bottom="10em" 
    content-left-third=next_left
    content-middle-third=next_mid
    content-right-third=next_right
%}
{% include slopecap.html 
    background="background-purple" 
    position="bottom" 
    slope="down" 
%}


<!-- workflows -->
{% capture wf_single %}
<div id="workflow"></div>
# Detailed Performance Benchmarks by Workflow by Query

The 30 queries represent fundamental data science workflows, in this case for a retailer with a brick and mortar and online presence. Common workflows include Big Data analytics use cases like basketing, sessionizing, inventory management, price analysis, sales analysis, recommendation systems, customer segmentation, and sentiment analysis. **[Find documentation, code, and readme here](https://github.com/rapidsai/tpcx-bb/tree/master/tpcx-bb1.3.1/rapids-queries){: target="_blank"}** . 
{: .subtitle}

{% endcapture %}

{% capture wf_left %}
## <i class="far fa-funnel-dollar"></i> Recommenders
Systems that recommend goods to customers that customers are likely to buy, typically on a website: 
[Query 1](#Q1), [Query 5](#Q5), [Query 25](#Q25), [Query 29](#Q29).

## <i class="far fa-browser"></i> Sessionizing
How a certain kind of customer interacts with a website during a visit; what their browsing/shopping behavior looks like:
[Query 2](#Q2), [Query 3](#Q3), [Query 4](#Q4).

## <i class="far fa-cart-arrow-down"></i> Basketing
How are items purchased together, do goods appear in similar “baskets” (customer orders):
[Query 1](#Q1), [Query 30](#Q30)

## <i class="far fa-barcode-alt"></i> Price Analysis
How customer behavior changes in response to changes in price:
[Query 16](#Q16), [Query 17](#Q17), [Query 22](#Q22), [Query 23](#Q23), [Query 24](#Q24).

{% endcapture %}

{% capture wf_right %}
## <i class="fal fa-analytics"></i> Sales Analysis
Things that impact sales beyond price:
[Query 8](#Q8), [Query 9](#Q9), [Query 12](#Q12), [Query 13](#Q13), [Query 14](#Q14), [Query 15](#Q15), [Query 21](#Q21).

## <i class="far fa-chalkboard-teacher"></i> Customer Segmentation
Methods of grouping customers together based on some set of shared characteristics:
[Query 6](#Q6), [Query 7](#Q7), [Query 20](#Q20), [Query 26](#Q26)

## <i class="fas fa-warehouse-alt"></i> Competitive Analysis
Identifying weaknesses and strengths of competition to improve efforts within the company:
[Query 1](#Q27).

## <i class="far fa-comments"></i> Sentiment Analysis
Methods for analyzing text to predict if the text is positive or negative:
[Query 10](#Q10), [Query 11](#Q11), [Query 18](#Q18), [Query 19](#Q19), [Query 28](#Q28).

{% endcapture %}

{% include slopecap.html 
    background="background-gray" 
    position="top" 
    slope="down" 
%}
{% include section-single.html
    background="background-gray" 
    padding-top="10em" padding-bottom="0em" 
    content-single=wf_single
%}
{% include section-halfs.html 
    background="background-gray" 
    padding-top="0em" padding-bottom="5em" 
    content-left-half=wf_left 
    content-right-half=wf_right 
%} 
{% include slopecap.html 
    background="background-gray" 
    position="bottom" 
    slope="up" 
%}

<!-- Query Details Sections 30x Generated -->
<section id="query-details" class="background-white padding-top-10em padding-bottom-10em"></section>

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
    link="start.html"
%}


<!-- Content Build Scripts -->
<script src="https://d3js.org/d3.v5.min.js"></script>
<script>
    /* grouped bar chart based on https://observablehq.com/@d3/grouped-bar-chart */
    filepath = 'assets/files/tpcxbb-results.json'
    d3.json(filepath).then(function(data) {
        
        buildBar(data.TPCxbb, '#results-1')
        buildDetails(data.TPCxbb)
        
        /* resize */
        window.addEventListener("resize", ()=>{
            
            buildBar(data.TPCxbb, '#results-1')

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
            '<div class="pure-u-1 pure-u-md-1-3"> <div id="'+ r1.query +'" class="query-margin"></div> <h3 class="query-title"><i class="fal fa-analytics"></i> '+ r1.query +'</h3> <a href="#workflow" class="query-wf">'+ r1.workflows.toString() +'</a> <div class="query-num-container"> <div class="query-num">'+ r1.rapids +'<div class="query-subtitle-rapids">RAPIDS</div></div><div class="query-num">'+ r1.huawei +'<div class="query-subtitle-comp">Hueiwai</div></div></div> <p class="query-desc">'+ r1.description +'</p><a class="query-source" href="'+ r1.link +'">Get Source Code on Github <i class="fas fa-angle-double-right"></i></a></div>'
            +   
            '<div class="pure-u-1 pure-u-md-1-3"> <div id="'+ r2.query +'" class="query-margin"></div> <h3 class="query-title"><i class="fal fa-analytics"></i> '+ r2.query +'</h3> <a href="#workflow" class="query-wf">'+ r2.workflows.toString() +'</a> <div class="query-num-container"> <div class="query-num">'+ r2.rapids +'<div class="query-subtitle-rapids">RAPIDS</div></div><div class="query-num">'+ r2.huawei +'<div class="query-subtitle-comp">Hueiwai</div></div></div> <p class="query-desc">'+ r2.description +'</p><a class="query-source" href="'+ r2.link +'">Get Source Code on Github <i class="fas fa-angle-double-right"></i></a></div>'
            +
            '<div class="pure-u-1 pure-u-md-1-3"> <div id="'+ r3.query +'" class="query-margin"></div> <h3 class="query-title"><i class="fal fa-analytics"></i> '+ r3.query +'</h3> <a href="#workflow" class="query-wf">'+ r3.workflows.toString() +'</a> <div class="query-num-container"> <div class="query-num">'+ r3.rapids +'<div class="query-subtitle-rapids">RAPIDS</div></div><div class="query-num">'+ r3.huawei +'<div class="query-subtitle-comp">Hueiwai</div></div></div> <p class="query-desc">'+ r3.description +'</p><a class="query-source" href="'+ r3.link +'">Get Source Code on Github <i class="fas fa-angle-double-right"></i></a></div>'
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
            .call(g => g.selectAll("text")
                .attr("dx", 10)
                .attr("dy", -7)
                .attr("transform", "rotate(90)")
                .style("text-anchor", "start"))

        color = d3.scaleOrdinal()
            .range(["#7306ff", "#ee7e56"])

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
            .padding(0.05)

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