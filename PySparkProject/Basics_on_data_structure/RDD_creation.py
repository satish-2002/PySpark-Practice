import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Sample RDD example").getOrCreate()

#Creating empty RDD using emptyRDD() method
empty_rdd = spark.sparkContext.emptyRDD()
print("Empty RDD : ", empty_rdd.collect())

#Creating rdd using range() method
rdd = spark.sparkContext.range(0,10)
print("RDD by using range method:", rdd.collect())
#To print no. of partitions. No. of partitions is depending upon the CPU cores available to the spark
print("RDD partitions :", rdd.getNumPartitions())

#Creating rdd by using python list
names = ["Ayyappa", "Satish", "Surya", "Siva"]
rdd_names = spark.sparkContext.parallelize(names)
print("RDD by using list:", rdd_names.collect())