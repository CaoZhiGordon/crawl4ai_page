# Benchmarks - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/benchmark.html

**爬取时间:** 2025-09-09 13:16:07.870393

**深度:** 1

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/benchmark.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/benchmark.html)
[ View this page ](https://pyod.readthedocs.io/en/latest/_sources/benchmark.rst.txt "View this page")
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Benchmarks[¶](https://pyod.readthedocs.io/en/latest/benchmark.html#benchmarks "Link to this heading")
## Latest ADBench (2022)[¶](https://pyod.readthedocs.io/en/latest/benchmark.html#latest-adbench-2022 "Link to this heading")
We just released a 45-page, the most comprehensive [ADBench: Anomaly Detection Benchmark](https://arxiv.org/abs/2206.09426) [[#Han2022ADBench]_](https://pyod.readthedocs.io/en/latest/benchmark.html#id6). The fully [open-sourced ADBench](https://github.com/Minqi824/ADBench) compares 30 anomaly detection algorithms on 57 benchmark datasets.
The organization of **ADBench** is provided below:
[![benchmark-fig](https://github.com/Minqi824/ADBench/blob/main/figs/ADBench.png?raw=true) ](https://github.com/Minqi824/ADBench/blob/main/figs/ADBench.png?raw=true)
For a simpler visualization, we make **the comparison of selected models** via [compare_all_models.py](https://github.com/yzhao062/pyod/blob/master/examples/compare_all_models.py).
[![Comparison_of_All](https://github.com/yzhao062/pyod/blob/development/examples/ALL.png?raw=true) ](https://github.com/yzhao062/pyod/blob/development/examples/ALL.png?raw=true)
## Old Results (2019)[¶](https://pyod.readthedocs.io/en/latest/benchmark.html#old-results-2019 "Link to this heading")
A benchmark is supplied for select algorithms to provide an overview of the implemented models. In total, 17 benchmark datasets are used for comparison, which can be downloaded at [ODDS](http://odds.cs.stonybrook.edu/#table1).
For each dataset, it is first split into 60% for training and 40% for testing. All experiments are repeated 10 times independently with random splits. The mean of 10 trials is regarded as the final result. Three evaluation metrics are provided:
  * The area under receiver operating characteristic (ROC) curve
  * Precision @ rank n (P@N)
  * Execution time


You could replicate this process by running [benchmark.py](https://github.com/yzhao062/pyod/blob/master/notebooks/benchmark.py).
We also provide the hardware specification for reference.
Specification | Value  
---|---  
Platform | PC  
OS | Microsoft Windows 10 Enterprise  
CPU | Intel i7-6820HQ @ 2.70GHz  
RAM | 32GB  
Software | PyCharm 2018.02  
Python | Python 3.6.2  
Core | Single core (no parallelization)  
## ROC Performance[¶](https://pyod.readthedocs.io/en/latest/benchmark.html#roc-performance "Link to this heading")
ROC Performances (average of 10 independent trials)[¶](https://pyod.readthedocs.io/en/latest/benchmark.html#id2 "Link to this table") Data | #Samples | # Dimensions | Outlier Perc | ABOD | CBLOF | FB | HBOS | IForest | KNN | LOF | MCD | OCSVM | PCA  
---|---|---|---|---|---|---|---|---|---|---|---|---|---  
arrhythmia | 452 | 274 | 14.6018 | 0.7688 | 0.7835 | 0.7781 | 0.8219 | 0.8005 | 0.7861 | 0.7787 | 0.7790 | 0.7812 | 0.7815  
cardio | 1831 | 21 | 9.6122 | 0.5692 | 0.9276 | 0.5867 | 0.8351 | 0.9213 | 0.7236 | 0.5736 | 0.8135 | 0.9348 | 0.9504  
glass | 214 | 9 | 4.2056 | 0.7951 | 0.8504 | 0.8726 | 0.7389 | 0.7569 | 0.8508 | 0.8644 | 0.7901 | 0.6324 | 0.6747  
ionosphere | 351 | 33 | 35.8974 | 0.9248 | 0.8134 | 0.8730 | 0.5614 | 0.8499 | 0.9267 | 0.8753 | 0.9557 | 0.8419 | 0.7962  
letter | 1600 | 32 | 6.2500 | 0.8783 | 0.5070 | 0.8660 | 0.5927 | 0.6420 | 0.8766 | 0.8594 | 0.8074 | 0.6118 | 0.5283  
lympho | 148 | 18 | 4.0541 | 0.9110 | 0.9728 | 0.9753 | 0.9957 | 0.9941 | 0.9745 | 0.9771 | 0.9000 | 0.9759 | 0.9847  
mnist | 7603 | 100 | 9.2069 | 0.7815 | 0.8009 | 0.7205 | 0.5742 | 0.8159 | 0.8481 | 0.7161 | 0.8666 | 0.8529 | 0.8527  
musk | 3062 | 166 | 3.1679 | 0.1844 | 0.9879 | 0.5263 | 1.0000 | 0.9999 | 0.7986 | 0.5287 | 0.9998 | 1.0000 | 1.0000  
optdigits | 5216 | 64 | 2.8758 | 0.4667 | 0.5089 | 0.4434 | 0.8732 | 0.7253 | 0.3708 | 0.4500 | 0.3979 | 0.4997 | 0.5086  
pendigits | 6870 | 16 | 2.2707 | 0.6878 | 0.9486 | 0.4595 | 0.9238 | 0.9435 | 0.7486 | 0.4698 | 0.8344 | 0.9303 | 0.9352  
pima | 768 | 8 | 34.8958 | 0.6794 | 0.7348 | 0.6235 | 0.7000 | 0.6806 | 0.7078 | 0.6271 | 0.6753 | 0.6215 | 0.6481  
satellite | 6435 | 36 | 31.6395 | 0.5714 | 0.6693 | 0.5572 | 0.7581 | 0.7022 | 0.6836 | 0.5573 | 0.8030 | 0.6622 | 0.5988  
satimage-2 | 5803 | 36 | 1.2235 | 0.8190 | 0.9917 | 0.4570 | 0.9804 | 0.9947 | 0.9536 | 0.4577 | 0.9959 | 0.9978 | 0.9822  
shuttle | 49097 | 9 | 7.1511 | 0.6234 | 0.6272 | 0.4724 | 0.9855 | 0.9971 | 0.6537 | 0.5264 | 0.9903 | 0.9917 | 0.9898  
vertebral | 240 | 6 | 12.5000 | 0.4262 | 0.3486 | 0.4166 | 0.3263 | 0.3905 | 0.3817 | 0.4081 | 0.3906 | 0.4431 | 0.4027  
vowels | 1456 | 12 | 3.4341 | 0.9606 | 0.5856 | 0.9425 | 0.6727 | 0.7585 | 0.9680 | 0.9410 | 0.8076 | 0.7802 | 0.6027  
wbc | 378 | 30 | 5.5556 | 0.9047 | 0.9227 | 0.9325 | 0.9516 | 0.9310 | 0.9366 | 0.9349 | 0.9210 | 0.9319 | 0.9159  
## P@N Performance[¶](https://pyod.readthedocs.io/en/latest/benchmark.html#p-n-performance "Link to this heading")
Precision @ N Performances (average of 10 independent trials)[¶](https://pyod.readthedocs.io/en/latest/benchmark.html#id3 "Link to this table") Data | #Samples | # Dimensions | Outlier Perc | ABOD | CBLOF | FB | HBOS | IForest | KNN | LOF | MCD | OCSVM | PCA  
---|---|---|---|---|---|---|---|---|---|---|---|---|---  
arrhythmia | 452 | 274 | 14.6018 | 0.3808 | 0.4539 | 0.4230 | 0.5111 | 0.4961 | 0.4464 | 0.4334 | 0.3995 | 0.4614 | 0.4613  
cardio | 1831 | 21 | 9.6122 | 0.2374 | 0.5876 | 0.1690 | 0.4476 | 0.5041 | 0.3323 | 0.1541 | 0.4317 | 0.5011 | 0.6090  
glass | 214 | 9 | 4.2056 | 0.1702 | 0.0726 | 0.1476 | 0.0000 | 0.0726 | 0.0726 | 0.1476 | 0.0000 | 0.1726 | 0.0726  
ionosphere | 351 | 33 | 35.8974 | 0.8442 | 0.6088 | 0.7056 | 0.3295 | 0.6369 | 0.8602 | 0.7063 | 0.8806 | 0.7000 | 0.5729  
letter | 1600 | 32 | 6.2500 | 0.3801 | 0.0749 | 0.3642 | 0.0715 | 0.1003 | 0.3312 | 0.3641 | 0.1933 | 0.1510 | 0.0875  
lympho | 148 | 18 | 4.0541 | 0.4483 | 0.7517 | 0.7517 | 0.8467 | 0.9267 | 0.7517 | 0.7517 | 0.5183 | 0.7517 | 0.7517  
mnist | 7603 | 100 | 9.2069 | 0.3555 | 0.3348 | 0.3299 | 0.1188 | 0.3135 | 0.4204 | 0.3343 | 0.3462 | 0.3962 | 0.3846  
musk | 3062 | 166 | 3.1679 | 0.0507 | 0.7766 | 0.2230 | 0.9783 | 0.9680 | 0.2733 | 0.1695 | 0.9742 | 1.0000 | 0.9799  
optdigits | 5216 | 64 | 2.8758 | 0.0060 | 0.0000 | 0.0244 | 0.2194 | 0.0301 | 0.0000 | 0.0234 | 0.0000 | 0.0000 | 0.0000  
pendigits | 6870 | 16 | 2.2707 | 0.0812 | 0.2768 | 0.0658 | 0.2979 | 0.3422 | 0.0984 | 0.0653 | 0.0893 | 0.3287 | 0.3187  
pima | 768 | 8 | 34.8958 | 0.5193 | 0.5413 | 0.4480 | 0.5424 | 0.5111 | 0.5413 | 0.4555 | 0.4962 | 0.4704 | 0.4943  
satellite | 6435 | 36 | 31.6395 | 0.3902 | 0.4152 | 0.3902 | 0.5690 | 0.5676 | 0.4994 | 0.3893 | 0.6845 | 0.5346 | 0.4784  
satimage-2 | 5803 | 36 | 1.2235 | 0.2130 | 0.8846 | 0.0555 | 0.6939 | 0.8754 | 0.3809 | 0.0555 | 0.6481 | 0.9356 | 0.8041  
shuttle | 49097 | 9 | 7.1511 | 0.1977 | 0.2943 | 0.0695 | 0.9551 | 0.9546 | 0.2184 | 0.1424 | 0.7506 | 0.9542 | 0.9501  
vertebral | 240 | 6 | 12.5000 | 0.0601 | 0.0000 | 0.0644 | 0.0071 | 0.0343 | 0.0238 | 0.0506 | 0.0071 | 0.0238 | 0.0226  
vowels | 1456 | 12 | 3.4341 | 0.5710 | 0.0831 | 0.3224 | 0.1297 | 0.1875 | 0.5093 | 0.3551 | 0.2186 | 0.2791 | 0.1364  
wbc | 378 | 30 | 5.5556 | 0.3060 | 0.5055 | 0.5188 | 0.5817 | 0.5088 | 0.4952 | 0.5188 | 0.4577 | 0.5125 | 0.4767  
## Execution Time[¶](https://pyod.readthedocs.io/en/latest/benchmark.html#execution-time "Link to this heading")
Time Elapsed in Seconds (average of 10 independent trials)[¶](https://pyod.readthedocs.io/en/latest/benchmark.html#id4 "Link to this table") Data | #Samples | # Dimensions | Outlier Perc | ABOD | CBLOF | FB | HBOS | IForest | KNN | LOF | MCD | OCSVM | PCA  
---|---|---|---|---|---|---|---|---|---|---|---|---|---  
arrhythmia | 452 | 274 | 14.6018 | 0.3667 | 0.2123 | 0.5651 | 0.1383 | 0.2669 | 0.1075 | 0.0743 | 1.4165 | 0.0473 | 0.0596  
cardio | 1831 | 21 | 9.6122 | 0.3824 | 0.1255 | 0.7741 | 0.0053 | 0.2672 | 0.2249 | 0.0993 | 0.5418 | 0.0883 | 0.0035  
glass | 214 | 9 | 4.2056 | 0.0352 | 0.0359 | 0.0317 | 0.0022 | 0.1724 | 0.0173 | 0.0025 | 0.0325 | 0.0010 | 0.0011  
ionosphere | 351 | 33 | 35.8974 | 0.0645 | 0.0459 | 0.0728 | 0.0082 | 0.1864 | 0.0302 | 0.0070 | 0.0718 | 0.0048 | 0.0018  
letter | 1600 | 32 | 6.2500 | 0.3435 | 0.1014 | 0.7361 | 0.0080 | 0.2617 | 0.1882 | 0.0935 | 1.1942 | 0.0888 | 0.0041  
lympho | 148 | 18 | 4.0541 | 0.0277 | 0.0353 | 0.0266 | 0.0037 | 0.1712 | 0.0111 | 0.0021 | 0.0327 | 0.0014 | 0.0012  
mnist | 7603 | 100 | 9.2069 | 7.4192 | 1.1339 | 48.2750 | 0.0480 | 1.9314 | 7.3431 | 6.7901 | 4.7448 | 5.0203 | 0.1569  
musk | 3062 | 166 | 3.1679 | 2.3860 | 0.4134 | 13.8610 | 0.0587 | 1.2736 | 2.2057 | 1.9835 | 25.5501 | 1.3774 | 0.1637  
optdigits | 5216 | 64 | 2.8758 | 2.7279 | 0.4977 | 14.2399 | 0.0303 | 0.7783 | 2.1205 | 1.7799 | 1.8599 | 1.5618 | 0.0519  
pendigits | 6870 | 16 | 2.2707 | 1.4339 | 0.2847 | 3.8185 | 0.0090 | 0.5879 | 0.8659 | 0.5936 | 2.2209 | 0.9666 | 0.0062  
pima | 768 | 8 | 34.8958 | 0.1357 | 0.0698 | 0.0908 | 0.0019 | 0.1923 | 0.0590 | 0.0102 | 0.0474 | 0.0087 | 0.0013  
satellite | 6435 | 36 | 31.6395 | 1.7970 | 0.4269 | 7.5566 | 0.0161 | 0.6449 | 1.2578 | 0.9868 | 2.6916 | 1.3697 | 0.0245  
satimage-2 | 5803 | 36 | 1.2235 | 1.5209 | 0.3705 | 5.6561 | 0.0148 | 0.5529 | 1.0587 | 0.7525 | 2.3935 | 1.1114 | 0.0151  
shuttle | 49097 | 9 | 7.1511 | 14.3611 | 1.2524 | 59.2131 | 0.0953 | 3.3906 | 9.4958 | 11.1500 | 12.1449 | 44.6830 | 0.0378  
vertebral | 240 | 6 | 12.5000 | 0.0529 | 0.0444 | 0.0339 | 0.0014 | 0.1786 | 0.0161 | 0.0025 | 0.0446 | 0.0015 | 0.0010  
vowels | 1456 | 12 | 3.4341 | 0.3380 | 0.0889 | 0.3125 | 0.0044 | 0.2751 | 0.1125 | 0.0367 | 0.9745 | 0.0469 | 0.0023  
wbc | 378 | 30 | 5.5556 | 0.1014 | 0.0691 | 0.0771 | 0.0063 | 0.2030 | 0.0287 | 0.0078 | 0.0864 | 0.0062 | 0.0035  
[ Next API CheatSheet ](https://pyod.readthedocs.io/en/latest/api_cc.html) [ Previous Examples ](https://pyod.readthedocs.io/en/latest/example.html)
Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
On this page 
  * [Benchmarks](https://pyod.readthedocs.io/en/latest/benchmark.html)
    * [Latest ADBench (2022)](https://pyod.readthedocs.io/en/latest/benchmark.html#latest-adbench-2022)
    * [Old Results (2019)](https://pyod.readthedocs.io/en/latest/benchmark.html#old-results-2019)
    * [ROC Performance](https://pyod.readthedocs.io/en/latest/benchmark.html#roc-performance)
    * [P@N Performance](https://pyod.readthedocs.io/en/latest/benchmark.html#p-n-performance)
    * [Execution Time](https://pyod.readthedocs.io/en/latest/benchmark.html#execution-time)


