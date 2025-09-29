# pyod.models.feature_bagging - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/_modules/pyod/models/feature_bagging.html

**爬取时间:** 2025-09-09 13:17:00.010277

**深度:** 2

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/feature_bagging.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/feature_bagging.html)
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Source code for pyod.models.feature_bagging
```
# -*- coding: utf-8 -*-
"""Feature bagging detector
"""
# Author: Yue Zhao <yzhao062@gmail.com>
# License: BSD 2 clause


importnumbers

importnumpyasnp
fromsklearn.baseimport clone
fromsklearn.utilsimport check_array
fromsklearn.utilsimport check_random_state
fromsklearn.utils.validationimport check_is_fitted

from.baseimport BaseDetector
from.combinationimport average, maximization
from.lofimport LOF
from..utils.utilityimport check_detector
from..utils.utilityimport check_parameter
from..utils.utilityimport generate_bagging_indices

MAX_INT = np.iinfo(np.int32).max


def_set_random_states(estimator, random_state=None):
"""Sets fixed random_state parameters for an estimator. Internal use only.
    Modified from sklearn/base.py

    Finds all parameters ending ``random_state`` and sets them to integers
    derived from ``random_state``.

    Parameters
    ----------
    estimator : estimator supporting get/set_params
        Estimator with potential randomness managed by random_state
        parameters.

    random_state : int, RandomState instance or None, optional (default=None)
        If int, random_state is the seed used by the random number generator;
        If RandomState instance, random_state is the random number generator;
        If None, the random number generator is the RandomState instance used
        by `np.random`.

    Notes
    -----
    This does not necessarily set *all* ``random_state`` attributes that
    control an estimator's randomness, only those accessible through
    ``estimator.get_params()``.  ``random_state``s not controlled include
    those belonging to:

        * cross-validation splitters
        * ``scipy.stats`` rvs
    """
    random_state = check_random_state(random_state)
    to_set = {}
    for key in sorted(estimator.get_params(deep=True)):
        if key == 'random_state' or key.endswith('__random_state'):
            to_set[key] = random_state.randint(MAX_INT)

    if to_set:
        estimator.set_params(**to_set)


# def _parallel_decision_function(estimators, estimators_features, X):
#     n_samples = X.shape[0]
#     scores = np.zeros((n_samples, len(estimators)))
#
#     for i, (estimator, features) in enumerate(
#             zip(estimators, estimators_features)):
#         if hasattr(estimator, 'decision_function'):
#             estimator_score = estimator.decision_function(
#                 X[:, features])
#             scores[:, i] = estimator_score
#         else:
#             raise NotImplementedError(
#                 'current base detector has no decision_function')
#     return scores


# TODO: should support parallelization at the model level
# TODO: detector score combination through BFS should be implemented
# See https://github.com/yzhao062/pyod/issues/59


[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.feature_bagging.FeatureBagging)
classFeatureBagging(BaseDetector):
""" A feature bagging detector is a meta estimator that fits a number of
    base detectors on various sub-samples of the dataset and use averaging
    or other combination methods to improve the predictive accuracy and
    control over-fitting.

    The sub-sample size is always the same as the original input sample size
    but the features are randomly sampled from half of the features to all
    features.

    By default, LOF is used as the base estimator. However, any estimator
    could be used as the base estimator, such as kNN and ABOD.

    Feature bagging first construct n subsamples by random selecting a subset
    of features, which induces the diversity of base estimators.

    Finally, the prediction score is generated by averaging/taking the maximum
    of all base detectors. See :cite:`lazarevic2005feature` for details.

    Parameters
    ----------
    base_estimator : object or None, optional (default=None)
        The base estimator to fit on random subsets of the dataset.
        If None, then the base estimator is a LOF detector.

    n_estimators : int, optional (default=10)
        The number of base estimators in the ensemble.

    contamination : float in (0., 0.5), optional (default=0.1)
        The amount of contamination of the data set,
        i.e. the proportion of outliers in the data set. Used when fitting to
        define the threshold on the decision function.

    max_features : int or float, optional (default=1.0)
        The number of features to draw from X to train each base estimator.

        - If int, then draw `max_features` features.
        - If float, then draw `max_features * X.shape[1]` features.

    bootstrap_features : bool, optional (default=False)
        Whether features are drawn with replacement.

    check_detector : bool, optional (default=True)
        If set to True, check whether the base estimator is consistent with
        pyod standard.

    check_estimator : bool, optional (default=False)
        If set to True, check whether the base estimator is consistent with
        sklearn standard.

        .. deprecated:: 0.6.9
          `check_estimator` will be removed in pyod 0.8.0.; it will be
          replaced by `check_detector`.

    n_jobs : optional (default=1)
        The number of jobs to run in parallel for both `fit` and
        `predict`. If -1, then the number of jobs is set to the
        number of cores.

    random_state : int, RandomState or None, optional (default=None)
        If int, random_state is the seed used by the random
        number generator; If RandomState instance, random_state is the random
        number generator; If None, the random number generator is the
        RandomState instance used by `np.random`.

    combination : str, optional (default='average')
        The method of combination:

        - if 'average': take the average of all detectors
        - if 'max': take the maximum scores of all detectors

    verbose : int, optional (default=0)
        Controls the verbosity of the building process.

    estimator_params : dict, optional (default=None)
        The list of attributes to use as parameters
        when instantiating a new base estimator. If none are given,
        default parameters are used.

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

    def__init__(self, base_estimator=None, n_estimators=10, contamination=0.1,
                 max_features=1.0, bootstrap_features=False,
                 check_detector=True, check_estimator=False, n_jobs=1,
                 random_state=None, combination='average', verbose=0,
                 estimator_params=None):

        super(FeatureBagging, self).__init__(contamination=contamination)
        self.base_estimator = base_estimator
        self.n_estimators = n_estimators
        self.max_features = max_features
        self.bootstrap_features = bootstrap_features
        self.check_detector = check_detector
        self.check_estimator = check_estimator
        self.combination = combination
        self.n_jobs = n_jobs
        self.random_state = random_state
        self.verbose = verbose
        if estimator_params is not None:
            self.estimator_params = estimator_params
        else:
            self.estimator_params = {}



[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.feature_bagging.FeatureBagging.fit)
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
        random_state = check_random_state(self.random_state)

        X = check_array(X)
        self.n_samples_, self.n_features_ = X.shape[0], X.shape[1]

        self._set_n_classes(y)

        # expect at least 2 features, does not make sense if only have
        # 1 feature
        check_parameter(self.n_features_, low=2, include_left=True,
                        param_name='n_features')

        # check parameters
        self._validate_estimator(default=LOF(n_jobs=self.n_jobs))

        # use at least half of the features
        self.min_features_ = int(0.5 * self.n_features_)

        # Validate max_features
        if isinstance(self.max_features, (numbers.Integral, np.integer)):
            self.max_features_ = self.max_features
        else:  # float
            self.max_features_ = int(self.max_features * self.n_features_)

        # min_features and max_features could equal
        check_parameter(self.max_features_, low=self.min_features_,
                        param_name='max_features', high=self.n_features_,
                        include_left=True, include_right=True)

        self.estimators_ = []
        self.estimators_features_ = []

        n_more_estimators = self.n_estimators - len(self.estimators_)

        if n_more_estimators < 0:
            raise ValueError('n_estimators=%d must be larger or equal to '
                             'len(estimators_)=%d when warm_start==True'
                             % (self.n_estimators, len(self.estimators_)))

        seeds = random_state.randint(MAX_INT, size=n_more_estimators)
        self._seeds = seeds

        for i in range(self.n_estimators):
            random_state = np.random.RandomState(seeds[i])

            # max_features is incremented by one since random
            # function is [min_features, max_features)
            features = generate_bagging_indices(random_state,
                                                self.bootstrap_features,
                                                self.n_features_,
                                                self.min_features_,
                                                self.max_features_ + 1)
            # initialize and append estimators
            estimator = self._make_estimator(append=False,
                                             random_state=random_state)
            estimator.fit(X[:, features])

            self.estimators_.append(estimator)
            self.estimators_features_.append(features)

        # decision score matrix from all estimators
        all_decision_scores = self._get_decision_scores()

        if self.combination == 'average':
            self.decision_scores_ = average(all_decision_scores)
        else:
            self.decision_scores_ = maximization(all_decision_scores)

        self._process_decision_scores()

        return self






[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.feature_bagging.FeatureBagging.decision_function)
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
        check_is_fitted(self, ['estimators_', 'estimators_features_',
                               'decision_scores_', 'threshold_', 'labels_'])
        X = check_array(X)

        if self.n_features_ != X.shape[1]:
            raise ValueError("Number of features of the model must "
                             "match the input. Model n_features is {0} and "
                             "input n_features is {1}."
                             "".format(self.n_features_, X.shape[1]))

        # Parallel loop
        # n_jobs, n_estimators, starts = _partition_estimators(self.n_estimators,
        #                                                      self.n_jobs)
        # all_pred_scores = Parallel(n_jobs=n_jobs, verbose=self.verbose)(
        #     delayed(_parallel_decision_function)(
        #         self.estimators_[starts[i]:starts[i + 1]],
        #         self.estimators_features_[starts[i]:starts[i + 1]],
        #         X)
        #     for i in range(n_jobs))
        #
        # # Reduce
        # all_pred_scores = np.concatenate(all_pred_scores, axis=1)
        all_pred_scores = self._predict_decision_scores(X)

        if self.combination == 'average':
            return average(all_pred_scores)
        else:
            return maximization(all_pred_scores)




    def_predict_decision_scores(self, X):
        all_pred_scores = np.zeros([X.shape[0], self.n_estimators])
        for i in range(self.n_estimators):
            features = self.estimators_features_[i]
            all_pred_scores[:, i] = self.estimators_[i].decision_function(
                X[:, features])
        return all_pred_scores

    def_get_decision_scores(self):
        all_decision_scores = np.zeros([self.n_samples_, self.n_estimators])
        for i in range(self.n_estimators):
            all_decision_scores[:, i] = self.estimators_[i].decision_scores_
        return all_decision_scores

    def_validate_estimator(self, default=None):
"""Check the estimator and the n_estimator attribute, set the
        `base_estimator_` attribute."""
        if not isinstance(self.n_estimators, (numbers.Integral, np.integer)):
            raise ValueError("n_estimators must be an integer, "
                             "got {0}.".format(type(self.n_estimators)))

        if self.n_estimators <= 0:
            raise ValueError("n_estimators must be greater than zero, "
                             "got {0}.".format(self.n_estimators))

        if self.base_estimator is not None:
            self.base_estimator_ = self.base_estimator
        else:
            self.base_estimator_ = default

        if self.base_estimator_ is None:
            raise ValueError("base_estimator cannot be None")

        # make sure estimator is consistent with sklearn
        if self.check_detector:
            check_detector(self.base_estimator_)

    def_make_estimator(self, append=True, random_state=None):
"""Make and configure a copy of the `base_estimator_` attribute.

        sklearn/base.py

        Warning: This method should be used to properly instantiate new
        sub-estimators.
        """

        # TODO: add a check for estimator_param
        estimator = clone(self.base_estimator_)
        estimator.set_params(**self.estimator_params)

        if random_state is not None:
            _set_random_states(estimator, random_state)

        if append:
            self.estimators_.append(estimator)

        return estimator

    def__len__(self):
"""Returns the number of estimators in the ensemble."""
        return len(self.estimators_)

    def__getitem__(self, index):
"""Returns the index'th estimator in the ensemble."""
        return self.estimators_[index]

    def__iter__(self):
"""Returns iterator over estimators in the ensemble."""
        return iter(self.estimators_)




```

Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
