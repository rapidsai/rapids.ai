---
title: "RAPIDS Branding and Guides"
description: "RAPIDS logos, style guides, and brand guidelines"
tagline: "Branding and Guides"
button_text: "LEARN MORE"
button_link: "https://rapids.ai/about.html"
layout: default

---

{% capture brand_left %}
# Guides and Themes
{: .section-title-halfs}
This page contains useful guides, assets, **[fonts](https://fonts.google.com/specimen/Open+Sans){: target="_blank"}**, and themes to help you style RAPIDS communications consistently and clearly. 

## <i class="far fa-bookmark"></i> RAPIDS Citation Guide
We welcome **[citations](citations.html)**! If you use RAPIDS in a publication, please use citations in the following format (BibTeX entry for LaTeX):
```tex
@Manual{,
  title = {RAPIDS: Collection of Libraries for End to End GPU Data Science},
  author = {RAPIDS Development Team},
  year = {2018},
  url = {https://rapids.ai},
}
```
{: .padding-bottom-3em }


## <i class="fas fa-book"></i> RAPIDS Style Guide
A concise visual guide on the colors, fonts, and layouts to best apply the RAPIDS style. 
{: .no-tb-margins }
**[Get style guide PDF <i class="fas fa-angle-double-right"></i>]({{ site.baseurl }}{% link /assets/files/rapids-style-guide-2019-r8-web.pdf %}){: target="_blank"}** 
{: .padding-bottom-3em }

## <i class="fab fa-css3"></i> RAPIDS Jupyter Notebook Theme
An easy to use RAPIDS theme for Jupyter Notebooks.
{: .no-tb-margins }
**[Get theme 'custom.css' <i class="fas fa-angle-double-right"></i>]({{ site.baseurl }}{% link /assets/files/custom.css %}){: target="_blank"}**

<img class="half-image-center" src="{{ site.baseurl }}{% link /assets/images/RAPIDStheme.png %}" alt="RAPIDS notebook theme">


### **NOTE** To apply theme globally, place .css in:
<i class="far fa-folder-open"></i> **`~/.jupyter/custom/`**
{: .no-tb-margins }

### **NOTE** To apply theme in a single notebook, in the first cell run:
```python
from IPython.core.display import HTML
import urllib.request
response = urllib.request.urlopen('https://rapids.ai/assets/files/custom.css')
CSSstyle = '<style>' + response.read().decode("utf-8") + ' </style>'
HTML(CSSstyle)
```
<!-- from https://gist.github.com/rlabbe/0a88151bbf3b4198151f -->

{% endcapture %}

{% capture brand_right %}
## <i class="fas fa-vector-square"></i> SVG Logos
{: .section-subtitle-top-1}
High resolution SVG files, right click to save.
<img class="half-image" src="{{ site.baseurl }}{% link /assets/images/RAPIDS-logo-purple.svg %}" alt="RAPIDS logo svg">
<img class="half-image" src="{{ site.baseurl }}{% link /assets/images/RAPIDS-logo-white.svg %}" alt="RAPIDS logo svg">
{: .padding-bottom-3em }


## <i class="far fa-file-image"></i> PNG Logos
High resolution PNG files, right click to save.
<img class="half-image" src="{{ site.baseurl }}{% link /assets/images/RAPIDS-logo-purple.png %}" alt="RAPIDS logo png">
<img class="half-image" src="{{ site.baseurl }}{% link /assets/images/RAPIDS-logo-white.png %}" alt="RAPIDS logo png">
{: .padding-bottom-3em }


## <i class="far fa-image"></i> Background
High resolution background SVG file, right click to save.
<img class="full-image" src="{{ site.baseurl }}{% link /assets/images/header-bg.svg %}" alt="RAPIDS motif">
{: .padding-bottom-3em }


## <i class="fas fa-palette"></i> Color Values
RAPIDS colors for easy reference.
{: .no-tb-margins }
### **Primary**
<div class="full-image" style="background-color:#7400ff; color: white; padding: 1em">#7400ff</div>
<div class="full-image" style="background-color:#d216d2; color: white; padding: 1em">#d216d2</div>
<div class="full-image" style="background-color:#ffb500; color: white; padding: 1em">#ffb500</div>
<div class="full-image" style="background-color:#36c9dd; color: white; padding: 1em">#36c9dd</div>

### **Secondary**
<div class="full-image" style="background-color:#8735fb; color: white; padding: 1em">#8735fb</div>
<div class="full-image" style="background-color:#984dfb; color: white; padding: 1em">#984dfb</div>
<div class="full-image" style="background-color:#a788e4; color: white; padding: 1em">#a788e4</div>
<div class="full-image" style="background-color:#bababc; color: white; padding: 1em">#babab</div>
<div class="full-image" style="background-color:#666666; color: white; padding: 1em">#666666</div>

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
link="https://medium.com/rapids-ai"
%}

