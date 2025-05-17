import torch
import torch.nn as nn
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score


class Autoencoder(nn.Module):
    def __init__(self, input_dim):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 16),
            nn.ReLU(),
            nn.Linear(16, 8)
        )
        self.decoder = nn.Sequential(
            nn.Linear(8, 16),
            nn.ReLU(),
            nn.Linear(16, input_dim)
        )

    def forward(self, x):
        return self.decoder(self.encoder(x))


def run_autoencoder(X, true_labels=None, epochs=50):
    # Step 1: Normalize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = Autoencoder(input_dim=X.shape[1])
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    X_tensor = torch.tensor(X_scaled, dtype=torch.float32)

    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(X_tensor)
        loss = criterion(outputs, X_tensor)
        loss.backward()
        optimizer.step()

    with torch.no_grad():
        reconstructed = model(X_tensor)
        reconstruction_loss = torch.mean((X_tensor - reconstructed) ** 2, dim=1).numpy()

    # Step 2: Dynamic threshold (95th percentile of loss)
    threshold = np.percentile(reconstruction_loss, 95)
    scores = (reconstruction_loss > threshold).astype(int)

    # Step 3: Calculate metrics if labels exist
    metrics = None
    if true_labels is not None:
        metrics = {
            "precision": precision_score(true_labels, scores, zero_division=0),
            "recall": recall_score(true_labels, scores, zero_division=0),
            "f1_score": f1_score(true_labels, scores, zero_division=0),
            "accuracy": accuracy_score(true_labels, scores)
        }

    return X.copy(), scores, metrics
