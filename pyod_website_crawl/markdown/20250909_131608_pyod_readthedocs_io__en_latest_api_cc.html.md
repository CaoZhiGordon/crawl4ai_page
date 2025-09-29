# API CheatSheet - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/api_cc.html

**爬取时间:** 2025-09-09 13:16:08.367336

**深度:** 1

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/api_cc.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/api_cc.html)
[ View this page ](https://pyod.readthedocs.io/en/latest/_sources/api_cc.rst.txt "View this page")
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# API CheatSheet[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#api-cheatsheet "Link to this heading")
The full API Reference is available at [PyOD Documentation](https://pyod.readthedocs.io/en/latest/pyod.html). Below is a quick cheatsheet for all detectors:
  * [`pyod.models.base.BaseDetector.fit()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.fit "pyod.models.base.BaseDetector.fit"): The parameter y is ignored in unsupervised methods.
  * [`pyod.models.base.BaseDetector.decision_function()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.decision_function "pyod.models.base.BaseDetector.decision_function"): Predict raw anomaly scores for X using the fitted detector.
  * [`pyod.models.base.BaseDetector.predict()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.predict "pyod.models.base.BaseDetector.predict"): Determine whether a sample is an outlier or not as binary labels using the fitted detector.
  * [`pyod.models.base.BaseDetector.predict_proba()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.predict_proba "pyod.models.base.BaseDetector.predict_proba"): Estimate the probability of a sample being an outlier using the fitted detector.
  * [`pyod.models.base.BaseDetector.predict_confidence()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.predict_confidence "pyod.models.base.BaseDetector.predict_confidence"): Assess the model’s confidence on a per-sample basis (applicable in predict and predict_proba) [[APVD20](https://pyod.readthedocs.io/en/latest/index.html#id108 "Lorenzo Perini, Vincent Vercruyssen, and Jesse Davis. Quantifying the confidence of anomaly detectors in their example-wise predictions. In Joint European Conference on Machine Learning and Knowledge Discovery in Databases, 227–243. Springer, 2020.")].


**Key Attributes of a fitted model** :
  * `pyod.models.base.BaseDetector.decision_scores_`: Outlier scores of the training data. Higher scores typically indicate more abnormal behavior. Outliers usually have higher scores. Outliers tend to have higher scores.
  * `pyod.models.base.BaseDetector.labels_`: Binary labels of the training data, where 0 indicates inliers and 1 indicates outliers/anomalies.


See base class definition below:
## pyod.models.base module[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#module-pyod.models.base "Link to this heading")
Base class for all outlier detector models 

_class_ pyod.models.base.BaseDetector(_contamination =0.1_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/base.html#BaseDetector)[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector "Link to this definition") 
    
Bases: [`object`](https://docs.python.org/3/library/functions.html#object "\(in Python v3.13\)")
Abstract class for all outlier detection algorithms.
### Parameters[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#parameters "Link to this heading") 

contaminationfloat in (0., 0.5), optional (default=0.1) 
    
The amount of contamination of the data set, i.e. the proportion of outliers in the data set. Used when fitting to define the threshold on the decision function.
### Attributes[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#attributes "Link to this heading") 

[decision_scores_](https://pyod.readthedocs.io/en/latest/api_cc.html#id24)numpy array of shape (n_samples,) 
    
The outlier scores of the training data. The higher, the more abnormal. Outliers tend to have higher scores. This value is available once the detector is fitted. 

[threshold_](https://pyod.readthedocs.io/en/latest/api_cc.html#id26)float 
    
The threshold is based on `contamination`. It is the `n_samples * contamination` most abnormal samples in `decision_scores_`. The threshold is calculated for generating binary outlier labels. 

[labels_](https://pyod.readthedocs.io/en/latest/api_cc.html#id28)int, either 0 or 1 
    
The binary labels of the training data. 0 stands for inliers and 1 for outliers/anomalies. It is generated by applying `threshold_` on `decision_scores_`. 

compute_rejection_stats(_T =32_, _delta =0.1_, _c_fp =1_, _c_fn =1_, _c_r =-1_, _verbose =False_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/base.html#BaseDetector.compute_rejection_stats)[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.compute_rejection_stats "Link to this definition") 
     

Add reject option into the unsupervised detector. 
    
This comes with guarantees: an estimate of the expected rejection rate (return_rejectrate=True), an upper bound of the rejection rate (return_ub_rejectrate= True), and an upper bound on the cost (return_ub_cost=True).
#### Parameters[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id2 "Link to this heading") 

T: int, optional(default=32)
    
It allows to set the rejection threshold to 1-2exp(-T). The higher the value of T, the more rejections are made. 

delta: float, optional (default = 0.1)
    
The upper bound rejection rate holds with probability 1-delta. 

c_fp, c_fn, c_r: floats (positive),
    
optional (default = [1,1, contamination]) costs for false positive predictions (c_fp), false negative predictions (c_fn) and rejections (c_r). 

verbose: bool, optional (default = False)
    
If true, it prints the expected rejection rate, the upper bound rejection rate, and the upper bound of the cost.
#### Returns[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#returns "Link to this heading")
expected_rejection_rate: float, the expected rejection rate; upperbound_rejection_rate: float, the upper bound for the rejection rate
> satisfied with probability 1-delta;
upperbound_cost: float, the upper bound for the cost; 

_abstractmethod_ decision_function(_X_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/base.html#BaseDetector.decision_function)[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.decision_function "Link to this definition") 
    
Predict raw anomaly scores of X using the fitted detector.
The anomaly score of an input sample is computed based on the fitted detector. For consistency, outliers are assigned with higher anomaly scores.
#### Parameters[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id3 "Link to this heading") 

Xnumpy array of shape (n_samples, n_features) 
    
The input samples. Sparse matrices are accepted only if they are supported by the base estimator.
#### Returns[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id4 "Link to this heading") 

anomaly_scoresnumpy array of shape (n_samples,) 
    
The anomaly score of the input samples. 

_abstractmethod_ fit(_X_ , _y =None_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/base.html#BaseDetector.fit)[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.fit "Link to this definition") 
    
Fit detector. y is ignored in unsupervised methods.
#### Parameters[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id5 "Link to this heading") 

Xnumpy array of shape (n_samples, n_features) 
    
The input samples. 

yIgnored 
    
Not used, present for API consistency by convention.
#### Returns[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id6 "Link to this heading") 

selfobject 
    
Fitted estimator. 

fit_predict(_X_ , _y =None_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/base.html#BaseDetector.fit_predict)[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.fit_predict "Link to this definition") 
    
Fit detector first and then predict whether a particular sample is an outlier or not. y is ignored in unsupervised models.
#### Parameters[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id7 "Link to this heading") 

Xnumpy array of shape (n_samples, n_features) 
    
The input samples. 

yIgnored 
    
Not used, present for API consistency by convention.
#### Returns[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id8 "Link to this heading") 

outlier_labelsnumpy array of shape (n_samples,) 
    
For each observation, tells whether it should be considered as an outlier according to the fitted model. 0 stands for inliers and 1 for outliers.
Deprecated since version 0.6.9: fit_predict will be removed in pyod 0.8.0.; it will be replaced by calling fit function first and then accessing labels_ attribute for consistency. 

fit_predict_score(_X_ , _y_ , _scoring ='roc_auc_score'_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/base.html#BaseDetector.fit_predict_score)[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.fit_predict_score "Link to this definition") 
    
Fit the detector, predict on samples, and evaluate the model by predefined metrics, e.g., ROC.
#### Parameters[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id9 "Link to this heading") 

Xnumpy array of shape (n_samples, n_features) 
    
The input samples. 

yIgnored 
    
Not used, present for API consistency by convention. 

scoringstr, optional (default=’roc_auc_score’) 
    
Evaluation metric:
  * ‘roc_auc_score’: ROC score
  * ‘prc_n_score’: Precision @ rank n score


#### Returns[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id10 "Link to this heading")
score : float
Deprecated since version 0.6.9: fit_predict_score will be removed in pyod 0.8.0.; it will be replaced by calling fit function first and then accessing labels_ attribute for consistency. Scoring could be done by calling an evaluation method, e.g., AUC ROC. 

get_params(_deep =True_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/base.html#BaseDetector.get_params)[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.get_params "Link to this definition") 
    
Get parameters for this estimator.
See <http://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html> and sklearn/base.py for more information.
#### Parameters[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id11 "Link to this heading") 

deepbool, optional (default=True) 
    
If True, will return the parameters for this estimator and contained subobjects that are estimators.
#### Returns[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id12 "Link to this heading") 

paramsmapping of string to any 
    
Parameter names mapped to their values. 

predict(_X_ , _return_confidence =False_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/base.html#BaseDetector.predict)[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.predict "Link to this definition") 
    
Predict if a particular sample is an outlier or not.
#### Parameters[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id13 "Link to this heading") 

Xnumpy array of shape (n_samples, n_features) 
    
The input samples. 

return_confidenceboolean, optional(default=False) 
    
If True, also return the confidence of prediction.
#### Returns[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id14 "Link to this heading") 

outlier_labelsnumpy array of shape (n_samples,) 
    
For each observation, tells whether it should be considered as an outlier according to the fitted model. 0 stands for inliers and 1 for outliers. 

confidencenumpy array of shape (n_samples,). 
    
Only if return_confidence is set to True. 

predict_confidence(_X_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/base.html#BaseDetector.predict_confidence)[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.predict_confidence "Link to this definition") 
    
Predict the model’s confidence in making the same prediction under slightly different training sets. See [[BPVD20](https://pyod.readthedocs.io/en/latest/pyod.models.html#id1153 "Lorenzo Perini, Vincent Vercruyssen, and Jesse Davis. Quantifying the confidence of anomaly detectors in their example-wise predictions. In Joint European Conference on Machine Learning and Knowledge Discovery in Databases, 227–243. Springer, 2020.")].
#### Parameters[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id16 "Link to this heading") 

Xnumpy array of shape (n_samples, n_features) 
    
The input samples.
#### Returns[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id17 "Link to this heading") 

confidencenumpy array of shape (n_samples,) 
    
For each observation, tells how consistently the model would make the same prediction if the training set was perturbed. Return a probability, ranging in [0,1]. 

predict_proba(_X_ , _method ='linear'_, _return_confidence =False_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/base.html#BaseDetector.predict_proba)[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.predict_proba "Link to this definition") 
    
Predict the probability of a sample being outlier. Two approaches are possible:
  1. simply use Min-max conversion to linearly transform the outlier scores into the range of [0,1]. The model must be fitted first.
  2. use unifying scores, see [[BKKSZ11](https://pyod.readthedocs.io/en/latest/pyod.models.html#id1114 "Hans-Peter Kriegel, Peer Kroger, Erich Schubert, and Arthur Zimek. Interpreting and unifying outlier scores. In Proceedings of the 2011 SIAM International Conference on Data Mining, 13–24. SIAM, 2011.")].


#### Parameters[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id19 "Link to this heading") 

Xnumpy array of shape (n_samples, n_features) 
    
The input samples. 

methodstr, optional (default=’linear’) 
    
probability conversion method. It must be one of ‘linear’ or ‘unify’. 

return_confidenceboolean, optional(default=False) 
    
If True, also return the confidence of prediction.
#### Returns[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id20 "Link to this heading") 

outlier_probabilitynumpy array of shape (n_samples, n_classes) 
    
For each observation, tells whether or not it should be considered as an outlier according to the fitted model. Return the outlier probability, ranging in [0,1]. Note it depends on the number of classes, which is by default 2 classes ([proba of normal, proba of outliers]). 

predict_with_rejection(_X_ , _T =32_, _return_stats =False_, _delta =0.1_, _c_fp =1_, _c_fn =1_, _c_r =-1_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/base.html#BaseDetector.predict_with_rejection)[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.predict_with_rejection "Link to this definition") 
     

Predict if a particular sample is an outlier or not, 
    
allowing the detector to reject (i.e., output = -2) low confidence predictions.
#### Parameters[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id21 "Link to this heading") 

Xnumpy array of shape (n_samples, n_features) 
    
The input samples. 

Tint, optional(default=32) 
    
It allows to set the rejection threshold to 1-2exp(-T). The higher the value of T, the more rejections are made. 

return_stats: bool, optional (default = False)
    
If true, it returns also three additional float values: the estimated rejection rate, the upper bound rejection rate, and the upper bound of the cost. 

delta: float, optional (default = 0.1)
    
The upper bound rejection rate holds with probability 1-delta. 

c_fp, c_fn, c_r: floats (positive), optional (default = [1,1, contamination])
    
costs for false positive predictions (c_fp), false negative predictions (c_fn) and rejections (c_r).
#### Returns[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id22 "Link to this heading") 

outlier_labelsnumpy array of shape (n_samples,) 
    
For each observation, it tells whether it should be considered as an outlier according to the fitted model. 0 stands for inliers, 1 for outliers and -2 for rejection.
expected_rejection_rate: float, if return_stats is True; upperbound_rejection_rate: float, if return_stats is True; upperbound_cost: float, if return_stats is True; 

set_params(_** params_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/base.html#BaseDetector.set_params)[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.set_params "Link to this definition") 
    
Set the parameters of this estimator. The method works on simple estimators as well as on nested objects (such as pipelines). The latter have parameters of the form `<component>__<parameter>` so that it’s possible to update each component of a nested object.
See <http://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html> and sklearn/base.py for more information.
#### Returns[¶](https://pyod.readthedocs.io/en/latest/api_cc.html#id23 "Link to this heading")
self : object
[ Next API Reference ](https://pyod.readthedocs.io/en/latest/pyod.html) [ Previous Benchmarks ](https://pyod.readthedocs.io/en/latest/benchmark.html)
Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
On this page 
  * [API CheatSheet](https://pyod.readthedocs.io/en/latest/api_cc.html)
    * [pyod.models.base module](https://pyod.readthedocs.io/en/latest/api_cc.html#module-pyod.models.base)
      * [`BaseDetector`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector)
        * [`BaseDetector.compute_rejection_stats()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.compute_rejection_stats)
        * [`BaseDetector.decision_function()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.decision_function)
        * [`BaseDetector.fit()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.fit)
        * [`BaseDetector.fit_predict()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.fit_predict)
        * [`BaseDetector.fit_predict_score()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.fit_predict_score)
        * [`BaseDetector.get_params()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.get_params)
        * [`BaseDetector.predict()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.predict)
        * [`BaseDetector.predict_confidence()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.predict_confidence)
        * [`BaseDetector.predict_proba()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.predict_proba)
        * [`BaseDetector.predict_with_rejection()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.predict_with_rejection)
        * [`BaseDetector.set_params()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.set_params)


