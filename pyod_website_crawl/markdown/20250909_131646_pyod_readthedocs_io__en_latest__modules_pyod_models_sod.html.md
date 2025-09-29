# pyod.models.sod - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/_modules/pyod/models/sod.html

**爬取时间:** 2025-09-09 13:16:46.389856

**深度:** 2

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/sod.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/sod.html)
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Source code for pyod.models.sod
```
# -*- coding: utf-8 -*-
"""Subspace Outlier Detection (SOD)
"""
# Author: Yahya Almardeny <almardeny@gmail.com>
# License: BSD 2 clause

importnumbaasnb
importnumpyasnp
fromsklearn.neighborsimport NearestNeighbors
fromsklearn.utilsimport check_array

from.baseimport BaseDetector
from..utils.utilityimport check_parameter


@nb.njit(parallel=True)
def_snn_imp(ind, ref_set_):
"""Internal function for fast snn calculation

    Parameters
    ----------
    ind : int
        Indices return by kNN.

    ref_set_ : int, optional (default=10)
        specifies the number of shared nearest neighbors to create the
        reference set. Note that ref_set must be smaller than n_neighbors.

    """
    n = ind.shape[0]
    _count = np.zeros(shape=(n, ref_set_), dtype=np.uint32)
    for i in nb.prange(n):
        temp = np.empty(n, dtype=np.uint32)
        test_element_set = set(ind[i])
        for j in nb.prange(n):
            temp[j] = len(set(ind[j]).intersection(test_element_set))
        temp[i] = np.iinfo(np.uint32).max
        _count[i] = np.argsort(temp)[::-1][1:ref_set_ + 1]

    return _count




[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.sod.SOD)
classSOD(BaseDetector):
"""Subspace outlier detection (SOD) schema aims to detect outlier in
    varying subspaces of a high dimensional feature space. For each data
    object, SOD explores the axis-parallel subspace spanned by the data
    object's neighbors and determines how much the object deviates from the
    neighbors in this subspace.

    See :cite:`kriegel2009outlier` for details.

    Parameters
    ----------
    n_neighbors : int, optional (default=20)
        Number of neighbors to use by default for k neighbors queries.

    ref_set: int, optional (default=10)
        specifies the number of shared nearest neighbors to create the
        reference set. Note that ref_set must be smaller than n_neighbors.

    alpha: float in (0., 1.), optional (default=0.8)
           specifies the lower limit for selecting subspace.
           0.8 is set as default as suggested in the original paper.

    contamination : float in (0., 0.5), optional (default=0.1)
        The amount of contamination of the data set, i.e.
        the proportion of outliers in the data set. Used when fitting to
        define the threshold on the decision function.

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

    def__init__(self, contamination=0.1, n_neighbors=20, ref_set=10,
                 alpha=0.8):
        super(SOD, self).__init__(contamination=contamination)
        if isinstance(n_neighbors, int):
            check_parameter(n_neighbors, low=1, param_name='n_neighbors')
        else:
            raise ValueError(
                "n_neighbors should be int. Got %s" % type(n_neighbors))

        if isinstance(ref_set, int):
            check_parameter(ref_set, low=1, high=n_neighbors,
                            param_name='ref_set')
        else:
            raise ValueError("ref_set should be int. Got %s" % type(ref_set))

        if isinstance(alpha, float):
            check_parameter(alpha, low=0.0, high=1.0, param_name='alpha')
        else:
            raise ValueError("alpha should be float. Got %s" % type(alpha))

        self.n_neighbors = n_neighbors
        self.ref_set = ref_set
        self.alpha = alpha



[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.sod.SOD.fit)
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
        self.decision_scores_ = self.decision_function(X)
        self._process_decision_scores()

        return self






[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.sod.SOD.decision_function)
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
        return self._sod(X)




    def_snn(self, X):
"""This function is called internally to calculate the shared nearest
        neighbors (SNN). SNN is reported to be more robust than k nearest
        neighbors.

        Returns
        -------
        snn_indices : numpy array of shape (n_shared_nearest_neighbors,)
            The indices of top k shared nearest neighbors for each observation.
        """
        knn = NearestNeighbors(n_neighbors=self.n_neighbors)
        knn.fit(X)
        # Get the knn index
        ind = knn.kneighbors(return_distance=False)
        return _snn_imp(ind, self.ref_set)

    def_sod(self, X):
"""This function is called internally to perform subspace outlier 
        detection algorithm.
        Returns
        -------
        anomaly_scores : numpy array of shape (n_samples,)
            The anomaly score of the input samples.
        """
        ref_inds = self._snn(X)
        anomaly_scores = np.zeros(shape=(X.shape[0],))
        for i in range(X.shape[0]):
            obs = X[i]
            ref = X[ref_inds[i,],]
            means = np.mean(ref, axis=0)  # mean of each column
            # average squared distance of the reference to the mean
            var_total = np.sum(np.sum(np.square(ref - means))) / self.ref_set
            var_expect = self.alpha * var_total / X.shape[1]
            var_actual = np.var(ref, axis=0)  # variance of each attribute
            var_inds = [1 if (j < var_expect) else 0 for j in var_actual]
            rel_dim = np.sum(var_inds)
            if rel_dim != 0:
                anomaly_scores[i] = np.sqrt(
                    np.dot(var_inds, np.square(obs - means)) / rel_dim)

        return anomaly_scores




```

Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
