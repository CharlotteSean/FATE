# Feature Binning

Feature binning or data binning is a data pre-processing technique. It can be use to reduce the effects of minor observation errors, calculate information values and so on.

In this version, we provide a widely used binning method called quantile binning. To achieve this approach, we have used a special data structure mentioned in this [paper](https://www.researchgate.net/profile/Michael_Greenwald/publication/2854033_Space-Efficient_Online_Computation_of_Quantile_Summaries/links/0f317533ee009cd3f3000000/Space-Efficient-Online-Computation-of-Quantile-Summaries.pdf). Feel free to check out the detail algorithm in the paper.

We are looking forward more binning methods and more methods will come out soon.

# Feature Selection

Feature selection is a process that select subset of features for use in model construction. Take good advantage of feature selection can improve the performance of a model.

In this version, we provides several filter methods for feature selection.

1. unique_value: filter the columns if all values in this feature is the same

2. iv_value_thres: Use information value to filter columns. Filter those columns whose iv is smaller than threshold.

3. iv_percentile: Use information value to filter columns. A float ratio threshold need to be provided. Pick floor(ratio * feature_num) features with higher iv. If multiple features around the threshold are same, all those columns will be keep.

4. coefficient_of_variation_value_thres: Use coefficient of variation to judge whether filtered or not.

5. outlier_cols: Filter columns whose certain percentile value is larger than a threshold.

Note: iv_value_thres and iv_percentile should not exist at the same times

More feature selection methods will be provided. Please make a discussion in issues if you have any needs.