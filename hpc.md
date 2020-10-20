---
title: "HPC RAPIDS DEPLOYMENT"
description: "How to Deploy RAPIDS on HPC"
tagline: "Deploying RAPIDS on HPC"
button_text: "Deploy Now"
layout: default
---

![cloud]({{ site.baseurl }}{% link /assets/images/RAPIDs-cloud.png %}){: .projects-logo}

{% capture intro_content %}

RAPIDS’s GPU accelerated data science tools can be deployed on all of the major clouds, allowing anyone to take advantage of the speed increases and TCO reductions that RAPIDS enables.
{: .subtitle}

RAPIDS works well in HPC settings where often users use SLURM to deploy jobs onto Multi-Node Multi-GPU clusters

{% endcapture %}

{% include section-single.html
    background="background-white"
    padding-top="0em" padding-bottom="10em"
    content-single=intro_content
%}

<!-- AWS -->
<div id="SLURM"></div>
{% capture aws_intro %}

![aws]({{ site.baseurl }}{% link /assets/images/slurm-logo.png %})
## <i class="fab"></i> SLURM

RAPIDS can be deployed on HPC in standard sbatch/srun/salloc ways:
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
## <i class="fab"></i> SLURM

**1. Start Scheduler.**

```bash
#!/usr/bin/env bash

#SBATCH -J dask-scheduler
#SBATCH -n 1
#SBATCH -t 00:10:00

module load cuda/11.0.3
CONDA_ROOT=/gpfs/fs1/user/miniconda3
source $CONDA_ROOT/etc/profile.d/conda.sh
conda activate rapids

LOCAL_DIRECTORY=/gpfs/fs1/user/dask-local-directory
mkdir $LOCAL_DIRECTORY
dask-scheduler \
    --protocol tcp \
    --scheduler-file "$LOCAL_DIRECTORY/dask-scheduler.json"
```


**1. Start Dask CUDA workers.**

```bash
#!/usr/bin/env bash

#SBATCH -J dask-cuda-workers
#SBATCH -t 00:10:00

module load cuda/11.0.3
CONDA_ROOT=/gpfs/fs1/bzaitlen/miniconda3
source $CONDA_ROOT/etc/profile.d/conda.sh
conda activate 20201020-nightly

LOCAL_DIRECTORY=/gpfs/fs1/bzaitlen/dask-local-directory
mkdir $LOCAL_DIRECTORY
dask-cuda-worker \
    --rmm-pool-size 14GB \
    --scheduler-file "$LOCAL_DIRECTORY/dask-scheduler.json"
```

{: .margin-bottom-3em}

**[Jump to Top <i class="fad fa-chevron-double-up"></i>](#deploy)**

{% endcapture %}

<div id="AWS-EC2"></div>
{% include section-single.html
    background="background-white"
    padding-top="6em" padding-bottom="0em"
    content-single=aws_ec2
%}
<div id="AWS-Dask"></div>
{% include section-single.html
    background="background-white"
    padding-top="3em" padding-bottom="0em"
    content-single=aws_dask
%}
<div id="AWS-Kubernetes"></div>
{% include section-single.html
    background="background-white"
    padding-top="3em" padding-bottom="0em"
    content-single=aws_kub
%}
<div id="AWS-Sagemaker"></div>
{% include section-single.html
    background="background-white"
    padding-top="3em" padding-bottom="10em"
    content-single=aws_sage
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
