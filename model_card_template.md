# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Samantha Leavitt created this model. It is a logistic regression using the default hyperparameters in scikit-learn 
0.24.2.
## Intended Use
This model is intended to be used to predict income bracket (above or below 50k annual income) based on demographic 
data.
## Data
The data is publicly available census data from 1995 obtained from the UC Irvine machine learning repository. The 
dataset has 48,842 records and 14 features.
### Training Data
Training data is a subset of the overall data, consisting of 80% of the original dataset. No stratification was 
stipulated. A One Hot Encoder was used on the features and a label binarizer was used on the labels.
### Evaluation Data
Evaluation data is a subset of the overall data, consisting of 20% of the original dataset with no stratification. A 
One Hot Encoder was used on the features and a label binarizer was used on the labels.
## Metrics
The model was evaluated using precision, recall, and F1 scores. The overall model scored 0.7343, 0.2603, and 0.3844 
respectively.
## Ethical Considerations
Bias in data can lead to bias in models. Evaluation was done on each categorical feature for each metric to identify 
categories where the model struggles to accurately classify income. The results can be found in slice_output.txt.
## Caveats and Recommendations
The data used to train this model is out of date and may perform poorly on current data.  Given how low this model 
scores in recall and F1, this model is not precise enough to make significant decisions involving a person's income 
bracket, but could be used for low-risk situations such as marketing decisions.