# Outlier Detection 101 - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/relevant_knowledge.html

**爬取时间:** 2025-09-09 13:16:05.387396

**深度:** 1

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/relevant_knowledge.html#furo-main-content)
Toggle site navigation sidebar
[pyod 2.0.5 documentation](https://pyod.readthedocs.io/en/latest/index.html)
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
[ pyod 2.0.5 documentation ](https://pyod.readthedocs.io/en/latest/index.html)
Getting Started
  * [Installation](https://pyod.readthedocs.io/en/latest/install.html)
  * [Model Save & Load](https://pyod.readthedocs.io/en/latest/model_persistence.html)
  * [Fast Train with SUOD](https://pyod.readthedocs.io/en/latest/fast_train.html)
  * [Examples](https://pyod.readthedocs.io/en/latest/example.html)
  * [Benchmarks](https://pyod.readthedocs.io/en/latest/benchmark.html)


Documentation
  * [API CheatSheet](https://pyod.readthedocs.io/en/latest/api_cc.html)
  * [API Reference](https://pyod.readthedocs.io/en/latest/pyod.html)
Toggle navigation of API Reference
    * [All Models](https://pyod.readthedocs.io/en/latest/pyod.models.html)
    * [Utility Functions](https://pyod.readthedocs.io/en/latest/pyod.utils.html)


Additional Information
  * [Known Issues & Warnings](https://pyod.readthedocs.io/en/latest/issues.html)
  * [Outlier Detection 101](https://pyod.readthedocs.io/en/latest/relevant_knowledge.html)
  * [Citations & Achievements](https://pyod.readthedocs.io/en/latest/pubs.html)
  * [Frequently Asked Questions](https://pyod.readthedocs.io/en/latest/faq.html)
  * [About us](https://pyod.readthedocs.io/en/latest/about.html)


[ Back to top ](https://pyod.readthedocs.io/en/latest/relevant_knowledge.html)
[ View this page ](https://pyod.readthedocs.io/en/latest/_sources/relevant_knowledge.rst.txt "View this page")
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Outlier Detection 101[¶](https://pyod.readthedocs.io/en/latest/relevant_knowledge.html#outlier-detection-101 "Link to this heading")
Outlier detection broadly refers to the task of identifying observations which may be considered anomalous given the distribution of a sample. Any observation belonging to the distribution is referred to as an inlier and any outlying point is referred to as an outlier.
In the context of machine learning, there are three common approaches for this task:
  1. 

Unsupervised Outlier Detection
    
     * Training data (unlabelled) contains both normal and anomalous observations.
     * The model identifies outliers during the fitting process.
     * This approach is taken when outliers are defined as points that exist in low-density regions in the data.
     * Any new observations that do not belong to high-density regions are considered outliers.
  2. 

Semi-supervised Novelty Detection
    
     * Training data consists only of observations describing normal behavior.
     * The model is fit on training data and then used to evaluate new observations.
     * This approach is taken when outliers are defined as points differing from the distribution of the training data.
     * Any new observations differing from the training data within a threshold, even if they form a high-density region, are considered outliers.
  3. 

Supervised Outlier Classification
    
     * The ground truth label (inlier vs outlier) for every observation is known.
     * The model is fit on imbalanced training data and then used to classify new observations.
     * This approach is taken when ground truth is available and it is assumed that outliers will follow the same distribution as in the training set.
     * Any new observations are classified using the model.


The algorithms found in _PyOD_ focus on the first two approaches which differ in terms of how the training data is defined and how the model’s outputs are interpreted. If interested in learning more, please refer to our [Anomaly Detection Resources](https://github.com/yzhao062/anomaly-detection-resources) page for relevant related books, papers, videos, and toolboxes.
[ Next Citations & Achievements ](https://pyod.readthedocs.io/en/latest/pubs.html) [ Previous Known Issues & Warnings ](https://pyod.readthedocs.io/en/latest/issues.html)
Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
