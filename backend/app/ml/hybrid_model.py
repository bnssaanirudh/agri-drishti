import torch
import torch.nn as nn
import numpy as np
from sklearn.ensemble import RandomForestRegressor

class TemporalEncoder(nn.Module):
    def __init__(self, input_dim=3, hidden_dim=16):
        super(TemporalEncoder, self).__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, batch_first=True)
    
    def forward(self, x):
        _, (hn, _) = self.lstm(x)
        return hn[-1]

class CropStressPredictor:
    def __init__(self):
        self.encoder = TemporalEncoder()
        # Pre-trained mock weights for demo
        self.rf = RandomForestRegressor(n_estimators=10, max_depth=5)
        # Fake training for initialization
        self.rf.fit(np.random.rand(10, 17), np.random.rand(10)) 

    def predict(self, temporal_data, static_data):
        """
        temporal_data: List of [NDVI, EVI, Rain] over time
        static_data: [SoilQuality]
        """
        # Convert to Tensor
        x_temp = torch.FloatTensor([temporal_data]) # Shape (1, seq, 3)
        
        # Get LSTM Features
        with torch.no_grad():
            lstm_feat = self.encoder(x_temp).numpy()
            
        # Combine
        combined = np.hstack([lstm_feat, [static_data]])
        
        # Predict
        score = self.rf.predict(combined)[0]
        return float(score)