# Module 12 Report Template

## Overview of the Analysis

In this section, describe the analysis you completed for the machine learning models used in this Challenge. This might include:

* Explain the purpose of the analysis.

    The purpose of this exersize is to determine loans that are healthy and loans that are potentially risky.

* Explain what financial information the data was on, and what you needed to predict.

    The data consists of certain economic factors such as:
    interest_rate,borrower_income,debt_to_income,num_of_accounts,derogatory_marks,total_debt


* Provide basic information about the variables you were trying to predict (e.g., `value_counts`).

  Were trying to predict if the data is a 1 (loan is indeed risky) 0(Loan is not low risk)



* Describe the stages of the machine learning process you went through as part of this analysis.

  1. We first used the original sample provided to us in the csv file. 
  2. We separted the features we need for training and set the out(target) to the loan status column.
  3. we then used confusion_matrix function to determine the true and negative outcomes and balanced_accuracy to determine the accuracy.
  4  We resampled the data to reduce any bias and we repeated the above steps to get a better prediction accuracy.


* Briefly touch on any methods you used (e.g., `LogisticRegression`, or any resampling method).

  train_test_split = separates all the features and outcomes to a test and trainging sets before running predicitions on each pair of data.
  LogisticRegression = Is used to get an outcome of true or false outcomes (0 or 1)
  classification_report_imbalanced = Calculates useful information about our data including precision.




## Results

Using bulleted lists, describe the balanced accuracy scores and the precision and recall scores of all machine learning models.

* Machine Learning Model 1:
  * Description of Model 1 Accuracy, Precision, and Recall scores.
  



* Machine Learning Model 2:
  * Description of Model 2 Accuracy, Precision, and Recall scores.

  

## Summary

Summarize the results of the machine learning models, and include a recommendation on the model to use, if any. For example:
* Which one seems to perform best? How do you know it performs best?

The resampled performance is better because we want to even out the samples in order to remove any bias.  without it, Generally the bias goes to the larger class.

* Does performance depend on the problem we are trying to solve? (For example, is it more important to predict the `1`'s, or predict the `0`'s? )

It is more important to predict the ones because we consider the 1s to be true.  So in this challenge we are saying if 1, the loan is bad.

If you do not recommend any of the models, please justify your reasoning.
