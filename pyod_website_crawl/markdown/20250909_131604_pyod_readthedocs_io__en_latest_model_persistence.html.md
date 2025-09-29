# Model Save & Load - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/model_persistence.html

**爬取时间:** 2025-09-09 13:16:04.836086

**深度:** 1

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/model_persistence.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/model_persistence.html)
[ View this page ](https://pyod.readthedocs.io/en/latest/_sources/model_persistence.rst.txt "View this page")
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Model Save & Load[¶](https://pyod.readthedocs.io/en/latest/model_persistence.html#model-save-load "Link to this heading")
PyOD takes a similar approach of sklearn regarding model persistence. See [model persistence](https://scikit-learn.org/stable/modules/model_persistence.html) for clarification.
In short, we recommend to use joblib or pickle for saving and loading PyOD models. See [“examples/save_load_model_example.py”](https://github.com/yzhao062/pyod/blob/master/examples/save_load_model_example.py) for an example. In short, it is simple as below:
```
fromjoblibimport dump, load

# save the model
dump(clf, 'clf.joblib')
# load the model
clf = load('clf.joblib')

```

It is known that there are challenges in saving neural network models. Check [#328](https://github.com/yzhao062/pyod/issues/328#issuecomment-917192704) and [#88](https://github.com/yzhao062/pyod/issues/88#issuecomment-615343139) for temporary workaround.
[ Next Fast Train with SUOD ](https://pyod.readthedocs.io/en/latest/fast_train.html) [ Previous Installation ](https://pyod.readthedocs.io/en/latest/install.html)
Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
