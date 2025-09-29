# Utility Functions - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/pyod.utils.html

**爬取时间:** 2025-09-09 13:15:59.282890

**深度:** 1

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/pyod.utils.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/pyod.utils.html)
[ View this page ](https://pyod.readthedocs.io/en/latest/_sources/pyod.utils.rst.txt "View this page")
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Utility Functions[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#utility-functions "Link to this heading")
## pyod.utils.data module[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#module-pyod.utils.data "Link to this heading")
Utility functions for manipulating data 

pyod.utils.data.check_consistent_shape(_X_train_ , _y_train_ , _X_test_ , _y_test_ , _y_train_pred_ , _y_test_pred_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/data.html#check_consistent_shape)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.data.check_consistent_shape "Link to this definition") 
    
Internal shape to check input data shapes are consistent.
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#parameters "Link to this heading") 

X_trainnumpy array of shape (n_samples, n_features) 
    
The training samples. 

y_trainlist or array of shape (n_samples,) 
    
The ground truth of training samples. 

X_testnumpy array of shape (n_samples, n_features) 
    
The test samples. 

y_testlist or array of shape (n_samples,) 
    
The ground truth of test samples. 

y_train_prednumpy array of shape (n_samples, n_features) 
    
The predicted binary labels of the training samples. 

y_test_prednumpy array of shape (n_samples, n_features) 
    
The predicted binary labels of the test samples.
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#returns "Link to this heading") 

X_trainnumpy array of shape (n_samples, n_features) 
    
The training samples. 

y_trainlist or array of shape (n_samples,) 
    
The ground truth of training samples. 

X_testnumpy array of shape (n_samples, n_features) 
    
The test samples. 

y_testlist or array of shape (n_samples,) 
    
The ground truth of test samples. 

y_train_prednumpy array of shape (n_samples, n_features) 
    
The predicted binary labels of the training samples. 

y_test_prednumpy array of shape (n_samples, n_features) 
    
The predicted binary labels of the test samples. 

pyod.utils.data.evaluate_print(_clf_name_ , _y_ , _y_pred_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/data.html#evaluate_print)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.data.evaluate_print "Link to this definition") 
    
Utility function for evaluating and printing the results for examples. Default metrics include ROC and Precision @ n
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id1 "Link to this heading") 

clf_namestr 
    
The name of the detector. 

ylist or numpy array of shape (n_samples,) 
    
The ground truth. Binary (0: inliers, 1: outliers). 

y_predlist or numpy array of shape (n_samples,) 
    
The raw outlier scores as returned by a fitted model. 

pyod.utils.data.generate_data(_n_train =1000_, _n_test =500_, _n_features =2_, _contamination =0.1_, _train_only =False_, _offset =10_, _behaviour ='new'_, _random_state =None_, _n_nan =0_, _n_inf =0_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/data.html#generate_data)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.data.generate_data "Link to this definition") 
    
Utility function to generate synthesized data. Normal data is generated by a multivariate Gaussian distribution and outliers are generated by a uniform distribution. “X_train, X_test, y_train, y_test” are returned.
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id2 "Link to this heading") 

n_trainint, (default=1000) 
    
The number of training points to generate. 

n_testint, (default=500) 
    
The number of test points to generate. 

n_featuresint, optional (default=2) 
    
The number of features (dimensions). 

contaminationfloat in (0., 0.5), optional (default=0.1) 
    
The amount of contamination of the data set, i.e. the proportion of outliers in the data set. Used when fitting to define the threshold on the decision function. 

train_onlybool, optional (default=False) 
    
If true, generate train data only. 

offsetint, optional (default=10) 
    
Adjust the value range of Gaussian and Uniform. 

behaviourstr, default=’new’ 
    
Behaviour of the returned datasets which can be either ‘old’ or ‘new’. Passing `behaviour='new'` returns “X_train, X_test, y_train, y_test”, while passing `behaviour='old'` returns “X_train, y_train, X_test, y_test”. 

random_stateint, RandomState instance or None, optional (default=None) 
    
If int, random_state is the seed used by the random number generator; If RandomState instance, random_state is the random number generator; If None, the random number generator is the RandomState instance used by np.random. 

n_nanint 
    
The number of values that are missing (np.nan). Defaults to zero. 

n_infint 
    
The number of values that are infinite. (np.inf). Defaults to zero.
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id3 "Link to this heading") 

X_trainnumpy array of shape (n_train, n_features) 
    
Training data. 

X_testnumpy array of shape (n_test, n_features) 
    
Test data. 

y_trainnumpy array of shape (n_train,) 
    
Training ground truth. 

y_testnumpy array of shape (n_test,) 
    
Test ground truth. 

pyod.utils.data.generate_data_categorical(_n_train =1000_, _n_test =500_, _n_features =2_, _n_informative =2_, _n_category_in =2_, _n_category_out =2_, _contamination =0.1_, _shuffle =True_, _random_state =None_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/data.html#generate_data_categorical)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.data.generate_data_categorical "Link to this definition") 
    
Utility function to generate synthesized categorical data.
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id4 "Link to this heading") 

n_trainint, (default=1000) 
    
The number of training points to generate. 

n_testint, (default=500) 
    
The number of test points to generate. 

n_featuresint, optional (default=2) 
    
The number of features for each sample. 

n_informativeint in (1, n_features), optional (default=2) 
    
The number of informative features in the outlier points. The higher the easier the outlier detection should be. Note that n_informative should not be less than or equal n_features. 

n_category_inint in (1, n_inliers), optional (default=2) 
    
The number of categories in the inlier points. 

n_category_outint in (1, n_outliers), optional (default=2) 
    
The number of categories in the outlier points. 

contaminationfloat in (0., 0.5), optional (default=0.1) 
    
The amount of contamination of the data set, i.e. the proportion of outliers in the data set. 

shuffle: bool, optional(default=True)
    
If True, inliers will be shuffled which makes more noisy distribution. 

random_stateint, RandomState instance or None, optional (default=None) 
    
If int, random_state is the seed used by the random number generator; If RandomState instance, random_state is the random number generator; If None, the random number generator is the RandomState instance used by np.random.
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id5 "Link to this heading") 

X_trainnumpy array of shape (n_train, n_features) 
    
Training data. 

y_trainnumpy array of shape (n_train,) 
    
Training ground truth. 

X_testnumpy array of shape (n_test, n_features) 
    
Test data. 

y_testnumpy array of shape (n_test,) 
    
Test ground truth. 

pyod.utils.data.generate_data_clusters(_n_train =1000_, _n_test =500_, _n_clusters =2_, _n_features =2_, _contamination =0.1_, _size ='same'_, _density ='same'_, _dist =0.25_, _random_state =None_, _return_in_clusters =False_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/data.html#generate_data_clusters)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.data.generate_data_clusters "Link to this definition") 
     

Utility function to generate synthesized data in clusters.
    
Generated data can involve the low density pattern problem and global outliers which are considered as difficult tasks for outliers detection algorithms.
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id6 "Link to this heading") 

n_trainint, (default=1000) 
    
The number of training points to generate. 

n_testint, (default=500) 
    
The number of test points to generate. 

n_clustersint, optional (default=2) 
    
The number of centers (i.e. clusters) to generate. 

n_featuresint, optional (default=2) 
    
The number of features for each sample. 

contaminationfloat in (0., 0.5), optional (default=0.1) 
    
The amount of contamination of the data set, i.e. the proportion of outliers in the data set. 

sizestr, optional (default=’same’) 
    
Size of each cluster: ‘same’ generates clusters with same size, ‘different’ generate clusters with different sizes. 

densitystr, optional (default=’same’) 
    
Density of each cluster: ‘same’ generates clusters with same density, ‘different’ generate clusters with different densities. 

dist: float, optional (default=0.25)
    
Distance between clusters. Should be between 0. and 1.0 It is used to avoid clusters overlapping as much as possible. However, if number of samples and number of clusters are too high, it is unlikely to separate them fully even if `dist` set to 1.0 

random_stateint, RandomState instance or None, optional (default=None) 
    
If int, random_state is the seed used by the random number generator; If RandomState instance, random_state is the random number generator; If None, the random number generator is the RandomState instance used by np.random. 

return_in_clustersbool, optional (default=False) 
    
If True, the function returns x_train, y_train, x_test, y_test each as a list of numpy arrays where each index represents a cluster. If False, it returns x_train, y_train, x_test, y_test each as numpy array after joining the sequence of clusters arrays,
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id7 "Link to this heading") 

X_trainnumpy array of shape (n_train, n_features) 
    
Training data. 

y_trainnumpy array of shape (n_train,) 
    
Training ground truth. 

X_testnumpy array of shape (n_test, n_features) 
    
Test data. 

y_testnumpy array of shape (n_test,) 
    
Test ground truth. 

pyod.utils.data.get_outliers_inliers(_X_ , _y_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/data.html#get_outliers_inliers)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.data.get_outliers_inliers "Link to this definition") 
    
Internal method to separate inliers from outliers.
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id8 "Link to this heading") 

Xnumpy array of shape (n_samples, n_features) 
    
The input samples 

ylist or array of shape (n_samples,) 
    
The ground truth of input samples.
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id9 "Link to this heading") 

X_outliersnumpy array of shape (n_samples, n_features) 
    
Outliers. 

X_inliersnumpy array of shape (n_samples, n_features) 
    
Inliers.
## pyod.utils.example module[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#module-pyod.utils.example "Link to this heading")
Utility functions for running examples 

pyod.utils.example.data_visualize(_X_train_ , _y_train_ , _show_figure =True_, _save_figure =False_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/example.html#data_visualize)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.example.data_visualize "Link to this definition") 
    
Utility function for visualizing the synthetic samples generated by generate_data_cluster function.
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id10 "Link to this heading") 

X_trainnumpy array of shape (n_samples, n_features) 
    
The training samples. 

y_trainlist or array of shape (n_samples,) 
    
The ground truth of training samples. 

show_figurebool, optional (default=True) 
    
If set to True, show the figure. 

save_figurebool, optional (default=False) 
    
If set to True, save the figure to the local. 

pyod.utils.example.visualize(_clf_name_ , _X_train_ , _y_train_ , _X_test_ , _y_test_ , _y_train_pred_ , _y_test_pred_ , _show_figure =True_, _save_figure =False_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/example.html#visualize)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.example.visualize "Link to this definition") 
    
Utility function for visualizing the results in examples. Internal use only.
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id11 "Link to this heading") 

clf_namestr 
    
The name of the detector. 

X_trainnumpy array of shape (n_samples, n_features) 
    
The training samples. 

y_trainlist or array of shape (n_samples,) 
    
The ground truth of training samples. 

X_testnumpy array of shape (n_samples, n_features) 
    
The test samples. 

y_testlist or array of shape (n_samples,) 
    
The ground truth of test samples. 

y_train_prednumpy array of shape (n_samples, n_features) 
    
The predicted binary labels of the training samples. 

y_test_prednumpy array of shape (n_samples, n_features) 
    
The predicted binary labels of the test samples. 

show_figurebool, optional (default=True) 
    
If set to True, show the figure. 

save_figurebool, optional (default=False) 
    
If set to True, save the figure to the local.
## pyod.utils.stat_models module[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#module-pyod.utils.stat_models "Link to this heading")
A collection of statistical models 

pyod.utils.stat_models.column_ecdf(_matrix :ndarray_) → ndarray[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/stat_models.html#column_ecdf)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.stat_models.column_ecdf "Link to this definition") 
    
Utility function to compute the column wise empirical cumulative distribution of a 2D feature matrix, where the rows are samples and the columns are features per sample. The accumulation is done in the positive direction of the sample axis.
E.G. p(1) = 0.2, p(0) = 0.3, p(2) = 0.1, p(6) = 0.4 ECDF E(5) = p(x <= 5) ECDF E would be E(-1) = 0, E(0) = 0.3, E(1) = 0.5, E(2) = 0.6, E(3) = 0.6, E(4) = 0.6, E(5) = 0.6, E(6) = 1
Similar to and tested against: <https://www.statsmodels.org/stable/generated/statsmodels.distributions.empirical_distribution.ECDF.html>
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id12 "Link to this heading") 

pyod.utils.stat_models.ecdf_terminate_equals_inplace(_matrix :ndarray_, _probabilities :ndarray_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/stat_models.html#ecdf_terminate_equals_inplace)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.stat_models.ecdf_terminate_equals_inplace "Link to this definition") 
    
This is a helper function for computing the ecdf of an array. It has been outsourced from the original function in order to be able to use the njit compiler of numpy for increased speeds, as it unfortunately needs a loop over all rows and columns of a matrix. It acts in place on the probabilities’ matrix.
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id13 "Link to this heading")
matrix : a feature matrix where the rows are samples and each column is a feature !(expected to be sorted)! 

probabilitiesa probability matrix that will be used building the ecdf. It has values between 0 and 1 and 
    
is also sorted.
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id14 "Link to this heading") 

pyod.utils.stat_models.pairwise_distances_no_broadcast(_X_ , _Y_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/stat_models.html#pairwise_distances_no_broadcast)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.stat_models.pairwise_distances_no_broadcast "Link to this definition") 
    
Utility function to calculate row-wise euclidean distance of two matrix. Different from pair-wise calculation, this function would not broadcast.
For instance, X and Y are both (4,3) matrices, the function would return a distance vector with shape (4,), instead of (4,4).
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id15 "Link to this heading") 

Xarray of shape (n_samples, n_features) 
    
First input samples 

Yarray of shape (n_samples, n_features) 
    
Second input samples
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id16 "Link to this heading") 

distancearray of shape (n_samples,) 
    
Row-wise euclidean distance of X and Y 

pyod.utils.stat_models.pearsonr_mat(_mat_ , _w =None_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/stat_models.html#pearsonr_mat)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.stat_models.pearsonr_mat "Link to this definition") 
    
Utility function to calculate pearson matrix (row-wise).
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id17 "Link to this heading") 

matnumpy array of shape (n_samples, n_features) 
    
Input matrix. 

wnumpy array of shape (n_features,) 
    
Weights.
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id18 "Link to this heading") 

pear_matnumpy array of shape (n_samples, n_samples) 
    
Row-wise pearson score matrix. 

pyod.utils.stat_models.wpearsonr(_x_ , _y_ , _w =None_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/stat_models.html#wpearsonr)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.stat_models.wpearsonr "Link to this definition") 
    
Utility function to calculate the weighted Pearson correlation of two samples.
See <https://stats.stackexchange.com/questions/221246/such-thing-as-a-weighted-correlation> for more information
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id19 "Link to this heading") 

xarray, shape (n,) 
    
Input x. 

yarray, shape (n,) 
    
Input y. 

warray, shape (n,) 
    
Weights w.
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id20 "Link to this heading") 

scoresfloat in range of [-1,1] 
    
Weighted Pearson Correlation between x and y.
## pyod.utils.utility module[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#module-pyod.utils.utility "Link to this heading")
A set of utility functions to support outlier detection. 

pyod.utils.utility.argmaxn(_value_list_ , _n_ , _order ='desc'_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/utility.html#argmaxn)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.argmaxn "Link to this definition") 
    
Return the index of top n elements in the list if order is set to ‘desc’, otherwise return the index of n smallest ones.
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id21 "Link to this heading") 

value_listlist, array, numpy array of shape (n_samples,) 
    
A list containing all values. 

nint 
    
The number of elements to select. 

orderstr, optional (default=’desc’) 
    
The order to sort {‘desc’, ‘asc’}:
  * ‘desc’: descending
  * ‘asc’: ascending


### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id22 "Link to this heading") 

index_listnumpy array of shape (n,) 
    
The index of the top n elements. 

pyod.utils.utility.check_detector(_detector_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/utility.html#check_detector)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.check_detector "Link to this definition") 
    
Checks if fit and decision_function methods exist for given detector
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id23 "Link to this heading") 

detectorpyod.models 
    
Detector instance for which the check is performed. 

pyod.utils.utility.check_parameter(_param_ , _low =-2147483647_, _high =2147483647_, _param_name =''_, _include_left =False_, _include_right =False_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/utility.html#check_parameter)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.check_parameter "Link to this definition") 
    
Check if an input is within the defined range.
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id24 "Link to this heading") 

paramint, float 
    
The input parameter to check. 

lowint, float 
    
The lower bound of the range. 

highint, float 
    
The higher bound of the range. 

param_namestr, optional (default=’’) 
    
The name of the parameter. 

include_leftbool, optional (default=False) 
    
Whether includes the lower bound (lower bound <=). 

include_rightbool, optional (default=False) 
    
Whether includes the higher bound (<= higher bound).
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id25 "Link to this heading") 

within_rangebool or raise errors 
    
Whether the parameter is within the range of (low, high) 

pyod.utils.utility.generate_bagging_indices(_random_state_ , _bootstrap_features_ , _n_features_ , _min_features_ , _max_features_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/utility.html#generate_bagging_indices)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.generate_bagging_indices "Link to this definition") 
    
Randomly draw feature indices. Internal use only.
Modified from sklearn/ensemble/bagging.py
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id26 "Link to this heading") 

random_stateRandomState 
    
A random number generator instance to define the state of the random permutations generator. 

bootstrap_featuresbool 
    
Specifies whether to bootstrap indice generation 

n_featuresint 
    
Specifies the population size when generating indices 

min_featuresint 
    
Lower limit for number of features to randomly sample 

max_featuresint 
    
Upper limit for number of features to randomly sample
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id27 "Link to this heading") 

feature_indicesnumpy array, shape (n_samples,) 
    
Indices for features to bag 

pyod.utils.utility.generate_indices(_random_state_ , _bootstrap_ , _n_population_ , _n_samples_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/utility.html#generate_indices)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.generate_indices "Link to this definition") 
    
Draw randomly sampled indices. Internal use only.
See sklearn/ensemble/bagging.py
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id28 "Link to this heading") 

random_stateRandomState 
    
A random number generator instance to define the state of the random permutations generator. 

bootstrapbool 
    
Specifies whether to bootstrap indice generation 

n_populationint 
    
Specifies the population size when generating indices 

n_samplesint 
    
Specifies number of samples to draw
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id29 "Link to this heading") 

indicesnumpy array, shape (n_samples,) 
    
randomly drawn indices 

pyod.utils.utility.get_diff_elements(_li1_ , _li2_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/utility.html#get_diff_elements)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.get_diff_elements "Link to this definition") 
    
get the elements in li1 but not li2, and vice versa
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id30 "Link to this heading") 

li1list or numpy array 
    
Input list 1. 

li2list or numpy array 
    
Input list 2.
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id31 "Link to this heading") 

differencelist 
    
The difference between li1 and li2. 

pyod.utils.utility.get_intersection(_lst1_ , _lst2_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/utility.html#get_intersection)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.get_intersection "Link to this definition") 
    
get the overlapping between two lists
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id32 "Link to this heading") 

li1list or numpy array 
    
Input list 1. 

li2list or numpy array 
    
Input list 2.
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id33 "Link to this heading") 

differencelist 
    
The overlapping between li1 and li2. 

pyod.utils.utility.get_label_n(_y_ , _y_pred_ , _n =None_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/utility.html#get_label_n)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.get_label_n "Link to this definition") 
    
Function to turn raw outlier scores into binary labels by assign 1 to top n outlier scores.
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id34 "Link to this heading") 

ylist or numpy array of shape (n_samples,) 
    
The ground truth. Binary (0: inliers, 1: outliers). 

y_predlist or numpy array of shape (n_samples,) 
    
The raw outlier scores as returned by a fitted model. 

nint, optional (default=None) 
    
The number of outliers. if not defined, infer using ground truth.
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id35 "Link to this heading") 

labelsnumpy array of shape (n_samples,) 
    
binary labels 0: normal points and 1: outliers
### Examples[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#examples "Link to this heading")
```
>>> frompyod.utils.utilityimport get_label_n
>>> y = [0, 1, 1, 0, 0]
>>> y_pred = [0.1, 0.5, 0.3, 0.2, 0.7]
>>> get_label_n(y, y_pred)
array([0, 1, 0, 0, 1])

```


pyod.utils.utility.get_list_diff(_li1_ , _li2_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/utility.html#get_list_diff)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.get_list_diff "Link to this definition") 
    
get the elements in li1 but not li2. li1-li2
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id36 "Link to this heading") 

li1list or numpy array 
    
Input list 1. 

li2list or numpy array 
    
Input list 2.
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id37 "Link to this heading") 

differencelist 
    
The difference between li1 and li2. 

pyod.utils.utility.get_optimal_n_bins(_X_ , _upper_bound =None_, _epsilon =1_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/utility.html#get_optimal_n_bins)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.get_optimal_n_bins "Link to this definition") 
    
Determine optimal number of bins for a histogram using the Birge Rozenblac method (see [[BBirgeR06](https://pyod.readthedocs.io/en/latest/pyod.models.html#id1152 "Lucien Birgé and Yves Rozenholc. How many bins should be put in a regular histogram. ESAIM: Probability and Statistics, 10:24–45, 2006.")] for details.)
See <https://doi.org/10.1051/ps:2006001>
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id39 "Link to this heading") 

Xarray-like of shape (n_samples, n_features)  
    
The samples to determine the optimal number of bins for. 

upper_boundint, default=None  
    
The maximum value of n_bins to be considered. If set to None, np.sqrt(X.shape[0]) will be used as upper bound. 

epsilonfloat, default = 1  
    
A stabilizing term added to the logarithm to prevent division by zero.
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id40 "Link to this heading") 

optimal_n_binsint  
    
The optimal value of n_bins according to the Birge Rozenblac method 

pyod.utils.utility.invert_order(_scores_ , _method ='multiplication'_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/utility.html#invert_order)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.invert_order "Link to this definition") 
    
Invert the order of a list of values. The smallest value becomes the largest in the inverted list. This is useful while combining multiple detectors since their score order could be different.
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id41 "Link to this heading") 

scoreslist, array or numpy array with shape (n_samples,) 
    
The list of values to be inverted 

methodstr, optional (default=’multiplication’) 
    
Methods used for order inversion. Valid methods are:
  * ‘multiplication’: multiply by -1
  * ‘subtraction’: max(scores) - scores


### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id42 "Link to this heading") 

inverted_scoresnumpy array of shape (n_samples,) 
    
The inverted list
### Examples[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id43 "Link to this heading")
```
>>> scores1 = [0.1, 0.3, 0.5, 0.7, 0.2, 0.1]
>>> invert_order(scores1)
array([-0.1, -0.3, -0.5, -0.7, -0.2, -0.1])
>>> invert_order(scores1, method='subtraction')
array([0.6, 0.4, 0.2, 0. , 0.5, 0.6])

```


pyod.utils.utility.precision_n_scores(_y_ , _y_pred_ , _n =None_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/utility.html#precision_n_scores)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.precision_n_scores "Link to this definition") 
    
Utility function to calculate precision @ rank n.
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id44 "Link to this heading") 

ylist or numpy array of shape (n_samples,) 
    
The ground truth. Binary (0: inliers, 1: outliers). 

y_predlist or numpy array of shape (n_samples,) 
    
The raw outlier scores as returned by a fitted model. 

nint, optional (default=None) 
    
The number of outliers. if not defined, infer using ground truth.
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id45 "Link to this heading") 

precision_at_rank_nfloat 
    
Precision at rank n score. 

pyod.utils.utility.score_to_label(_pred_scores_ , _outliers_fraction =0.1_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/utility.html#score_to_label)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.score_to_label "Link to this definition") 
    
Turn raw outlier outlier scores to binary labels (0 or 1).
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id46 "Link to this heading") 

pred_scoreslist or numpy array of shape (n_samples,) 
    
Raw outlier scores. Outliers are assumed have larger values. 

outliers_fractionfloat in (0,1) 
    
Percentage of outliers.
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id47 "Link to this heading") 

outlier_labelsnumpy array of shape (n_samples,) 
    
For each observation, tells whether or not it should be considered as an outlier according to the fitted model. Return the outlier probability, ranging in [0,1]. 

pyod.utils.utility.standardizer(_X_ , _X_t =None_, _keep_scalar =False_)[[source]](https://pyod.readthedocs.io/en/latest/_modules/pyod/utils/utility.html#standardizer)[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.standardizer "Link to this definition") 
    
Conduct Z-normalization on data to turn input samples become zero-mean and unit variance.
### Parameters[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id48 "Link to this heading") 

Xnumpy array of shape (n_samples, n_features) 
    
The training samples 

X_tnumpy array of shape (n_samples_new, n_features), optional (default=None) 
    
The data to be converted 

keep_scalarbool, optional (default=False) 
    
The flag to indicate whether to return the scalar
### Returns[¶](https://pyod.readthedocs.io/en/latest/pyod.utils.html#id49 "Link to this heading") 

X_normnumpy array of shape (n_samples, n_features) 
    
X after the Z-score normalization 

X_t_normnumpy array of shape (n_samples, n_features) 
    
X_t after the Z-score normalization 

scalarsklearn scalar object 
    
The scalar used in conversion
[ Next Known Issues & Warnings ](https://pyod.readthedocs.io/en/latest/issues.html) [ Previous All Models ](https://pyod.readthedocs.io/en/latest/pyod.models.html)
Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
On this page 
  * [Utility Functions](https://pyod.readthedocs.io/en/latest/pyod.utils.html)
    * [pyod.utils.data module](https://pyod.readthedocs.io/en/latest/pyod.utils.html#module-pyod.utils.data)
      * [`check_consistent_shape()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.data.check_consistent_shape)
      * [`evaluate_print()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.data.evaluate_print)
      * [`generate_data()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.data.generate_data)
      * [`generate_data_categorical()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.data.generate_data_categorical)
      * [`generate_data_clusters()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.data.generate_data_clusters)
      * [`get_outliers_inliers()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.data.get_outliers_inliers)
    * [pyod.utils.example module](https://pyod.readthedocs.io/en/latest/pyod.utils.html#module-pyod.utils.example)
      * [`data_visualize()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.example.data_visualize)
      * [`visualize()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.example.visualize)
    * [pyod.utils.stat_models module](https://pyod.readthedocs.io/en/latest/pyod.utils.html#module-pyod.utils.stat_models)
      * [`column_ecdf()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.stat_models.column_ecdf)
      * [`ecdf_terminate_equals_inplace()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.stat_models.ecdf_terminate_equals_inplace)
      * [`pairwise_distances_no_broadcast()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.stat_models.pairwise_distances_no_broadcast)
      * [`pearsonr_mat()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.stat_models.pearsonr_mat)
      * [`wpearsonr()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.stat_models.wpearsonr)
    * [pyod.utils.utility module](https://pyod.readthedocs.io/en/latest/pyod.utils.html#module-pyod.utils.utility)
      * [`argmaxn()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.argmaxn)
      * [`check_detector()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.check_detector)
      * [`check_parameter()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.check_parameter)
      * [`generate_bagging_indices()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.generate_bagging_indices)
      * [`generate_indices()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.generate_indices)
      * [`get_diff_elements()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.get_diff_elements)
      * [`get_intersection()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.get_intersection)
      * [`get_label_n()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.get_label_n)
      * [`get_list_diff()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.get_list_diff)
      * [`get_optimal_n_bins()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.get_optimal_n_bins)
      * [`invert_order()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.invert_order)
      * [`precision_n_scores()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.precision_n_scores)
      * [`score_to_label()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.score_to_label)
      * [`standardizer()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.standardizer)


