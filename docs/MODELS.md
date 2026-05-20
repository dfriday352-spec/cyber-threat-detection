# Machine Learning Models

## Threat Classification Models

### Model 1: Deep Neural Network
- **Architecture**: Feed-forward DNN
- **Framework**: TensorFlow/Keras
- **Purpose**: Binary threat classification
- **Training Data**: Labeled security events

### Model 2: LSTM Network
- **Architecture**: Bidirectional LSTM
- **Framework**: PyTorch
- **Purpose**: Sequential threat pattern detection
- **Training Data**: Time-series security data

### Model 3: Ensemble Classifier
- **Architecture**: Random Forest + Gradient Boosting
- **Framework**: scikit-learn
- **Purpose**: Threat type classification
- **Training Data**: Feature-engineered security events

## Anomaly Detection Models

### Model 1: Isolation Forest
- **Purpose**: Detect outliers in network behavior
- **Framework**: scikit-learn

### Model 2: Autoencoder
- **Architecture**: Variational Autoencoder (VAE)
- **Framework**: TensorFlow
- **Purpose**: Learn normal behavior patterns

## Model Training

- **Data**: Balanced dataset of normal and malicious events
- **Validation**: Cross-validation with stratified folds
- **Hyperparameter Tuning**: Bayesian optimization
- **Monitoring**: Track loss, accuracy, AUC-ROC metrics
