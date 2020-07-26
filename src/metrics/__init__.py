import numpy as np


def RMSE(model, data_loader):
    RMSE = np.array([], dtype=np.float32)
    for features, feature_values, label in data_loader:
        features = features.cuda()
        feature_values = feature_values.cuda()
        label = label.cuda()

        prediction = model(features, feature_values)
        prediction = prediction.clamp(min=-1.0, max=1.0)
        SE = (prediction - label).pow(2)
        RMSE = np.append(RMSE, SE.detach().cpu().numpy())

    return np.sqrt(RMSE.mean())
