---
layout: post
title: "Make sense of the universe with Rapids.ai"
categories: [blog]
tags: machine-learning gpu nvidia kaggle astronomy
author: allan
excerpt_separator: <!--more-->
---

> ![Large Synoptic Survey Telescope (LSST)](https://cdn-images-1.medium.com/max/1600/1*oeustFcjTXUVPCXM6qe9Pw.png)

Classification of astronomical sources in the night sky is important for understanding the universe. It helps us understand the properties of what makes up celestial systems from our solar system to the most distant galaxy and everything in between.<!--more--> The **[Photometric LSST Astronomical Time-Series Classification Challenge (PLAsTiCC)](https://www.kaggle.com/c/PLAsTiCC-2018)** wanted to revolutionize the field by automatically classify 10–100x faster than previous methods and provided Kagglers a great dataset for solving this Kaggle problem using machine learning. I am honored to represent [RAPIDS.ai](https://rapids.ai) for this competition and ended up with **[8th place out of 1094](https://www.kaggle.com/c/PLAsTiCC-2018/leaderboard) teams**! My solution achieved an up to **140x speedup for ETL and 25x end-to-end speedup over the CPU solution**. Here is the story how we make sense of the universe in a RAPIDS way 🚀.

<script src="https://gist.github.com/daxiongshu/57d079b8233bcfa25787ca70649cd11a.js"></script>
> If you just dive into the code, here is the [full rapids demo notebook and source code link](https://github.com/daxiongshu/notebooks/tree/kaggle/kaggle)

### Background

For hundreds of years, astronomers have developed many ways to discern different types of stars, ranging from the naked human eyes to today’s method of [spectroscopy analysis](https://ed.ted.com/lessons/how-do-we-study-the-stars-yuan-sen-ting). Spectroscopy analysis uses the modern telescope to extract the exact fingerprint of the astrophysical sources by dispersing the beam of light into a spectrum and finding out what wavelength is missing. Unfortunately, this type of analysis takes so much time that it can’t keep up with the enormous **40 Terabytes data per night** data rate that the new [Large Synoptic Survey Telescope (LSST)](https://lsst-tvssc.github.io/) generates. This is where machine learning comes into play to learn the pattern from the light curves data directly. However, it is still very challenging to ingest such a big data in real time. We believe GPU is the most promising solution to this problem **as my end-to-end GPU demo takes only 40 seconds to process 20 gigabytes data!**

In this Kaggle challenge, a training data set of 7000 objects and a test data set of 3 million objects are provided. For each object [there are two types of information](https://www.kaggle.com/c/PLAsTiCC-2018/data):

1. time series of observations of the objects, or so called light curves,
2. meta features that do not vary over time.

> ![The light curve time series by LSST of object 615 with all six passbands.](https://cdn-images-1.medium.com/max/1600/1*35YAp_KSqDNrVfBU51xbMg.png)
> The light curve time series by LSST of object 615 with all six passbands.

The light curve time series is the most critical information for solving the puzzle. There are some common challenges with time series classification, like:

1. **the length of light curve for each object could be vary different.** In this data set, it ranges from 100 to 500 observations. Two methods are utilized to map the light curve to a vector of a fixed dimensionality: cudf groupby aggregation and a RNN encoder.
2. **the brightness magnitude (flux) can have huge variance.** Thus, logarithmic normalization is critical for neural network models.

### Solution Overview

> ![Solution Overview](https://cdn-images-1.medium.com/max/1600/1*tv0fuN-usAsQLJzTj1zSLQ.png)

An all-GPU solution is implemented with Rapids.ai libraries and tensorflow:

1. Extract features from both time series and meta data using [rapids cudf](https://github.com/rapidsai/cudf), especially the groupby aggregation functionality.
2. Train base classifiers of Xgboost and multi-layer perceptron (MLP) with features from Step 1.
3. Use predictions from Step 2 as features and train [stack models](http://www.machine-learning.martinsewell.com/ensembles/stacking/Wolpert1992.pdf).
4. Use the predictions of **test data** from step 3 as pseudo labels to train a bidirectional recurrent neural network (RNN) and extract the bottleneck features with attention, which are weighted sum of all hidden states of RNN cells.
5. Use the bottleneck features of step 4 along with features from step 1 to train Xgboost and MLP again.
6. Use predictions from step 5 as features and train [stack models](http://www.machine-learning.martinsewell.com/ensembles/stacking/Wolpert1992.pdf) to get final predictions.
7. Repeat steps 1 to 6 until the hold out validation accuracy converges.

### Feature engineering

RAPIDS’ cudf is crucial to efficient feature engineering and feature selection thanks to its amazing performance using GPUs. The main features built are statistical metrics (mean, max, etc) that summarize each object’s light curve characteristics with the [groupby-aggregation](https://pandas.pydata.org/pandas-docs/stable/groupby.html) operation. The input data is a dataframe with light curves of all the objects. The groupby-aggregation operation splits the dataframe based on the object ID, processes each object’s light curve independently and combines the summarized results back to one dataframe, which is ready for the classifier.

The GPU based cudf achieves amazing speedup compared to the CPU based pandas. In general, it is at least **10x faster** for reading data and groupby aggregation. For the best case, **groupby and aggregation with *skew*** function, cudf achieves **120x~140x speedup!!** Although the *skew* function is not supported directly by cudf, I implemented a workaround with cudf’s *[apply_grouped](https://github.com/rapidsai/cudf/blob/fcccb51a2d5e0764a4461ae46f3bc0fd885dee43/python/cudf/tests/test_groupby.py#L206)* primitives and *numba* to write GPU kernel functions.

<script src="https://gist.github.com/daxiongshu/fd59a85590357b98f223532c18fab280.js"></script>

The *apply_grouped* method launches one kernel, *compute_skew* in this case, for each group in parallel. In other words, all we need to implement is *[compute_skew](https://github.com/daxiongshu/notebooks/blob/kaggle/kaggle/cudf_workaround.py#L66)* and everything else is taken care of by cudf. This is a great example that showcases both the performance and the flexibility of cudf.

<script src="https://gist.github.com/daxiongshu/310957de43ef0b16c8b532c0c02cf814.js"></script>

Such speedup brought by RAPIDS is the key to ingest the enormous data generated by LSST in real time. It is also extremely useful to improve data scientists’ efficiency, which allows fast iterative experimenting of ETL, feature selection, and practically every step of the machine learning pipeline. Eventually, these features are fed to a GPU version of the Xgboost classifier and it can already achieve 80% accuracy of the final complex ensemble. The details of features can be found in the [demo notebook](https://github.com/daxiongshu/notebooks/blob/kaggle/kaggle/rapids_lsst_demo.ipynb) at the beginning of the blog.

### Stacking and self-training.

With the solid feature engineering, I created several good base models that can place in top 10% of the competition. To break into top 1%, some of the most effective kaggle tricks were employed: stacking and semi-supervised self-training.

Stacking is a non-linear ensemble technique where new features are generated from the base models’ predictions in a cross validation manner.

> ![Image from Kazanova’s stacknet blog](https://cdn-images-1.medium.com/max/1600/1*HTCRhhqGOWhZ0KFYdLJqiQ.jpeg)
> Image from [Kazanova’s stacknet blog](http://blog.kaggle.com/2017/06/15/stacking-made-easy-an-introduction-to-stacknet-by-competitions-grandmaster-marios-michailidis-kazanova/)

[Self-training](https://en.wikipedia.org/wiki/Semi-supervised_learning) is a semi-supervised technique where the predictions are used as pseudo labels. Different from stacking, self-training can train the unlabelled test data with pseudo labels, which essentially augment the training data. In this competition, the size of test data is 500x of training data so self-training can be very effective. Specifically, I built a bidirectional RNN to learn from the raw light curve time series directly with self-training so that it can complement the manually crafted features by cudf. All the test data are used for training the RNN and all the original training data are just used for validation and early stopping. In this way, we enforce the RNN to learn a middle ground that can fit the pseudo labels of test data and true labels of training data simultaneously. The loop of feature engineering, stacking and self training is repeated until the holdout validation accuracy converged. More details about stacking and self-training can be found at my [kaggle post](https://www.kaggle.com/c/PLAsTiCC-2018/discussion/75012).

### Further improvement

Rapids is so fast and powerful that sometimes I forgot it is only three months old. What I don’t forget is its great potential and we can definitely improve rapids with the valuable lessons learned from the competition.

1. Better GPU memory management. The main challenge of this competition is to handle the big data size. With a single GPU, out-of-memory error (OOM) is very likely to occur. To prevent such OOM errors, several tricks are utilized such as manually moving data back and forth between host and device, deleting columns immediately after operations and so on. Despite being effective and relatively low-overhead, such tricks still burden users with hardware details. Instead, we are working on **[dask-cudf](https://github.com/rapidsai/dask-cudf)** integration where large dataframes can be transparently ingested and manipulated in an out-of-core chunked manner.
2. More functionalities. Kaggle competitions are all about distilling the last bit of useful information from data to push the accuracy. Hence kagglers crave every possible functions to transform the data from a different angle. For example, groupby-aggregation is the most common ETL trick which summarizes a group’s behavior by calculating a certain statistical metric. Currently some aggregation functions are not supported yet by rapids such as *median*. Workarounds for these functions can be implemented with cudf’s *apply_grouped* primitives and *numba* but there are definitely room for improvement.
3. Consistency, readability, and everything else. Sometimes so much time can be saved from digging in the documents if the functions have consistent patterns and the error messages are straightforward. For example, most of the cudf’s functions return a dataframe or data series except for *drop_column* and *reset_index*, which are in place by default. We can either make them consistent or help users realize the difference with better naming of the functions or better error message.

### Conclusion

This competition is a fantastic learning process for me. Without any astronomical background, I achieved amazing results through systematic iterative trial and error. And it is not possible without the lightspeed [rapids.ai](https://rapids.ai) library. This reminds me why I love machine learning in the first place: with enough data, the *right library*, and massive computing power, the model can be (almost) as good as any domain experts 😃.