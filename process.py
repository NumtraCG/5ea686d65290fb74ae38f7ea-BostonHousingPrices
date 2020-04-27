import json
import Connectors
import Transformations
import AutoML
try:
    BostonHousingPrices_DBFS = Connectors.DBFSConnector.fetch(
        [], {}, "5ea686d65290fb74ae38f7eb", spark, "{'url': '/Demo/BostonTrain.csv', 'file_type': 'Delimeted', 'dbfs_token': 'dapib8073bbfa952efa9d363b234ce06e2c6', 'dbfs_domain': 'westus.azuredatabricks.net', 'delimiter': ',', 'is_header': 'Use Header Line'}")

except Exception as ex:
    print(ex)
try:
    BostonHousingPrices_AutoFE = Transformations.TransformationMain.run(["5ea686d65290fb74ae38f7eb"], {"5ea686d65290fb74ae38f7eb": BostonHousingPrices_DBFS}, "5ea686d65290fb74ae38f7ec", spark, json.dumps({"FE": [{"transformationsData": {}, "feature": "CRIM", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "464", "mean": "3.51", "stddev": "8.33", "min": "0.00632", "max": "88.9762", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "ZN", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "464", "mean": "11.44", "stddev": "23.37", "min": "0.0", "max": "100.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "INDUS", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "464", "mean": "11.16", "stddev": "6.89", "min": "0.46", "max": "27.74", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "CHAS", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "464", "mean": "0.07", "stddev": "0.26", "min": "0.0", "max": "1.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "NOX", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "464", "mean": "0.55", "stddev": "0.12", "min": "0.385", "max": "0.871", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "RM", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "464", "mean": "6.29", "stddev": "0.7", "min": "3.561", "max": "8.78", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "AGE", "type": "real", "selected": "True", "replaceby": "mean", "stats": {
                                                                        "count": "464", "mean": "68.87", "stddev": "28.28", "min": "2.9", "max": "100.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "DIS", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "464", "mean": "3.81", "stddev": "2.12", "min": "1.1296", "max": "12.1265", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "RAD", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "464", "mean": "9.44", "stddev": "8.63", "min": "1.0", "max": "24.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "TAX", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "464", "mean": "407.39", "stddev": "167.11", "min": "187.0", "max": "711.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "PTRATIO", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "464", "mean": "18.43", "stddev": "2.17", "min": "12.6", "max": "22.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "B", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "464", "mean": "356.24", "stddev": "91.47", "min": "0.32", "max": "396.9", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "LSTAT", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "464", "mean": "12.67", "stddev": "7.18", "min": "1.73", "max": "37.97", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "MEDV", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "464", "mean": "22.64", "stddev": "9.31", "min": "5.0", "max": "50.0", "missing": "0"}, "transformation": ""}]}))

except Exception as ex:
    print(ex)
try:
    AutoML.functionRegression(BostonHousingPrices_AutoFE, [
                              "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"], "MEDV")

except Exception as ex:
    print(ex)
