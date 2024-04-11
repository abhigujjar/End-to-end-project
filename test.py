from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

cust_data_obj=CustomData(1.7,62.6,59.0,7.65,7.61,4.77,"Premium","G","VS2")

trial=cust_data_obj.get_data_as_dataframe()
print(trial)