Project P010
=============


Project Goals
-------------

You are looking at time series for measurements made at weather stations, and a number of quantified large scale climatic factors that potentially affect local climate at each weather station. You want to investigate the predictive capabilities of those factors (predictors) and construct simple linear multiple regression models for your weather stations. This is the core of a method that is commonly used to statistically downscale coarse model output either for near-future weather or distant-future climate. Specifically, you will investigate local temperature as a predictand, and use the multivariate ENSO index (MEI), antarctic oscillation index (AAOI) and regional means for temperature as predictors. (You will have to extract the regional means of the last two.)

Project Data
------------

You are provided with weather station data, and a number of potentially impactful climatic factors. 


Project Methods
---------------

Train simple multiple regression models for your weather stations with the data you have been provided with. You may, for example, use a stepwise multiple regression method with forward selection and bootstrapping. The bootstrapping part of the procedure (i.e. taking random subsets of your data for training) is important to ensure the robustness of your models. Attempt to construct robust models, calculate the coefficients of determination and the explained variance for each of your predictors.

**Optional**: Vary any of your training parameters (e.g. the significance threshold in your forward selection) and think about the reasons behind differences in results.
