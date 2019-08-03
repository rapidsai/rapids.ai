---
title: "RAPIDS + BlazingSQL | RAPIDS"
og_title: "RAPIDS + BlazingSQL"
og_description: "Blazing Fast SQL on RAPIDS"
brand_name: ""
brand_tagline: "Blazing Fast SQL on RAPIDS"
brand_button: "BLAZINGSQL.COM"
brand_link: "https://blazingsql.com/"
layout: default
---

![BLAZINGSQL]({{ site.baseurl }}{% link /assets/images/blazingsql.png %}){: .projects-logo-bsql}

# Blazing fast SQL on Rapids
{: .section-title-full}
{% capture intro_content %}
BlazingSQL is an incredibly fast distributed SQL engine on GPUs. BlazingSQL enables data scientists to easily connect large-scale data lakes to GPU-accelerated analytics. With a few lines of code, you can directly query raw file formats such as CSV and Apache Parquet inside Data Lakes like HDSF and AWS S3, and directly pipe the results into GPU memory. 
{: .subtitle .pading-top-0em .margin-top-0em}

{% endcapture %}

{% capture benefit_left %}
## <i class="fas fa-sort-amount-up-alt"></i> ETL at Scale
Distributed architecture scales to thousands of GPUs. Relative performance improvements  of engine continue to increase with scale of cluster.

{% endcapture %}

{% capture benefit_middle %}
## <i class="fas fa-burn"></i> BLazing Fast ETL
BlazingSQL currently runs ETL 20x faster than an Apache Spark cluster at price parity on a single node. With BlazingSQL, enterprise scale workloads run in seconds rather than hours. **[Read more on our blog <i class="fas fa-angle-double-right"></i>](https://blog.blazingdb.com/blazingsql-the-gpu-sql-engine-now-runs-over-20x-faster-than-apache-spark-1b0bffc990a9){: target="_blank"}**

{% endcapture %}

{% capture benefit_right %}

## <i class="fas fa-code-branch"></i> Built on RAPIDS
BlazingSQL is built on the GPU DataFrame, a shared memory model that enables libraries in the  RAPIDS AI ecosystem to seamlessly interoperate with each other. **[Read more on our blog <i class="fas fa-angle-double-right"></i>](https://blog.blazingdb.com/blazingsql-part-1-the-gpu-dataframe-gdf-and-cudf-in-rapids-ai-96ec15102240){: target="_blank"}**

{% endcapture %}


{% include section-single.html
    background="background-white" 
    padding-top="0em" padding-bottom="0em" 
    content-single=intro_content
%}
{% include section-single.html
    background="background-white" 
    padding-top="0em" padding-bottom="0em" 
    content-single=gpus_single
%}
{% include section-thirds.html 
    background="background-white" 
    padding-top="0em" padding-bottom="10em" 
    content-left-third=benefit_left 
    content-middle-third=benefit_middle 
    content-right-third=benefit_right 
%}




{% capture start_left %}
# GETTING STARTED
{: .section-title-halfs}

It’s easy to get started with BlazingSQL + RAPIDS
{: .subtitle}

## <i class="fas fa-bolt"></i> Try Now In Colab
The fastest way to get up and running is with Google Colab, a free web-based interface similar to a Jupyter Notebook that lets you quickly run BlazingSQL + RAPIDS on T4 GPUs. **[Try now in Colabratory <i class="fas fa-angle-double-right"></i>](https://colab.research.google.com/drive/1r7S15Ie33yRw8cmET7_bjCpvjJiDOdub#scrollTo=14GwxmLsTV_p){: target="_blank"}**


{% endcapture %}

{% capture start_right %}
## <i class="fab fa-readme"></i> Learn More
{: .section-subtitle-top-1}

Learn more about Colab, our Docker Container, and getting started. **[More info on BlazingSQL <i class="fas fa-angle-double-right"></i>](https://www.blazingsql.com/getstarted){: target="_blank"}**

## <i class="far fa-file-code"></i> Access BlazingSQL Docs
See the latest **[documentation from BlazingSQL <i class="fas fa-angle-double-right"></i>](https://docs.blazingdb.com/docs){: target="_blank"}**

{% endcapture %}
{% include slopecap.html 
    background="background-gray" 
    position="top" 
    slope="down" 
%}
{% include section-halfs.html 
    background="background-gray" 
    padding-top="5em" padding-bottom="10em" 
    content-left-half=start_left 
    content-right-half=start_right 
%} 
{% include slopecap.html 
    background="background-white" 
    position="top" 
    slope="up" 
%}



{% capture start_left %}
# BlazingSQL Demos

Get started with **[BlazingSQL](https://blazingsql.com/getstarted){: target="_blank"}** + **[RAPIDS](https://rapids.ai/start.html){: target="_blank"}** and try all the demos free on Google CoLab. 
{: .subtitle}

## <i class="far fa-hand-point-down"></i> Getting Started Demo
Walk through the process for getting BlazingSQL and cuDF running. Then go through a basic ETL process and query.

**[GET STARTED](https://colab.research.google.com/drive/1r7S15Ie33yRw8cmET7_bjCpvjJiDOdub#scrollTo=14GwxmLsTV_p){: target="_blank" .primary-button .blue-btn}**

{% endcapture %}

{% capture start_right %}
## <i class="far fa-file-code"></i> Federated Query Demo
{: .section-subtitle-top-1}

In a single query, join an Apache Parquet Gilem a CSV, and a GPU DataFrame (GDF) in GPU memory. **[Try now in Colabratory <i class="fas fa-angle-double-right"></i>](https://colab.research.google.com/drive/1W_kk0n2KyiUpvdCvPfAqUI_BmISGLI_P){: target="_blank"}**

## <i class="far fa-file-code"></i> Netflow Demo
{: .section-subtitle-top-1}
Query 65M rows of network security data (netflow) with BlazingSQL. **[Try now in Colabratory <i class="fas fa-angle-double-right"></i>](https://colab.research.google.com/drive/1RYOYthqxUl922LYMAuNneKgmWB8YGTKB){: target="_blank"}**

## <i class="far fa-file-code"></i> Taxi Demo
Train a linear regression model with cuML on 55 million rows of public NYC Taxi Data loaded with BlazingSQL. **[Try now in Colabratory <i class="fas fa-angle-double-right"></i>](https://colab.research.google.com/drive/1yrml5FhQd7VHwcvpUql1LspjCjKg8u0w){: target="_blank"}**

## <i class="far fa-file-code"></i> BlazingSQL vs Apache Spark Demo
Analyze 20 million rows of net flow data. Compare BlazingSQL and Apache Spark timings for the same workload. **[Try now in Colabratory <i class="fas fa-angle-double-right"></i>](https://colab.research.google.com/drive/1EbPE9FwFur7fE2054BH9s23Kd0FiUgGo#scrollTo=kJyD4oSbugE0){: target="_blank"}**

{% endcapture %}
{% include section-halfs.html 
    background="background-white" 
    padding-top="5em" padding-bottom="10em" 
    content-left-half=start_left 
    content-right-half=start_right 
%} 


{% capture end_bottom %}
# Get Started With BlazingSQL
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

{% include cta-footer-blazingsql.html 
   background="background-darkpurple" 
%}

