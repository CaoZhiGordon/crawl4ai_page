# Installation - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/install.html

**爬取时间:** 2025-09-09 13:16:03.939381

**深度:** 1

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/install.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/install.html)
[ View this page ](https://pyod.readthedocs.io/en/latest/_sources/install.rst.txt "View this page")
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Installation[¶](https://pyod.readthedocs.io/en/latest/install.html#installation "Link to this heading")
PyOD is designed for easy installation using either **pip** or **conda**. We recommend using the latest version of PyOD due to frequent updates and enhancements:
```
# normal install
pip# or update if needed

```

Alternatively, you can clone and run the setup.py file:
```
cd
```

**Required Dependencies** :
  * Python 3.8 or higher
  * joblib
  * matplotlib
  * numpy>=1.19
  * numba>=0.51
  * scipy>=1.5.1
  * scikit_learn>=0.22.0


**Optional Dependencies (see details below)** :
  * combo (optional, required for models/combination.py and FeatureBagging)
  * pytorch (optional, required for deep learning models)
  * suod (optional, required for running SUOD model)
  * xgboost (optional, required for XGBOD)
  * pythresh (optional, required for thresholding)


Warning
PyOD includes several neural network-based models, such as AutoEncoders, implemented in PyTorch. These deep learning libraries are not automatically installed by PyOD to avoid conflicts with existing installations. If you plan to use neural-net based models, please ensure these libraries are installed. See the [neural-net FAQ](https://github.com/yzhao062/pyod/wiki/Setting-up-Keras-and-Tensorflow-for-Neural-net-Based-models) for guidance. Additionally, xgboost is not installed by default but is required for models like XGBOD.
[ Next Model Save & Load ](https://pyod.readthedocs.io/en/latest/model_persistence.html) [ Previous Home ](https://pyod.readthedocs.io/en/latest/index.html)
Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
