---
title: "RAPIDS + pip"
description: "RAPIDS + pip"
tagline: "RAPIDS + pip"
button_text: "Install Now"
button_link: "#install"
layout: default
---

![RAPIDS pip]({{ site.baseurl }}{% link /assets/images/pypip.png %}){: .projects-logo}


# RAPIDS is back on Pip
{: .section-title-full}

{% capture intro_content %}

RAPIDS users can once again install RAPIDS via pip!  This is an **experimental release** supporting single GPU usage.  cuDF, dask-cuDF, cuML, cuGraph, RMM and RAFT release 22.10 pip packages are available **[right now](#install)**.  The team is excited to get these packages out into the wild and see how the RAPIDS community uses them!

[If you find issues, please file them in the respective RAPIDS Repositories](https://github.com/rapidsai){: target="_blank"}.
{: .subtitle}

{% endcapture %}

{% include section-single.html
    background="background-white"
    padding-top="3em" padding-bottom="10em"
    content-single=intro_content
%}

<div id="install"></div>
{% capture start_single %}
# Installing RAPIDS via pip
{: .section-title-full .text-white}
{% endcapture %}

{% capture start_left %}

## Prerequisites

> <i class="fas fa-desktop text-white"></i> **OS:** One of the following OS versions:

>> <i class="fa-brands fa-ubuntu text-white"></i> Ubuntu 18.04/20.04 or CentOS 7 / Rocky Linux 8 with <code>gcc/++</code> 9.0+

>> <i class="fas fa-desktop text-white"></i> Windows 11 using WSL2  **[See separate install guide <i class="fa fa-angle-double-right" aria-hidden="true"></i>](wsl2.html){: target="_blank"}**

>>> <i class="fas fa-chevron-circle-right text-white"></i> In addition, WSL2 pip installations require following **[this guide to install the CUDA Toolkit without drivers.](https://docs.nvidia.com/cuda/wsl-user-guide/index.html#cuda-support-for-wsl2){: target="_blank"}**

> <i class="fas fa-info-circle text-white"></i> **Glibc version:** x86_64 wheels require glibc >= 2.17 and aarch64 wheels require glibc >= 2.31.

> <i class="fas fa-microchip text-white"></i> **GPU:** Only GPUs with **[Compute capability](https://developer.nvidia.com/cuda-gpus){: target="_blank"}** 6.0 or higher (i.e. Pascal generation or newer) are supported.

> <i class="fas fa-download text-white"></i> **CUDA >= 11.5**, with at least the v495.29.05 driver. To use CUDA 11.2, 11.3, or 11.4, please see Troubleshooting and Known Issues.

> <i class="fab fa-python text-white"></i> **Python and pip version:** Python 3.8 or 3.9 using pip 20.3+ with **[PEP600 support](https://peps.python.org/pep-0600/){: target="_blank"}**.

## <i class="far fa-comments text-white"></i> Connect

> Join our community conversations about RAPIDS and pip using **[Twitter](https://twitter.com/rapidsai){: target="_blank"}**, **[Slack]({{ site.slack_invite }}){: target="_blank"}**, or ask a question on **[StackOverflow](https://stackoverflow.com/tags/rapids){: target="_blank"}**.

> If you find issues, please file them in the respective RAPIDS repo:

>> **[cuDF](https://github.com/rapidsai/cudf/issues/new/choose ){: target="_blank"}** |
>> **[cuML](https://github.com/rapidsai/cuml/issues/new/choose ){: target="_blank"}** |
>> **[cuGraph](https://github.com/rapidsai/cugraph/issues/new/choose ){: target="_blank"}** |
>> **[RMM](https://github.com/rapidsai/rmm/issues/new/choose ){: target="_blank"}** |
>> **[RAFT](https://github.com/rapidsai/raft/issues/new/choose ){: target="_blank"}**
{% endcapture %}

{% capture start_right %}
## <i class="fad fa-terminal text-white"></i> Installation Commands


	pip install cudf-cu11 dask-cudf-cu11 --extra-index-url=https://pypi.ngc.nvidia.com
	pip install cuml-cu11 --extra-index-url=https://pypi.ngc.nvidia.com
	pip install cugraph-cu11 --extra-index-url=https://pypi.ngc.nvidia.com

> <i class="fas fa-info-circle text-white"></i> The RAPIDS pip packages are hosted on the NVIDIA NGC index today.

> <i class="fas fa-info-circle text-white"></i> On aarch64, cupy needs to be installed separately:

	pip install cupy-cuda11x -f https://pip.cupy.dev/aarch64

## <i class="fa-solid fa-screwdriver-wrench text-white"></i> Troubleshooting and Known Issues

> <i class="fas fa-info-circle text-white"></i> When installing these packages with CUDA 11.2, 11.3, or 11.4, you may experience a "Failed to import CuPy" error. To resolve this error, please uninstall cupy-cuda115 and install cupy-cuda11x:

    pip uninstall cupy-cuda115; pip install cupy-cuda11x

> <i class="fas fa-info-circle text-white"></i> The following error message indicates a problem with your environment:

    ERROR: Could not find a version that satisfies the requirement cudf-cu11 (from versions: 0.0.1, 22.10.0)
    ERROR: No matching distribution found for cudf-cu11

> Check the suggestions below for possible resolutions.

> <i class="fas fa-chevron-circle-right text-white"></i> Your Python version must be 3.8 or 3.9.

> <i class="fas fa-chevron-circle-right text-white"></i> RAPIDS pip packages require a recent version of pip that **[supports PEP600](https://peps.python.org/pep-0600/){: target="_blank"}**.  Some users may need to update pip:

	pip install -U pip

> <i class="fas fa-chevron-circle-right text-white"></i> Infiniband is not supported yet in this release

> <i class="fas fa-chevron-circle-right text-white"></i> These packages are not compatible with Tensorflow pip packages. Please use the <a href="https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tensorflow">NGC containers</a> or conda packages instead.

> <i class="fas fa-chevron-circle-right text-white"></i> Dask / Jupyter / Tornado 6.2 dependency conflicts can occur. Install jupyter-client 7.3.4 if the error below occurs:

      ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
      jupyter-client 7.4.2 requires tornado>=6.2, but you have tornado 6.1 which is incompatible.


{% endcapture %}

{% include slopecap.html
    background="background-purple"
    position="top"
    slope="down"
%}
{% include section-single.html
    background="background-purple"
    padding-top="2em" padding-bottom="0em"
    content-single=start_single
%}
{% include section-halfs.html
    background="background-purple"
    padding-top="0em" padding-bottom="10em"
    content-left-half=start_left
    content-right-half=start_right
%}
{% include cta-footer-help.html
   background="background-darkpurple"
%}
