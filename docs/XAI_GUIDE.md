# Explainable AI (XAI) Guide

## Overview

This guide explains how the system uses XAI techniques to make threat predictions interpretable and trustworthy.

## SHAP (SHapley Additive exPlanations)

### What is SHAP?
SHAP values provide a unified measure of feature importance based on cooperative game theory.

### Using SHAP
```python
from src.explainability.xai_engine import XAIEngine

xai_engine = XAIEngine(model, config)
shap_values = xai_engine.explain_with_shap(features)
```

### Interpretation
- Red bars: Features that increase threat probability
- Blue bars: Features that decrease threat probability
- Bar length: Magnitude of impact

## LIME (Local Interpretable Model-agnostic Explanations)

### What is LIME?
LIME explains individual predictions by fitting a local interpretable model.

### Using LIME
```python
lime_values = xai_engine.explain_with_lime(features, feature_names)
```

### Interpretation
- Shows which features contributed to the prediction
- Provides local approximation of model behavior
- Model-agnostic approach

## Best Practices

1. **Always explain critical decisions**: High-risk threat classifications should be explained
2. **Use multiple methods**: Combine SHAP and LIME for robust explanations
3. **Monitor explanations over time**: Track how explanations change
4. **Validate with domain experts**: Have security experts review explanations
