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

{% capture gpus_single %}

# Benefits
{: .pading-bottom-0em}

{% endcapture %}
{% capture benefit_left %}

## <i class="fas fa-sort-amount-up-alt"></i> ETL at Scale
{: .margin-top-0em}

Distributed architecture scales to thousands of GPUs. Relative performance improvements  of engine continue to increase with scale of cluster.
<br>
{: .padding-bottom-6em}
{% endcapture %}

{% capture benefit_middle %}

## <i class="fas fa-bolt"></i> BLazing Fast ETL
{: .margin-top-0em}

BlazingSQL currently runs ETL 20x faster than an Apache Spark cluster at price parity on a single node. With BlazingSQL, enterprise scale workloads run in seconds rather than hours.
<br>
**[Read more on our blog <i class="fas fa-angle-double-right"></i>](https://blog.blazingdb.com/blazingsql-the-gpu-sql-engine-now-runs-over-20x-faster-than-apache-spark-1b0bffc990a9){: target="_blank"}**
{: .padding-bottom-6em}
{% endcapture %}

{% capture benefit_right %}

## <i class="fas fa-microchip"></i> Built on RAPIDS
{: .margin-top-0em}

BlazingSQL is built on the GPU DataFrame, a shared memory model that enables libraries in the  RAPIDS AI ecosystem to seamlessly interoperate with each other.
**[Read More <i class="fas fa-angle-double-right"></i>](https://blog.blazingdb.com/blazingsql-part-1-the-gpu-dataframe-gdf-and-cudf-in-rapids-ai-96ec15102240){: target="_blank"}**
{: .padding-bottom-6em}
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
    padding-top="0em" padding-bottom="4em" 
    content-left-third=benefit_left 
    content-middle-third=benefit_middle 
    content-right-third=benefit_right 
%}




{% capture start_left %}
# GETTING STARTED
{: .section-title-halfs}

It’s easy to get started with BlazingSQL + RAPIDS.ai 
{: .subtitle}

## <i class="fas fa-burn"></i> Run on Colab
<br>
The fastest way to get up and running is with Google Colab, a free web-based interface similar to a Jupyter Notebook that lets you quickly run BlazingSQL + RAPIDS AI on T4 GPUs.
<br>
**[Try Now in COLAB](https://colab.research.google.com/drive/1r7S15Ie33yRw8cmET7_bjCpvjJiDOdub#scrollTo=14GwxmLsTV_p){: target="_blank"}**.


{% endcapture %}

{% capture start_right %}

## <i class="fas fa-arrow-circle-right padding-top-1em"></i> Learn More
<br>
Learn more about Colab, our Docker Container, and getting started. 
<br>
**[More Info on BlazingSQL](https://www.blazingsql.com/getstarted){: target="_blank"}**.
<br>
<br>
## <i class="fab fa-readme"></i> Access BlazingSQL Docs
<br>
See the latest **[documentation from BlazingSQL](https://docs.blazingdb.com/docs){: target="_blank"}**.

{% endcapture %}
{% include slopecap.html 
    background="background-gray" 
    position="top" 
    slope="down" 
%}
{% include section-halfs.html 
    background="background-gray" 
    padding-top="4em" padding-bottom="10em" 
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

Try **[BlazingSQL](https://blazingsql.com/getstarted){: target="_blank"}** + **[Rapids AI](https://rapids.ai/start.html){: target="_blank"}** Demos free on Google Colab.
{: .subtitle}

## <i class="far fa-star"></i> Getting Started Demo
Walk through the process for getting BlazingSQL and cuDF running. Then go through a basic ETL process and query.
{: .section-title-halfs} 
<br>
**[Try It](https://colab.research.google.com/drive/1r7S15Ie33yRw8cmET7_bjCpvjJiDOdub#scrollTo=14GwxmLsTV_p){: target="_blank" .primary-button .blue-btn}**

{% endcapture %}

{% capture start_right %}

## <i class="far fa-file-code"></i> Federated Query Demo
{: .section-subtitle-top-1}
In a single query, join an Apache Parquet Gilem a CSV, and a GPU DataFrame (GDF) in GPU memory.
{: .section-title-halfs}

**[Try It](https://colab.research.google.com/drive/1W_kk0n2KyiUpvdCvPfAqUI_BmISGLI_P){: target="_blank"}**

## <i class="far fa-file-code"></i> Netflow Demo
{: .section-subtitle-top-1}
Query 65M rows of network security data (netflow) with BlazingSQL.
{: .section-title-halfs}

**[Try It](https://colab.research.google.com/drive/1RYOYthqxUl922LYMAuNneKgmWB8YGTKB){: target="_blank"}**

## <i class="far fa-file-code"></i> Taxi Demo
Train a linear regression model with cuML on 55 million rows of public NYC Taxi Data loaded with BlazingSQL.
{: .section-title-halfs}

**[Try It](https://colab.research.google.com/drive/1yrml5FhQd7VHwcvpUql1LspjCjKg8u0w){: target="_blank"}**

## <i class="far fa-file-code"></i> BlazingSQL vs Apache Spark Demo
Analyze 20 million rows of net flow data. Compare BlazingSQL and Apache Spark timings for the same workload.
{: .section-title-halfs}

**[Try It](https://colab.research.google.com/drive/1EbPE9FwFur7fE2054BH9s23Kd0FiUgGo#scrollTo=kJyD4oSbugE0){: target="_blank"}**

{% endcapture %}
{% include section-halfs.html 
    background="background-white" 
    padding-top="5em" padding-bottom="10em" 
    content-left-half=start_left 
    content-right-half=start_right 
%} 


{% capture end_bottom %}
# Get started with BlazingSQL
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

