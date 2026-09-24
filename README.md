# zepto-ai-capstone
Zepto AI Capstone Project
## Module 1 – Data Collection, Cleaning and SQL Analysis

- Scraped book data automatically using Python and BeautifulSoup.
- Collected book details including title, price, rating, availability, and category.
- Cleaned and prepared the collected dataset using Pandas.
- Stored the cleaned data in a SQLite database.
- Performed SQL queries and analysis on the book data.
- Used Pandas `read_sql()` to retrieve and analyze database results.
- Completed the end-to-end data pipeline from web scraping to SQL analysis.


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





## Module 3 – GenAI Support Assistant

- Built a Zepto Support Assistant using RAG (Retrieval-Augmented Generation).
- Used Sentence Transformers for embeddings.
- Stored and retrieved policy documents using ChromaDB.
- Implemented workflow using LangGraph.
- Added policy-based question answering with source retrieval.
- Created a FastAPI endpoint for the support assistant.
- Tested the API successfully using Swagger UI.
- Verified the refund-policy query and received a grounded response from the policy documents.
- Containerized the Support Assistant API using Docker and successfully verified it on port 8000.