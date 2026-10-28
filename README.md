# Email Spam Detection

A machine learning project that classifies emails as Spam or Ham (not spam).

## Models used
- Naive Bayes
- Logistic Regression
- Linear SVM (best model)

## Results
| Model | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|
| Naive Bayes | 0.9681 | 0.990 | 0.7557 | 0.8571 |
| Logistic Regression | 0.9642 | 1.000 | 0.7176 | 0.8356 |
| Linear SVM | 0.9836 | 0.975 | 0.8931 | 0.9323 |

## Method
1. Text preprocessing and TF-IDF vectorization
2. Training and comparing 3 models
3. Evaluation using accuracy, precision, recall, F1
4. Saved best model using joblib

## Files
- `Untitled0 (1).ipynb` : full code
- `spam_model (1).pkl` : trained model
- `vectorizer (1).pkl` : TF-IDF vectorizer

## Author
Rythm Kukkar
