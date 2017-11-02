# AIC and BIC

## Definition
The **Akaike Information Criterion (AIC, Akaike is the name of its author)** and the **Bayesian Information Criterion (BIC)**, also called Schwarz (the name of its author) Criterion were defined in the seventies.
Based on the likelihood, they both define a way to penalize the model complexity [1][2].

**BIC :**![BIC](images/bic.gif)

**AIC :**![AIC](images/aic.gif)

with *n* the number of data, *k* the number of clusters, *q(k)* a function that describes the complexity of the model, and *L* the likelihood.
Most of the time, *q(k)=k*.

## Code

These criteria were implemented using sklearn with results from gaussian mixture models.

## References
[1] Schwarz, G. (1978). Estimating the dimension of a model. *The annals of statistics*, 6(2), 461-464.

[2] Akaike, H. (1974). A new look at the statistical identiﬁcation model. *IEEE Trans. Auto. Control*, 19, 716-723.

[3] Christopher D. Manning, Prabhakar Raghavan and Hinrich Schütze, *Introduction to Information Retrieval*, Cambridge University Press. 2008. 
