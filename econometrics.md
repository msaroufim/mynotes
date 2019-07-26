# Econometrics

A guide to econometrics by Peter Kennedy 4th edition

* Unbiased estimator - 0 mean of estimate distribution relative to target distribution
* MCMC can be used to test the statistics of a distribution we're working with
* Consistent estimator: the more data you get the more you converge to the true value
* Other interesting properties of estimators are on page 32: admissible, robust, MELO, Concentration (small variance)
* Assumptions of Classical Regression Mode (table summary on page 55)
    1. Dependent variable = f(independent variables) + disturbance where f is linear
    2. E[disturbance] = 0
    3. All disturbances have the same variance (i.e not autocorrelated and no heteroskedasticity where disturbances don't have the same variance)
    4. Observations fixed on repeated samples - no lag, error or autocorrelation in observations
    5. Number of observations > number of variables - no multicolinearity
* Non linear functions can be made linear by 
    1. moving the non linearity to the parameters Z = X^2 substitution
    2. Transforming the entire equation - using logs for example
* Can test a joint hypthesis with an f test and a single parameter with t test
* t-test works by taking two samples from two different populations  to compare them - t = signal /noise = difference between group means / variability of groups. If t > 1 then we know that there is more info than noise so tells us the two sets are different - this is why we can also use t tests for hypothesis testing