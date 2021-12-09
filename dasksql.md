---
title: "RAPIDS + Dask-SQL"
description: "Fast, Scalable SQL on RAPIDS with Dask-SQL"
tagline: "Fast, Scalable SQL on RAPIDS"
button_text: "Dask-SQL"
button_link: "https://dask-sql.readthedocs.io/en/latest/"
layout: default
---

![Dask-SQL]({{ site.baseurl }}{% link /assets/images/dasksql3.png %}){: .projects-logo-bsql}

# Fast, Scalable SQL on Rapids
{: .section-title-full}
{% capture intro_content %}
Dask-SQL is an incredibly fast distributed SQL engine on GPUs.  Dask-SQL enables data scientists to easily connect large-scale data lakes to GPU-accelerated analytics.  It now has experimental support for running SQL queries on CUDA-enabled GPUs by utilizing RAPIDS libraries like cuDF, enabling highly scalable, GPU accelerated compute for SQL.
{: .subtitle .pading-top-0em .margin-top-0em}

{% endcapture %}

{% capture benefit_left %}
## <i class="fas fa-sort-amount-up-alt"></i> ETL at Scale
Distributed architecture scales to thousands of GPUs. Relative performance improvements of the engine continue to increase with scale of cluster.  Dask-SQL understands a large amount of formats (csv, parquet, json,…) and locations (s3, hdfs, gcs,…).  If Dask supports it, so will Dask-SQL!
<br> <br>

{% endcapture %}

{% capture benefit_middle %}
## <i class="fas fa-burn"></i> Based on BlazingSQL
Dask-SQL follows BlazingSQL's syntax, making converting over your GPU accelerated workflows easy.  It can run ETL 20x faster than an Apache Spark cluster at price parity on a single node. With Dask-SQL, enterprise scale workloads run in seconds rather than hours. 
<br> <br>

{% endcapture %}

{% capture benefit_right %}

## <i class="fas fa-code-branch"></i> Enabled with RAPIDS
Dask-SQL has been adapted for the GPU DataFrame, a shared memory model that enables libraries in the RAPIDS AI ecosystem to seamlessly interoperate with each other. 
<br><br>

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

It’s easy to get started with RAPIDS + Dask-SQL
{: .subtitle}

## <i class="fad fa-bookmark"></i> Try with RAPIDS 
You can use Dask-SQL with a RAPIDS install on our <br> **[Get Started Page <i class="fas fa-angle-double-right"></i>](start.html)**. 

{% endcapture %}

{% capture start_right %}
## <i class="fab fa-readme"></i> Learn More
{: .section-subtitle-top-1}

Learn more about Dask-SQL on the and try out their examples on their 
**[Welcome To Dask-SQL Github Repository <i class="fas fa-angle-double-right"></i>](https://github.com/rapidsai-community/notebooks-contrib/tree/main/community_tutorials_and_guides/dask-sql){: target="_blank"}**

## <i class="far fa-file-code"></i> Access Dask-SQL Docs
See the latest **[documentation for Dask-SQL <i class="fas fa-angle-double-right"></i>](https://dask-sql.readthedocs.io/en/latest/){: target="_blank"}**

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

