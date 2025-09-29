# pyod.models.mcd - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/_modules/pyod/models/mcd.html

**爬取时间:** 2025-09-09 13:16:56.864492

**深度:** 2

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/mcd.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/mcd.html)
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Source code for pyod.models.mcd
```
# -*- coding: utf-8 -*-
"""Outlier Detection with Minimum Covariance Determinant (MCD)
"""
# Author: Yue Zhao <zhaoy@cmu.edu>
# License: BSD 2 clause


fromsklearn.covarianceimport MinCovDet
fromsklearn.utils.validationimport check_array
fromsklearn.utils.validationimport check_is_fitted

from.baseimport BaseDetector

__all__ = ['MCD']




[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.mcd.MCD)
classMCD(BaseDetector):
"""Detecting outliers in a Gaussian distributed dataset using
    Minimum Covariance Determinant (MCD): robust estimator of covariance.

    The Minimum Covariance Determinant covariance estimator is to be applied
    on Gaussian-distributed data, but could still be relevant on data
    drawn from a unimodal, symmetric distribution. It is not meant to be used
    with multi-modal data (the algorithm used to fit a MinCovDet object is
    likely to fail in such a case).
    One should consider projection pursuit methods to deal with multi-modal
    datasets.

    First fit a minimum covariance determinant model and then compute the
    Mahalanobis distance as the outlier degree of the data

    See :cite:`rousseeuw1999fast,hardin2004outlier` for details.

    Parameters
    ----------
    contamination : float in (0., 0.5), optional (default=0.1)
        The amount of contamination of the data set,
        i.e. the proportion of outliers in the data set. Used when fitting to
        define the threshold on the decision function.

    store_precision : bool
        Specify if the estimated precision is stored.

    assume_centered : bool
        If True, the support of the robust location and the covariance
        estimates is computed, and a covariance estimate is recomputed from
        it, without centering the data.
        Useful to work with data whose mean is significantly equal to
        zero but is not exactly zero.
        If False, the robust location and covariance are directly computed
        with the FastMCD algorithm without additional treatment.

    support_fraction : float, 0 < support_fraction < 1
        The proportion of points to be included in the support of the raw
        MCD estimate. Default is None, which implies that the minimum
        value of support_fraction will be used within the algorithm:
        [n_sample + n_features + 1] / 2

    random_state : int, RandomState instance or None, optional (default=None)
        If int, random_state is the seed used by the random number generator;
        If RandomState instance, random_state is the random number generator;
        If None, the random number generator is the RandomState instance used
        by `np.random`.

    Attributes
    ----------
    raw_location_ : array-like, shape (n_features,)
        The raw robust estimated location before correction and re-weighting.

    raw_covariance_ : array-like, shape (n_features, n_features)
        The raw robust estimated covariance before correction and re-weighting.

    raw_support_ : array-like, shape (n_samples,)
        A mask of the observations that have been used to compute
        the raw robust estimates of location and shape, before correction
        and re-weighting.

    location_ : array-like, shape (n_features,)
        Estimated robust location

    covariance_ : array-like, shape (n_features, n_features)
        Estimated robust covariance matrix

    precision_ : array-like, shape (n_features, n_features)
        Estimated pseudo inverse matrix.
        (stored only if store_precision is True)

    support_ : array-like, shape (n_samples,)
        A mask of the observations that have been used to compute
        the robust estimates of location and shape.

    decision_scores_ : numpy array of shape (n_samples,)
        The outlier scores of the training data.
        The higher, the more abnormal. Outliers tend to have higher
        scores. This value is available once the detector is
        fitted. Mahalanobis distances of the training set (on which
        `:meth:`fit` is called) observations.

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

    def__init__(self, contamination=0.1, store_precision=True,
                 assume_centered=False, support_fraction=None,
                 random_state=None):
        super(MCD, self).__init__(contamination=contamination)
        self.store_precision = store_precision
        self.assume_centered = assume_centered
        self.support_fraction = support_fraction
        self.random_state = random_state

    # noinspection PyIncorrectDocstring


[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.mcd.MCD.fit)
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
        # Validate inputs X and y (optional)
        X = check_array(X)
        self._set_n_classes(y)

        self.detector_ = MinCovDet(store_precision=self.store_precision,
                                   assume_centered=self.assume_centered,
                                   support_fraction=self.support_fraction,
                                   random_state=self.random_state)
        self.detector_.fit(X=X, y=y)

        # Use mahalanabis distance as the outlier score
        self.decision_scores_ = self.detector_.dist_
        self._process_decision_scores()
        return self






[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.mcd.MCD.decision_function)
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
        check_is_fitted(self, ['decision_scores_', 'threshold_', 'labels_'])
        X = check_array(X)

        # Computer mahalanobis distance of the samples
        return self.detector_.mahalanobis(X)




    @property
    defraw_location_(self):
"""The raw robust estimated location before correction and
        re-weighting.

        Decorator for scikit-learn MinCovDet attributes.
        """
        return self.detector_.raw_location_

    @property
    defraw_covariance_(self):
"""The raw robust estimated location before correction and
        re-weighting.

        Decorator for scikit-learn MinCovDet attributes.
        """
        return self.detector_.raw_covariance_

    @property
    defraw_support_(self):
"""A mask of the observations that have been used to compute
        the raw robust estimates of location and shape, before correction
        and re-weighting.

        Decorator for scikit-learn MinCovDet attributes.
        """
        return self.detector_.raw_support_

    @property
    deflocation_(self):
"""Estimated robust location.

        Decorator for scikit-learn MinCovDet attributes.
        """
        return self.detector_.location_

    @property
    defcovariance_(self):
"""Estimated robust covariance matrix.

        Decorator for scikit-learn MinCovDet attributes.
        """
        return self.detector_.covariance_

    @property
    defprecision_(self):
""" Estimated pseudo inverse matrix.
        (stored only if store_precision is True)

        Decorator for scikit-learn MinCovDet attributes.
        """
        return self.detector_.precision_

    @property
    defsupport_(self):
"""A mask of the observations that have been used to compute
        the robust estimates of location and shape.

        Decorator for scikit-learn MinCovDet attributes.
        """
        return self.detector_.support_




```

Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
