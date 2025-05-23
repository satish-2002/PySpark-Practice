from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType, DoubleType, IntegerType

spark = SparkSession.builder.appName('udf_functions').getOrCreate()

# Defining user defined function --> string as argument
def captalize_string(str):
    res = ""
    arr = str.split(" ")
    for x in arr:
        res = res + x[0:1].upper() + x[1:len(x)] + " "
    return res

# Defining user defined function --> Integer value as single argument
def hike_sal(salary):
    return (salary / 10) + salary                                        # for 10% hike we can use (*1.10) to the salary

# Defining user defined function --> Integer values as multiple arguments
def new_sal(salary, hike):
    if salary is not None and hike is not None:
        return int((salary / 100 * hike) + salary)
    return None

#converting function to UDF
nameUDF = udf(lambda x: captalize_string(x),StringType())
salaryUDF = udf(hike_sal, DoubleType())
hikeUDF = udf(new_sal, IntegerType())

Data01 = [("satish","Developer","Platform_Services",80000,24,7),
    ("siva sai","Tester","Caremore",39000,27,10),
    ("sekhar kamala","Developer","HealthCare",36000,24,8),
    ("sanjay karthik","Tester","Members",29000,25,11)]
columns= ["name","role","department","salary","age","hike"]

# Creation of dataframe
df = spark.createDataFrame(Data01, columns)

df.select(col("department").alias("DEPARTMENT"), col("name").alias("NAME"), col("salary").alias("SALARY")).show(truncate=False)

# Calling User Defined Function by passing single argument
df.select(col("department").alias("DEPARTMENT"), nameUDF(col("name")).alias("NAME"), salaryUDF(col("salary")).alias("SALARY")).show(truncate=False)

# Calling User Defined Function by passing multiple arguments as parameters
df.select(col("department").alias("DEPARTMENT"), nameUDF(col("name")).alias("NAME"), hikeUDF(col("salary"),col("hike")).alias("SALARY")).show(truncate=False)
