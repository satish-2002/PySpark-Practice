import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder.appName("RDD_to_DF example").getOrCreate()

#Creating empty RDD using emptyRDD() method
empty_rdd = spark.sparkContext.emptyRDD()
print("Empty RDD : ", empty_rdd.collect())

#Creating empty Dataframe using toDF() method
#df = empty_rdd.toDF()    ---->  It throws error because we need to pass schema to convert rdd to df
# Reason : RDD can hold structured / unstructured data whereas DF can hold only structured data.
sample_schema = StructType([
    StructField('Column1', StringType(),True),
    StructField('Column2', StringType(),True),
    StructField('Column3', IntegerType(),True)
])
#Creating empty dataframe using toDF() method
df = empty_rdd.toDF(sample_schema)
df.show()

#Creating empty dataframe using createDataFrame() method
df1 = spark.createDataFrame([],sample_schema)
df1.show()
df1.printSchema()

#Creating DF from RDD without schema
df2 = spark.createDataFrame([], StructType([]))
df2.show()

#Creating DF from RDD with Column names
marks = [("Ayyappa",89),("Satish",92),("Surya",85),("Siva",85)]    # list
marks_rdd = spark.sparkContext.parallelize(marks)                  # Creating RDD
df_columns = ["Names", "Marks"]                                    # Initializing  column names
marks_df = marks_rdd.toDF(df_columns)                              # Converting RDD to Dataframe & explicit schema by column names
marks_df.show(truncate=False)

#Creating DF from RDD with schema
schema = StructType([                                              # Initializing schema first
    StructField('Names', StringType(), True),
    StructField('Marks', IntegerType(),True)
])
marks_df1 = spark.createDataFrame(marks_rdd, schema)               # Converting RDD to Dataframe by mentioning rdd and schema directly
marks_df1.show(truncate=False)
