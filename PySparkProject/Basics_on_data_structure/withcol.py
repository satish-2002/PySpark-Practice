import pyspark

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StringType, IntegerType

spark = SparkSession.builder.appName('with_column_func').getOrCreate()

data = [
    ("Satish", "Kollipaka", "8919903684", "Kakinada", "60000"),
    ("Ayyappa Maruthi", "Alapati", "7899891234", "Guntur", "120000"),
    ("Surya Prakash", "Kollipaka", "9391231991", "Kakinada", "20000"),
    ("Satish", "Kollipaka", "8919903684", "Kakinada", "60000"),
    ("Siva Sai", "Nekkala", "9934564212", "Pithapuram", "39000")
]

Columns = ["first_Name", "last_Name", "Phone", "Address", "Salary"]

df = spark.createDataFrame(data, Columns)
df.printSchema()
df.show(truncate=False)

df.withColumn("Salary",col("Salary").cast("Integer")).show(truncate=False)                                             # type change using withcolumn
hikedf = df.withColumn("Hike", (col("Salary")/10).cast(IntegerType()).cast(StringType()))                              # adding new col using withcolumn
hikedf.show(truncate=False)

hikeDF = hikedf.withColumn("Now",((col("Salary")+col("Hike"))).cast(IntegerType()).cast(StringType()))                 # adding new col (type change + withcolumn)
hikeDF.show(truncate=False)

print("withColumnRenamed")
finalHikeDF = hikeDF.withColumnRenamed("Salary", "old_Salary") \
                    .withColumnRenamed("Now","New_salary")  # Usage of withColumnRenamed
finalHikeDF.show(truncate=False)
finalHikeDF.drop("Hike").show(truncate=False)                                                                                   # dropping existing column

finalHikeDF.filter(finalHikeDF.Address == "Kakinada").show(truncate=False)                                                      # filter() on single column
finalHikeDF.filter(col("New_salary") > 50000).show(truncate=False)                                                              # filter() with col()
finalHikeDF.filter((col("New_salary") > 50000) | (col("Address") == "Kakinada")).show(truncate=False)                           # filter() on Multiple column

eastGodavari = ["Kakinada", "Samarlakota", "Pedhapuram", "Pithapuram", "Tuni", "Annavaram", "Rajanagaram", "Rajamundry", "Aleshwaram", "Gokavaram"]

finalHikeDF.filter(col("Address") .isin(eastGodavari)).show(truncate=False)                                                     # filter based on list values

finalHikeDF.distinct().show(truncate=False)                                                                                     # distinct() function
finalHikeDF.drop_duplicates(["last_Name","Address"]).show(truncate=False)                                                       # drop_duplicated() functions



