---
title: "RAPIDS + Plotly Dash"
description: "Learn How to Use RAPIDS with Plotly Dash"
tagline: "Build Web Applications With Dash"
button_text: "Plotly Dash"
button_link: "https://dash.plotly.com/"
layout: default
---

![Placeholder]({{ site.baseurl }}{% link /assets/images/Plotly_Dash_logo.png %}){: .projects-logo}

# Put AI and ML <br> in the hands of business users
{: .section-title-full}

{% capture intro_content %}

**[Plotly’s Dash](https://dash.plotly.com/){: target="_blank"}** enables Data Science teams to focus on the data and models, while producing and sharing enterprise-ready analytic apps that sit on top of RAPIDS-accelerated Python dataframes. What would typically require a team of back-end developers, front-end developers, and IT can all be done by Data Science teams with Dash.
{: .subtitle}

{% endcapture %}

{% include section-single.html
    background="background-white" 
    padding-top="0em" padding-bottom="0em" 
    content-single=intro_content
%}


{% capture yd_header %}
# Why Use Dash
{: .section-title-full}

{% endcapture %}

{% capture yd_left %}
## <i class="fal fa-feather"></i> Productive & Light
Before Dash, it would take an entire team of engineers and designers to create interactive analytics apps. Dash apps require very little boilerplate to get started. A fully-functional analytics app can weigh in at just 40 lines of Python code.

{% endcapture %}

{% capture yd_mid %}
## <i class="fad fa-sliders-h"></i> Customizable
Every aesthetic element of a Dash app is customizable and rendered in the web so you can employ the full power of CSS.

{% endcapture %}

{% capture yd_right %}
## <i class="far fa-gamepad"></i> Direct Control
Dash links interactive UI controls and displays, like sliders, dropdown menus, and graphs, to your data analytics code, giving you hands-on input for your data views.

{% endcapture %}

{% capture rpd_header %}
# Using Dash with RAPIDS
{: .section-title-full}

![viz app]({{ site.baseurl }}{% link /assets/images/RAPIDS-Dash-App.png %}){: .full-image-center}

{% endcapture %}

{% capture rpd_left %}
## <i class="fal fa-boxes-alt"></i> Easy Integration
Read how straightforward it is to integrate RAPIDS libraries like cuDF with a Plotly Dash App on the **[Making Of Census Viz Blog Post](https://medium.com/rapids-ai/plotly-census-viz-dashboard-powered-by-rapids-1503b3506652){: target="_blank"}**.

{% endcapture %}

{% capture rpd_mid %}
## <i class="fal fa-analytics"></i> Example Apps

Explore the code for the **[2010 Plotly Dash + RAPIDS Census Visualization](https://github.com/rapidsai/plotly-dash-rapids-census-demo/tree/master){: target="_blank"}** and its **[Covid-19 Branch](https://github.com/rapidsai/plotly-dash-rapids-census-demo/tree/covid-19){: target="_blank"}** on GitHub. 

{% endcapture %}

{% capture rpd_right %}
## <i class="fal fa-handshake"></i> RAPIDS Partnership

Learn more about the partnership with RAPIDS and future plans on this **[Blog Post Announcement](https://medium.com/plotly/plotly-and-nvidia-partner-to-integrate-dash-and-rapids-8a8c53cd7daf){: target="_blank"}**.

{% endcapture %}

{% include section-single.html
    background="background-white" 
    padding-top="2em" padding-bottom="0em" 
    content-single=yd_header
%}
{% include section-thirds.html 
    background="background-white" 
    padding-top="0em" padding-bottom="1em" 
    content-left-third=yd_left
    content-middle-third=yd_mid
    content-right-third=yd_right
%}
{% include section-single.html
    background="background-white" 
    padding-top="0em" padding-bottom="0em" 
    content-single=rpd_header
%}
{% include section-thirds.html 
    background="background-white" 
    padding-top="0em" padding-bottom="10em" 
    content-left-third=rpd_left
    content-middle-third=rpd_mid
    content-right-third=rpd_right
%}


{% capture start_left %}
# Getting Started
{: .section-title-halfs}
Get started with Dash by checking out the Plotly example gallery and comprehensive documentation.

## <i class="fas fa-laptop-code"></i> Install Dash
Install Dash via pip or conda **[Find details here](https://dash.plotly.com/installation){: target="_blank"}**.

## <i class="far fa-binoculars"></i> Get an Overview
Read the Plotly **[1.0 launch article](https://medium.com/plotly/welcoming-dash-1-0-0-f3af4b84bae){: target="_blank"}** from 2019 or rewind back to 2017 for the **[essay that kicked everything off](https://medium.com/plotly/introducing-dash-5ecf7191b503){: target="_blank"}**.

## <i class="fal fa-browser"></i> Check out the Gallery
See what’s possible with Dash at **[the App Gallery](https://dash-gallery.plotly.host/Portal/){: target="_blank"}**.

{% endcapture %}

{% capture start_right %}
## <i class="far fa-book-open"></i> Read Our Tutorial
{: .section-subtitle-top-1}
The **[Dash tutorial](https://dash.plotly.com/){: target="_blank"}** walks you through how to create an app, from layout to callbacks.

## <i class="fad fa-comments"></i> Show and Tell
Members of the Dash community share what they’ve build in the **[Community Forum](https://community.plotly.com/tag/show-and-tell){: target="_blank"}**.


## <i class="fab fa-medium"></i> Articles
Read a comprehensive list of **[ articles and more on Medium](https://medium.com/plotly){: target="_blank"}**, or view some of the highlighted articles below: 

<i class="fas fa-caret-right"></i> **[Pattern-Matching Callbacks in Dash](https://medium.com/plotly/pattern-matching-callbacks-in-dash-9014eee99858){: target="_blank"}**

<i class="fas fa-caret-right"></i> **[Productionize Object Detection Models with Dash Enterprise](https://medium.com/plotly/productionizing-object-detection-models-with-dash-enterprise-dba1c9402c2f){: target="_blank"}**

<i class="fas fa-caret-right"></i> **[Develop NLP Visualizations for clear, immediate insights into text data and outputs](https://medium.com/plotly/nlp-visualisations-for-clear-immediate-insights-into-text-data-and-outputs-9ebfab168d5b){: target="_blank"}**

<i class="fas fa-caret-right"></i> **[Understanding Word Embedding Arithmetic: Why there’s no single answer to “King − Man + Woman = ?”](https://medium.com/plotly/understanding-word-embedding-arithmetic-why-theres-no-single-answer-to-king-man-woman-cd2760e2cb7f){: target="_blank"}**

{% endcapture %}
{% include slopecap.html 
    background="background-gray" 
    position="top" 
    slope="down" 
%}
{% include section-halfs.html 
    background="background-gray" 
    padding-top="5em" padding-bottom="10em" 
    content-left-half=start_left 
    content-right-half=start_right 
%} 


{% capture cl_single%}
# Component Libraries
Dash is comprised of several component libraries suited for a variety of use cases. See the overview below.
{: .subtitle}

{% endcapture %}
{% capture cl_left_top %}
## <i class="fad fa-terminal"></i> Dash HTML Components
Dash is a web application framework that provides pure Python abstraction around HTML, CSS, and JavaScript. Instead of writing HTML or using an HTML templating engine, you compose your layout using Python structures with the dash-html-components library. <br> **[Learn More <i class="fas fa-angle-double-right"></i>](https://dash.plotly.com/dash-html-components){: target="_blank"}**

{% endcapture %}

{% capture cl_left_mid %}
## <i class="fad fa-terminal"></i> Dash DataTable
Dash DataTable is an interactive table component designed for viewing, editing, and exploring large datasets. DataTable is rendered with standard, semantic HTML <table/> markup, which makes it accessible, responsive, and easy to style. <br> **[Learn More <i class="fas fa-angle-double-right"></i>](https://dash.plotly.com/datatable){: target="_blank"}**

{% endcapture %}

{% capture cl_left_bottom %}
## <i class="fad fa-terminal"></i> Dash DAQ
Dash DAQ comprises a robust set of controls that make it simpler to integrate data acquisition and controls into your Dash applications. <br> **[Learn More <i class="fas fa-angle-double-right"></i>](https://dash.plotly.com/dash-daq){: target="_blank"}**

{% endcapture %}

{% capture cl_right_top %}
## <i class="fad fa-terminal"></i> Dash Core Components
Dash ships with supercharged components for interactive user interfaces. A core set of components, written and maintained by the Dash team, is available in the dash-core-components library. <br> **[Learn More <i class="fas fa-angle-double-right"></i>](https://dash.plotly.com/dash-core-components){: target="_blank"}**

{% endcapture %}

{% capture cl_right_mid %}
## <i class="fad fa-terminal"></i> Dash Bio
Dash Bio is a suite of bioinformatics components that make it simpler to analyze and visualize bioinformatics data and interact with them in a Dash application. <br> **[Learn More <i class="fas fa-angle-double-right"></i>](https://dash.plotly.com/dash-bio){: target="_blank"}**

{% endcapture %}

{% capture cl_right_bottom %}
## <i class="fad fa-terminal"></i> Dash Cytoscape
Dash Cytoscape is a graph visualization component for creating easily customizable, high-performance, interactive, and web-based networks. <br> **[Learn More <i class="fas fa-angle-double-right"></i>](https://dash.plotly.com/cytoscape){: target="_blank"}**

{% endcapture %}

{% include slopecap.html 
    background="background-purple" 
    position="top" 
    slope="up" 
%}

{% include section-single.html
    background="background-purple" 
    padding-top="5em" padding-bottom="0em" 
    content-single=cl_single
%}
{% include section-halfs.html 
    background="background-purple" 
    padding-top="0em" padding-bottom="0em" 
    content-left-half=cl_left_top
    content-right-half=cl_right_top
%}
{% include section-halfs.html 
    background="background-purple" 
    padding-top="0em" padding-bottom="0em" 
    content-left-half=cl_left_mid
    content-right-half=cl_right_mid
%}
{% include section-halfs.html 
    background="background-purple" 
    padding-top="0em" padding-bottom="10em" 
    content-left-half=cl_left_bottom
    content-right-half=cl_right_bottom
%}

{% capture end_bottom %}
# Get Started with Plotly Dash
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
{% include cta-footer-plotly.html 
   background="background-darkpurple" 
%}


