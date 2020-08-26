---
title: "RAPIDS + Cloud"
description: "Deploying RAPIDS in the Cloud"
tagline: "Deploying RAPIDS in the Cloud"
button_text: "Deploy Now"
button_link: "https://rapids.ai/cloud"
layout: default
---

![Placeholder]({{ site.baseurl }}{% link /assets/images/RAPIDs-cloud.png %}){: .projects-logo}

# How to Deploy RAPIDS in the Cloud
{: .section-title-full}

{% capture intro_content %}

RAPIDS’s GPU accelerated data science tools can be deployed on all of the major clouds, allowing anyone to take advantage of the speed increases and TCO reductions that RAPIDS enables.
{: .subtitle}

RAPIDS can be deployed in a number of ways, from hosted Jupyter notebooks, to the major HPO services, all the way up to large-scale clusters via Dask or Kubernetes.

Deploying on the cloud will require you to make use of supported GPU instances. Each major cloud provider has GPU instances that are supported by RAPIDS with varying capabilities and price points--the below chart identifies the major instance types at each cloud.


{% endcapture %}

{% include section-single.html
    background="background-white" 
    padding-top="0em" padding-bottom="10em" 
    content-single=intro_content
%}

{% capture csp_left %}
![aws]({{ site.baseurl }}{% link /assets/images/AWS-logo.png %}){: .center-logo}
[Amazon Web Services](#aws){: .center-text}

{% endcapture %}
{% capture csp_mid %}
![azure]({{ site.baseurl }}{% link /assets/images/MS-azure-logo.png %}){: .center-logo}
[Microsoft Azure](#azure){: .center-text}

{% endcapture %}
{% capture csp_right %}
![gcp]({{ site.baseurl }}{% link /assets/images/GCP-logo.png %}){: .center-logo}
[Google Cloud](#GCP){: .center-text}

{% endcapture %}
<!-- https://tableconvert.com/ -->
{% capture csp_table %}

| Cloud Provider | Instance Type | Instance name  | \# GPUs | GPU Type | Per GPU RAM \(GB\) | Per GPU SP Performance \(TFLOPS\) |
|----------------|---------------|----------------|---------|----------|--------------------|-----------------------------------|
| AWS            | G4            | g4dn\.xlarge   | 1       | T4       | 16                 | 8\.1                              |
|                |               | g4dn\.8xlarge  | 1       | T4       | 16                 | 8\.1                              |
|                |               | g4dn\.12xlarge | 4       | T4       | 16                 | 8\.1                              |
|                |               | g4dn\.16xlarge | 1       | T4       | 16                 | 8\.1                              |
|                |               | g4dn\.metal    | 8       | T4       | 16                 | 8\.1                              |
|                | P3            | p3\.2xlarge    | 1       | V100     | 16                 | 14                                |
|                |               | p3\.8xlarge    | 4       | V100     | 16                 | 14                                |
|                |               | p3\.16xlarge   | 8       | V100     | 16                 | 14                                |
|                |               | p3dn\.24xlarge | 8       | V100     | 32                 | 14                                |


| Cloud Provider | Instance Type | Instance name | \# GPUs | GPU Type | Per GPU RAM \(GB\) | Per GPU SP Performance \(TFLOPS\) |
|----------------|---------------|---------------|---------|----------|--------------------|-----------------------------------|
| AzureML        | NDs Series    | ND6s          | 1       | P40      | 8                  | 12                                |
|                |               | ND12s         | 2       | P40      | 8                  | 12                                |
|                |               | ND24s         | 4       | P40      | 8                  | 12                                |
|                |               | ND24rs        | 4       | P40      | 8                  | 12                                |
|                | NCs v2 Series | NC6s v2       | 1       | P100     | 16                 | 10\.6                             |
|                |               | NC12s v2      | 2       | P100     | 16                 | 10\.6                             |
|                |               | NC24s v2      | 4       | P100     | 16                 | 10\.6                             |
|                |               | NC24rs v2     | 4       | P100     | 16                 | 10\.6                             |
|                | NCs v3 Series | NC6s v3       | 1       | V100     | 16                 | 14                                |
|                |               | NC12s v3      | 2       | V100     | 16                 | 14                                |
|                |               | NC24s v3      | 4       | V100     | 16                 | 14                                |
|                |               | NC24rs v3     | 4       | V100     | 16                 | 14                                |
|                | NDs v2 Series | ND40rs        | 8       | V100     | 16                 | 14                                |



| Cloud Provider | Instance Type              | Instance name    | \# GPUs    | GPU Type | Per GPU RAM \(GB\) | Per GPU SP Performance \(TFLOPS\) |
|----------------|----------------------------|------------------|------------|----------|--------------------|-----------------------------------|
| GCP            | GPU Compute Workload Addon | Any Machine Type | As desired | P4       | 8                  | 5\.5                              |
|                |                            | Any Machine Type | As desired | P100     | 16                 | 10\.6                             |
|                |                            | Any Machine Type | As desired | T4       | 16                 | 8\.1                              |
|                |                            | Any Machine Type | As desired | V100     | 16                 | 14                                |
|                | A2                         | TBD \- In beta   | As desired | A100     | 32                 | 78                                |


{% endcapture %}

{% include slopecap.html 
    background="background-purple" 
    position="top" 
    slope="down" 
%}
{% include section-thirds.html 
    background="background-purple" 
    padding-top="5em" padding-bottom="5em" 
    content-left-third=csp_left
    content-middle-third=csp_mid
    content-right-third=csp_right
%}
{% include section-single.html
    background="background-purple" 
    padding-top="5em" padding-bottom="5em" 
    content-single=csp_table
%}
{% include slopecap.html 
    background="background-purple" 
    position="bottom" 
    slope="up" 
%}

<!-- AWS -->
{% capture aws_intro %}
![aws]({{ site.baseurl }}{% link /assets/images/AWS-logo.png %})

RAPIDS can be deployed on Amazon Web Services (AWS) in several ways:
On a single EC2 instance
On a cluster using Dask
On a cluster using Kubernetes and EKS/GKE/AKS
On Amazon Sagemaker

{% endcapture %}

{% include section-single.html
    background="background-gray" 
    padding-top="10em" padding-bottom="3em" 
    content-single=aws_intro
%}
{% include slopecap.html 
    background="background-gray" 
    position="bottom" 
    slope="down" 
%}

{% capture aws_ec2 %}
## <i class="fal fa-cloud-upload"></i> Single Instance (EC2)

text

{% endcapture %}

{% capture aws_dask %}
## <i class="fal fa-cloud-upload"></i> Cluster via Dask

text

{% endcapture %}

{% capture aws_kub %}
## <i class="fal fa-cloud-upload"></i> Cluster via Kubernetes

text

{% endcapture %}

{% capture aws_sage %}
## <i class="fal fa-cloud-upload"></i> Sagemaker

text

{% endcapture %}

{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="3em" 
    content-single=aws_ec2
%}
{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="3em" 
    content-single=aws_dask
%}
{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="3em" 
    content-single=aws_kub
%}
{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="10'em" 
    content-single=aws_sage
%}

<!-- Azure -->
{% capture azure_intro %}
![azure]({{ site.baseurl }}{% link /assets/images/MS-azure-logo.png %})

  RAPIDS can be deployed on Microsoft Azure via several methods:
  On a single instance
  In a cluster via Dask
  In a cluster via Kubernetes
  On Azure’s AzureML service
{% endcapture %}

{% include slopecap.html 
    background="background-gray" 
    position="top" 
    slope="down" 
%}
{% include section-single.html
    background="background-gray" 
    padding-top="5em" padding-bottom="3em" 
    content-single=azure_intro
%}
{% include slopecap.html 
    background="background-gray" 
    position="bottom" 
    slope="up" 
%}

{% capture az_single %}
## <i class="fal fa-cloud-upload"></i> Single Instance (VM)

text

{% endcapture %}

{% capture az_dask %}
## <i class="fal fa-cloud-upload"></i> Cluster via Dask

text

{% endcapture %}

{% capture az_kub %}
## <i class="fal fa-cloud-upload"></i> Cluster via Kubernetes

text

{% endcapture %}

{% capture az_ml %}
## <i class="fal fa-cloud-upload"></i> AzureML Service

text

{% endcapture %}

{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="3em" 
    content-single=az_single
%}
{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="3em" 
    content-single=az_dask
%}
{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="3em" 
    content-single=az_kub
%}
{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="10em" 
    content-single=az_ml
%}

<!-- Google Cloud -->
{% capture gcp_intro %}
![gcp]({{ site.baseurl }}{% link /assets/images/GCP-logo.png %})

  RAPIDS can be used in Google Cloud in several different ways:
  On a single instance
  On a cluster using Dask (via Dataproc)
  On a cluster using Kubernetes
  On CloudAI

{% endcapture %}

{% include slopecap.html 
    background="background-gray" 
    position="top" 
    slope="down" 
%}
{% include section-single.html
    background="background-gray" 
    padding-top="5em" padding-bottom="3em" 
    content-single=gcp_intro
%}
{% include slopecap.html 
    background="background-gray" 
    position="bottom" 
    slope="up" 
%}

{% capture gc_single %}
## <i class="fal fa-cloud-upload"></i> Single Instance

text

{% endcapture %}

{% capture gc_dask %}
## <i class="fal fa-cloud-upload"></i> Cluster via Dask (Dataproc)

text

{% endcapture %}

{% capture gc_kub %}
## <i class="fal fa-cloud-upload"></i> Cluster via Kubernetes

text

{% endcapture %}

{% capture gc_ai %}
## <i class="fal fa-cloud-upload"></i> Google CloudAI

text

{% endcapture %}

{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="3em" 
    content-single=az_single
%}
{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="3em" 
    content-single=gc_dask
%}
{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="3em" 
    content-single=gc_kub
%}
{% include section-single.html
    background="background-white" 
    padding-top="5em" padding-bottom="10em" 
    content-single=gc_ai
%}


{% capture end_bottom %}
# TRY RAPIDS in the Cloud
{: .section-title-full .text-white}

{% endcapture %}
{% include slopecap.html 
    background="background-darkpurple" 
    position="top" 
    slope="up" 
%}
{% include section-single.html
    background="background-darkpurple" 
    padding-top="0em" padding-bottom="0em" 
    content-single=end_bottom
%}
{% include cta-footer.html 
    name="Experience Data Science on GPUs with RAPIDS" 
    tagline=""
    button="GET STARTED"
    link="start.html"
%}
