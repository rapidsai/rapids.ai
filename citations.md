---
title: "RAPIDS Citations"
description: "RAPIDS Citations"
tagline: "RAPIDS Citations"
button_text: "LEARN MORE"
button_link: "https://rapids.ai/"
layout: default

---

{% capture brand_left %}
# Citation Guide
{: .section-title-halfs}

## <i class="far fa-bookmark"></i> To Cite RAPIDS 
If you use RAPIDS in a publication, please use citations in the following format (BibTeX entry for LaTeX):
```tex
@Manual{,
  title = {RAPIDS: Collection of Libraries for End to End GPU Data Science},
  author = {RAPIDS Development Team},
  year = {2018},
  url = {https://rapids.ai},
}
```
{: .padding-bottom-3em }


{% endcapture %}

{% capture brand_right %}
## Current Citations

@article{
  raschka2020machine,
  title={Machine Learning in Python: Main developments and technology trends in data science, machine learning, and artificial intelligence},
  author={Raschka, Sebastian and Patterson, Joshua and Nolet, Corey},
  journal={Information},
  volume={11},
  number={4},
  pages={193},
  year={2020},
  publisher={Multidisciplinary Digital Publishing Institute}
}

{% endcapture %}


{% include section-halfs.html
    background="background-white" 
    padding-top="1em" padding-bottom="10em" 
    content-left-half=brand_left 
    content-right-half=brand_right
%} 

{% include slopecap.html 
    background="background-darkpurple" 
    position="top" 
    slope="up"
%}
{% include cta-footer.html 
name="Try Data Science on GPUs with RAPIDS" 
tagline=""
button="LEARN MORE"
link="https://rapids.ai/"
%}

