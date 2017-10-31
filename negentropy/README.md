# Negentropy increment

## About

In **[1] and [2]**, Lago-Fernández et al. make the assumption that the quality of a model returned by a clustering algorithm can be calculated using entropy. 
Their hypothesis is that clusters may be modeled by gaussian distributions. Thus, they calculate the negentropy, basically the difference between the clusters entropy, and models of the clusters as gaussian distributions using the same covariance matrix as the real clusters. 
Furthermore, they claim that the negentropy increment that they define make calculations easiers. This index is defined as the negentropy of the model with k clusters considered less the negentropy of the data (no clusters). 

However, considering the maths in [1], we did not succeed to get equation 4 from equation 3. One can find our maths [here](negentropy.pdf). Furthermore, as one can see, the negentropy increment is not the same in [1] and [2] and we could not guess why.

Then we wrote code for the negentropy increment defined in [1] and for the formula given by our maths but it seems it was not performing well.
Code can be found in *quality.py*, *get_negentropy* is the negentropy as defined by authors, *get_negentropy_us* as in our pdf.

## References
[1] Lago-Fernández, L. F., & Corbacho, F. (2009, June). Using the negentropy increment to determine the number of clusters. In *International Work-Conference on Artificial Neural Networks (pp. 448-455)*. Springer, Berlin, Heidelberg.

[2] Lago-Fernández, L. F., Aragón, J., Martínez-Muñoz, G., González, A. M., & Sánchez-Montañés, M. (2014). Cluster validation in problems with increasing dimensionality and unbalanced clusters. Neurocomputing, 123, 33-39.
