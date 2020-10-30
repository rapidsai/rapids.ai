---
title: "RAPIDS Citations"
description: "RAPIDS Citations"
tagline: "RAPIDS Citations"
button_text: "LEARN MORE"
button_link: "https://rapids.ai/"
layout: default

---

{% capture cit_single %}
# Citation Guide
{: .section-title-halfs}

## <i class="fal fa-quote-left"></i> To Cite RAPIDS 
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


## <i class="fal fa-book"></i> Current Known Citations:

### <i class="fas fa-caret-right"></i> Bringing UMAP Closer to the Speed of Light <br> with GPU Acceleration
```tex
@misc{
      nolet2020bringing,
      title={Bringing UMAP Closer to the Speed of Light with GPU Acceleration}, 
      author={Corey J. Nolet, Victor Lafargue, Edward Raff, Thejaswi Nanditale, Tim Oates, John Zedlewski, and Joshua Patterson},
      year={2020},
      eprint={2008.00325},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```

### <i class="fas fa-caret-right"></i> Machine Learning in Python: <br> Main developments and technology trends in data science, machine learning, and artificial intelligence
```tex
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
```


{% endcapture %}

{% include section-single.html
    background="background-white" 
    padding-top="0em" padding-bottom="10em" 
    content-single=cit_single
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

