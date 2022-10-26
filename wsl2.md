---
title: "RAPIDS + WSL 2"
description: "Use RAPIDS on Windows with WSL 2"
tagline: "The power of RAPIDS, now available for Windows"
button_text: "Install Now"
button_link: "#install"
layout: default
---

![RAPIDS WSL 2]({{ site.baseurl }}{% link /assets/images/csp+hpo.png %}){: .projects-logo}


# Use RAPIDS <br> on Windows
{: .section-title-full}

{% capture intro_content %}

Windows users can now tap into GPU accelerated data science on their local machines using RAPIDS on Windows Subsystem for Linux 2 (WSL 2)! WSL 2 is a Windows feature that enables users to run native Linux command-line tools directly on Windows. Using this feature does not require a dual boot environment, removing complexity and saving you time. An NVIDIA GPU with [Compute capability](https://developer.nvidia.com/cuda-gpus){: target="_blank"} 7.0 or higher is required.
{: .subtitle}

{% endcapture %}

{% include section-single.html
    background="background-white"
    padding-top="3em" padding-bottom="5em"
    content-single=intro_content
%}

<div id="prereqs"></div>
{% capture start_single %}
# Before Installing
{: .section-title-full .text-white}
{% endcapture %}

{% capture start_left %}
## Prerequisites

> <i class="fas fa-desktop text-white"></i> **OS:** Windows 11.

> <i class="fas fa-info-circle text-white"></i> **WSL Version:** WSL 2.  WSL 1 is not supported.

> <i class="fas fa-microchip text-white"></i> **GPU:** Only GPUs with [Compute capability](https://developer.nvidia.com/cuda-gpus){: target="_blank"} 7.0 or higher are supported on RAPIDS in WSL 2.  GPUs with 16GB or more of RAM is recommended

> <i class="fas fa-download text-white"></i> **WSL 2 Instance:** Ubuntu 20.04 instance for WSL 2.

## <i class="fad fa-terminal"></i> Limitations

> <i class="fas fa-info-circle text-white"></i> Only single GPU is supported.

> <i class="fas fa-info-circle text-white"></i> GPU Direct Storage is not supported.

> <i class="fas fa-info-circle text-white"></i> At least 8 GB of RAM and a relatively fast CPU are strongly recommended https://docs.microsoft.com/en-us/windows/wsl/install

{% endcapture %}

{% capture start_right %}
## <i class="fab fa-docker"></i> Choose a Docker Installation Method
> <i class="fab fa-windows text-white"></i> **Install Docker Desktop in Windows** and enable the WSL 2 backend.
 Docker packages run in WSL 2 will only work if Docker Desktop is correctly set up and running in Windows.  [Learn more](https://docs.docker.com/desktop/windows/wsl/).

> <i class="fab fa-linux text-white"></i> **Install Docker + nvidia-docker directly in WSL 2** following the current instructions on the RAPIDS site. Note that WSL 2 does not have systemd so Docker will not start automatically. You have to manually run `sudo service docker start` after each reboot.  [[Learn more](https://stackoverflow.com/a/65814529)].

## <i class="fa-solid fa-screwdriver-wrench"></i> Troubleshooting

> When installing with conda, if an `http 000 connection error` occurs when accessing the repository data, run `wsl --shutdown` and then restart the WSL instance. [More information](https://stackoverflow.com/questions/67923183/miniconda-on-wsl2-ubuntu-20-04-fails-with-condahttperror-http-000-connection)

## <i class="far fa-comments text-white"></i> Connect
> Join our community conversations about RAPIDS on WSL 2 using **[Twitter](https://twitter.com/rapidsai){: target="_blank"}**, **[Slack]({{ site.slack_invite }}){: target="_blank"}**, or ask a question on **[StackOverflow](https://stackoverflow.com/tags/rapids){: target="_blank"}**.

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
<div id="install"></div>
{% capture yd_header %}
# Installation Instructions
{: .section-title-full}

{% endcapture %}

{% capture yd_left %}
## <i class="fas fa-laptop-code"></i> Conda <br>(Preferred Method)

1. Install WSL 2 and the Ubuntu 20.04 package [using Microsoft's instructions](https://docs.microsoft.com/en-us/windows/wsl/install){: target="_blank"}.
2. Install the [latest NVIDIA Drivers](https://www.nvidia.com/download/index.aspx){: target="_blank"} on the Windows host.
3. Log in to the WSL 2 Linux instance.
4. Install Conda in the WSL 2 Linux Instance using [our Conda instructions](https://rapids.ai/start.html#environment){: target="_blank"}.
5. Install RAPIDS via Conda, [using the RAPIDS Release Selector tool](https://rapids.ai/start.html#get-rapids){: target="_blank"}.
6. Run this code to check that the RAPIDS installation is working:
	```
	import cudf
	print(cudf.Series([1, 2, 3]))
	```
7. Install additional GitHub repositories and enablements [from the Learn More section](https://rapids.ai/start.html#next-steps){: target="_blank"}.

{% endcapture %}
{% capture yd_mid %}
## <i class="fab fa-docker text-purple"></i> pip

1. Install WSL 2 and the Ubuntu 20.04 package [using Microsoft's instructions](https://docs.microsoft.com/en-us/windows/wsl/install){: target="_blank"}.
2. Install the [latest NVIDIA Drivers](https://www.nvidia.com/download/index.aspx){: target="_blank"} on the Windows host.
3. Log in to the WSL 2 Linux instance.
4. Follow **[this guide to install the CUDA Toolkit without drivers](https://docs.nvidia.com/cuda/wsl-user-guide/index.html#cuda-support-for-wsl2){: target="_blank"}** into the WSL 2 instance.
5. Install RAPIDS pip packages on the WSL 2 Linux Instance using the [pip instructions](https://rapids.ai/pip.html#install){: target="_blank"}.
6. Run this code to check that the RAPIDS installation is working:
	```
	import cudf
	print(cudf.Series([1, 2, 3]))
	```
7. Install additional GitHub repos, enablements, and 3rd party tools [from the Learn More section](https://rapids.ai/start.html#next-steps){: target="_blank"}.

{% endcapture %}
{% capture yd_right %}
## <i class="fab fa-docker text-purple"></i> Docker Desktop

1. Install WSL 2 and the Ubuntu 20.04 package [using Microsoft's instructions](https://docs.microsoft.com/en-us/windows/wsl/install){: target="_blank"}.
2. Install the [latest NVIDIA Drivers](https://www.nvidia.com/download/index.aspx){: target="_blank"} on the Windows host.
3. Install latest Docker Desktop for Windows [according to your applicable licensing terms](https://docs.docker.com/desktop/install/windows-install/){: target="_blank"}.
4. Log in to the WSL 2 Linux instance.
5. Generate and run the RAPIDS `docker pull` and `docker run` commands based on your desired configuration [using the RAPIDS Release Selector](https://rapids.ai/start.html#get-rapids){: target="_blank"}.
6. Inside the Docker instance, run this code to check that the RAPIDS installation is working:
	```
	import cudf
	print(cudf.Series([1, 2, 3]))
	```
7. Install additional GitHub repos, enablements, and 3rd party tools [from the Learn More section](https://rapids.ai/start.html#next-steps){: target="_blank"}.

{% endcapture %}
{% include slopecap.html
    background="background-white"
    position="top"
    slope="up"
%}
{% include section-single.html
    background="background-white"
    padding-top="2em" padding-bottom="0em"
    content-single=yd_header
%}
{% include section-thirds.html
    background="background-white"
    padding-top="0em" padding-bottom="10em"
    content-left-third=yd_left
    content-middle-third=yd_mid
    content-right-third=yd_right
%}
{% include cta-footer-help.html
   background="background-darkpurple"
%}
