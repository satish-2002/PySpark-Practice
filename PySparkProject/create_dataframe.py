from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("exampleofdataframe").getOrCreate()

data = [(1,'gopi',100),(2,'ayyappa',200),(3,'mahesh',300),(4,'prasanth',400),(5,'bhargav',500)]

columns = ['id','name','salary']
rdd1 = spark.sparkContext.parallelize(data)

df = spark.createDataFrame(rdd1).toDF(*columns)

df.show(truncate=False)