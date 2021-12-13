---
title: "RAPIDS + BlazingSQL"
description: "Blazing Fast SQL on RAPIDS with BlazingSQL"
tagline: "Blazing Fast SQL on RAPIDS"
button_text: "BLAZINGSQL.COM"
button_link: "https://blazingsql.com/"
layout: default
---

![BLAZINGSQL]({{ site.baseurl }}{% link /assets/images/blazingsql.png %}){: .projects-logo-bsql}

# Blazing fast SQL on Rapids
{: .section-title-full}
{% capture intro_content %}
**[RAPIDS support of BlazingSQL has been deprecated with release 21.12](https://docs.rapids.ai/notices/rsn0012/) in favor of [Dask-SQL](https://dask-sql.readthedocs.io/en/latest/)**. You can still use it with RAPIDS 21.08 and 21.10.
<br><br>BlazingSQL is an incredibly fast distributed SQL engine on GPUs. BlazingSQL enabled data scientists to easily connect large-scale data lakes to GPU-accelerated analytics. With a few lines of code, you can directly query raw file formats such as CSV and Apache Parquet inside Data Lakes like HDFS and AWS S3, and directly pipe the results into GPU memory. 

{: .subtitle .pading-top-0em .margin-top-0em}

{% endcapture %}

{% capture benefit_left %}
## <i class="fas fa-sort-amount-up-alt"></i> ETL at Scale
Distributed architecture scales to thousands of GPUs. Relative performance improvements of the engine continue to increase with scale of cluster.
<br> <br>
**[Read more on our blog <i class="fas fa-angle-double-right"></i>](https://www.infoworld.com/article/3610188/blazingsql-review-fast-etl-for-gpu-based-data-science.html){: target="_blank"}**

{% endcapture %}

{% capture benefit_middle %}
## <i class="fas fa-burn"></i> BLazing Fast ETL
BlazingSQL currently runs ETL 20x faster than an Apache Spark cluster at price parity on a single node. With BlazingSQL, enterprise scale workloads run in seconds rather than hours. 
<br> <br>
**[Read more on our blog <i class="fas fa-angle-double-right"></i>](https://blog.blazingdb.com/blazingsql-the-gpu-sql-engine-now-runs-over-20x-faster-than-apache-spark-1b0bffc990a9){: target="_blank"}**

{% endcapture %}

{% capture benefit_right %}

## <i class="fas fa-code-branch"></i> Built on RAPIDS
BlazingSQL is built on the GPU DataFrame, a shared memory model that enables libraries in the RAPIDS AI ecosystem to seamlessly interoperate with each other. 
<br><br>
**[Read more on our blog <i class="fas fa-angle-double-right"></i>](https://blog.blazingdb.com/blazingsql-part-1-the-gpu-dataframe-gdf-and-cudf-in-rapids-ai-96ec15102240){: target="_blank"}**

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

It’s easy to get started with RAPIDS + BlazingSQL
{: .subtitle}

## <i class="fad fa-bookmark"></i> Try with RAPIDS 
You can use BlazingSQL with a RAPIDS 21.08 or 21.10 install from: <br>
**Conda**:
```
conda install -c rapidsai -c nvidia -c conda-forge blazingsql=21.10
```
or 
```
conda install -c rapidsai -c nvidia -c conda-forge blazingsql=21.08
```
<br>
**Docker**:<br>
Pull either the 21.08 or 21.10 Docker containers with tag (BlazingSQL is included)

{% endcapture %}

{% capture start_right %}
## <i class="fab fa-readme"></i> Learn More
{: .section-subtitle-top-1}

Learn more about BlazingSQL on the and try out their examples on their 
**[Welcome To BlazingSQL Github Repository <i class="fas fa-angle-double-right"></i>](https://github.com/BlazingDB/Welcome_to_BlazingSQL_Notebooks){: target="_blank"}**

## <i class="far fa-file-code"></i> Access BlazingSQL Docs
See the latest **[documentation for BlazingSQL <i class="fas fa-angle-double-right"></i>](https://docs.blazingsql.com/){: target="_blank"}**

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


{% capture end_bottom %}
# Get Started With BlazingSQL
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

{% include cta-footer-blazingsql.html 
   background="background-darkpurple" 
%}

