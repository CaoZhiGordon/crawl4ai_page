# pyod.models.lmdd - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/_modules/pyod/models/lmdd.html

**爬取时间:** 2025-09-09 13:16:49.906109

**深度:** 2

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/lmdd.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/lmdd.html)
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Source code for pyod.models.lmdd
```
# -*- coding: utf-8 -*-
"""Linear Model Deviation-base outlier detection (LMDD).
"""
# Author: Yahya Almardeny <almardeny@gmail.com>
# License: BSD 2 clause


importnumpyasnp
fromnumbaimport njit
fromscipyimport stats
fromsklearn.utilsimport check_array, check_random_state

frompyod.utilsimport check_parameter
from.baseimport BaseDetector


@njit
def_aad(X):
"""Internal Function to Calculate Average Absolute Deviation
    (a.k.a Mean Absolute Deviation)
    """
    return np.mean(np.absolute(X - np.mean(X)))


def_check_params(n_iter, dis_measure, random_state):
"""Internal function to check for and validate class parameters.
    Also, to return random state instance and the appropriate dissimilarity
    measure if valid.
    """
    if isinstance(n_iter, int):
        check_parameter(n_iter, low=1, param_name='n_iter')
    else:
        raise TypeError("n_iter should be int, got %s" % n_iter)

    if isinstance(dis_measure, str):
        if dis_measure not in ('aad', 'var', 'iqr'):
            raise ValueError("Unknown dissimilarity measure type, "
                             "dis_measure should be in "
                             "(\'aad\', \'var\', \'iqr\'), "
                             "got %s" % dis_measure)
        # TO-DO: 'mad': Median Absolute Deviation to be added
        # once Scipy stats version 1.3.0 is released
    else:
        raise TypeError("dis_measure should be str, got %s" % dis_measure)

    return check_random_state(random_state), _aad if dis_measure == 'aad' \
        else (np.var if dis_measure == 'var'
              else (stats.iqr if dis_measure == 'iqr' else None))




[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.lmdd.LMDD)
classLMDD(BaseDetector):
"""Linear Method for Deviation-based Outlier Detection.

    LMDD employs the concept of the smoothing factor which
    indicates how much the dissimilarity can be reduced by
    removing a subset of elements from the data-set.
    Read more in the :cite:`arning1996linear`.

    Note: this implementation has minor modification to make it output scores
    instead of labels.

    Parameters
    ----------
    contamination : float in (0., 0.5), optional (default=0.1)
        The amount of contamination of the data set, i.e.
        the proportion of outliers in the data set. Used when fitting to
        define the threshold on the decision function.

    n_iter : int, optional (default=50)
        Number of iterations where in each iteration,
        the process is repeated after randomizing the order of the input.
        Note that n_iter is a very important factor that affects the accuracy.
        The higher the better the accuracy and the longer the execution.

    dis_measure: str, optional (default='aad')
        Dissimilarity measure to be used in calculating the smoothing factor
        for points, options available:

        - 'aad': Average Absolute Deviation
        - 'var': Variance
        - 'iqr': Interquartile Range

    random_state : int, RandomState instance or None, optional (default=None)
        If int, random_state is the seed used by the random number generator;
        If RandomState instance, random_state is the random number generator;
        If None, the random number generator is the RandomState instance used
        by `np.random`.

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
    """

    def__init__(self, contamination=0.1, n_iter=50, dis_measure='aad',
                 random_state=None):
        super(LMDD, self).__init__(contamination=contamination)
        self.n_iter, self.n_iter_ = n_iter, n_iter
        self.dis_measure, self.dis_measure_ = dis_measure, dis_measure

        # add this assignment to prevent clone error; not being used.
        self.random_state = random_state
        self.random_state_, self.dis_measure_ = _check_params(n_iter,
                                                              dis_measure,
                                                              random_state)



[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.lmdd.LMDD.fit)
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
        X = check_array(X)
        self._set_n_classes(y)
        self.decision_scores_ = self.decision_function(X)
        self._process_decision_scores()
        return self






[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.lmdd.LMDD.decision_function)
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
        return self.__sf(X)




    def__dis(self, X):
"""
        Internal function to calculate for
        dissimilarity in a sequence of sets.
        """
        res_ = np.zeros(shape=(X.shape[0],))
        var_max, j = -np.inf, 0
        # this can be vectorized but just for comforting memory
        for i in range(1, X.shape[0]):
            _var = self.dis_measure_(X[:i + 1]) - self.dis_measure_(X[:i])
            if _var > var_max:
                var_max = _var
                j = i

        if var_max > res_[j]:
            res_[j] = var_max

            for k in range(j + 1, X.shape[0]):
                dk_diff = self.dis_measure_(np.vstack((X[:j], X[k]))) \
                          - self.dis_measure_(np.vstack((X[:j + 1], X[k])))
                if dk_diff >= 0:
                    res_[k] = dk_diff + var_max

        return res_

    def__sf(self, X):
"""Internal function to calculate for Smoothing Factors of data points
        Repeated n_iter_ of times in randomized mode.
        """
        dis_ = np.zeros(shape=(X.shape[0],))
        card_ = np.zeros(shape=(X.shape[0],))
        # perform one process with the original input order
        itr_res = self.__dis(X)
        np.put(card_, X.shape[0] - sum([i > 0. for i in itr_res]),
               np.where(itr_res > 0.))

        # create a copy of random state to preserve original state for
        # future fits (if any)
        random_state = np.random.RandomState(
            seed=self.random_state_.get_state()[1][0])
        indices = np.arange(X.shape[0])
        for _ in range(self.n_iter_):
            ind_ = indices
            random_state.shuffle(ind_)
            _x = X[indices]
            # get dissimilarity of this iteration and restore original order
            itr_res = self.__dis(_x)[np.argsort(ind_)]
            current_card = X.shape[0] - sum([i > 0. for i in itr_res])
            # compare with previous iteration to get the maximal dissimilarity
            for i, j in enumerate(itr_res):
                if j > dis_[i]:
                    dis_[i] = j
                    card_[i] = current_card
            # Increase random state seed by one to reorder input next iteration
            random_state.seed(random_state.get_state()[1][0] + 1)

        return np.multiply(dis_, card_)




```

Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
