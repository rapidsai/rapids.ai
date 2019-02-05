---
layout: post
title: "Accelerating Cross Filtering with cuDF"
categories: [blog]
tags: ['data science','rapids','cudf','visualization','data visualization']
author: Allan Enemark
excerpt_separator: <!--more-->
brand_name: "BLOG"
brand_tagline: "Open GPU Data Science"
---

> ![Sample Pic](https://cdn-images-1.medium.com/max/1600/1*wJsInVArmvRiNsaSImSEPg.png)

RAPIDS is all about enabling data scientists with enterprise grade tools and GPU performance. Visualization being a key component in a data scientist’s toolbox, we are naturally working on ways to accelerate that experience.<!--more-->

I’m a huge advocate of data visualization. It’s one of the closest things we have to a universal language that can distill and communicate complex, supported ideas to a broad domain of audiences. And although the types of visualizations out there are as varied as the types of data, the ability to quickly explore concurrent views of multivariate data is universally useful. In short, we wanted cross filtering.

Inspired by the original javascript library, we wanted to improve it with GPU acceleration and multi-gigabyte data sizes and keeping a straightforward javascript API. Simple, right? Introducing cuXfilter ( ku-cross-filter ), a proof of concept utilization of the RAPIDS cuDF library.