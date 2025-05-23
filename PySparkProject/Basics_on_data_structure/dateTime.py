from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName('date_time_functions').getOrCreate()

Data01 = [("227","satish","2002-01-16"),
    ("239","siva sai","1998-10-02"),
    ("214","sai pavan","2001-10-14"),
    ("231","karim","2002-09-28")]
df = spark.createDataFrame(Data01, ["id","name","dob"])

Data02 = [("227","satish","16-01-2002 08 10 19 06"),
    ("239","siva sai","02-10-1998 11 01 19 06"),
    ("214","sai pavan","14-10-2001 12 05 19 06"),
    ("231","karim","28-09-2002 19 01 19 06")]
df02 = spark.createDataFrame(Data02, ["id","name","dob_timestamp"])

df.select(col("id"), col("name"), col("dob"), current_date().alias("Current_date")).show(truncate=False)                         #current_date
df.select(col("id"),col("name"),col("dob"),date_format(col("dob"),"dd-MM-yyyy").alias("Date_format")).show(truncate=False)#date_format
df.select(col("id"),col("name"),col("dob"),datediff(current_date(),col("dob")).alias("Date_diff")).show(truncate=False)          #datediff
df.select(col("id"),col("name"),col("dob"),months_between(current_date(),col("dob")).alias("Months")).show(truncate=False)       #months_between
df.select(col("id"),col("name"),col("dob"),add_months(col("dob"),3).alias("+3 months")).show(truncate=False)             #add_months
df.select(col("id"),col("name"),col("dob"),date_add(col("dob"),90).alias("Prob ends")).show(truncate=False)                #date_add / date_sub
df.select(col("id"),col("name"),year(col("dob")).alias("YEAR"),month(col("dob")).alias("MONTH")).show(truncate=False)            #month / year / day
df.select(col("id"),col("name"),col("dob"),next_day(col("dob"),"friday").alias("NEXT_DAY")).show(truncate=False)      #next_day
df.select(col("id"),col("name"),col("dob"),weekofyear(col("dob")).alias("WEEK OF THE YEAR")).show(truncate=False)                #weekofyear
df.select(col("id"),col("name"),col("dob"),dayofyear(col("dob")).alias("DAY OF THE YEAR")).show(truncate=False)                  #dayofyear()
df.select(col("id"),col("name"),col("dob"),current_timestamp().alias("Current timestamp")).show(truncate=False)                  #current_timestamp()

#Usage of to_timestamp function
df02.select(col("id"),col("name"),col("dob_timestamp"),to_timestamp(col("dob_timestamp"), "dd-MM-yyyy HH mm ss SSS").alias("timestamp")).show(truncate=False)