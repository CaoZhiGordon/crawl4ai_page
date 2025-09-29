# pyod.models.loci - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/_modules/pyod/models/loci.html

**爬取时间:** 2025-09-09 13:16:56.611813

**深度:** 2

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/loci.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/loci.html)
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Source code for pyod.models.loci
```
# -*- coding: utf-8 -*-
"""Local Correlation Integral (LOCI).
Part of the codes are adapted from https://github.com/Cloudy10/loci
"""
# Author: Winston Li <jk_zhengli@hotmail.com>
# License: BSD 2 clause


importnumpyasnp
fromnumbaimport njit
fromscipy.spatial.distanceimport pdist, squareform
fromsklearn.utilsimport check_array
fromsklearn.utils.validationimport check_is_fitted

from.baseimport BaseDetector


@njit
def_get_critical_values(dist_matrix, alpha, p_ix, r_max,
                         r_min=0):  # pragma: no cover
"""Computes the critical values of a given distance matrix.

    Parameters
    ----------
    dist_matrix : array-like, shape (n_samples, n_features)
        The distance matrix w.r.t. to the training samples.

    p_ix : int
        Subsetting index

    alpha : int, default = 0.5
        The neighbourhood parameter measures how large of a neighbourhood
        should be considered "local".

    r_max : int
        Maximum neighbourhood radius

    r_min : int, default = 0
        Minimum neighbourhood radius

    Returns
    -------
    cv : array, shape (n_critical_val, )
        Returns a list of critical values.
    """

    distances = dist_matrix[p_ix, :]
    mask = (r_min < distances) & (distances <= r_max)
    cv = np.sort(
        np.concatenate((distances[mask], distances[mask] / alpha)))
    return cv


@njit
def_get_sampling_N(dist_matrix, p_ix, r):  # pragma: no cover
"""Computes the set of r-neighbours.

    Parameters
    ----------
    dist_matrix : array-like, shape (n_samples, n_features)
        The distance matrix w.r.t. to the training samples.

    p_ix : int
        Subsetting index

    r : int
        Neighbourhood radius


    Returns
    -------
    sample : array, shape (n_sample, )
        Returns a list of neighbourhood data points.
    """

    p_distances = dist_matrix[p_ix, :]
    sample = np.nonzero(p_distances <= r)[0]
    return sample




[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.loci.LOCI)
classLOCI(BaseDetector):
"""Local Correlation Integral.
    LOCI is highly effective for detecting outliers and groups of 
    outliers ( a.k.a.micro-clusters), which offers the following advantages 
    and novelties: (a) It provides an automatic, data-dictated cut-off to 
    determine whether a point is an outlier—in contrast, previous methods 
    force users to pick cut-offs, without any hints as to what cut-off value 
    is best for a given dataset. (b) It can provide a LOCI plot for each 
    point; this plot summarizes a wealth of information about the data in 
    the vicinity of the point, determining clusters, micro-clusters, their 
    diameters and their inter-cluster distances. None of the existing 
    outlier-detection methods can match this feature, because they output 
    only a single number for each point: its outlierness score.(c) It can 
    be computed as quickly as the best previous methods
    Read more in the :cite:`papadimitriou2003loci`.
    Parameters
    ----------
    contamination : float in (0., 0.5), optional (default=0.1) 
        The amount of contamination of the data set, i.e.
        the proportion of outliers in the data set. Used when fitting to
        define the threshold on the decision function.
    alpha : int, default = 0.5
        The neighbourhood parameter measures how large of a neighbourhood
        should be considered "local".
    k: int, default = 3
        An outlier cutoff threshold for determine whether or not a point 
        should be considered an outlier.

    Attributes
    ----------
    decision_scores_ : numpy array of shape (n_samples,)
        The outlier scores of the training data.
        The higher, the more abnormal. Outliers tend to have higher
        scores. This value is available once the detector is fitted.

    threshold_ : float
        The threshold is based on ``contamination``. It is the
        ``n_samples * contamination`` most abnormal samples in
        ``decision_scores_``. The threshold is calculated for generating
        binary outlier labels.

    labels_ : int, either 0 or 1
        The binary labels of the training data. 0 stands for inliers
        and 1 for outliers/anomalies. It is generated by applying
        ``threshold_`` on ``decision_scores_``.

    Examples
    --------
    >>> from pyod.models.loci import LOCI
    >>> from pyod.utils.data import generate_data
    >>> n_train = 50
    >>> n_test = 50
    >>> contamination = 0.1
    >>> X_train, y_train, X_test, y_test = generate_data(
    ...     n_train=n_train, n_test=n_test,
    ...     contamination=contamination, random_state=42)
    >>> clf = LOCI()
    >>> clf.fit(X_train)
    LOCI(alpha=0.5, contamination=0.1, k=None)
    """

    def__init__(self, contamination=0.1, alpha=0.5, k=3):
        super(LOCI, self).__init__(contamination=contamination)
        self.alpha = alpha
        self.threshold_ = k

    def_get_alpha_n(self, dist_matrix, indices, r):
"""Computes the alpha neighbourhood points.

        Parameters
        ----------
        dist_matrix : array-like, shape (n_samples, n_features)
            The distance matrix w.r.t. to the training samples.

        indices : int
            Subsetting index

        r : int
            Neighbourhood radius

        Returns
        -------
        alpha_n : array, shape (n_alpha, )
            Returns the alpha neighbourhood points.
        """

        if type(indices) is int:
            alpha_n = np.count_nonzero(
                dist_matrix[indices, :] < (r * self.alpha))
            return alpha_n
        else:
            alpha_n = np.count_nonzero(
                dist_matrix[indices, :] < (r * self.alpha), axis=1)
            return alpha_n

    def_calculate_decision_score(self, X):
"""Computes the outlier scores.
        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            The input data points.
        Returns
        -------
        outlier_scores : list
            Returns the list of outlier scores for input dataset.       
        """
        outlier_scores = [0] * X.shape[0]
        dist_matrix = squareform(pdist(X, metric="euclidean"))
        max_dist = dist_matrix.max()
        r_max = max_dist / self.alpha

        for p_ix in range(X.shape[0]):
            critical_values = _get_critical_values(dist_matrix, self.alpha,
                                                   p_ix, r_max)
            for r in critical_values:
                n_values = self._get_alpha_n(dist_matrix,
                                             _get_sampling_N(dist_matrix,
                                                             p_ix, r), r)
                cur_alpha_n = self._get_alpha_n(dist_matrix, p_ix, r)
                n_hat = np.mean(n_values)
                mdef = 1 - (cur_alpha_n / n_hat)
                sigma_mdef = np.std(n_values) / n_hat
                if n_hat >= 20:
                    outlier_scores[p_ix] = mdef / sigma_mdef
                    if mdef > (self.threshold_ * sigma_mdef):
                        break
        return np.asarray(outlier_scores)



[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.loci.LOCI.fit)
    deffit(self, X, y=None):
"""Fit the model using X as training data.
        Parameters
        ----------
        X : array, shape (n_samples, n_features)
            Training data.

        y : Ignored
            Not used, present for API consistency by convention.
        Returns
        -------
        self : object

        """
        X = check_array(X)
        self._set_n_classes(y)
        self.decision_scores_ = self._calculate_decision_score(X)
        self.labels_ = (self.decision_scores_ > self.threshold_).astype(
            'int').ravel()

        # calculate for predict_proba()

        self._mu = np.mean(self.decision_scores_)
        self._sigma = np.std(self.decision_scores_)
        return self






[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.loci.LOCI.decision_function)
    defdecision_function(self, X):
        check_is_fitted(self, ['decision_scores_', 'threshold_', 'labels_'])
        X = check_array(X)
        return self._calculate_decision_score(X)






```

Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
