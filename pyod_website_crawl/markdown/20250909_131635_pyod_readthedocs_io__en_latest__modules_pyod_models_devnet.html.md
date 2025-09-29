# pyod.models.devnet - pyod 2.0.5 documentation

**URL:** https://pyod.readthedocs.io/en/latest/_modules/pyod/models/devnet.html

**爬取时间:** 2025-09-09 13:16:35.665015

**深度:** 2

---

Contents Menu Expand Light mode Dark mode Auto light/dark, in light mode Auto light/dark, in dark mode
Hide navigation sidebar
Hide table of contents sidebar
[Skip to content](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/devnet.html#furo-main-content)
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


[ Back to top ](https://pyod.readthedocs.io/en/latest/_modules/pyod/models/devnet.html)
Toggle Light / Dark / Auto color theme
Toggle table of contents sidebar
# Source code for pyod.models.devnet
```
# -*- coding: utf-8 -*-

"""Deep anomaly detection with deviation networks
Part of the codes are adapted from
https://github.com/GuansongPang/deviation-network
"""
# Author: Sihan Chen <schen976@usc.edu>
# License: BSD 2 clause


# Import necessary libraries
importnumpyasnp
importtorch
importtorch.nnasnn
importtorch.optimasoptim
fromsklearn.utilsimport check_array
fromtorch.utils.dataimport Dataset, DataLoader

from.baseimport BaseDetector
from..utils.torch_utilityimport TorchDataset

MAX_INT = np.iinfo(np.int32).max
data_format = 0

# Set random seed for reproducibility
np.random.seed(42)
torch.manual_seed(42)


# Define the network architectures
classDevNetD(nn.Module):
    def__init__(self, input_shape):
        super(DevNetD, self).__init__()
        self.fc1 = nn.Linear(input_shape, 1000)
        self.fc2 = nn.Linear(1000, 250)
        self.fc3 = nn.Linear(250, 20)
        self.score = nn.Linear(20, 1)

    defforward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = self.score(x)
        return x


classDevNetS(nn.Module):
    def__init__(self, input_shape):
        super(DevNetS, self).__init__()
        self.fc1 = nn.Linear(input_shape, 1000)
        self.score = nn.Linear(1000, 1)

    defforward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.score(x)
        return x


classDevNetLinear(nn.Module):
    def__init__(self, input_shape):
        super(DevNetLinear, self).__init__()
        self.score = nn.Linear(input_shape, 1)

    defforward(self, x):
        x = self.score(x)
        return x


defdeviation_loss(y_true, y_pred):
'''
    Z-score-based deviation loss translated to PyTorch.
    '''
    confidence_margin = 5.0
    # size=5000 is the setting of l in algorithm 1 in the paper
    ref = torch.randn(5000, device=y_pred.device,
                      dtype=torch.float32)  # Generate normal distributed ref values
    dev = (y_pred - ref.mean()) / ref.std()
    inlier_loss = torch.abs(dev)
    outlier_loss = torch.abs(torch.clamp(confidence_margin - dev, min=0))

    # Compute the mean of the weighted sum of inlier and outlier losses
    return torch.mean((1 - y_true) * inlier_loss + y_true * outlier_loss)


# Define the training and testing process
deftrain_and_test(model, train_loader, test_loader, epochs, device):
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    model.train()

    for epoch in range(epochs):
        for inputs, labels in train_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

    model.eval()
    with torch.no_grad():
        total_loss = 0
        for inputs, labels in test_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            total_loss += criterion(outputs, labels).item()
        print('Test Loss:', total_loss / len(test_loader))


# Main function to run the model
defdeviation_network(input_shape, network_depth):
'''
    Construct the deviation network-based detection model in PyTorch style
    '''
    # Select the model based on the network depth
    if network_depth == 4:
        model = DevNetD(input_shape)
    elif network_depth == 2:
        model = DevNetS(input_shape)
    elif network_depth == 1:
        model = DevNetLinear(input_shape)
    else:
        raise ValueError(
            "The network depth is not set properly")  # Use exception instead of sys.exit

    # Initialize the optimizer
    optimizer = optim.RMSprop(model.parameters(), lr=0.001,
                              weight_decay=1e-6)  # Set clipnorm equivalent in PyTorch
    return model, optimizer


classSupDataset(Dataset):
    def__init__(self, x, outlier_indices, inlier_indices, rng):
        self.x = x
        self.outlier_indices = outlier_indices
        self.inlier_indices = inlier_indices
        self.rng = np.random.RandomState(
            42)  # Ensure rng is seeded outside or fixed

    def__len__(self):
        return len(self.outlier_indices) + len(
            self.inlier_indices)  # or any other appropriate length

    def__getitem__(self, idx):
        if idx < len(self.inlier_indices):
            # Assuming inliers are processed first
            label = 0  # Assuming inlier label
            index = self.inlier_indices[idx]
        else:
            # Processing outliers
            label = 1  # Assuming outlier label
            index = self.outlier_indices[idx - len(self.inlier_indices)]

        return self.x[index], label


definput_batch_generation_sup_sparse(x_train, outlier_indices, inlier_indices,
                                      batch_size, rng):
'''
    Batch generation for samples, alternating between positive and negative.
    Adjusted for use with PyTorch, handling data in tensors.
    '''
    training_data = []
    training_labels = []
    n_inliers = len(inlier_indices)
    n_outliers = len(outlier_indices)

    for i in range(batch_size):
        if i % 2 == 0:
            sid = rng.choice(n_inliers, 1)
            training_data.append(x_train[inlier_indices[sid.item()]])
            training_labels.append(0)
        else:
            sid = rng.choice(n_outliers, 1)
            training_data.append(x_train[outlier_indices[sid.item()]])
            training_labels.append(1)

    # Convert lists to tensors
    training_data = torch.stack(training_data)
    training_labels = torch.tensor(training_labels, dtype=torch.long)

    return training_data, training_labels


defload_model_weight_predict(model, x_test):
    # Ensure x_test is a PyTorch tensor and also ensure it's on the same device as the model
    x_test = torch.tensor(x_test, dtype=torch.float32)

    # Assuming data_format variable should be defined somewhere in the context or as a parameter
    data_format = 0  # Assuming it's set correctly according to your use-case

    if data_format == 0:
        scores = model(x_test)
    else:
        data_size = x_test.shape[0]
        scores = torch.zeros([data_size, ])
        batch_size = 512
        for i in range(0, data_size, batch_size):
            end = min(i + batch_size, data_size)
            subset = x_test[i:end]
            scores[i:end] = model(subset)

    # Make sure the output is flattened before returning
    scores = scores.flatten()  # Flatten the tensor to ensure it's one-dimensional

    return scores.detach().cpu().numpy()  # Convert to numpy array if needed




[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.devnet.DevNet)
classDevNet(BaseDetector):
    def__init__(self,
                 network_depth=2,
                 batch_size=512,
                 epochs=50,
                 nb_batch=20,
                 known_outliers=30,
                 cont_rate=0.02,
                 data_format=0,  # Assuming '0' for CSV
                 random_seed=42,
                 device=None,
                 contamination=0.1):
        super(DevNet, self).__init__(contamination=contamination)
        self._classes = 2
        self.network_depth = network_depth
        self.batch_size = batch_size
        self.epochs = epochs
        self.nb_batch = nb_batch
        self.known_outliers = known_outliers
        self.cont_rate = cont_rate
        self.data_format = data_format
        self.random_seed = random_seed
        self.device = device
        if self.device is None:
            self.device = torch.device(
                "cuda:0" if torch.cuda.is_available() else "cpu")



[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.devnet.DevNet.fit)
    deffit(self, X, y):
        outlier_indices = np.where(y == 1)[0]
        inlier_indices = np.where(y == 0)[0]
        n_outliers = len(outlier_indices)
        print("Original training size: %d, No. outliers: %d" % (
            X.shape[0], n_outliers))
        n_noise = len(np.where(y == 0)[0]) * self.contamination / (
                1. - self.contamination)
        n_noise = int(n_noise)
        outlier_indices = np.where(y == 1)[0]
        inlier_indices = np.where(y == 0)[0]
        print(y.shape[0], outlier_indices.shape[0], inlier_indices.shape[0],
              n_noise)
        # Data manipulation part can be adjusted as needed.
        self.model, optimizer = deviation_network(X.shape[1],
                                                  self.network_depth)
        rng = np.random.RandomState(42)
        train_dataset = SupDataset(X, outlier_indices, inlier_indices, rng)
        train_loader = DataLoader(train_dataset, batch_size=self.batch_size,
                                  shuffle=True)

        deftrain_model(model, data_loader, epochs):
            model.train()
            for epoch in range(epochs):
                for data, labels in data_loader:
                    data, labels = data.to(torch.float32), labels.to(
                        torch.float32)  # Ensure data types
                    optimizer.zero_grad()
                    outputs = model(data)
                    loss = deviation_loss(outputs, labels)
                    loss.backward()
                    optimizer.step()
                print(f'Epoch {epoch+1}, Loss: {loss.item()}')

        # Training the model
        train_model(self.model, train_loader, epochs=self.epochs)
        self.decision_scores_ = self.decision_function(X)
        self._process_decision_scores()
        return self






[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.devnet.DevNet.decision_function)
    defdecision_function(self, X):
        X = check_array(X)

        dataset = TorchDataset(X=X, return_idx=True)

        dataloader = torch.utils.data.DataLoader(dataset,
                                                 batch_size=self.batch_size,
                                                 shuffle=False)
        # enable the evaluation mode
        self.model.eval()

        # construct the vector for holding the reconstruction error
        outlier_scores = np.zeros([X.shape[0], ])
        with torch.no_grad():
            for data, data_idx in dataloader:
                data_cuda = data.to(self.device).float()
                # this is the outlier score
                outlier_scores[data_idx] = load_model_weight_predict(
                    self.model, data)
        return outlier_scores






[docs][](https://pyod.readthedocs.io/en/latest/pyod.models.html#pyod.models.devnet.DevNet.fit_predict_score)
    deffit_predict_score(self, X, y, scoring='roc_auc_score'):
"""
        Fit the detector with labels, predict on samples, and evaluate the model by predefined metrics.

        Parameters
        ----------
        X : numpy array of shape (n_samples, n_features)
            The input samples.
        y : numpy array of shape (n_samples,)
            The labels or target values corresponding to X.
        scoring : str, optional (default='roc_auc_score')
            Evaluation metric:
            - 'roc_auc_score': ROC score
            - 'prc_n_score': Precision @ rank n score

        Returns
        -------
        score : float
        """

        # Fit the model with both X and y
        self.fit(X, y)

        # Prediction and scoring
        if scoring == 'roc_auc_score':
            fromsklearn.metricsimport roc_auc_score
            score = roc_auc_score(y, self.decision_scores_)
        elif scoring == 'prc_n_score':
            fromsklearn.metricsimport precision_recall_curve
            precision, _, _ = precision_recall_curve(y, self.decision_scores_)
            score = precision[
                1]  # Assuming this is how you'd compute Precision @ rank n
        else:
            raise NotImplementedError('PyOD built-in scoring only supports '
                                      'ROC and Precision @ rank n')

        print("{metric}: {score}".format(metric=scoring, score=score))

        return score






```

Copyright © 2022, Yue Zhao 
Made with [Sphinx](https://www.sphinx-doc.org/) and [@pradyunsg](https://pradyunsg.me)'s [Furo](https://github.com/pradyunsg/furo)
