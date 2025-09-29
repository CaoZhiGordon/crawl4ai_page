# pyod.models.cd - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/_modules/pyod/models/cd.html

**爬取时间:** 2025-09-09 13:17:03.536227

**深度:** 2

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/cd.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/cd.html)
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Source code for pyod.models.cd
```
# -*- coding: utf-8 -*-
"""Cook's distance outlier detection (CD)
"""

# Author: D Kulik
# License: BSD 2 clause


importnumpyasnp
fromsklearn.linear_modelimport LinearRegression
fromsklearn.utilsimport check_array
fromsklearn.utils.validationimport check_is_fitted

from.baseimport BaseDetector


def_Cooks_dist(X, y, model):
"""Calculated the Cook's distance

    Parameters
    ----------
    X : numpy array of shape (n_samples, n_features)
        The training dataset.

    y : numpy array of shape (n_samples)
        The training datset

    model : object
        Regression model used to calculate the Cook's distance

    Returns
    -------
    distances_ : numpy array of shape (n_samples)
        Cook's distance
    """

    # Leverage is computed as the diagonal of the projection matrix of X
    leverage = (X * np.linalg.pinv(X).T).sum(1)

    # Compute the rank and the degrees of freedom of the model
    rank = np.linalg.matrix_rank(X)
    df = X.shape[0] - rank

    # Compute the MSE from the residuals
    residuals = y - model.predict(X)
    mse = np.dot(residuals, residuals) / df

    # Compute Cook's distance
    if (mse != 0) or (mse != np.nan):
        residuals_studentized = residuals / np.sqrt(mse) / np.sqrt(
            1 - leverage)
        distance_ = residuals_studentized ** 2 / X.shape[1]
        distance_ *= leverage / (1 - leverage)
        distance_ = ((distance_ - distance_.min())
                     / (distance_.max() - distance_.min()))

    else:
        distance_ = np.ones(len(y)) * np.nan

    return distance_


def_process_distances(X, model):
"""Calculated the mean Cook's distances for
    each feature

    Parameters
    ----------
    X : numpy array of shape (n_samples, n_features)
        The training dataset.

    model : object
        Regression model used to calculate the Cook's distance

    Returns
    -------
    distances_ : numpy array of shape (n_samples)
        mean Cook's distance
    """

    distances_ = []
    for i in range(X.shape[1]):
        mod = model

        # Extract new X and y inputs
        exp = np.delete(X.copy(), i, axis=1)
        resp = X[:, i]

        exp = exp.reshape(-1, 1) if exp.ndim == 1 else exp

        # Fit the model
        mod.fit(exp, resp)

        # Get Cook's Distance
        distance_ = _Cooks_dist(exp, resp, mod)

        distances_.append(distance_)

    distances_ = np.nanmean(distances_, axis=0)

    return distances_




[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.cd.CD)
classCD(BaseDetector):
"""Cook's distance can be used to identify points that negatively
       affect a regression model. A combination of each observation’s
       leverage and residual values are used in the measurement. Higher
       leverage and residuals relate to  higher Cook’s distances. Note
       that this method is unsupervised and requires at least two 
       features for X with which to calculate the mean Cook's distance
       for each datapoint. Read more in the :cite:`cook1977detection`.

    Parameters
    ----------
    contamination : float in (0., 0.5), optional (default=0.1)
        The amount of contamination of the data set, i.e.
        the proportion of outliers in the data set. Used when fitting to
        define the threshold on the decision function.
    model : object, optional (default=LinearRegression())
        Regression model used to calculate the Cook's distance
    Attributes
    ----------
    decision_scores_ : numpy array of shape (n_samples,)
        The outlier scores of the training data.
        The higher, the more abnormal. Outliers tend to have higher
        scores. This value is available once the detector is
        fitted.

    threshold_ : float
       The modified z-score to use as a threshold. Observations with
       a modified z-score (based on the median absolute deviation) greater
       than this value will be classified as outliers.

    labels_ : int, either 0 or 1
        The binary labels of the training data. 0 stands for inliers
        and 1 for outliers/anomalies. It is generated by applying
        ``threshold_`` on ``decision_scores_``.
        """

    def__init__(self, contamination=0.1, model=LinearRegression()):
        super(CD, self).__init__(contamination=contamination)
        self.model = model



[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.cd.CD.fit)
    deffit(self, X, y=None):
""""Fit detector. y is ignored in unsupervised methods.

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

        # Validate inputs X and y
        X = check_array(X)

        self._set_n_classes(y)

        # Get Cook's distance
        distances_ = _process_distances(X, self.model)

        self.decision_scores_ = distances_

        self._process_decision_scores()

        return self






[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.cd.CD.decision_function)
    defdecision_function(self, X):
"""Predict raw anomaly score of X using the fitted detector.
        For consistency, outliers are assigned with larger anomaly scores.

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

        # Validate input X
        X = check_array(X)

        # Get Cook's distance
        distances_ = _process_distances(X, self.model)

        return distances_






```

Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
