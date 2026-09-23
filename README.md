# zepto-ai-capstone
Zepto AI Capstone Project
## Module 2 – EDA, Modeling, Evaluation and Prediction

In this module, exploratory data analysis and machine learning modeling were performed on the Titanic dataset.

The data was prepared by handling missing values and separating numerical and categorical features. A preprocessing pipeline was created using imputation, scaling, and one-hot encoding.

A Logistic Regression model was trained using the training dataset and evaluated on the test dataset. The model achieved an accuracy of approximately 77.09%.

The classification report and confusion matrix were used to evaluate the model performance. Predictions were also generated for the test dataset.

Overall, the modeling workflow demonstrates the complete process from data preprocessing to model training, evaluation, and prediction.

### Additional Module 2 Work

- Applied SMOTE to handle class imbalance.
- Trained and evaluated Logistic Regression, Decision Tree, and Random Forest models.
- Used Accuracy, Precision, Recall, F1 Score, Confusion Matrix and ROC-AUC for model evaluation.
- Performed Hyperparameter Tuning using GridSearchCV.
- Used 3-fold Cross-Validation during hyperparameter tuning.
- Performed Fare Analysis and Random Forest Feature Importance analysis.
- Saved the optimized Random Forest model using Joblib.
- Successfully loaded the saved Joblib model and generated test predictions.