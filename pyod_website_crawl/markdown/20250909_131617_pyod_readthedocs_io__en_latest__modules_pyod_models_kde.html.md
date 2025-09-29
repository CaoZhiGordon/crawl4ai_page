# pyod.models.kde - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/_modules/pyod/models/kde.html

**爬取时间:** 2025-09-09 13:16:17.255301

**深度:** 2

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/kde.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/kde.html)
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Source code for pyod.models.kde
```
# -*- coding: utf-8 -*-
"""Kernel Density Estimation (KDE) for Unsupervised Outlier Detection.
"""
# Author: Akira Tamamori <tamamori5917@gmail.com>
# License: BSD 2 clause


fromwarningsimport warn

fromsklearn.neighborsimport KernelDensity
fromsklearn.utilsimport check_array
fromsklearn.utils.validationimport check_is_fitted

from.baseimport BaseDetector
from..utils.utilityimport invert_order




[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.kde.KDE)
classKDE(BaseDetector):
"""KDE class for outlier detection.

    For an observation, its negative log probability density could be viewed
    as the outlying score.

    See :cite:`latecki2007outlier` for details.

    Parameters
    ----------
    contamination : float in (0., 0.5), optional (default=0.1)
        The amount of contamination of the data set,
        i.e. the proportion of outliers in the data set. Used when fitting to
        define the threshold on the decision function.

    bandwidth : float, optional (default=1.0)
        The bandwidth of the kernel.

    algorithm : {'auto', 'ball_tree', 'kd_tree'}, optional
        Algorithm used to compute the kernel density estimator:

        - 'ball_tree' will use BallTree
        - 'kd_tree' will use KDTree
        - 'auto' will attempt to decide the most appropriate algorithm
          based on the values passed to :meth:`fit` method.

    leaf_size : int, optional (default = 30)
        Leaf size passed to BallTree. This can affect the
        speed of the construction and query, as well as the memory
        required to store the tree.  The optimal value depends on the
        nature of the problem.

    metric : string or callable, default 'minkowski'
        metric to use for distance computation. Any metric from scikit-learn
        or scipy.spatial.distance can be used.

        If metric is a callable function, it is called on each
        pair of instances (rows) and the resulting value recorded. The callable
        should take two arrays as input and return one value indicating the
        distance between them. This works for Scipy's metrics, but is less
        efficient than passing the metric name as a string.

        Distance matrices are not supported.

        Valid values for metric are:

        - from scikit-learn: ['cityblock', 'cosine', 'euclidean', 'l1', 'l2',
          'manhattan']

        - from scipy.spatial.distance: ['braycurtis', 'canberra', 'chebyshev',
          'correlation', 'dice', 'hamming', 'jaccard', 'kulsinski',
          'mahalanobis', 'matching', 'minkowski', 'rogerstanimoto',
          'russellrao', 'seuclidean', 'sokalmichener', 'sokalsneath',
          'sqeuclidean', 'yule']

        See the documentation for scipy.spatial.distance for details on these
        metrics.

    metric_params : dict, optional (default = None)
        Additional keyword arguments for the metric function.

    Attributes
    ----------
    decision_scores_ : numpy array of shape (n_samples,)
        The outlier scores of the training data.
        The higher, the more abnormal. Outliers tend to have higher
        scores. This value is available once the detector is
        fitted.

    threshold_ : float
        The threshold is based on ``contamination``. It is the
        ``n_samples * contamination`` most abnormal samples in
        ``decision_scores_``. The threshold is calculated for generating
        binary outlier labels.

    labels_ : int, either 0 or 1
        The binary labels of the training data. 0 stands for inliers
        and 1 for outliers/anomalies. It is generated by applying
        ``threshold_`` on ``decision_scores_``.
    """

    def__init__(
            self,
            contamination=0.1,
            bandwidth=1.0,
            algorithm="auto",
            leaf_size=30,
            metric="minkowski",
            metric_params=None,
    ):
        super().__init__(contamination=contamination)
        self.bandwidth = bandwidth
        self.algorithm = algorithm
        self.leaf_size = leaf_size
        self.metric = metric
        self.metric_params = metric_params

        if self.algorithm != "auto" and self.algorithm != "ball_tree":
            warn(
                "algorithm parameter is deprecated and will be removed "
                "in version 0.7.6. By default, ball_tree will be used.",
                FutureWarning,
            )

        self.kde_ = KernelDensity(
            bandwidth=self.bandwidth,
            algorithm=self.algorithm,
            leaf_size=self.leaf_size,
            metric=self.metric,
            metric_params=self.metric_params,
        )

        self.decision_scores_ = None



[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.kde.KDE.fit)
    deffit(self, X, y=None):
"""Fit detector. y is ignored in unsupervised methods.

        Parameters
        ----------
        X : numpy array of shape (n_samples, n_features)
            The input samples.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        self : object
            Fitted estimator.
        """

        # validate inputs X and y (optional)
        X = check_array(X)
        self._set_n_classes(y)

        self.kde_.fit(X)

        # invert decision_scores_. Outliers comes with higher outlier scores.
        self.decision_scores_ = invert_order(self.kde_.score_samples(X))
        self._process_decision_scores()

        return self






[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.kde.KDE.decision_function)
    defdecision_function(self, X):
"""Predict raw anomaly score of X using the fitted detector.

        The anomaly score of an input sample is computed based on different
        detector algorithms. For consistency, outliers are assigned with
        larger anomaly scores.

        Parameters
        ----------
        X : numpy array of shape (n_samples, n_features)
            The training input samples. Sparse matrices are accepted only
            if they are supported by the base estimator.

        Returns
        -------
        anomaly_scores : numpy array of shape (n_samples,)
            The anomaly score of the input samples.
        """
        check_is_fitted(self, ["decision_scores_", "threshold_", "labels_"])

        X = check_array(X)

        # invert outlier scores. Outliers comes with higher outlier scores.
        return invert_order(self.kde_.score_samples(X))






```

Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
