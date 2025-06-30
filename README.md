Data Science & Machine Learning Projects

Welcome to my GitHub repository! This README provides an in-depth overview of three key projects showcasing my expertise in data science, machine learning, and algorithmic trading using Python. Each project demonstrates my ability to tackle real-world problems, collaborate effectively, and deliver impactful results in domains like housing, sports analytics, and finance.

1. Boston Housing Price Prediction (Kaggle)

Overview

As part of a team-based academic project, I developed a machine learning model to predict median house prices in Boston using Kaggle’s Boston Housing dataset. The dataset includes 506 samples with 13 features (e.g., crime rate, average rooms per dwelling, proximity to employment centers) from 1970s Boston suburbs.

Objectives





Build a regression model to accurately predict house prices.



Collaborate with teammates to optimize model performance and outshine historical benchmarks.



Uncover insights into housing market drivers through data analysis.

Methods





Data Preprocessing: Used Pandas for cleaning and feature scaling, handling missing values, and encoding categorical variables.



Feature Engineering: Created interaction terms (e.g., rooms vs. crime rate) to capture non-linear relationships.



Modeling: Implemented regression models in Scikit-learn, including Linear Regression, Random Forest, and Gradient Boosting. Tuned hyperparameters using GridSearchCV.



Evaluation: Measured performance with R² score and Mean Squared Error (MSE).

Results





Our team achieved the lowest R² score (indicating superior predictive accuracy) among all student teams in our professor’s 5-year tenure, a testament to our collaborative model optimization.



Identified key price drivers (e.g., average room count, crime rate) through feature importance analysis, visualized using Matplotlib and Seaborn.



Delivered a robust model with strong generalization to unseen data, validated via cross-validation.

Impact

This project honed my skills in team-based model development, feature engineering, and regression analysis, while deepening my understanding of housing market dynamics, relevant to real estate analytics.

2. Corbin Burnes Pitching Analysis

Overview

I designed a deep learning model to analyze and predict pitch types and sequences for MLB pitcher Corbin Burnes, leveraging 2023–2024 Statcast data. This solo project explored sports analytics through advanced machine learning techniques.

Objectives





Classify pitch types (e.g., fastball, slider, curveball) and predict pitch sequences.



Extract actionable insights for pitching strategies using real-world baseball data.



Apply deep learning to time-series sports data.

Methods





Data Acquisition: Sourced pitch-by-pitch data using pybaseball and Statcast APIs, filtering for Burnes’ 2023–2024 seasons.



Preprocessing: Engineered features like pitch velocity, spin rate, and release point; normalized data for model compatibility.



Modeling: Built a CNN-LSTM hybrid model in TensorFlow/Keras to capture spatial (pitch characteristics) and temporal (sequence) patterns. Used Grad-CAM for interpretability.



Evaluation: Assessed model with accuracy, F1 score, and confusion matrices for multi-class pitch classification.

Results





Achieved high accuracy in pitch type classification (e.g., ~85% for key pitches like sliders), enabling reliable strategy predictions.



Visualized pitch patterns with Grad-CAM heatmaps, revealing Burnes’ tendencies (e.g., slider usage in two-strike counts).



Demonstrated robust sequence prediction, validated on 2024 game data, enhancing strategic applications.

Impact

This project strengthened my expertise in deep learning, time-series analysis, and sports analytics, showcasing my ability to derive insights from complex datasets, applicable to performance optimization in sports.

3. Alpaca Stock Trading System

Overview

I developed an automated algorithmic trading system using Python, integrating Alpha Vantage for market data and Alpaca’s paper trading API to execute strategies on stocks like AAPL, META, and TSLA. This project explored fintech and quantitative trading.

Objectives





Automate trading decisions using data-driven strategies.



Optimize portfolio performance through backtesting and live paper trading.



Build a scalable system for real-time market analysis.

Methods





Data Pipeline: Retrieved historical and real-time stock data via Alpha Vantage, processed with Pandas for technical indicators (e.g., RSI, moving averages).



Trading Strategies: Implemented Mean Reversion, Moving Average Crossover, and Momentum strategies, coded in Python with custom logic for entry/exit signals.



Automation: Integrated Alpaca API for paper trading, scheduling trades with crontab for daily execution.



Evaluation: Backtested strategies using historical data, measuring returns, Sharpe ratio, and drawdowns.

Results





Successfully automated trading for 10+ stocks, with backtested strategies yielding positive simulated returns (e.g., ~12% annualized for Mean Reversion on TSLA).



Optimized strategy parameters through iterative testing, improving risk-adjusted returns.



Deployed a live paper trading system, monitoring performance and refining logic in real-time.

Impact

This project enhanced my skills in algorithmic trading, API integration, and financial data analysis, equipping me to build data-driven solutions for fintech and investment applications.

Contact

For more details or to discuss these projects, connect with me via LinkedIn or email at zachwillits2@gmail.com Explore the code in this repository to see my work in action!
