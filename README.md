# Multi-Stock Direction Prediction using XGBoost
## Overview

This project explores next-day stock return direction prediction across multiple equities using machine learning techniques.
The objective is to establish a baseline financial ML framework capable of learning directional patterns from historical price data.
Unlike stock-specific modeling, this approach merges multiple equities into a unified dataset to evaluate cross-asset generalization.

## Problem Statement

Financial markets are highly noisy, non-stationary, and regime-dependent.
Short-term directional prediction is inherently difficult due to weak signal-to-noise ratio.
This project formulates the task as a binary classification problem:

1 → Next-day return > 0
0 → Next-day return ≤ 0

The goal is to evaluate whether tree-based boosting methods can detect nonlinear directional patterns across multiple stocks.

## Dataset

 - Source: Yahoo Finance (via yfinance)
 - Frequency: Daily OHLCV data
 - Assets: 3 publicly traded equities
 - Time Period: [Insert period used]
The individual stock datasets were merged into a single dataset to increase training volume and test cross-asset generalization.

## Feature Engineering

Engineered features include:
 - Daily returns
 - Lagged returns (t-1, t-2, etc.)
 - Moving averages (MA10)
 - Rolling volatility
 - Volume-based indicators
Feature engineering is critical in financial modeling due to the limited predictive power of raw price data.

## Train-Test Strategy

A chronological 80/20 split was used to preserve temporal ordering and prevent look-ahead bias.
Time-series integrity was maintained by avoiding random shuffling.

## Model

XGBoost classifier was selected due to:
 - Strong performance on structured tabular data
 - Ability to model nonlinear relationships
 - Built-in regularization to reduce overfitting

## Results

The baseline model achieved approximately 50% directional accuracy across the merged multi-stock dataset.
Given the stochastic nature of short-horizon financial markets, this performance serves as an experimental benchmark rather than a deployable trading strategy.
This highlights the complexity of financial ML and motivates further research-driven improvements.

## Limitations

 - Financial markets are non-stationary
 - Regime shifts impact model generalization
 - A single split may not fully capture time-varying behavior

## Future Work

 - Implement Rainbow DQN for reinforcement learning-based trading policy optimization
 - Apply walk-forward validation
 - Combine tree-based models with LSTM for ensemble learning
 - Evaluate using risk-adjusted metrics (Sharpe Ratio, drawdown)

## Key Skills Demonstrated

 - Time-Series Feature Engineering
 - Multi-Asset Data Integration
 - Gradient Boosting (XGBoost)
 - Chronological Model Evaluation
 - Research-Oriented Financial ML Development
