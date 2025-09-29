# Frequently Asked Questions - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/faq.html

**爬取时间:** 2025-09-09 13:16:02.358997

**深度:** 1

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/faq.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/faq.html)
[ View this page ](https://pyod.readthedocs.io/en/latest/_sources/faq.rst.txt "View this page")
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Frequently Asked Questions[¶](https://pyod.readthedocs.io/en/latest/faq.html#frequently-asked-questions "Link to this heading")
* * *
## What is the Next?[¶](https://pyod.readthedocs.io/en/latest/faq.html#what-is-the-next "Link to this heading")
This is the central place to track important things to be fixed/added:
  * GPU support (it is noted that keras with TensorFlow backend will automatically run on GPU; auto_encoder_example.py takes around 96.95 seconds on a RTX 2060 GPU).
  * Installation efficiency improvement, such as using docker
  * Add contact channel with [Gitter](https://gitter.im)
  * Support additional languages, see [Manage Translations](https://docs.readthedocs.io/en/latest/guides/manage-translations.html)
  * Fix the bug that numba enabled function may be excluded from code coverage
  * Decide which Python interpreter should readthedocs use. 3.X invokes Python 3.7 which has no TF supported for now.


Feel free to open on issue report if needed. See [Issues](https://github.com/yzhao062/pyod/issues).
* * *
## How to Contribute[¶](https://pyod.readthedocs.io/en/latest/faq.html#how-to-contribute "Link to this heading")
You are welcome to contribute to this exciting project:
  * Please first check Issue lists for “help wanted” tag and comment the one you are interested. We will assign the issue to you.
  * Fork the master branch and add your improvement/modification/fix.
  * Create a pull request to **development branch** and follow the pull request template [PR template](https://github.com/yzhao062/pyod/blob/master/PULL_REQUEST_TEMPLATE.md)
  * Automatic tests will be triggered. Make sure all tests are passed. Please make sure all added modules are accompanied with proper test functions.


To make sure the code has the same style and standard, please refer to abod.py, hbos.py, or feature_bagging.py for example.
You are also welcome to share your ideas by opening an issue or dropping me an email at zhaoy@cmu.edu :)
## Inclusion Criteria[¶](https://pyod.readthedocs.io/en/latest/faq.html#inclusion-criteria "Link to this heading")
Similarly to [scikit-learn](https://scikit-learn.org/stable/faq.html#what-are-the-inclusion-criteria-for-new-algorithms), We mainly consider well-established algorithms for inclusion. A rule of thumb is at least two years since publication, 50+ citations, and usefulness.
However, we encourage the author(s) of newly proposed models to share and add your implementation into PyOD for boosting ML accessibility and reproducibility. This exception only applies if you could commit to the maintenance of your model for at least two year period.
[ Next About us ](https://pyod.readthedocs.io/en/latest/about.html) [ Previous Citations & Achievements ](https://pyod.readthedocs.io/en/latest/pubs.html)
Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
On this page 
  * [Frequently Asked Questions](https://pyod.readthedocs.io/en/latest/faq.html)
    * [What is the Next?](https://pyod.readthedocs.io/en/latest/faq.html#what-is-the-next)
    * [How to Contribute](https://pyod.readthedocs.io/en/latest/faq.html#how-to-contribute)
    * [Inclusion Criteria](https://pyod.readthedocs.io/en/latest/faq.html#inclusion-criteria)


