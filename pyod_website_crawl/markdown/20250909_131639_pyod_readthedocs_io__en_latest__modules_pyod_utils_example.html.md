# pyod.utils.example - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/example.html

**爬取时间:** 2025-09-09 13:16:39.022731

**深度:** 2

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/example.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/example.html)
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Source code for pyod.utils.example
```
# -*- coding: utf-8 -*-
"""Utility functions for running examples
"""
# Author: Yue Zhao <zhaoy@cmu.edu>
# License: BSD 2 clause


from__future__import division
from__future__import print_function

importmatplotlib.pyplotasplt

from.dataimport check_consistent_shape
from.dataimport get_outliers_inliers




[docs][](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.example.visualize)
defvisualize(clf_name, X_train, y_train, X_test, y_test, y_train_pred,
              y_test_pred, show_figure=True,
              save_figure=False):  # pragma: no cover
"""Utility function for visualizing the results in examples.
    Internal use only.

    Parameters
    ----------
    clf_name : str
        The name of the detector.

    X_train : numpy array of shape (n_samples, n_features)
        The training samples.

    y_train : list or array of shape (n_samples,)
        The ground truth of training samples.

    X_test : numpy array of shape (n_samples, n_features)
        The test samples.

    y_test : list or array of shape (n_samples,)
        The ground truth of test samples.

    y_train_pred : numpy array of shape (n_samples, n_features)
        The predicted binary labels of the training samples.

    y_test_pred : numpy array of shape (n_samples, n_features)
        The predicted binary labels of the test samples.

    show_figure : bool, optional (default=True)
        If set to True, show the figure.

    save_figure : bool, optional (default=False)
        If set to True, save the figure to the local.

    """

    def_add_sub_plot(X_inliers, X_outliers, sub_plot_title,
                      inlier_color='blue', outlier_color='orange'):
"""Internal method to add subplot of inliers and outliers.

        Parameters
        ----------
        X_inliers : numpy array of shape (n_samples, n_features)
            Outliers.

        X_outliers : numpy array of shape (n_samples, n_features)
            Inliers.

        sub_plot_title : str
            Subplot title.

        inlier_color : str, optional (default='blue')
            The color of inliers.

        outlier_color : str, optional (default='orange')
            The color of outliers.

        """
        plt.axis("equal")
        plt.scatter(X_inliers[:, 0], X_inliers[:, 1], label='inliers',
                    color=inlier_color, s=40)
        plt.scatter(X_outliers[:, 0], X_outliers[:, 1],
                    label='outliers', color=outlier_color, s=50, marker='^')
        plt.title(sub_plot_title, fontsize=15)
        plt.xticks([])
        plt.yticks([])
        plt.legend(loc=3, prop={'size': 10})

    # check input data shapes are consistent
    X_train, y_train, X_test, y_test, y_train_pred, y_test_pred = \
        check_consistent_shape(X_train, y_train, X_test, y_test, y_train_pred,
                               y_test_pred)

    if X_train.shape[1] != 2:
        raise ValueError("Input data has to be 2-d for visualization. The "
                         "input data has {shape}.".format(shape=X_train.shape))

    X_train_outliers, X_train_inliers = get_outliers_inliers(X_train, y_train)
    X_train_outliers_pred, X_train_inliers_pred = get_outliers_inliers(
        X_train, y_train_pred)

    X_test_outliers, X_test_inliers = get_outliers_inliers(X_test, y_test)
    X_test_outliers_pred, X_test_inliers_pred = get_outliers_inliers(
        X_test, y_test_pred)

    # plot ground truth vs. predicted results
    fig = plt.figure(figsize=(12, 10))
    plt.suptitle("Demo of {clf_name} Detector".format(clf_name=clf_name),
                 fontsize=15)

    fig.add_subplot(221)
    _add_sub_plot(X_train_inliers, X_train_outliers, 'Train Set Ground Truth',
                  inlier_color='blue', outlier_color='orange')

    fig.add_subplot(222)
    _add_sub_plot(X_train_inliers_pred, X_train_outliers_pred,
                  'Train Set Prediction', inlier_color='blue',
                  outlier_color='orange')

    fig.add_subplot(223)
    _add_sub_plot(X_test_inliers, X_test_outliers, 'Test Set Ground Truth',
                  inlier_color='green', outlier_color='red')

    fig.add_subplot(224)
    _add_sub_plot(X_test_inliers_pred, X_test_outliers_pred,
                  'Test Set Prediction', inlier_color='green',
                  outlier_color='red')

    if save_figure:
        plt.savefig('{clf_name}.png'.format(clf_name=clf_name), dpi=300)

    if show_figure:
        plt.show()







[docs][](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.example.data_visualize)
defdata_visualize(X_train, y_train, show_figure=True,
                   save_figure=False):  # pragma: no cover
"""Utility function for visualizing the synthetic samples generated by
    generate_data_cluster function.

    Parameters
    ----------
    X_train : numpy array of shape (n_samples, n_features)
        The training samples.

    y_train : list or array of shape (n_samples,)
        The ground truth of training samples.

    show_figure : bool, optional (default=True)
        If set to True, show the figure.

    save_figure : bool, optional (default=False)
        If set to True, save the figure to the local.

    """

    def_plot(X_inliers, X_outliers, inlier_color='blue',
              outlier_color='orange'):
"""Internal method to add subplot of inliers and outliers.

        Parameters
        ----------
        X_inliers : numpy array of shape (n_samples, n_features)
            Outliers.

        X_outliers : numpy array of shape (n_samples, n_features)
            Inliers.

        sub_plot_title : str
            Subplot title.

        inlier_color : str, optional (default='blue')
            The color of inliers.

        outlier_color : str, optional (default='orange')
            The color of outliers.

        """
        plt.axis("equal")
        plt.scatter(X_inliers[:, 0], X_inliers[:, 1], label='inliers',
                    color=inlier_color, s=40)
        plt.scatter(X_outliers[:, 0], X_outliers[:, 1],
                    label='outliers', color=outlier_color, s=50, marker='^')
        plt.xticks([])
        plt.yticks([])
        plt.legend(loc='best', prop={'size': 10})

    assert len(X_train) <= 5
    in_colors = ['blue', 'green', 'purple', 'brown', 'black']
    out_colors = ['red', 'orange', 'grey', 'violet', 'pink']
    plt.figure(figsize=(13, 10))
    plt.suptitle("Demo of Generating Data in Clusters", fontsize=15)
    for i, cluster in enumerate(X_train):
        X_train_outliers, X_train_inliers = get_outliers_inliers(cluster,
                                                                 y_train[i])
        _plot(X_train_inliers, X_train_outliers,
              inlier_color=in_colors[i],
              outlier_color=out_colors[i])

    if save_figure:
        plt.savefig()

    if show_figure:
        plt.show()




```

Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
