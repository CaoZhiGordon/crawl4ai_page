# pyod.models.auto_encoder - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/_modules/pyod/models/auto_encoder.html

**爬取时间:** 2025-09-09 13:16:46.311175

**深度:** 2

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/auto_encoder.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/auto_encoder.html)
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Source code for pyod.models.auto_encoder
```
# -*- coding: utf-8 -*-
"""Using AutoEncoder with Outlier Detection
"""
# Author: Tiankai Yang <tiankaiy@usc.edu>
# License: BSD 2 clause


try:
    importtorch
except ImportError:
    print('please install torch first')

fromtorchimport nn

frompyod.models.base_dlimport BaseDeepLearningDetector
frompyod.utils.stat_modelsimport pairwise_distances_no_broadcast
frompyod.utils.torch_utilityimport LinearBlock




[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.auto_encoder.AutoEncoder)
classAutoEncoder(BaseDeepLearningDetector):
"""
    Auto Encoder (AE) is a type of neural networks for learning useful data
    representations in an unsupervised manner. Similar to PCA, AE could be used
    to detect outlying objects in the data by calculating the reconstruction
    errors. See :cite:`aggarwal2015outlier` Chapter 3 for details.

    Parameters
    ----------
    contamination : float in (0., 0.5), optional (default=0.1)
        The amount of contamination of the data set, 
        i.e. the proportion of outliers in the data set. 
        Used when fitting to define the threshold on the decision function.

    preprocessing : bool, optional (default=True)
        If True, apply the preprocessing procedure before training models.

    lr : float, optional (default=1e-3)
        The initial learning rate for the optimizer.

    epoch_num : int, optional (default=10)
        The number of epochs for training.

    batch_size : int, optional (default=32)
        The batch size for training.

    optimizer_name : str, optional (default='adam')
        The name of theoptimizer used to train the model.

    device : str, optional (default=None)
        The device to use for the model. If None, it will be decided
        automatically. If you want to use MPS, set it to 'mps'.

    random_state : int, optional (default=42)
        The random seed for reproducibility.

    use_compile : bool, optional (default=False)
        Whether to compile the model.
        If True, the model will be compiled before training.
        This is only available for
        PyTorch version >= 2.0.0. and Python < 3.12.

    compile_mode : str, optional (default='default')
        The mode to compile the model.
        Can be either “default”, “reduce-overhead”,
        “max-autotune” or “max-autotune-no-cudagraphs”.
        See https://pytorch.org/docs/stable/generated/torch.compile.html#torch-compile for details.

    verbose : int, optional (default=1)
        Verbosity mode.
        - 0 = silent
        - 1 = progress bar
        - 2 = one line per epoch.

    optimizer_params : dict, optional (default={'weight_decay': 1e-5})
        Additional parameters for the optimizer.
        For example, `optimizer_params={'weight_decay': 1e-5}`.

    hidden_neuron_list : list, optional (default=[64, 32])
        The number of neurons per hidden layers. 
        So the network has the structure as [feature_size, 64, 32, 32, 64, feature_size].

    hidden_activation_name : str, optional (default='relu')
        The activation function used in hidden layers.

    batch_norm : boolean, optional (default=True)
        Whether to apply Batch Normalization,
        See https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm1d.html

    dropout_rate : float in (0., 1), optional (default=0.2)
        The dropout to be used across all layers.

    Attributes
    ----------
    model : torch.nn.Module
        The underlying AutoEncoder model.

    optimizer : torch.optim
        The optimizer used to train the model.

    criterion : torch.nn.modules
        The loss function used to train the model.

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

    def__init__(self,
                 contamination=0.1, preprocessing=True,
                 lr=1e-3, epoch_num=10, batch_size=32,
                 optimizer_name='adam',
                 device=None, random_state=42,
                 use_compile=False, compile_mode='default',
                 verbose=1,
                 optimizer_params: dict = {'weight_decay': 1e-5},
                 hidden_neuron_list=[64, 32],
                 hidden_activation_name='relu',
                 batch_norm=True, dropout_rate=0.2):
        super(AutoEncoder, self).__init__(contamination=contamination,
                                          preprocessing=preprocessing,
                                          lr=lr, epoch_num=epoch_num,
                                          batch_size=batch_size,
                                          optimizer_name=optimizer_name,
                                          criterion_name='mse',
                                          device=device,
                                          random_state=random_state,
                                          use_compile=use_compile,
                                          compile_mode=compile_mode,
                                          verbose=verbose,
                                          optimizer_params=optimizer_params)
        self.hidden_neuron_list = hidden_neuron_list
        self.hidden_activation_name = hidden_activation_name
        self.batch_norm = batch_norm
        self.dropout_rate = dropout_rate



[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.auto_encoder.AutoEncoder.build_model)
    defbuild_model(self):
        self.model = AutoEncoderModel(
            self.feature_size,
            hidden_neuron_list=self.hidden_neuron_list,
            hidden_activation_name=self.hidden_activation_name,
            batch_norm=self.batch_norm,
            dropout_rate=self.dropout_rate)






[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.auto_encoder.AutoEncoder.training_forward)
    deftraining_forward(self, batch_data):
        x = batch_data
        x = x.to(self.device)
        self.optimizer.zero_grad()
        x_recon = self.model(x)
        loss = self.criterion(x_recon, x)
        loss.backward()
        self.optimizer.step()
        return loss.item()




    defevaluating_forward(self, batch_data):
        x = batch_data
        x_gpu = x.to(self.device)
        x_recon = self.model(x_gpu)
        score = pairwise_distances_no_broadcast(x.numpy(),
                                                x_recon.cpu().numpy())
        return score





classAutoEncoderModel(nn.Module):
    def__init__(self,
                 feature_size,
                 hidden_neuron_list=[64, 32],
                 hidden_activation_name='relu',
                 batch_norm=True, dropout_rate=0.2):
        super(AutoEncoderModel, self).__init__()

        self.feature_size = feature_size
        self.hidden_neuron_list = hidden_neuron_list
        self.hidden_activation_name = hidden_activation_name
        self.batch_norm = batch_norm
        self.dropout_rate = dropout_rate

        self.encoder = self._build_encoder()
        self.decoder = self._build_decoder()

    def_build_encoder(self):
        encoder_layers = []
        last_neuron_size = self.feature_size
        for neuron_size in self.hidden_neuron_list:
            encoder_layers.append(LinearBlock(
                last_neuron_size, neuron_size,
                activation_name=self.hidden_activation_name,
                batch_norm=self.batch_norm,
                dropout_rate=self.dropout_rate))
            last_neuron_size = neuron_size
        return nn.Sequential(*encoder_layers)

    def_build_decoder(self):
        decoder_layers = []
        last_neuron_size = self.hidden_neuron_list[-1]
        for neuron_size in reversed(self.hidden_neuron_list[:-1]):
            decoder_layers.append(LinearBlock(
                last_neuron_size, neuron_size,
                activation_name=self.hidden_activation_name,
                batch_norm=self.batch_norm,
                dropout_rate=self.dropout_rate))
            last_neuron_size = neuron_size
        decoder_layers.append(nn.Linear(last_neuron_size, self.feature_size))
        return nn.Sequential(*decoder_layers)

    defforward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

```

Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
