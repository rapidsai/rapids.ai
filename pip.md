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

RAPIDS users can once again install RAPIDS via pip!  This is an experimental release.  These packages are still experimental! They come from a snapshot build of RAPIDS 22.10. The team is continuing to improve these and work toward a 22.10 release. [If you find issues, please file them in the RAPIDS pip Repo](https://github.com/rapidsai/pypi-wheel-scripts).
{: .subtitle}

{% endcapture %}

{% include section-single.html
    background="background-white" 
    padding-top="3em" padding-bottom="5em" 
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

>> <i class="fa-brands fa-ubuntu text-white"></i> Ubuntu 20.04 or CentOS 7 / Rocky Linux 8 with <code>gcc/++</code> 9.0+
	
>> <i class="fas fa-desktop text-white"></i> Windows 11 using WSL2  **[See separate install guide <i class="fa fa-angle-double-right" aria-hidden="true"></i>](wsl2.html){: target="_blank"}**

> <i class="fas fa-info-circle text-white"></i> **Manylinux Version:** 2_32. Requires glibc >.= 2.32

> <i class="fas fa-microchip text-white"></i> **GPU:** Only GPUs with [Compute capability](https://developer.nvidia.com/cuda-gpus){: target="_blank"} 7.0 or higher are supported.
  
> <i class="fas fa-download text-white"></i> **CUDA:** >= 11.2, with at least the v460.27.03 driver

> <i class="fab fa-python text-white"></i> **Python and pip version:** Python 3.8 or 3.9 using pip 20.3+ 

{% endcapture %}

{% capture start_right %}
## <i class="fad fa-terminal text-white"></i> Installation Command


	pip install -i https://pypi.k8s.rapids.ai/simple rmm-cu11 cudf-cu11

The RAPIDS pip packages are hosted in a private repo, but will found on public repos soon.  Please check back for any updates!

## <i class="fa-solid fa-screwdriver-wrench text-white"></i> Troubleshooting

> <i class="fas fa-info-circle text-white"></i> RAPIDS pip packages require PEP600 support.  Some users may need to update pip using 
	
	`pip install -U pip` 

> before using the installation command above.

> <i class="fas fa-info-circle text-white"></i> Infiniband is not supported yet in this release

## <i class="far fa-comments text-white"></i> Connect 

> Join our community conversations about RAPIDS and pip using **[Twitter](https://twitter.com/rapidsai){: target="_blank"}**, **[Slack]({{ site.slack_invite }}){: target="_blank"}**, or ask a question on **[StackOverflow](https://stackoverflow.com/tags/rapids){: target="_blank"}**.

> If you find issues, please [file them in the RAPIDS pip Repo](https://github.com/rapidsai/pypi-wheel-scripts).

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
