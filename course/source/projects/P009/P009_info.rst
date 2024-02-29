Project P009
=============


Project Goals
-------------

You are looking at time series for measurements made at weather stations, and a number of quantified large scale climatic factors that potentially affect local climate at each weather station. You want to investigate the predictive capabilities of those factors (predictors) and construct random forest regression models for your weather stations. Specifically, you will investigate local temperature as a predictand, and use the multivariate ENSO index (MEI), antarctic oscillation index (AAOI) and regional means for temperature and wind speeds as predictors. (You will have to extract the regional means of the last two.)

Project Data
------------

You are provided with weather station data, and a number of potentially impactful climatic factors. 


Project Methods
---------------

Split your stations records up into training and validation period (e.g. pre- and post 2000). Use one part of your records to train random forest regression models for your weather stations with the data you have been provided with. Calculate the coefficients of determination to get a sense of model performance.

**Optional**: Vary any of your training parameters (e.g. tree depth) and think about the reasons behind differences in results.
