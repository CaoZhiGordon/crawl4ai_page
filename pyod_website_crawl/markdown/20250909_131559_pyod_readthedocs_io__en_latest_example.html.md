# Examples - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/example.html

**爬取时间:** 2025-09-09 13:15:59.033422

**深度:** 1

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/example.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/example.html)
[ View this page ](https://pyod.readthedocs.io/en/latest/_sources/example.rst.txt "View this page")
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Examples[¶](https://pyod.readthedocs.io/en/latest/example.html#examples "Link to this heading")
* * *
## Featured Tutorials[¶](https://pyod.readthedocs.io/en/latest/example.html#featured-tutorials "Link to this heading")
PyOD has been well acknowledged by the machine learning community with a few featured posts and tutorials.
**Analytics Vidhya** : [An Awesome Tutorial to Learn Outlier Detection in Python using PyOD Library](https://www.analyticsvidhya.com/blog/2019/02/outlier-detection-python-pyod/)
**KDnuggets** : [Intuitive Visualization of Outlier Detection Methods](https://www.kdnuggets.com/2019/02/outlier-detection-methods-cheat-sheet.html)
**Towards Data Science** : [Anomaly Detection for Dummies](https://towardsdatascience.com/anomaly-detection-for-dummies-15f148e559c1)
**awesome-machine-learning** : [General-Purpose Machine Learning](https://github.com/josephmisiti/awesome-machine-learning#python-general-purpose)
* * *
## kNN Example[¶](https://pyod.readthedocs.io/en/latest/example.html#knn-example "Link to this heading")
Full example: [knn_example.py](https://github.com/yzhao062/Pyod/blob/master/examples/knn_example.py)
  1. Import models
> ```
frompyod.models.knnimport KNN   # kNN detector

```

  2. Generate sample data with [`pyod.utils.data.generate_data()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.data.generate_data "pyod.utils.data.generate_data"):
> ```
contamination = 0.1  # percentage of outliers
n_train = 200  # number of training points
n_test = 100  # number of testing points

X_train, X_test, y_train, y_test = generate_data(
    n_train=n_train, n_test=n_test, contamination=contamination)

```

  3. Initialize a [`pyod.models.knn.KNN`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.knn.KNN "pyod.models.knn.KNN") detector, fit the model, and make the prediction.
> ```
# train kNN detector
clf_name = 'KNN'
clf = KNN()
clf.fit(X_train)

# get the prediction labels and outlier scores of the training data
y_train_pred = clf.labels_  # binary labels (0: inliers, 1: outliers)
y_train_scores = clf.decision_scores_  # raw outlier scores

# get the prediction on the test data
y_test_pred = clf.predict(X_test)  # outlier labels (0 or 1)
y_test_scores = clf.decision_function(X_test)  # outlier scores

# it is possible to get the prediction confidence as well
y_test_pred, y_test_pred_confidence = clf.predict(X_test, return_confidence=True)  # outlier labels (0 or 1) and confidence in the range of [0,1]

```

  4. Evaluate the prediction using ROC and Precision @ Rank n [`pyod.utils.data.evaluate_print()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.data.evaluate_print "pyod.utils.data.evaluate_print").
> ```
frompyod.utils.dataimport evaluate_print
# evaluate and print the results
print("\nOn Training Data:")
evaluate_print(clf_name, y_train, y_train_scores)
print("\nOn Test Data:")
evaluate_print(clf_name, y_test, y_test_scores)

```

  5. See sample outputs on both training and test data.
  6. Generate the visualizations by visualize function included in all examples.
> ```
visualize(clf_name, X_train, y_train, X_test, y_test, y_train_pred,
          y_test_pred, show_figure=True, save_figure=False)

```


![kNN demo](https://pyod.readthedocs.io/en/latest/_images/KNN.png)
* * *
## Model Combination Example[¶](https://pyod.readthedocs.io/en/latest/example.html#model-combination-example "Link to this heading")
Outlier detection often suffers from model instability due to its unsupervised nature. Thus, it is recommended to combine various detector outputs, e.g., by averaging, to improve its robustness. Detector combination is a subfield of outlier ensembles; refer [[BKalayciE18](https://pyod.readthedocs.io/en/latest/example.html#id26 "İlker Kalaycı and Tuncay Ercan. Anomaly detection in wireless sensor networks data by using histogram based outlier score method. In 2018 2nd International Symposium on Multidisciplinary Studies and Innovative Technologies \(ISMSIT\), 1–6. IEEE, 2018.")] for more information.
Four score combination mechanisms are shown in this demo:
  1. **Average** : average scores of all detectors.
  2. **maximization** : maximum score across all detectors.
  3. **Average of Maximum (AOM)** : divide base detectors into subgroups and take the maximum score for each subgroup. The final score is the average of all subgroup scores.
  4. **Maximum of Average (MOA)** : divide base detectors into subgroups and take the average score for each subgroup. The final score is the maximum of all subgroup scores.


“examples/comb_example.py” illustrates the API for combining the output of multiple base detectors ([comb_example.py](https://github.com/yzhao062/pyod/blob/master/examples/comb_example.py), [Jupyter Notebooks](https://mybinder.org/v2/gh/yzhao062/pyod/master)). For Jupyter Notebooks, please navigate to **“/notebooks/Model Combination.ipynb”**
  1. Import models and generate sample data.
> ```
frompyod.models.knnimport KNN  # kNN detector
frompyod.models.combinationimport aom, moa, average, maximization
frompyod.utils.dataimport generate_data

X, y= generate_data(train_only=True)  # load data

```

  2. Initialize 20 kNN outlier detectors with different k (10 to 200), and get the outlier scores.
> ```
# initialize 20 base detectors for combination
k_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140,
            150, 160, 170, 180, 190, 200]
n_clf = len(k_list) # Number of classifiers being trained

train_scores = np.zeros([X_train.shape[0], n_clf])
test_scores = np.zeros([X_test.shape[0], n_clf])

for i in range(n_clf):
    k = k_list[i]

    clf = KNN(n_neighbors=k, method='largest')
    clf.fit(X_train_norm)

    train_scores[:, i] = clf.decision_scores_
    test_scores[:, i] = clf.decision_function(X_test_norm)

```

  3. Then the output scores are standardized into zero average and unit std before combination. This step is crucial to adjust the detector outputs to the same scale.
> ```
frompyod.utils.utilityimport standardizer

# scores have to be normalized before combination
train_scores_norm, test_scores_norm = standardizer(train_scores, test_scores)

```

  4. Four different combination algorithms are applied as described above:
> ```
comb_by_average = average(test_scores_norm)
comb_by_maximization = maximization(test_scores_norm)
comb_by_aom = aom(test_scores_norm, 5) # 5 groups
comb_by_moa = moa(test_scores_norm, 5) # 5 groups

```

  5. Finally, all four combination methods are evaluated by ROC and Precision @ Rank n:
> ```
20
```



## Thresholding Example[¶](https://pyod.readthedocs.io/en/latest/example.html#thresholding-example "Link to this heading")
Full example: [threshold_example.py](https://github.com/yzhao062/Pyod/blob/master/examples/threshold_example.py)
  1. Import models
> ```
frompyod.models.knnimport KNN   # kNN detector
frompyod.models.thresholdsimport FILTER  # Filter thresholder

```

  2. Generate sample data with [`pyod.utils.data.generate_data()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.data.generate_data "pyod.utils.data.generate_data"):
> ```
contamination = 0.1  # percentage of outliers
n_train = 200  # number of training points
n_test = 100  # number of testing points

X_train, X_test, y_train, y_test = generate_data(
    n_train=n_train, n_test=n_test, contamination=contamination)

```

  3. Initialize a [`pyod.models.knn.KNN`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.knn.KNN "pyod.models.knn.KNN") detector, fit the model, and make the prediction.
> ```
# train kNN detector and apply FILTER thresholding
clf_name = 'KNN'
clf = KNN(contamination=FILTER())
clf.fit(X_train)

# get the prediction labels and outlier scores of the training data
y_train_pred = clf.labels_  # binary labels (0: inliers, 1: outliers)
y_train_scores = clf.decision_scores_  # raw outlier scores

```



References
[[BKalayciE18](https://pyod.readthedocs.io/en/latest/example.html#id1)]
İlker Kalaycı and Tuncay Ercan. Anomaly detection in wireless sensor networks data by using histogram based outlier score method. In _2018 2nd International Symposium on Multidisciplinary Studies and Innovative Technologies (ISMSIT)_ , 1–6. IEEE, 2018.
[ Next Benchmarks ](https://pyod.readthedocs.io/en/latest/benchmark.html) [ Previous Fast Train with SUOD ](https://pyod.readthedocs.io/en/latest/fast_train.html)
Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
On this page 
  * [Examples](https://pyod.readthedocs.io/en/latest/example.html)
    * [Featured Tutorials](https://pyod.readthedocs.io/en/latest/example.html#featured-tutorials)
    * [kNN Example](https://pyod.readthedocs.io/en/latest/example.html#knn-example)
    * [Model Combination Example](https://pyod.readthedocs.io/en/latest/example.html#model-combination-example)
    * [Thresholding Example](https://pyod.readthedocs.io/en/latest/example.html#thresholding-example)


