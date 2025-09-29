# pyod.models.combination - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/_modules/pyod/models/combination.html

**爬取时间:** 2025-09-09 13:16:31.933372

**深度:** 2

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/combination.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/combination.html)
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Source code for pyod.models.combination
```
# -*- coding: utf-8 -*-
"""A collection of model combination functionalities.
"""
# Author: Yue Zhao <yzhao062@gmail.com>
# License: BSD 2 clause


try:
    importcombo
except ImportError:
    print('please install combo first for combination by `pip install combo`')

fromcombo.models.score_combimport aom as combo_aom
fromcombo.models.score_combimport average as combo_average
fromcombo.models.score_combimport majority_vote as combo_majority_vote
fromcombo.models.score_combimport maximization as combo_maximization
fromcombo.models.score_combimport median as combo_median
fromcombo.models.score_combimport moa as combo_moa




[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.combination.aom)
defaom(scores, n_buckets=5, method='static', bootstrap_estimators=False,
        random_state=None):
"""Average of Maximum - An ensemble method for combining multiple
    estimators. See :cite:`aggarwal2015theoretical` for details.

    First dividing estimators into subgroups, take the maximum score as the
    subgroup score. Finally, take the average of all subgroup outlier scores.

    Parameters
    ----------
    scores : numpy array of shape (n_samples, n_estimators)
        The score matrix outputted from various estimators

    n_buckets : int, optional (default=5)
        The number of subgroups to build

    method : str, optional (default='static')
        {'static', 'dynamic'}, if 'dynamic', build subgroups
        randomly with dynamic bucket size.

    bootstrap_estimators : bool, optional (default=False)
        Whether estimators are drawn with replacement.

    random_state : int, RandomState instance or None, optional (default=None)
        If int, random_state is the seed used by the
        random number generator; If RandomState instance, random_state is
        the random number generator; If None, the random number generator
        is the RandomState instance used by `np.random`.

    Returns
    -------
    combined_scores : Numpy array of shape (n_samples,)
        The combined outlier scores.

    """

    return combo_aom(scores, n_buckets, method, bootstrap_estimators,
                     random_state)







[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.combination.moa)
defmoa(scores, n_buckets=5, method='static', bootstrap_estimators=False,
        random_state=None):
"""Maximization of Average - An ensemble method for combining multiple
    estimators. See :cite:`aggarwal2015theoretical` for details.

    First dividing estimators into subgroups, take the average score as the
    subgroup score. Finally, take the maximization of all subgroup outlier
    scores.

    Parameters
    ----------
    scores : numpy array of shape (n_samples, n_estimators)
        The score matrix outputted from various estimators

    n_buckets : int, optional (default=5)
        The number of subgroups to build

    method : str, optional (default='static')
        {'static', 'dynamic'}, if 'dynamic', build subgroups
        randomly with dynamic bucket size.

    bootstrap_estimators : bool, optional (default=False)
        Whether estimators are drawn with replacement.

    random_state : int, RandomState instance or None, optional (default=None)
        If int, random_state is the seed used by the
        random number generator; If RandomState instance, random_state is
        the random number generator; If None, the random number generator
        is the RandomState instance used by `np.random`.

    Returns
    -------
    combined_scores : Numpy array of shape (n_samples,)
        The combined outlier scores.

    """
    return combo_moa(scores, n_buckets, method, bootstrap_estimators,
                     random_state)







[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.combination.average)
defaverage(scores, estimator_weights=None):
"""Combination method to merge the outlier scores from multiple estimators
    by taking the average.

    Parameters
    ----------
    scores : numpy array of shape (n_samples, n_estimators)
        Score matrix from multiple estimators on the same samples.

    estimator_weights : list of shape (1, n_estimators)
        If specified, using weighted average

    Returns
    -------
    combined_scores : numpy array of shape (n_samples, )
        The combined outlier scores.

    """
    return combo_average(scores, estimator_weights)







[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.combination.maximization)
defmaximization(scores):
"""Combination method to merge the outlier scores from multiple estimators
    by taking the maximum.

    Parameters
    ----------
    scores : numpy array of shape (n_samples, n_estimators)
        Score matrix from multiple estimators on the same samples.

    Returns
    -------
    combined_scores : numpy array of shape (n_samples, )
        The combined outlier scores.

    """
    return combo_maximization(scores)







[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.combination.majority_vote)
defmajority_vote(scores, weights=None):
"""Combination method to merge the scores from multiple estimators
    by majority vote.

    Parameters
    ----------
    scores : numpy array of shape (n_samples, n_estimators)
        Score matrix from multiple estimators on the same samples.


    weights : numpy array of shape (1, n_estimators)
        If specified, using weighted majority weight.

    Returns
    -------
    combined_scores : numpy array of shape (n_samples, )
        The combined scores.

    """
    return combo_majority_vote(scores, n_classes=2, weights=weights)







[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.combination.median)
defmedian(scores):
"""Combination method to merge the scores from multiple estimators
    by taking the median.

    Parameters
    ----------
    scores : numpy array of shape (n_samples, n_estimators)
        Score matrix from multiple estimators on the same samples.

    Returns
    -------
    combined_scores : numpy array of shape (n_samples, )
        The combined scores.

    """
    return combo_median(scores)




```

Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
