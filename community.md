---
title: "RAPIDS Developer and Contributor Community | RAPIDS"
og_title: "RAPIDS Developer and Contributor Community"
og_description: "Learn how to become a RAPIDS adopter, contributor and more. Start contributing today!"
brand_name: ""
brand_tagline: "Learn how to become an adopter,<br/>a contributor, and more."
brand_button: "CONTRIBUTE"
brand_link: "https://github.com/rapidsai"
layout: default
---

{% capture com_left %}
# RAPIDS Community
{: .section-title-halfs}

RAPIDS is for everyone—users, adopters, and contributors. If you’re a data scientist, researcher, engineer, or developer using pandas, Dask, scikit-learn, or Spark on CPUs and looking for 50X end-to-end pipeline speedups at scale, look no further. Download RAPIDS and give us a run. The RAPIDS cuDF library is almost a drop-in, API-compatible, GPU-accelerated replacement for pandas and Dask (if you want to scale to multi-GPU and multi-node).
{% endcapture %}

{% capture com_right %}
## <i class="fas fa-code"></i> Open Source
{: .section-subtitle-top}
RAPIDS is also open sourced under the Apache 2.0 open-source license and is intended to be built upon and hardened in the community. While significant time and effort have been invested into making the platform usable and relevant, we need active contributors to help improve it and build its future.

## <i class="fab fa-github"></i> Become a RAPIDS Contributor
Contributors include anyone who helps improve the project—whether by reporting issues, adding documentation and examples, or contributing code. RAPIDS is built on open-source projects, fork our repositories from GitHub, start hacking, and open a pull request. Join us on Google Groups and let us know what you're working on.
{% endcapture %}

{% include section-halfs.html
    background="background-white" 
    padding-top="0" padding-bottom="1" 
    content-left-half=com_left 
    content-right-half=com_right
%} 

# Contributors
{: .section-title-full}
{% include contributing-logos.html 
    padding-top="0" padding-bottom="2" 
%}

{% include slopecap.html 
    background="background-darkpurple" 
    position="top" 
    slope="down"
%}
{% include cta-footer-help.html 
   background="background-darkpurple" 
%}
