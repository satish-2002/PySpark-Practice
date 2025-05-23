from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import MapType, StringType

spark = SparkSession.builder.appName('json_functions').getOrCreate()

jsonString = """{"id":227, "Name":"Satish", "Role":"Developer", "salary":80000}"""
df01 = spark.createDataFrame([(1, jsonString)],["s_no","value"])
df01.show(truncate=False)                                                                                               # dataframe

df02 = df01.withColumn("value",from_json(df01.value,MapType(StringType(),StringType())))                        # conversion of json data to dataframe format
df02.show(truncate=False)

df02.withColumn("value",to_json(col("value"))).show(truncate=False)                                             # conversion of dataframe to json format

df01.select(json_tuple(col("value"),"id","Name","salary")).toDF("id","Name","salary").show(truncate=False) # created new rows from json format

df01.select(get_json_object(col("value"),"$.Name").alias("Name")).show(truncate=False)                             # printing particular json object