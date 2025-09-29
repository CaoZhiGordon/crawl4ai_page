# pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/index.html

**爬取时间:** 2025-09-09 13:15:52.010795

**深度:** 0

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/index.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/index.html)
[ View this page ](https://pyod.readthedocs.io/en/latest/_sources/index.rst.txt "View this page")
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Welcome to PyOD V2 documentation![¶](https://pyod.readthedocs.io/en/latest/index.html#welcome-to-pyod-v2-documentation "Link to this heading")
**Deployment & Documentation & Stats & License**
[![PyPI version](https://img.shields.io/pypi/v/pyod.svg?color=brightgreen) ](https://pypi.org/project/pyod/) [![Anaconda version](https://anaconda.org/conda-forge/pyod/badges/version.svg) ](https://anaconda.org/conda-forge/pyod) [![Documentation status](https://readthedocs.org/projects/pyod/badge/?version=latest) ](https://pyod.readthedocs.io/en/latest/?badge=latest) [![GitHub stars](https://img.shields.io/github/stars/yzhao062/pyod.svg) ](https://github.com/yzhao062/pyod/stargazers) [![GitHub forks](https://img.shields.io/github/forks/yzhao062/pyod.svg?color=blue) ](https://github.com/yzhao062/pyod/network) [![Downloads](https://pepy.tech/badge/pyod) ](https://pepy.tech/project/pyod) [![Testing](https://github.com/yzhao062/pyod/actions/workflows/testing.yml/badge.svg) ](https://github.com/yzhao062/pyod/actions/workflows/testing.yml) [![Coverage Status](https://coveralls.io/repos/github/yzhao062/pyod/badge.svg) ](https://coveralls.io/github/yzhao062/pyod) [![Maintainability](https://api.codeclimate.com/v1/badges/bdc3d8d0454274c753c4/maintainability) ](https://codeclimate.com/github/yzhao062/Pyod/maintainability) [![License](https://img.shields.io/github/license/yzhao062/pyod.svg) ](https://github.com/yzhao062/pyod/blob/master/LICENSE) [![Benchmark](https://img.shields.io/badge/ADBench-benchmark_results-pink) ](https://github.com/Minqi824/ADBench)
* * *
## Read Me First[¶](https://pyod.readthedocs.io/en/latest/index.html#read-me-first "Link to this heading")
Welcome to PyOD, a comprehensive but easy-to-use Python library for detecting anomalies in multivariate data. Whether you are working with a small-scale project or large datasets, PyOD provides a range of algorithms to suit your needs.
**PyOD Version 2 is now available** ([Paper](https://www.arxiv.org/abs/2412.12154)) [[ACQS+24](https://pyod.readthedocs.io/en/latest/index.html#id126 "Sihan Chen, Zhuangzhuang Qian, Wingchun Siu, Xingcan Hu, Jiaqi Li, Shawn Li, Yuehan Qin, Tiankai Yang, Zhuo Xiao, Wanghao Ye, and others. Pyod 2: a python library for outlier detection with llm-powered model selection. arXiv preprint arXiv:2412.12154, 2024.")], featuring:
  * **Expanded Deep Learning Support** : Integrates 12 modern neural models into a single PyTorch-based framework, bringing the total number of outlier detection methods to 45.
  * **Enhanced Performance and Ease of Use** : Models are optimized for efficiency and consistent performance across different datasets.
  * **LLM-based Model Selection** : Automated model selection guided by a large language model reduces manual tuning and assists users who may have limited experience with outlier detection.


**Additional Resources** :
  * **NLP Anomaly Detection** : [NLP-ADBench](https://github.com/USC-FORTIS/NLP-ADBench) provides both NLP anomaly detection datasets and algorithms [[ALLX+24](https://pyod.readthedocs.io/en/latest/index.html#id127 "Yuangang Li, Jiaqi Li, Zhuo Xiao, Tiankai Yang, Yi Nian, Xiyang Hu, and Yue Zhao. Nlp-adbench: nlp anomaly detection benchmark. arXiv preprint arXiv:2412.04784, 2024.")]
  * **Time-series Outlier Detection** : [TODS](https://github.com/datamllab/tods)
  * **Graph Outlier Detection** : [PyGOD](https://pygod.org/)
  * **Performance Comparison & Datasets**: We have a 45-page, comprehensive [anomaly detection benchmark paper](https://openreview.net/forum?id=foA_SFQ9zo0). The fully [open-sourced ADBench](https://github.com/Minqi824/ADBench) compares 30 anomaly detection algorithms on 57 benchmark datasets.
  * **PyOD on Distributed Systems** : You can also run [PyOD on Databricks](https://www.databricks.com/blog/2023/03/13/unsupervised-outlier-detection-databricks.html)
  * **Learn More** : [Anomaly Detection Resources](https://github.com/yzhao062/anomaly-detection-resources)


**Check out our latest research on LLM-based anomaly detection** [[AYNL+24](https://pyod.readthedocs.io/en/latest/index.html#id125 "Tiankai Yang, Yi Nian, Shawn Li, Ruiyao Xu, Yuangang Li, Jiaqi Li, Zhuo Xiao, Xiyang Hu, Ryan Rossi, Kaize Ding, and others. Ad-llm: benchmarking large language models for anomaly detection. arXiv preprint arXiv:2412.11142, 2024.")]: [AD-LLM: Benchmarking Large Language Models for Anomaly Detection](https://arxiv.org/abs/2412.11142).
* * *
## About PyOD[¶](https://pyod.readthedocs.io/en/latest/index.html#about-pyod "Link to this heading")
PyOD, established in 2017, has become a go-to **Python library** for **detecting anomalous/outlying objects** in multivariate data. This exciting yet challenging field is commonly referred to as [Outlier Detection](https://en.wikipedia.org/wiki/Anomaly_detection) or [Anomaly Detection](https://en.wikipedia.org/wiki/Anomaly_detection).
PyOD includes more than 50 detection algorithms, from classical LOF (SIGMOD 2000) to the cutting-edge ECOD and DIF (TKDE 2022 and 2023). Since 2017, PyOD has been successfully used in numerous academic research projects and commercial products with more than [26 million downloads](https://pepy.tech/project/pyod). It is also well acknowledged by the machine learning community with various dedicated posts/tutorials, including [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2019/02/outlier-detection-python-pyod/), [KDnuggets](https://www.kdnuggets.com/2019/02/outlier-detection-methods-cheat-sheet.html), and [Towards Data Science](https://towardsdatascience.com/anomaly-detection-for-dummies-15f148e559c1).
**PyOD is featured for** :
  * **Unified, User-Friendly Interface** across various algorithms.
  * **Wide Range of Models** , from classic techniques to the latest deep learning methods in **PyTorch**.
  * **High Performance & Efficiency**, leveraging [numba](https://github.com/numba/numba) and [joblib](https://github.com/joblib/joblib) for JIT compilation and parallel processing.
  * **Fast Training & Prediction**, achieved through the SUOD framework [[AZHC+21](https://pyod.readthedocs.io/en/latest/index.html#id105 "Yue Zhao, Xiyang Hu, Cheng Cheng, Cong Wang, Changlin Wan, Wen Wang, Jianing Yang, Haoping Bai, Zheng Li, Cao Xiao, Yunlong Wang, Zhi Qiao, Jimeng Sun, and Leman Akoglu. Suod: accelerating large-scale unsupervised heterogeneous outlier detection. Proceedings of Machine Learning and Systems, 2021.")].


**Outlier Detection with 5 Lines of Code** :
```
# Example: Training an ECOD detector
frompyod.models.ecodimport ECOD
clf = ECOD()
clf.fit(X_train)
y_train_scores = clf.decision_scores_  # Outlier scores for training data
y_test_scores = clf.decision_function(X_test)  # Outlier scores for test data

```

**Selecting the Right Algorithm:** Unsure where to start? Consider these robust and interpretable options:
  * [ECOD](https://github.com/yzhao062/pyod/blob/master/examples/ecod_example.py): Example of using ECOD for outlier detection
  * [Isolation Forest](https://github.com/yzhao062/pyod/blob/master/examples/iforest_example.py): Example of using Isolation Forest for outlier detection


Alternatively, explore [MetaOD](https://github.com/yzhao062/MetaOD) for a data-driven approach.
**Citing PyOD** :
If you use PyOD in a scientific publication, we would appreciate citations to the following paper(s):
[PyOD 2: A Python Library for Outlier Detection with LLM-powered Model Selection](https://arxiv.org/abs/2412.12154) is available as a preprint. If you use PyOD in a scientific publication, we would appreciate citations to the following paper:
```
@article{zhao2024pyod2,
    author  = {Chen, Sihan and Qian, Zhuangzhuang and Siu, Wingchun and Hu, Xingcan and Li, Jiaqi and Li, Shawn and Qin, Yuehan and Yang, Tiankai and Xiao, Zhuo and Ye, Wanghao and Zhang, Yichi and Dong, Yushun and Zhao, Yue},
    title   = {PyOD 2: A Python Library for Outlier Detection with LLM-powered Model Selection},
    journal = {arXiv preprint arXiv:2412.12154},
    year    = {2024}
}

```

[PyOD paper](http://www.jmlr.org/papers/volume20/19-011/19-011.pdf) is published in [Journal of Machine Learning Research (JMLR)](http://www.jmlr.org/) (MLOSS track).:
```
@article{zhao2019pyod,
    author  = {Zhao, Yue and Nasrullah, Zain and Li, Zheng},
    title   = {PyOD: A Python Toolbox for Scalable Outlier Detection},
    journal = {Journal of Machine Learning Research},
    year    = {2019},
    volume  = {20},
    number  = {96},
    pages   = {1-7},
    url     = {http://jmlr.org/papers/v20/19-011.html}
}

```

or:
```
Zhao, Y., Nasrullah, Z. and Li, Z., 2019. PyOD: A Python Toolbox for Scalable Outlier Detection. Journal of machine learning research (JMLR), 20(96), pp.1-7.

```

For a broader perspective on anomaly detection, see our NeurIPS papers [ADBench: Anomaly Detection Benchmark Paper](https://arxiv.org/abs/2206.09426) and [ADGym: Design Choices for Deep Anomaly Detection](https://arxiv.org/abs/2309.15376):
```
@article{han2022adbench,
    title={Adbench: Anomaly detection benchmark},
    author={Han, Songqiao and Hu, Xiyang and Huang, Hailiang and Jiang, Minqi and Zhao, Yue},
    journal={Advances in Neural Information Processing Systems},
    volume={35},
    pages={32142--32159},
    year={2022}
}

@article{jiang2023adgym,
    title={ADGym: Design Choices for Deep Anomaly Detection},
    author={Jiang, Minqi and Hou, Chaochuan and Zheng, Ao and Han, Songqiao and Huang, Hailiang and Wen, Qingsong and Hu, Xiyang and Zhao, Yue},
    journal={Advances in Neural Information Processing Systems},
    volume={36},
    year={2023}
}

```

* * *
## ADBench Benchmark and Datasets[¶](https://pyod.readthedocs.io/en/latest/index.html#adbench-benchmark-and-datasets "Link to this heading")
We just released a 45-page, the most comprehensive [ADBench: Anomaly Detection Benchmark](https://arxiv.org/abs/2206.09426) [[AHHH+22](https://pyod.readthedocs.io/en/latest/index.html#id116 "Songqiao Han, Xiyang Hu, Hailiang Huang, Mingqi Jiang, and Yue Zhao. Adbench: anomaly detection benchmark. arXiv preprint arXiv:2206.09426, 2022.")]. The fully [open-sourced ADBench](https://github.com/Minqi824/ADBench) compares 30 anomaly detection algorithms on 57 benchmark datasets.
The organization of **ADBench** is provided below:
[![benchmark-fig](https://github.com/Minqi824/ADBench/blob/main/figs/ADBench.png?raw=true) ](https://github.com/Minqi824/ADBench/blob/main/figs/ADBench.png?raw=true)
For a simpler visualization, we make **the comparison of selected models** via [compare_all_models.py](https://github.com/yzhao062/pyod/blob/master/examples/compare_all_models.py).
[![Comparison_of_All](https://github.com/yzhao062/pyod/blob/development/examples/ALL.png?raw=true) ](https://github.com/yzhao062/pyod/blob/development/examples/ALL.png?raw=true)
# Implemented Algorithms[¶](https://pyod.readthedocs.io/en/latest/index.html#implemented-algorithms "Link to this heading")
PyOD toolkit consists of three major functional groups:
**(i) Individual Detection Algorithms** :
Type | Abbr | Algorithm | Year | Class | Ref  
---|---|---|---|---|---  
Probabilistic | ECOD | Unsupervised Outlier Detection Using Empirical Cumulative Distribution Functions | 2022 | [`pyod.models.ecod.ECOD`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.ecod.ECOD "pyod.models.ecod.ECOD") | [[ALZH+22](https://pyod.readthedocs.io/en/latest/index.html#id109 "Zheng Li, Yue Zhao, Xiyang Hu, Nicola Botta, Cezar Ionescu, and H. George Chen. Ecod: unsupervised outlier detection using empirical cumulative distribution functions. IEEE Transactions on Knowledge and Data Engineering, 2022.")]  
Probabilistic | COPOD | COPOD: Copula-Based Outlier Detection | 2020 | [`pyod.models.copod.COPOD`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.copod.COPOD "pyod.models.copod.COPOD") | [[ALZB+20](https://pyod.readthedocs.io/en/latest/index.html#id103 "Zheng Li, Yue Zhao, Nicola Botta, Cezar Ionescu, and Xiyang Hu. COPOD: copula-based outlier detection. In IEEE International Conference on Data Mining \(ICDM\). IEEE, 2020.")]  
Probabilistic | ABOD | Angle-Based Outlier Detection | 2008 | [`pyod.models.abod.ABOD`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.abod.ABOD "pyod.models.abod.ABOD") | [[AKZ+08](https://pyod.readthedocs.io/en/latest/index.html#id73 "Hans-Peter Kriegel, Arthur Zimek, and others. Angle-based outlier detection in high-dimensional data. In Proceedings of the 14th ACM SIGKDD international conference on Knowledge discovery and data mining, 444–452. ACM, 2008.")]  
Probabilistic | FastABOD | Fast Angle-Based Outlier Detection using approximation | 2008 | [`pyod.models.abod.ABOD`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.abod.ABOD "pyod.models.abod.ABOD") | [[AKZ+08](https://pyod.readthedocs.io/en/latest/index.html#id73 "Hans-Peter Kriegel, Arthur Zimek, and others. Angle-based outlier detection in high-dimensional data. In Proceedings of the 14th ACM SIGKDD international conference on Knowledge discovery and data mining, 444–452. ACM, 2008.")]  
Probabilistic | MAD | Median Absolute Deviation (MAD) | 1993 | [`pyod.models.mad.MAD`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.mad.MAD "pyod.models.mad.MAD") | [[AIH93](https://pyod.readthedocs.io/en/latest/index.html#id102 "Boris Iglewicz and David Caster Hoaglin. How to detect and handle outliers. Volume 16. Asq Press, 1993.")]  
Probabilistic | SOS | Stochastic Outlier Selection | 2012 | [`pyod.models.sos.SOS`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.sos.SOS "pyod.models.sos.SOS") | [[AJHuszarPvdH12](https://pyod.readthedocs.io/en/latest/index.html#id84 "JHM Janssens, Ferenc Huszár, EO Postma, and HJ van den Herik. Stochastic outlier selection. Technical Report, Technical report TiCC TR 2012-001, Tilburg University, Tilburg Center for Cognition and Communication, Tilburg, The Netherlands, 2012.")]  
Probabilistic | QMCD | Quasi-Monte Carlo Discrepancy outlier detection | 2001 | [`pyod.models.qmcd.QMCD`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.qmcd.QMCD "pyod.models.qmcd.QMCD") | [[AFM01](https://pyod.readthedocs.io/en/latest/index.html#id120 "Kai-Tai Fang and Chang-Xing Ma. Wrap-around l2-discrepancy of random sampling, latin hypercube and uniform designs. Journal of complexity, 17\(4\):608–624, 2001.")]  
Probabilistic | KDE | Outlier Detection with Kernel Density Functions | 2007 | [`pyod.models.kde.KDE`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.kde.KDE "pyod.models.kde.KDE") | [[ALLP07](https://pyod.readthedocs.io/en/latest/index.html#id111 "Longin Jan Latecki, Aleksandar Lazarevic, and Dragoljub Pokrajac. Outlier detection with kernel density functions. In International Workshop on Machine Learning and Data Mining in Pattern Recognition, 61–75. Springer, 2007.")]  
Probabilistic | Sampling | Rapid distance-based outlier detection via sampling | 2013 | [`pyod.models.sampling.Sampling`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.sampling.Sampling "pyod.models.sampling.Sampling") | [[ASB13](https://pyod.readthedocs.io/en/latest/index.html#id112 "Mahito Sugiyama and Karsten Borgwardt. Rapid distance-based outlier detection via sampling. Advances in neural information processing systems, 2013.")]  
Probabilistic | GMM | Probabilistic Mixture Modeling for Outlier Analysis |  | [`pyod.models.gmm.GMM`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.gmm.GMM "pyod.models.gmm.GMM") | [[AAgg15](https://pyod.readthedocs.io/en/latest/index.html#id77 "Charu C Aggarwal. Outlier analysis. In Data mining, 75–79. Springer, 2015.")] [Ch.2]  
Linear Model | PCA | Principal Component Analysis (the sum of weighted projected distances to the eigenvector hyperplanes) | 2003 | [`pyod.models.pca.PCA`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.pca.PCA "pyod.models.pca.PCA") | [[ASCSC03](https://pyod.readthedocs.io/en/latest/index.html#id76 "Mei-Ling Shyu, Shu-Ching Chen, Kanoksri Sarinnapakorn, and LiWu Chang. A novel anomaly detection scheme based on principal component classifier. Technical Report, MIAMI UNIV CORAL GABLES FL DEPT OF ELECTRICAL AND COMPUTER ENGINEERING, 2003.")]  
Linear Model | KPCA | Kernel Principal Component Analysis | 2007 | [`pyod.models.kpca.KPCA`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.kpca.KPCA "pyod.models.kpca.KPCA") | [[AHof07](https://pyod.readthedocs.io/en/latest/index.html#id119 "Heiko Hoffmann. Kernel pca for novelty detection. Pattern recognition, 40\(3\):863–874, 2007.")]  
Linear Model | MCD | Minimum Covariance Determinant (use the mahalanobis distances as the outlier scores) | 1999 | [`pyod.models.mcd.MCD`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.mcd.MCD "pyod.models.mcd.MCD") | [[AHR04](https://pyod.readthedocs.io/en/latest/index.html#id81 "Johanna Hardin and David M Rocke. Outlier detection in the multiple cluster setting using the minimum covariance determinant estimator. Computational Statistics & Data Analysis, 44\(4\):625–638, 2004."), [ARD99](https://pyod.readthedocs.io/en/latest/index.html#id80 "Peter J Rousseeuw and Katrien Van Driessen. A fast algorithm for the minimum covariance determinant estimator. Technometrics, 41\(3\):212–223, 1999.")]  
Linear Model | CD | Use Cook’s distance for outlier detection | 1977 | [`pyod.models.cd.CD`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.cd.CD "pyod.models.cd.CD") | [[ACoo77](https://pyod.readthedocs.io/en/latest/index.html#id110 "R Dennis Cook. Detection of influential observation in linear regression. Technometrics, 19\(1\):15–18, 1977.")]  
Linear Model | OCSVM | One-Class Support Vector Machines | 2001 | [`pyod.models.ocsvm.OCSVM`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.ocsvm.OCSVM "pyod.models.ocsvm.OCSVM") | [[AScholkopfPST+01](https://pyod.readthedocs.io/en/latest/index.html#id91 "Bernhard Schölkopf, John C Platt, John Shawe-Taylor, Alex J Smola, and Robert C Williamson. Estimating the support of a high-dimensional distribution. Neural computation, 13\(7\):1443–1471, 2001.")]  
Linear Model | LMDD | Deviation-based Outlier Detection (LMDD) | 1996 | [`pyod.models.lmdd.LMDD`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.lmdd.LMDD "pyod.models.lmdd.LMDD") | [[AAAR96](https://pyod.readthedocs.io/en/latest/index.html#id98 "Andreas Arning, Rakesh Agrawal, and Prabhakar Raghavan. A linear method for deviation detection in large databases. In KDD, volume 1141, 972–981. 1996.")]  
Proximity-Based | LOF | Local Outlier Factor | 2000 | [`pyod.models.lof.LOF`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.lof.LOF "pyod.models.lof.LOF") | [[ABKNS00](https://pyod.readthedocs.io/en/latest/index.html#id78 "Markus M Breunig, Hans-Peter Kriegel, Raymond T Ng, and Jörg Sander. Lof: identifying density-based local outliers. In ACM sigmod record, volume 29, 93–104. ACM, 2000.")]  
Proximity-Based | COF | Connectivity-Based Outlier Factor | 2002 | [`pyod.models.cof.COF`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.cof.COF "pyod.models.cof.COF") | [[ATCFC02](https://pyod.readthedocs.io/en/latest/index.html#id92 "Jian Tang, Zhixiang Chen, Ada Wai-Chee Fu, and David W Cheung. Enhancing effectiveness of outlier detections for low density patterns. In Pacific-Asia Conference on Knowledge Discovery and Data Mining, 535–548. Springer, 2002.")]  
Proximity-Based | Incr. COF | Memory Efficient Connectivity-Based Outlier Factor (slower but reduce storage complexity) | 2002 | [`pyod.models.cof.COF`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.cof.COF "pyod.models.cof.COF") | [[ATCFC02](https://pyod.readthedocs.io/en/latest/index.html#id92 "Jian Tang, Zhixiang Chen, Ada Wai-Chee Fu, and David W Cheung. Enhancing effectiveness of outlier detections for low density patterns. In Pacific-Asia Conference on Knowledge Discovery and Data Mining, 535–548. Springer, 2002.")]  
Proximity-Based | CBLOF | Clustering-Based Local Outlier Factor | 2003 | [`pyod.models.cblof.CBLOF`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.cblof.CBLOF "pyod.models.cblof.CBLOF") | [[AHXD03](https://pyod.readthedocs.io/en/latest/index.html#id82 "Zengyou He, Xiaofei Xu, and Shengchun Deng. Discovering cluster-based local outliers. Pattern Recognition Letters, 24\(9-10\):1641–1650, 2003.")]  
Proximity-Based | LOCI | LOCI: Fast outlier detection using the local correlation integral | 2003 | [`pyod.models.loci.LOCI`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.loci.LOCI "pyod.models.loci.LOCI") | [[APKGF03](https://pyod.readthedocs.io/en/latest/index.html#id85 "Spiros Papadimitriou, Hiroyuki Kitagawa, Phillip B Gibbons, and Christos Faloutsos. Loci: fast outlier detection using the local correlation integral. In Data Engineering, 2003. Proceedings. 19th International Conference on, 315–326. IEEE, 2003.")]  
Proximity-Based | HBOS | Histogram-based Outlier Score | 2012 | [`pyod.models.hbos.HBOS`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.hbos.HBOS "pyod.models.hbos.HBOS") | [[AGD12](https://pyod.readthedocs.io/en/latest/index.html#id75 "Markus Goldstein and Andreas Dengel. Histogram-based outlier score \(hbos\): a fast unsupervised anomaly detection algorithm. KI-2012: Poster and Demo Track, pages 59–63, 2012.")]  
Proximity-Based | kNN | k Nearest Neighbors (use the distance to the kth nearest neighbor as the outlier score | 2000 | [`pyod.models.knn.KNN`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.knn.KNN "pyod.models.knn.KNN") | [[AAP02](https://pyod.readthedocs.io/en/latest/index.html#id72 "Fabrizio Angiulli and Clara Pizzuti. Fast outlier detection in high dimensional spaces. In European Conference on Principles of Data Mining and Knowledge Discovery, 15–27. Springer, 2002."), [ARRS00](https://pyod.readthedocs.io/en/latest/index.html#id71 "Sridhar Ramaswamy, Rajeev Rastogi, and Kyuseok Shim. Efficient algorithms for mining outliers from large data sets. In ACM Sigmod Record, volume 29, 427–438. ACM, 2000.")]  
Proximity-Based | AvgKNN | Average kNN (use the average distance to k nearest neighbors as the outlier score) | 2002 | [`pyod.models.knn.KNN`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.knn.KNN "pyod.models.knn.KNN") | [[AAP02](https://pyod.readthedocs.io/en/latest/index.html#id72 "Fabrizio Angiulli and Clara Pizzuti. Fast outlier detection in high dimensional spaces. In European Conference on Principles of Data Mining and Knowledge Discovery, 15–27. Springer, 2002."), [ARRS00](https://pyod.readthedocs.io/en/latest/index.html#id71 "Sridhar Ramaswamy, Rajeev Rastogi, and Kyuseok Shim. Efficient algorithms for mining outliers from large data sets. In ACM Sigmod Record, volume 29, 427–438. ACM, 2000.")]  
Proximity-Based | MedKNN | Median kNN (use the median distance to k nearest neighbors as the outlier score) | 2002 | [`pyod.models.knn.KNN`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.knn.KNN "pyod.models.knn.KNN") | [[AAP02](https://pyod.readthedocs.io/en/latest/index.html#id72 "Fabrizio Angiulli and Clara Pizzuti. Fast outlier detection in high dimensional spaces. In European Conference on Principles of Data Mining and Knowledge Discovery, 15–27. Springer, 2002."), [ARRS00](https://pyod.readthedocs.io/en/latest/index.html#id71 "Sridhar Ramaswamy, Rajeev Rastogi, and Kyuseok Shim. Efficient algorithms for mining outliers from large data sets. In ACM Sigmod Record, volume 29, 427–438. ACM, 2000.")]  
Proximity-Based | SOD | Subspace Outlier Detection | 2009 | [`pyod.models.sod.SOD`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.sod.SOD "pyod.models.sod.SOD") | [[AKKrogerSZ09](https://pyod.readthedocs.io/en/latest/index.html#id94 "Hans-Peter Kriegel, Peer Kröger, Erich Schubert, and Arthur Zimek. Outlier detection in axis-parallel subspaces of high dimensional data. In Pacific-Asia Conference on Knowledge Discovery and Data Mining, 831–838. Springer, 2009.")]  
Proximity-Based | ROD | Rotation-based Outlier Detection | 2020 | [`pyod.models.rod.ROD`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.rod.ROD "pyod.models.rod.ROD") | [[AABC20](https://pyod.readthedocs.io/en/latest/index.html#id104 "Yahya Almardeny, Noureddine Boujnah, and Frances Cleary. A novel outlier detection method for multivariate data. IEEE Transactions on Knowledge and Data Engineering, 2020.")]  
Outlier Ensembles | IForest | Isolation Forest | 2008 | [`pyod.models.iforest.IForest`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.iforest.IForest "pyod.models.iforest.IForest") | [[ALTZ08](https://pyod.readthedocs.io/en/latest/index.html#id67 "Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou. Isolation forest. In Data Mining, 2008. ICDM'08. Eighth IEEE International Conference on, 413–422. IEEE, 2008."), [ALTZ12](https://pyod.readthedocs.io/en/latest/index.html#id68 "Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou. Isolation-based anomaly detection. ACM Transactions on Knowledge Discovery from Data \(TKDD\), 6\(1\):3, 2012.")]  
Outlier Ensembles | INNE | Isolation-based Anomaly Detection Using Nearest-Neighbor Ensembles | 2018 | [`pyod.models.inne.INNE`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.inne.INNE "pyod.models.inne.INNE") | [[ABTA+18](https://pyod.readthedocs.io/en/latest/index.html#id113 "Tharindu R Bandaragoda, Kai Ming Ting, David Albrecht, Fei Tony Liu, Ye Zhu, and Jonathan R Wells. Isolation-based anomaly detection using nearest-neighbor ensembles. Computational Intelligence, 34\(4\):968–998, 2018.")]  
Outlier Ensembles | DIF | Deep Isolation Forest for Anomaly Detection | 2023 | [`pyod.models.dif.DIF`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.dif.DIF "pyod.models.dif.DIF") | [[AXPWW23](https://pyod.readthedocs.io/en/latest/index.html#id121 "Hongzuo Xu, Guansong Pang, Yijie Wang, and Yongjun Wang. Deep isolation forest for anomaly detection. IEEE Transactions on Knowledge and Data Engineering, \(\):1-14, 2023. doi:10.1109/TKDE.2023.3270293.")]  
Outlier Ensembles | FB | Feature Bagging | 2005 | [`pyod.models.feature_bagging.FeatureBagging`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.feature_bagging.FeatureBagging "pyod.models.feature_bagging.FeatureBagging") | [[ALK05](https://pyod.readthedocs.io/en/latest/index.html#id74 "Aleksandar Lazarevic and Vipin Kumar. Feature bagging for outlier detection. In Proceedings of the eleventh ACM SIGKDD international conference on Knowledge discovery in data mining, 157–166. ACM, 2005.")]  
Outlier Ensembles | LSCP | LSCP: Locally Selective Combination of Parallel Outlier Ensembles | 2019 | [`pyod.models.lscp.LSCP`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.lscp.LSCP "pyod.models.lscp.LSCP") | [[AZNHL19](https://pyod.readthedocs.io/en/latest/index.html#id86 "Yue Zhao, Zain Nasrullah, Maciej K Hryniewicki, and Zheng Li. LSCP: locally selective combination in parallel outlier ensembles. In Proceedings of the 2019 SIAM International Conference on Data Mining, SDM 2019, 585–593. Calgary, Canada, May 2019. SIAM. URL: https://doi.org/10.1137/1.9781611975673.66, doi:10.1137/1.9781611975673.66.")]  
Outlier Ensembles | XGBOD | Extreme Boosting Based Outlier Detection **(Supervised)** | 2018 | [`pyod.models.xgbod.XGBOD`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.xgbod.XGBOD "pyod.models.xgbod.XGBOD") | [[AZH18](https://pyod.readthedocs.io/en/latest/index.html#id79 "Yue Zhao and Maciej K Hryniewicki. Xgbod: improving supervised outlier detection with unsupervised representation learning. In International Joint Conference on Neural Networks \(IJCNN\). IEEE, 2018.")]  
Outlier Ensembles | LODA | Lightweight On-line Detector of Anomalies | 2016 | [`pyod.models.loda.LODA`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.loda.LODA "pyod.models.loda.LODA") | [[APevny16](https://pyod.readthedocs.io/en/latest/index.html#id100 "Tomáš Pevn\\`y. Loda: lightweight on-line detector of anomalies. Machine Learning, 102\(2\):275–304, 2016.")]  
Outlier Ensembles | SUOD | SUOD: Accelerating Large-scale Unsupervised Heterogeneous Outlier Detection **(Acceleration)** | 2021 | [`pyod.models.suod.SUOD`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.suod.SUOD "pyod.models.suod.SUOD") | [[AZHC+21](https://pyod.readthedocs.io/en/latest/index.html#id105 "Yue Zhao, Xiyang Hu, Cheng Cheng, Cong Wang, Changlin Wan, Wen Wang, Jianing Yang, Haoping Bai, Zheng Li, Cao Xiao, Yunlong Wang, Zhi Qiao, Jimeng Sun, and Leman Akoglu. Suod: accelerating large-scale unsupervised heterogeneous outlier detection. Proceedings of Machine Learning and Systems, 2021.")]  
Neural Networks | AutoEncoder | Fully connected AutoEncoder (use reconstruction error as the outlier score) | 2015 | [`pyod.models.auto_encoder.AutoEncoder`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.auto_encoder.AutoEncoder "pyod.models.auto_encoder.AutoEncoder") | [[AAgg15](https://pyod.readthedocs.io/en/latest/index.html#id77 "Charu C Aggarwal. Outlier analysis. In Data mining, 75–79. Springer, 2015.")] [Ch.3]  
Neural Networks | VAE | Variational AutoEncoder (use reconstruction error as the outlier score) | 2013 | [`pyod.models.vae.VAE`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.vae.VAE "pyod.models.vae.VAE") | [[AKW13](https://pyod.readthedocs.io/en/latest/index.html#id99 "Diederik P Kingma and Max Welling. Auto-encoding variational bayes. arXiv preprint arXiv:1312.6114, 2013.")]  
Neural Networks | Beta-VAE | Variational AutoEncoder (all customized loss term by varying gamma and capacity) | 2018 | [`pyod.models.vae.VAE`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.vae.VAE "pyod.models.vae.VAE") | [[ABHP+18](https://pyod.readthedocs.io/en/latest/index.html#id101 "Christopher P Burgess, Irina Higgins, Arka Pal, Loic Matthey, Nick Watters, Guillaume Desjardins, and Alexander Lerchner. Understanding disentangling in betvae. arXiv preprint arXiv:1804.03599, 2018.")]  
Neural Networks | SO_GAAL | Single-Objective Generative Adversarial Active Learning | 2019 | [`pyod.models.so_gaal.SO_GAAL`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.so_gaal.SO_GAAL "pyod.models.so_gaal.SO_GAAL") | [[ALLZ+19](https://pyod.readthedocs.io/en/latest/index.html#id87 "Yezheng Liu, Zhe Li, Chong Zhou, Yuanchun Jiang, Jianshan Sun, Meng Wang, and Xiangnan He. Generative adversarial active learning for unsupervised outlier detection. IEEE Transactions on Knowledge and Data Engineering, 2019.")]  
Neural Networks | MO_GAAL | Multiple-Objective Generative Adversarial Active Learning | 2019 | [`pyod.models.mo_gaal.MO_GAAL`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.mo_gaal.MO_GAAL "pyod.models.mo_gaal.MO_GAAL") | [[ALLZ+19](https://pyod.readthedocs.io/en/latest/index.html#id87 "Yezheng Liu, Zhe Li, Chong Zhou, Yuanchun Jiang, Jianshan Sun, Meng Wang, and Xiangnan He. Generative adversarial active learning for unsupervised outlier detection. IEEE Transactions on Knowledge and Data Engineering, 2019.")]  
Neural Networks | DeepSVDD | Deep One-Class Classification | 2018 | [`pyod.models.deep_svdd.DeepSVDD`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.deep_svdd.DeepSVDD "pyod.models.deep_svdd.DeepSVDD") | [[ARVG+18](https://pyod.readthedocs.io/en/latest/index.html#id106 "Lukas Ruff, Robert Vandermeulen, Nico Görnitz, Lucas Deecke, Shoaib Siddiqui, Alexander Binder, Emmanuel Müller, and Marius Kloft. Deep one-class classification. International conference on machine learning, 2018.")]  
Neural Networks | AnoGAN | Anomaly Detection with Generative Adversarial Networks | 2017 | [`pyod.models.anogan.AnoGAN`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.anogan.AnoGAN "pyod.models.anogan.AnoGAN") | [[ASSeebockW+17](https://pyod.readthedocs.io/en/latest/index.html#id114 "Thomas Schlegl, Philipp Seeböck, Sebastian M Waldstein, Ursula Schmidt-Erfurth, and Georg Langs. Unsupervised anomaly detection with generative adversarial networks to guide marker discovery. In International conference on information processing in medical imaging, 146–157. Springer, 2017.")]  
Neural Networks | ALAD | Adversarially learned anomaly detection | 2018 | [`pyod.models.alad.ALAD`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.alad.ALAD "pyod.models.alad.ALAD") | [[AZRF+18](https://pyod.readthedocs.io/en/latest/index.html#id118 "Houssam Zenati, Manon Romain, Chuan-Sheng Foo, Bruno Lecouat, and Vijay Chandrasekhar. Adversarially learned anomaly detection. In 2018 IEEE International conference on data mining \(ICDM\), 727–736. IEEE, 2018.")]  
Neural Networks | DevNet | Deep Anomaly Detection with Deviation Networks | 2019 | [`pyod.models.devnet.DevNet`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.devnet.DevNet "pyod.models.devnet.DevNet") | [[APSVDH19](https://pyod.readthedocs.io/en/latest/index.html#id123 "Guansong Pang, Chunhua Shen, and Anton Van Den Hengel. Deep anomaly detection with deviation networks. In Proceedings of the 25th ACM SIGKDD international conference on knowledge discovery & data mining, 353–362. 2019.")]  
Neural Networks | AE1SVM | Autoencoder-based One-class Support Vector Machine | 2019 | [`pyod.models.ae1svm.AE1SVM`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.ae1svm.AE1SVM "pyod.models.ae1svm.AE1SVM") | [[ANV19](https://pyod.readthedocs.io/en/latest/index.html#id122 "Minh-Nghia Nguyen and Ngo Anh Vien. Scalable and interpretable one-class svms with deep learning and random fourier features. In Machine Learning and Knowledge Discovery in Databases: European Conference, ECML PKDD 2018, Dublin, Ireland, September 10–14, 2018, Proceedings, Part I 18, 157–172. Springer, 2019.")]  
Graph-based | R-Graph | Outlier detection by R-graph | 2017 | [`pyod.models.rgraph.RGraph`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.rgraph.RGraph "pyod.models.rgraph.RGraph") | [[AYRV17](https://pyod.readthedocs.io/en/latest/index.html#id117 "Chong You, Daniel P Robinson, and René Vidal. Provable self-representation based outlier detection in a union of subspaces. In Proceedings of the IEEE conference on computer vision and pattern recognition, 3395–3404. 2017.")]  
Graph-based | LUNAR | LUNAR: Unifying Local Outlier Detection Methods via Graph Neural Networks | 2022 | [`pyod.models.lunar.LUNAR`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.lunar.LUNAR "pyod.models.lunar.LUNAR") | [[AGHNN22](https://pyod.readthedocs.io/en/latest/index.html#id115 "Adam Goodge, Bryan Hooi, See-Kiong Ng, and Wee Siong Ng. Lunar: unifying local outlier detection methods via graph neural networks. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 36, 6737–6745. 2022.")]  
**(ii) Outlier Ensembles & Outlier Detector Combination Frameworks**:
Type | Abbr | Algorithm | Year | Ref |   
---|---|---|---|---|---  
Outlier Ensembles |  | Feature Bagging | 2005 | [`pyod.models.feature_bagging.FeatureBagging`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.feature_bagging.FeatureBagging "pyod.models.feature_bagging.FeatureBagging") | [[ALK05](https://pyod.readthedocs.io/en/latest/index.html#id74 "Aleksandar Lazarevic and Vipin Kumar. Feature bagging for outlier detection. In Proceedings of the eleventh ACM SIGKDD international conference on Knowledge discovery in data mining, 157–166. ACM, 2005.")]  
Outlier Ensembles | LSCP | LSCP: Locally Selective Combination of Parallel Outlier Ensembles | 2019 | [`pyod.models.lscp.LSCP`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.lscp.LSCP "pyod.models.lscp.LSCP") | [[AZNHL19](https://pyod.readthedocs.io/en/latest/index.html#id86 "Yue Zhao, Zain Nasrullah, Maciej K Hryniewicki, and Zheng Li. LSCP: locally selective combination in parallel outlier ensembles. In Proceedings of the 2019 SIAM International Conference on Data Mining, SDM 2019, 585–593. Calgary, Canada, May 2019. SIAM. URL: https://doi.org/10.1137/1.9781611975673.66, doi:10.1137/1.9781611975673.66.")]  
Outlier Ensembles | XGBOD | Extreme Boosting Based Outlier Detection **(Supervised)** | 2018 | [`pyod.models.xgbod.XGBOD`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.xgbod.XGBOD "pyod.models.xgbod.XGBOD") | [[AZH18](https://pyod.readthedocs.io/en/latest/index.html#id79 "Yue Zhao and Maciej K Hryniewicki. Xgbod: improving supervised outlier detection with unsupervised representation learning. In International Joint Conference on Neural Networks \(IJCNN\). IEEE, 2018.")]  
Outlier Ensembles | LODA | Lightweight On-line Detector of Anomalies | 2016 | [`pyod.models.loda.LODA`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.loda.LODA "pyod.models.loda.LODA") | [[APevny16](https://pyod.readthedocs.io/en/latest/index.html#id100 "Tomáš Pevn\\`y. Loda: lightweight on-line detector of anomalies. Machine Learning, 102\(2\):275–304, 2016.")]  
Outlier Ensembles | SUOD | SUOD: Accelerating Large-scale Unsupervised Heterogeneous Outlier Detection **(Acceleration)** | 2021 | [`pyod.models.suod.SUOD`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.suod.SUOD "pyod.models.suod.SUOD") | [[AZHC+21](https://pyod.readthedocs.io/en/latest/index.html#id105 "Yue Zhao, Xiyang Hu, Cheng Cheng, Cong Wang, Changlin Wan, Wen Wang, Jianing Yang, Haoping Bai, Zheng Li, Cao Xiao, Yunlong Wang, Zhi Qiao, Jimeng Sun, and Leman Akoglu. Suod: accelerating large-scale unsupervised heterogeneous outlier detection. Proceedings of Machine Learning and Systems, 2021.")]  
Combination | Average | Simple combination by averaging the scores | 2015 | [`pyod.models.combination.average()`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.combination.average "pyod.models.combination.average") | [[AAS15](https://pyod.readthedocs.io/en/latest/index.html#id70 "Charu C Aggarwal and Saket Sathe. Theoretical foundations and algorithms for outlier ensembles. ACM SIGKDD Explorations Newsletter, 17\(1\):24–47, 2015.")]  
Combination | Weighted Average | Simple combination by averaging the scores with detector weights | 2015 | [`pyod.models.combination.average()`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.combination.average "pyod.models.combination.average") | [[AAS15](https://pyod.readthedocs.io/en/latest/index.html#id70 "Charu C Aggarwal and Saket Sathe. Theoretical foundations and algorithms for outlier ensembles. ACM SIGKDD Explorations Newsletter, 17\(1\):24–47, 2015.")]  
Combination | Maximization | Simple combination by taking the maximum scores | 2015 | [`pyod.models.combination.maximization()`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.combination.maximization "pyod.models.combination.maximization") | [[AAS15](https://pyod.readthedocs.io/en/latest/index.html#id70 "Charu C Aggarwal and Saket Sathe. Theoretical foundations and algorithms for outlier ensembles. ACM SIGKDD Explorations Newsletter, 17\(1\):24–47, 2015.")]  
Combination | AOM | Average of Maximum | 2015 | [`pyod.models.combination.aom()`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.combination.aom "pyod.models.combination.aom") | [[AAS15](https://pyod.readthedocs.io/en/latest/index.html#id70 "Charu C Aggarwal and Saket Sathe. Theoretical foundations and algorithms for outlier ensembles. ACM SIGKDD Explorations Newsletter, 17\(1\):24–47, 2015.")]  
Combination | MOA | Maximum of Average | 2015 | [`pyod.models.combination.moa()`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.combination.moa "pyod.models.combination.moa") | [[AAS15](https://pyod.readthedocs.io/en/latest/index.html#id70 "Charu C Aggarwal and Saket Sathe. Theoretical foundations and algorithms for outlier ensembles. ACM SIGKDD Explorations Newsletter, 17\(1\):24–47, 2015.")]  
Combination | Median | Simple combination by taking the median of the scores | 2015 | [`pyod.models.combination.median()`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.combination.median "pyod.models.combination.median") | [[AAS15](https://pyod.readthedocs.io/en/latest/index.html#id70 "Charu C Aggarwal and Saket Sathe. Theoretical foundations and algorithms for outlier ensembles. ACM SIGKDD Explorations Newsletter, 17\(1\):24–47, 2015.")]  
Combination | majority Vote | Simple combination by taking the majority vote of the labels (weights can be used) | 2015 | [`pyod.models.combination.majority_vote()`](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.combination.majority_vote "pyod.models.combination.majority_vote") | [[AAS15](https://pyod.readthedocs.io/en/latest/index.html#id70 "Charu C Aggarwal and Saket Sathe. Theoretical foundations and algorithms for outlier ensembles. ACM SIGKDD Explorations Newsletter, 17\(1\):24–47, 2015.")]  
**(iii) Utility Functions** :
Type | Name | Function  
---|---|---  
Data | [`pyod.utils.data.generate_data()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.data.generate_data "pyod.utils.data.generate_data") | Synthesized data generation; normal data is generated by a multivariate Gaussian and outliers are generated by a uniform distribution  
Data | [`pyod.utils.data.generate_data_clusters()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.data.generate_data_clusters "pyod.utils.data.generate_data_clusters") | Synthesized data generation in clusters; more complex data patterns can be created with multiple clusters  
Stat | [`pyod.utils.stat_models.wpearsonr()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.stat_models.wpearsonr "pyod.utils.stat_models.wpearsonr") | Calculate the weighted Pearson correlation of two samples  
Utility | [`pyod.utils.utility.get_label_n()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.get_label_n "pyod.utils.utility.get_label_n") | Turn raw outlier scores into binary labels by assign 1 to top n outlier scores  
Utility | [`pyod.utils.utility.precision_n_scores()`](https://pyod.readthedocs.io/en/latest/pyod.utils.html#pyod.utils.utility.precision_n_scores "pyod.utils.utility.precision_n_scores") | calculate precision @ rank n  
# API Cheatsheet & Reference[¶](https://pyod.readthedocs.io/en/latest/index.html#api-cheatsheet-reference "Link to this heading")
The following APIs are applicable for all detector models for easy use.
  * [`pyod.models.base.BaseDetector.fit()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.fit "pyod.models.base.BaseDetector.fit"): Fit detector. y is ignored in unsupervised methods.
  * [`pyod.models.base.BaseDetector.decision_function()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.decision_function "pyod.models.base.BaseDetector.decision_function"): Predict raw anomaly score of X using the fitted detector.
  * [`pyod.models.base.BaseDetector.predict()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.predict "pyod.models.base.BaseDetector.predict"): Predict if a particular sample is an outlier or not using the fitted detector.
  * [`pyod.models.base.BaseDetector.predict_proba()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.predict_proba "pyod.models.base.BaseDetector.predict_proba"): Predict the probability of a sample being outlier using the fitted detector.
  * [`pyod.models.base.BaseDetector.predict_confidence()`](https://pyod.readthedocs.io/en/latest/api_cc.html#pyod.models.base.BaseDetector.predict_confidence "pyod.models.base.BaseDetector.predict_confidence"): Predict the model’s sample-wise confidence (available in predict and predict_proba).


Key Attributes of a fitted model:
  * `pyod.models.base.BaseDetector.decision_scores_`: The outlier scores of the training data. The higher, the more abnormal. Outliers tend to have higher scores.
  * `pyod.models.base.BaseDetector.labels_`: The binary labels of the training data. 0 stands for inliers and 1 for outliers/anomalies.


* * *
* * *
References
[AAgg15] ([1](https://pyod.readthedocs.io/en/latest/index.html#id16),[2](https://pyod.readthedocs.io/en/latest/index.html#id42))
Charu C Aggarwal. Outlier analysis. In _Data mining_ , 75–79. Springer, 2015.
[AAS15] ([1](https://pyod.readthedocs.io/en/latest/index.html#id59),[2](https://pyod.readthedocs.io/en/latest/index.html#id60),[3](https://pyod.readthedocs.io/en/latest/index.html#id61),[4](https://pyod.readthedocs.io/en/latest/index.html#id62),[5](https://pyod.readthedocs.io/en/latest/index.html#id63),[6](https://pyod.readthedocs.io/en/latest/index.html#id64),[7](https://pyod.readthedocs.io/en/latest/index.html#id65))
Charu C Aggarwal and Saket Sathe. Theoretical foundations and algorithms for outlier ensembles. _ACM SIGKDD Explorations Newsletter_ , 17(1):24–47, 2015.
[[AABC20](https://pyod.readthedocs.io/en/latest/index.html#id33)]
Yahya Almardeny, Noureddine Boujnah, and Frances Cleary. A novel outlier detection method for multivariate data. _IEEE Transactions on Knowledge and Data Engineering_ , 2020.
[AAP02] ([1](https://pyod.readthedocs.io/en/latest/index.html#id29),[2](https://pyod.readthedocs.io/en/latest/index.html#id30),[3](https://pyod.readthedocs.io/en/latest/index.html#id31))
Fabrizio Angiulli and Clara Pizzuti. Fast outlier detection in high dimensional spaces. In _European Conference on Principles of Data Mining and Knowledge Discovery_ , 15–27. Springer, 2002.
[[AAAR96](https://pyod.readthedocs.io/en/latest/index.html#id22)]
Andreas Arning, Rakesh Agrawal, and Prabhakar Raghavan. A linear method for deviation detection in large databases. In _KDD_ , volume 1141, 972–981. 1996.
[[ABTA+18](https://pyod.readthedocs.io/en/latest/index.html#id35)]
Tharindu R Bandaragoda, Kai Ming Ting, David Albrecht, Fei Tony Liu, Ye Zhu, and Jonathan R Wells. Isolation-based anomaly detection using nearest-neighbor ensembles. _Computational Intelligence_ , 34(4):968–998, 2018.
[[ABKNS00](https://pyod.readthedocs.io/en/latest/index.html#id23)]
Markus M Breunig, Hans-Peter Kriegel, Raymond T Ng, and Jörg Sander. Lof: identifying density-based local outliers. In _ACM sigmod record_ , volume 29, 93–104. ACM, 2000.
[[ABHP+18](https://pyod.readthedocs.io/en/latest/index.html#id44)]
Christopher P Burgess, Irina Higgins, Arka Pal, Loic Matthey, Nick Watters, Guillaume Desjardins, and Alexander Lerchner. Understanding disentangling in betvae. _arXiv preprint arXiv:1804.03599_ , 2018.
[[ACQS+24](https://pyod.readthedocs.io/en/latest/index.html#id1)]
Sihan Chen, Zhuangzhuang Qian, Wingchun Siu, Xingcan Hu, Jiaqi Li, Shawn Li, Yuehan Qin, Tiankai Yang, Zhuo Xiao, Wanghao Ye, and others. Pyod 2: a python library for outlier detection with llm-powered model selection. _arXiv preprint arXiv:2412.12154_ , 2024.
[[ACoo77](https://pyod.readthedocs.io/en/latest/index.html#id20)]
R Dennis Cook. Detection of influential observation in linear regression. _Technometrics_ , 19(1):15–18, 1977.
[[AFM01](https://pyod.readthedocs.io/en/latest/index.html#id13)]
Kai-Tai Fang and Chang-Xing Ma. Wrap-around l2-discrepancy of random sampling, latin hypercube and uniform designs. _Journal of complexity_ , 17(4):608–624, 2001.
[[AGD12](https://pyod.readthedocs.io/en/latest/index.html#id28)]
Markus Goldstein and Andreas Dengel. Histogram-based outlier score (hbos): a fast unsupervised anomaly detection algorithm. _KI-2012: Poster and Demo Track_ , pages 59–63, 2012.
[[AGHNN22](https://pyod.readthedocs.io/en/latest/index.html#id53)]
Adam Goodge, Bryan Hooi, See-Kiong Ng, and Wee Siong Ng. Lunar: unifying local outlier detection methods via graph neural networks. In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 36, 6737–6745. 2022.
[[AHHH+22](https://pyod.readthedocs.io/en/latest/index.html#id5)]
Songqiao Han, Xiyang Hu, Hailiang Huang, Mingqi Jiang, and Yue Zhao. Adbench: anomaly detection benchmark. _arXiv preprint arXiv:2206.09426_ , 2022.
[[AHR04](https://pyod.readthedocs.io/en/latest/index.html#id19)]
Johanna Hardin and David M Rocke. Outlier detection in the multiple cluster setting using the minimum covariance determinant estimator. _Computational Statistics & Data Analysis_, 44(4):625–638, 2004.
[[AHXD03](https://pyod.readthedocs.io/en/latest/index.html#id26)]
Zengyou He, Xiaofei Xu, and Shengchun Deng. Discovering cluster-based local outliers. _Pattern Recognition Letters_ , 24(9-10):1641–1650, 2003.
[[AHof07](https://pyod.readthedocs.io/en/latest/index.html#id18)]
Heiko Hoffmann. Kernel pca for novelty detection. _Pattern recognition_ , 40(3):863–874, 2007.
[[AIH93](https://pyod.readthedocs.io/en/latest/index.html#id11)]
Boris Iglewicz and David Caster Hoaglin. _How to detect and handle outliers_. Volume 16. Asq Press, 1993.
[[AJHuszarPvdH12](https://pyod.readthedocs.io/en/latest/index.html#id12)]
JHM Janssens, Ferenc Huszár, EO Postma, and HJ van den Herik. Stochastic outlier selection. Technical Report, Technical report TiCC TR 2012-001, Tilburg University, Tilburg Center for Cognition and Communication, Tilburg, The Netherlands, 2012.
[[AKW13](https://pyod.readthedocs.io/en/latest/index.html#id43)]
Diederik P Kingma and Max Welling. Auto-encoding variational bayes. _arXiv preprint arXiv:1312.6114_ , 2013.
[[AKKrogerSZ09](https://pyod.readthedocs.io/en/latest/index.html#id32)]
Hans-Peter Kriegel, Peer Kröger, Erich Schubert, and Arthur Zimek. Outlier detection in axis-parallel subspaces of high dimensional data. In _Pacific-Asia Conference on Knowledge Discovery and Data Mining_ , 831–838. Springer, 2009.
[AKZ+08] ([1](https://pyod.readthedocs.io/en/latest/index.html#id9),[2](https://pyod.readthedocs.io/en/latest/index.html#id10))
Hans-Peter Kriegel, Arthur Zimek, and others. Angle-based outlier detection in high-dimensional data. In _Proceedings of the 14th ACM SIGKDD international conference on Knowledge discovery and data mining_ , 444–452. ACM, 2008.
[[ALLP07](https://pyod.readthedocs.io/en/latest/index.html#id14)]
Longin Jan Latecki, Aleksandar Lazarevic, and Dragoljub Pokrajac. Outlier detection with kernel density functions. In _International Workshop on Machine Learning and Data Mining in Pattern Recognition_ , 61–75. Springer, 2007.
[ALK05] ([1](https://pyod.readthedocs.io/en/latest/index.html#id37),[2](https://pyod.readthedocs.io/en/latest/index.html#id54))
Aleksandar Lazarevic and Vipin Kumar. Feature bagging for outlier detection. In _Proceedings of the eleventh ACM SIGKDD international conference on Knowledge discovery in data mining_ , 157–166. ACM, 2005.
[[ALLX+24](https://pyod.readthedocs.io/en/latest/index.html#id2)]
Yuangang Li, Jiaqi Li, Zhuo Xiao, Tiankai Yang, Yi Nian, Xiyang Hu, and Yue Zhao. Nlp-adbench: nlp anomaly detection benchmark. _arXiv preprint arXiv:2412.04784_ , 2024.
[[ALZB+20](https://pyod.readthedocs.io/en/latest/index.html#id8)]
Zheng Li, Yue Zhao, Nicola Botta, Cezar Ionescu, and Xiyang Hu. COPOD: copula-based outlier detection. In _IEEE International Conference on Data Mining (ICDM)_. IEEE, 2020.
[[ALZH+22](https://pyod.readthedocs.io/en/latest/index.html#id7)]
Zheng Li, Yue Zhao, Xiyang Hu, Nicola Botta, Cezar Ionescu, and H. George Chen. Ecod: unsupervised outlier detection using empirical cumulative distribution functions. _IEEE Transactions on Knowledge and Data Engineering_ , 2022.
[[ALTZ08](https://pyod.readthedocs.io/en/latest/index.html#id34)]
Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou. Isolation forest. In _Data Mining, 2008. ICDM'08. Eighth IEEE International Conference on_ , 413–422. IEEE, 2008.
[[ALTZ12](https://pyod.readthedocs.io/en/latest/index.html#id34)]
Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou. Isolation-based anomaly detection. _ACM Transactions on Knowledge Discovery from Data (TKDD)_ , 6(1):3, 2012.
[ALLZ+19] ([1](https://pyod.readthedocs.io/en/latest/index.html#id45),[2](https://pyod.readthedocs.io/en/latest/index.html#id46))
Yezheng Liu, Zhe Li, Chong Zhou, Yuanchun Jiang, Jianshan Sun, Meng Wang, and Xiangnan He. Generative adversarial active learning for unsupervised outlier detection. _IEEE Transactions on Knowledge and Data Engineering_ , 2019.
[[ANV19](https://pyod.readthedocs.io/en/latest/index.html#id51)]
Minh-Nghia Nguyen and Ngo Anh Vien. Scalable and interpretable one-class svms with deep learning and random fourier features. In _Machine Learning and Knowledge Discovery in Databases: European Conference, ECML PKDD 2018, Dublin, Ireland, September 10–14, 2018, Proceedings, Part I 18_ , 157–172. Springer, 2019.
[[APSVDH19](https://pyod.readthedocs.io/en/latest/index.html#id50)]
Guansong Pang, Chunhua Shen, and Anton Van Den Hengel. Deep anomaly detection with deviation networks. In _Proceedings of the 25th ACM SIGKDD international conference on knowledge discovery & data mining_, 353–362. 2019.
[[APKGF03](https://pyod.readthedocs.io/en/latest/index.html#id27)]
Spiros Papadimitriou, Hiroyuki Kitagawa, Phillip B Gibbons, and Christos Faloutsos. Loci: fast outlier detection using the local correlation integral. In _Data Engineering, 2003. Proceedings. 19th International Conference on_ , 315–326. IEEE, 2003.
[APVD20]
Lorenzo Perini, Vincent Vercruyssen, and Jesse Davis. Quantifying the confidence of anomaly detectors in their example-wise predictions. In _Joint European Conference on Machine Learning and Knowledge Discovery in Databases_ , 227–243. Springer, 2020.
[APevny16] ([1](https://pyod.readthedocs.io/en/latest/index.html#id40),[2](https://pyod.readthedocs.io/en/latest/index.html#id57))
Tomáš Pevn\\`y. Loda: lightweight on-line detector of anomalies. _Machine Learning_ , 102(2):275–304, 2016.
[ARRS00] ([1](https://pyod.readthedocs.io/en/latest/index.html#id29),[2](https://pyod.readthedocs.io/en/latest/index.html#id30),[3](https://pyod.readthedocs.io/en/latest/index.html#id31))
Sridhar Ramaswamy, Rajeev Rastogi, and Kyuseok Shim. Efficient algorithms for mining outliers from large data sets. In _ACM Sigmod Record_ , volume 29, 427–438. ACM, 2000.
[[ARD99](https://pyod.readthedocs.io/en/latest/index.html#id19)]
Peter J Rousseeuw and Katrien Van Driessen. A fast algorithm for the minimum covariance determinant estimator. _Technometrics_ , 41(3):212–223, 1999.
[[ARVG+18](https://pyod.readthedocs.io/en/latest/index.html#id47)]
Lukas Ruff, Robert Vandermeulen, Nico Görnitz, Lucas Deecke, Shoaib Siddiqui, Alexander Binder, Emmanuel Müller, and Marius Kloft. Deep one-class classification. _International conference on machine learning_ , 2018.
[[ASSeebockW+17](https://pyod.readthedocs.io/en/latest/index.html#id48)]
Thomas Schlegl, Philipp Seeböck, Sebastian M Waldstein, Ursula Schmidt-Erfurth, and Georg Langs. Unsupervised anomaly detection with generative adversarial networks to guide marker discovery. In _International conference on information processing in medical imaging_ , 146–157. Springer, 2017.
[[AScholkopfPST+01](https://pyod.readthedocs.io/en/latest/index.html#id21)]
Bernhard Schölkopf, John C Platt, John Shawe-Taylor, Alex J Smola, and Robert C Williamson. Estimating the support of a high-dimensional distribution. _Neural computation_ , 13(7):1443–1471, 2001.
[[ASCSC03](https://pyod.readthedocs.io/en/latest/index.html#id17)]
Mei-Ling Shyu, Shu-Ching Chen, Kanoksri Sarinnapakorn, and LiWu Chang. A novel anomaly detection scheme based on principal component classifier. Technical Report, MIAMI UNIV CORAL GABLES FL DEPT OF ELECTRICAL AND COMPUTER ENGINEERING, 2003.
[[ASB13](https://pyod.readthedocs.io/en/latest/index.html#id15)]
Mahito Sugiyama and Karsten Borgwardt. Rapid distance-based outlier detection via sampling. _Advances in neural information processing systems_ , 2013.
[ATCFC02] ([1](https://pyod.readthedocs.io/en/latest/index.html#id24),[2](https://pyod.readthedocs.io/en/latest/index.html#id25))
Jian Tang, Zhixiang Chen, Ada Wai-Chee Fu, and David W Cheung. Enhancing effectiveness of outlier detections for low density patterns. In _Pacific-Asia Conference on Knowledge Discovery and Data Mining_ , 535–548. Springer, 2002.
[[AXPWW23](https://pyod.readthedocs.io/en/latest/index.html#id36)]
Hongzuo Xu, Guansong Pang, Yijie Wang, and Yongjun Wang. Deep isolation forest for anomaly detection. _IEEE Transactions on Knowledge and Data Engineering_ , ():1–14, 2023. [doi:10.1109/TKDE.2023.3270293](https://doi.org/10.1109/TKDE.2023.3270293).
[[AYNL+24](https://pyod.readthedocs.io/en/latest/index.html#id3)]
Tiankai Yang, Yi Nian, Shawn Li, Ruiyao Xu, Yuangang Li, Jiaqi Li, Zhuo Xiao, Xiyang Hu, Ryan Rossi, Kaize Ding, and others. Ad-llm: benchmarking large language models for anomaly detection. _arXiv preprint arXiv:2412.11142_ , 2024.
[[AYRV17](https://pyod.readthedocs.io/en/latest/index.html#id52)]
Chong You, Daniel P Robinson, and René Vidal. Provable self-representation based outlier detection in a union of subspaces. In _Proceedings of the IEEE conference on computer vision and pattern recognition_ , 3395–3404. 2017.
[[AZRF+18](https://pyod.readthedocs.io/en/latest/index.html#id49)]
Houssam Zenati, Manon Romain, Chuan-Sheng Foo, Bruno Lecouat, and Vijay Chandrasekhar. Adversarially learned anomaly detection. In _2018 IEEE International conference on data mining (ICDM)_ , 727–736. IEEE, 2018.
[AZH18] ([1](https://pyod.readthedocs.io/en/latest/index.html#id39),[2](https://pyod.readthedocs.io/en/latest/index.html#id56))
Yue Zhao and Maciej K Hryniewicki. Xgbod: improving supervised outlier detection with unsupervised representation learning. In _International Joint Conference on Neural Networks (IJCNN)_. IEEE, 2018.
[AZHC+21] ([1](https://pyod.readthedocs.io/en/latest/index.html#id4),[2](https://pyod.readthedocs.io/en/latest/index.html#id41),[3](https://pyod.readthedocs.io/en/latest/index.html#id58))
Yue Zhao, Xiyang Hu, Cheng Cheng, Cong Wang, Changlin Wan, Wen Wang, Jianing Yang, Haoping Bai, Zheng Li, Cao Xiao, Yunlong Wang, Zhi Qiao, Jimeng Sun, and Leman Akoglu. Suod: accelerating large-scale unsupervised heterogeneous outlier detection. _Proceedings of Machine Learning and Systems_ , 2021.
[AZNHL19] ([1](https://pyod.readthedocs.io/en/latest/index.html#id38),[2](https://pyod.readthedocs.io/en/latest/index.html#id55))
Yue Zhao, Zain Nasrullah, Maciej K Hryniewicki, and Zheng Li. LSCP: locally selective combination in parallel outlier ensembles. In _Proceedings of the 2019 SIAM International Conference on Data Mining, SDM 2019_ , 585–593. Calgary, Canada, May 2019. SIAM. URL: <https://doi.org/10.1137/1.9781611975673.66>, [doi:10.1137/1.9781611975673.66](https://doi.org/10.1137/1.9781611975673.66).
[ Next Installation ](https://pyod.readthedocs.io/en/latest/install.html)
Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
On this page 
  * [Welcome to PyOD V2 documentation!](https://pyod.readthedocs.io/en/latest/index.html)
    * [Read Me First](https://pyod.readthedocs.io/en/latest/index.html#read-me-first)
    * [About PyOD](https://pyod.readthedocs.io/en/latest/index.html#about-pyod)
    * [ADBench Benchmark and Datasets](https://pyod.readthedocs.io/en/latest/index.html#adbench-benchmark-and-datasets)
  * [Implemented Algorithms](https://pyod.readthedocs.io/en/latest/index.html#implemented-algorithms)
  * [API Cheatsheet & Reference](https://pyod.readthedocs.io/en/latest/index.html#api-cheatsheet-reference)


