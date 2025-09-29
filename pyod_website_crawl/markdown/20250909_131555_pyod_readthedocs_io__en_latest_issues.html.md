# Known Issues & Warnings - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/issues.html

**爬取时间:** 2025-09-09 13:15:55.572869

**深度:** 1

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/issues.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/issues.html)
[ View this page ](https://pyod.readthedocs.io/en/latest/_sources/issues.rst.txt "View this page")
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Known Issues & Warnings[¶](https://pyod.readthedocs.io/en/latest/issues.html#known-issues-warnings "Link to this heading")
This is the central place to track known issues.
## Installation[¶](https://pyod.readthedocs.io/en/latest/issues.html#installation "Link to this heading")
There are some known dependency issues/notes. Refer [installation](https://pyod.readthedocs.io/en/latest/install.html) for more information.
## Neural Networks[¶](https://pyod.readthedocs.io/en/latest/issues.html#neural-networks "Link to this heading")
SO_GAAL and MO_GAAL may only work under Python 3.5+.
## Differences between PyOD and scikit-learn[¶](https://pyod.readthedocs.io/en/latest/issues.html#differences-between-pyod-and-scikit-learn "Link to this heading")
Although PyOD is built on top of scikit-learn and inspired by its API design, some differences should be noted:
  * All models in PyOD follow the tradition that the outlying objects come with higher scores while the normal objects have lower scores. scikit-learn has an inverted design–lower scores stand for outlying objects.
  * PyOD uses “0” to represent inliers and “1” to represent outliers. Differently, scikit-learn returns “-1” for anomalies/outliers and “1” for inliers.
  * Although Isolation Forests, One-class SVM, and Local Outlier Factor are implemented in both PyOD and scikit-learn, users are not advised to mix the use of them, e.g., calling one model from PyOD and another model from scikit-learn. It is recommended to only use one library for consistency (for three models, the PyOD implementation is indeed a set of wrapper functions of scikit-learn).
  * PyOD models may not work with scikit-learn’s check_estimator function. Similarly, scikit-learn models would not work with PyOD’s check_estimator function.


[ Next Outlier Detection 101 ](https://pyod.readthedocs.io/en/latest/relevant_knowledge.html) [ Previous Utility Functions ](https://pyod.readthedocs.io/en/latest/pyod.utils.html)
Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
On this page 
  * [Known Issues & Warnings](https://pyod.readthedocs.io/en/latest/issues.html)
    * [Installation](https://pyod.readthedocs.io/en/latest/issues.html#installation)
    * [Neural Networks](https://pyod.readthedocs.io/en/latest/issues.html#neural-networks)
    * [Differences between PyOD and scikit-learn](https://pyod.readthedocs.io/en/latest/issues.html#differences-between-pyod-and-scikit-learn)


