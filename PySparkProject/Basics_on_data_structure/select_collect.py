from os import truncate
import pyspark

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StringType, StructType, StructField

spark = SparkSession.builder.appName('select and collect usage').getOrCreate()

Nested_Customer_Data = [
    (("Satish", "Kollipaka"), "8919903684", "Kakinada", 60000),
    (("Ayyappa Maruthi", "Alapati"), "7899891234", "Guntur", 120000),
    (("Surya Prakash", "Kollipaka"), "9391231991", "Kakinada", 20000),
    (("Siva Sai", "Nekkala"), "9934564212", "Pithapuram", 39000)
]

Columns = ["Names", "Phone", "Address", "Salary"]

df = spark.createDataFrame(Nested_Customer_Data, Columns)
df.show(truncate=False)

df.select("Names").show(truncate=False)                                      # Simple select statement
df.select(df.Names, df.Phone).show(truncate=False)                           # Simple select statement
df.select(col("Names"), col("Address")).show(truncate=False)                 # select statement with col()
df.select(df["Names"], df["Salary"]).show(2, truncate=False)              # Simple select statement with show count
df.select(*Columns).show(2, truncate=False)                               # multiple select statement

df.select(df.columns[2]).show(2, truncate=False)                          # select with indexing
df.select(df.columns[2:4]).show(3, truncate=False)                        # select with slicing

schema = StructType([                                                        # Defining Schema
    StructField("Name", StructType([
        StructField("FirstName", StringType(), True),
        StructField("LastName", StringType(), True),])),
    StructField("Phone", StringType(), True),
    StructField("Address", StringType(), True),
    StructField("Salary", StringType(), True)
])

DF = spark.createDataFrame(Nested_Customer_Data, schema)
#DF.show(truncate=False)

DF.select("Name.FirstName", "Name.LastName", "Address").show(truncate=False)  # Select on Nested columns
DF.select("Name.*", "Salary").show(truncate=False)                            # selecting all child columns

dataCollect = DF.collect()
print(dataCollect)                                                            # Collect usage

for row in dataCollect:                                                       # for loop on datacollect
    print(row['Name']['FirstName'] , row['Phone'])
