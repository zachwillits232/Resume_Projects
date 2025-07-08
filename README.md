Data Science & Machine Learning Projects

Welcome to my GitHub repository, where I showcase three key projects demonstrating my expertise in data science, machine learning, and algorithmic trading using Python. These projects highlight my ability to solve complex problems, collaborate effectively, and deliver impactful results in housing, sports analytics, and finance domains. Each section below provides a detailed explanation of the project’s objectives, methods, results, and significance, with code available in this repository for further exploration.

Boston Housing Price Prediction (Kaggle)

In a team-based academic project, I collaborated with peers to develop a machine learning model predicting median house prices in Boston using Kaggle’s Boston Housing dataset, which includes 506 samples and 13 features like crime rate and average rooms per dwelling from 1970s Boston suburbs. Our goal was to create an accurate regression model, optimize performance through teamwork, and uncover housing market insights.

We used Pandas to clean and scale data, handle missing values, and encode categorical variables, while engineering interaction terms like rooms versus crime rate to capture non-linear patterns. With Scikit-learn, we implemented regression models, including Linear Regression, Random Forest, and Gradient Boosting, tuning hyperparameters via GridSearchCV and evaluating performance with R² score and Mean Squared Error.

Our team achieved the lowest R² score among all student teams in our professor’s 5-year tenure, reflecting our effective collaboration and model optimization. Feature importance analysis, visualized with Matplotlib and Seaborn, identified key price drivers like room count and crime rate, and cross-validation ensured robust generalization.

This project strengthened my skills in team-based model development, feature engineering, and regression analysis, while providing insights into housing market dynamics relevant to real estate analytics.

Corbin Burnes Pitching Analysis

I designed a deep learning model to analyze and predict pitch types and sequences for MLB pitcher Corbin Burnes, using 2023–2024 Statcast data in a solo project focused on sports analytics. The aim was to classify pitches like fastballs and sliders, predict pitch sequences, and extract strategic insights from real-world baseball data.

I sourced pitch-by-pitch data with pybaseball and Statcast APIs, engineering features such as velocity, spin rate, and release point, and normalized them for model compatibility. A CNN-LSTM hybrid model, built in TensorFlow/Keras, captured spatial pitch characteristics and temporal sequence patterns, with Grad-CAM used for interpretability. I evaluated the model using accuracy, F1 score, and confusion matrices for multi-class classification.

The model achieved approximately 85% accuracy in classifying key pitches like sliders, enabling reliable strategy predictions, while Grad-CAM heatmaps visualized tendencies such as slider usage in two-strike counts. Sequence predictions, validated on 2024 game data, supported strategic applications.

This project enhanced my expertise in deep learning, time-series analysis, and sports analytics, demonstrating my ability to derive insights from complex datasets for performance optimization.

Alpaca Stock Trading System

I developed an automated algorithmic trading system in Python, integrating Alpha Vantage for market data and Alpaca’s paper trading API to execute strategies on stocks like AAPL, META, and TSLA, exploring fintech and quantitative trading. The system aimed to automate trading decisions, optimize portfolio performance, and enable scalable market analysis.

I built a data pipeline with Alpha Vantage and Pandas to process historical and real-time stock data, computing technical indicators like RSI and moving averages. Trading strategies, including Mean Reversion, Moving Average Crossover, and Momentum, were coded with custom entry and exit logic, and I integrated the Alpaca API for paper trading, scheduling daily trades with crontab.

Backtesting on historical data measured returns, Sharpe ratio, and drawdowns, with strategies yielding approximately 12% annualized returns for Mean Reversion on TSLA. Iterative testing optimized strategy parameters, improving risk-adjusted returns, and a live paper trading system allowed real-time performance monitoring and refinement.

This project bolstered my skills in algorithmic trading, API integration, and financial data analysis, preparing me for data-driven fintech solutions.

Envision Utah Housing Crisis Analysis

In a collaborative project with a teammate, I analyzed the housing crisis in Summit County, UT, focusing on challenges faced by the seasonal working population. Our goal was to develop data-driven recommendations to improve housing accessibility and affordability for seasonal workers by comparing housing prices with nearby counties using data analysis and Tableau visualizations.

We collected housing and demographic data from public sources, such as Census and local government reports, and used Pandas to clean and analyze data, comparing housing prices across Summit County and nearby counties to highlight price disparities. Interactive Tableau dashboards were built to visualize these drastic price differences and support policy recommendations.

Our analysis revealed significantly higher housing prices in Summit County compared to surrounding counties, exacerbating challenges for seasonal workers. We recommended policy solutions, such as subsidized housing and zoning reforms, presented in Tableau dashboards. Stakeholder feedback praised the actionable insights, and the visualizations enhanced communication of findings. The Tableau file (envision_utah/envision_utah_housing.twbx) must be downloaded to view in Tableau Desktop/Reader.

This project strengthened my skills in collaborative data analysis, visualization, and policy analysis, demonstrating my ability to address real-world social issues with data-driven solutions.

Contact

For more details or to discuss these projects, connect with me via LinkedIn or email at zachwillits2@gmail.com. Explore the code in this repository to see my work in action!
