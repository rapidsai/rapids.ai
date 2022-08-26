---
title: "RAPIDS + WSL2"
description: "Learn How to Use RAPIDS with WSL2 on Windows"
tagline: "Power of RAPIDS, now on Windows"
button_text: "Install Now"
button_link: "#install"
layout: default
---

![RAPIDS WSL2]({{ site.baseurl }}{% link /assets/images/csp+hpo.png %}){: .projects-logo}


# Use RAPIDS <br> on Windows
{: .section-title-full}

{% capture intro_content %}

Windows users can now tap into GPU accelerated data science on their local machines using RAPIDS on Windows Subsystem for Linux2 (WSL2)!  WSL2 is a Windows 11 feature that enables users to run native Linux command-line tools directly on Windows. Using this feature does not require a dual boot environment, taking away complexity and hopefully saving you time. Your computer will need an NVIDIA GPU with [Compute capability](https://developer.nvidia.com/cuda-gpus){: target="_blank"} 7.0 or higher. 
{: .subtitle}

{% endcapture %}

{% include section-single.html
    background="background-white" 
    padding-top="3em" padding-bottom="5em" 
    content-single=intro_content
%}

<div id="prereqs"></div>
{% capture start_single %}
# Before You Install
{: .section-title-full .text-white}
{% endcapture %}

{% capture start_left %}
## Starting Prerequisites

> <i class="fas fa-desktop text-white"></i> **OS:** Windows 11.  Some Windows 10 versions (2004+) may work, but YMMV

> <i class="fas fa-info-circle text-white"></i> **WSL Version:** WSL2.  This will not work if you use WSL1

> <i class="fas fa-microchip text-white"></i> **GPU:** Only GPUs with [Compute capability](https://developer.nvidia.com/cuda-gpus){: target="_blank"} 7.0 or higher are supported on RAPIDS in WSL2.
8GB or more of RAM

> <i class="fas fa-download text-white"></i> **WSL2 Instance:** Ubuntu instance for WSL2.  Others may work, but only Ubuntu is officially supported.

## <i class="fad fa-terminal"></i> Known Limitations

> <i class="fas fa-info-circle text-white"></i> While you may have success with MultiGPU processing using TCP, on a single node, neither its usage nor advanced MultiGPU communications (ucx, nvlink, RAFT), is currently supported. YMMV

> <i class="fas fa-info-circle text-white"></i> GPU Direct Storage is not currently supported.

> <i class="fas fa-info-circle text-white"></i> At least 8 GB of memory and a relatively fast CPU are strongly recommended https://docs.microsoft.com/en-us/windows/wsl/install

{% endcapture %}

{% capture start_right %}
## <i class="fab fa-docker"></i> Differences between Docker Install Methods
> <i class="fab fa-windows text-white"></i> **Install Docker Desktop in Windows** and enable the WSL2 backend, this will enable Docker in WSL2 and supports GPUs but only works if Docker Desktop is running. [[Learn more](https://www.docker.com/blog/wsl-2-gpu-support-for-docker-desktop-on-nvidia-gpus/)].

> <i class="fab fa-linux text-white"></i> **Install Docker + nvidia-docker directly in WSL2** following the current instructions on the RAPIDS site. The big caveat here is that WSL2 does not have systemd so Docker will not start automatically even if you follow all the post-install steps. You have to manually run sudo service docker start after each reboot or do this.  [[Learn more](https://stackoverflow.com/a/65814529)].

## <i class="fa-solid fa-screwdriver-wrench"></i> Troubleshooting

> When conda solving, if you get an `http 000 connection error` when accessing the repository data and nothing installs, run `wsl --shutdown` and then restart the WSL Linux instance. [[Source](https://stackoverflow.com/questions/67923183/miniconda-on-wsl2-ubuntu-20-04-fails-with-condahttperror-http-000-connection)]

## <i class="far fa-comments text-white"></i> Connect 
> Join our community conversations about RAPIDS on WSL2 using **[Twitter](https://twitter.com/rapidsai){: target="_blank"}**, **[Slack]({{ site.slack_invite }}){: target="_blank"}**, or ask question on **[Stack Overflow](https://stackoverflow.com/tags/rapids){: target="_blank"}**.

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
## <i class="fas fa-laptop-code"></i> Conda <br>(Preffered Method)

1. Install WSL2 [using Microsoft's instructions](https://docs.microsoft.com/en-us/windows/wsl/install){: target="_blank"}.
2. Install the [latest NVIDIA Drivers](https://www.nvidia.com/download/index.aspx){: target="_blank"}.
3. Install and log into your WSL2 Linux instance.
4. Install Conda on your WSL2 Linux Instance using [our Conda instructions](https://rapids.ai/start.html#environment){: target="_blank"}.
5. Install RAPIDS via Conda, as well as some third party RAPIDS ecosystem tools, [using the RAPIDS Release Selector tool](https://rapids.ai/start.html#get-rapids){: target="_blank"}. (third party libraries in WSL2 is outside the scope of RAPIDS support, but it’s good to report results to let the community know).
6. Install additional git hub repos and enablements [from the Learn More section](https://rapids.ai/start.html#next-steps){: target="_blank"}.
7. Run this code to check that your RAPIDS installation is working:
	```
	import cudf
	print(cudf.Series([1, 2, 3]))
	```
8. Enjoy running RAPIDS!

{% endcapture %}
{% capture yd_mid %}
## <i class="fab fa-docker text-purple"></i> Docker Desktop <br>(Docker Method #1)

1. Install WSL2 [using Microsoft's instructions](https://docs.microsoft.com/en-us/windows/wsl/install){: target="_blank"}.
2. Install the [latest NVIDIA Drivers](https://www.nvidia.com/download/index.aspx){: target="_blank"}.
3. Install latest Docker Desktop for Windows [according to your applicable licensing terms](https://docs.docker.com/desktop/install/windows-install/){: target="_blank"}.
4. Install and log into your WSL2 Linux instance.
5. Generate and run the RAPIDS `docker pull` and `docker run` commands based on your desired configuration [using the RAPIDS Release Selector](https://rapids.ai/start.html#get-rapids){: target="_blank"}. 
6. Inside your docker instance, run this code to check that your RAPIDS installation is working:
	```
	import cudf
	print(cudf.Series([1, 2, 3]))
	```
7. Install additional Github repos, enablements, and 3rd party tools [from the Learn More section](https://rapids.ai/start.html#next-steps){: target="_blank"}.
8. Enjoy running RAPIDS!

{% endcapture %}
{% capture yd_right %}
## <i class="fab fa-docker text-purple"></i> Docker on WSL2 <br>(Docker Method #2)
1. Install WSL2 [using Microsoft's instructions](https://docs.microsoft.com/en-us/windows/wsl/install){: target="_blank"}.
2. Install the [latest NVIDIA Drivers](https://www.nvidia.com/download/index.aspx){: target="_blank"}.
3. Install and log into your WSL2 Linux instance.
4. Install the Docker Environment on your WSL2 Linux instance [using the Docker instructions](https://rapids.ai/start.html#environment){: target="_blank"}.  You may need  to add `sudo` before any Docker command.
5. Generate and run the RAPIDS `docker pull` and `docker run` commands based on your desired configuration [using the RAPIDS Release Selector](https://rapids.ai/start.html#get-rapids){: target="_blank"}. You may need  to add `sudo` before any Docker command.
6. Inside your docker instance, run this code to check that your RAPIDS installation is working:
	```
	import cudf
	print(cudf.Series([1, 2, 3]))
	```
7. Install additional Github repos, enablements, and 3rd party tools [from the Learn More section](https://rapids.ai/start.html#next-steps){: target="_blank"}.
8. Enjoy running RAPIDS!
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
