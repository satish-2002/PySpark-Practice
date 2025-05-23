'''union() method of the DataFrame is used to merge two DataFrame’s of the same structure/schema.
 The output includes all rows from both DataFrames and duplicates are retained. If schemas are not the same it
 returns an error. To deal with the DataFrames of different schemas we need to use unionByName() transformation.'''
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('union_functions').getOrCreate()

Data01 = [("Satish","","Developer","Platform_Services",80000,24,35000),
    ("Siva","Sai","Tester","Caremore",39000,27,40000),
    ("Sekhar","","Developer","HealthCare",39000,24,30000),
    ("Sanjay","Karthik","Tester","Members",39000,25,28000)]

Data02 = [("Ayyappa","Maruthi","Developer","Platform_Services",120000,30,40000),
    ("Akhill","","Developer","Caremore",160000,32,25000),
    ("Siva","Sai","Tester","Caremore",39000,27,40000),
    ("Lok","Sai","Developer","Members",180000,28,35000),
    ("Hari","Chandana","Tester","Platform_Services",80000,26,18000),
    ("Manasa","","Support","Claims",40000,24,24000)]

columns= ["fname", "lname", "role","department","salary","age","bonus"]

df01 = spark.createDataFrame(Data01, columns)
df02 = spark.createDataFrame(Data02, columns)

# NOTE : In pyspark there is no concept of unionALL because here union and unionALL both works as same union doesn't remove duplicates here.
# To work like union you can use the .dropDuplicates() transformation after performing the union() or apply .distinct() to remove the duplicates.
#     SQL              pyspark
#    UNION   --->  union().distinct()
#   UNIONALL --->    unionAll()

union_df = df01.union(df02)                                                                  # Simple union() statement --> allow duplicates
union_df.show(truncate=False)
df01.union(df02).distinct().show(truncate=False)                                             # union() statement --> filtering duplicates by using .distinct()
union_df.dropDuplicates().show(truncate=False)                                               # usage of dropDuplicates after union of dataframes
df01.unionAll(df02).show(truncate=False)                                                     # unionAll() statement

Data03 = [("Satish","","Developer","Platform_Services",80000,35000,24),
    ("Siva","sai","Tester","Caremore",39000,40000,27),
    ("Sanjay","karthik","Tester","Members",39000,28000,25)]

new_col = ["fname","lname","role","department","salary","bonus","age"]                       # dataframe with not-inline column names
df03 = spark.createDataFrame(Data03, new_col)

df02.unionByName(df03).show(truncate=False)                                                  # unionByName() statement

Data04 = [("Satish","Developer","Platform_Services",80000,35000,24),
    ("Siva","Tester","Caremore",39000,40000,27),
    ("Sanjay","Tester","Members",39000,28000,25)]

new_cols = ["fname","role","department","salary","bonus","age"]                              # dataframe with missing column names
df04 = spark.createDataFrame(Data04, new_cols)

df02.unionByName(df04, allowMissingColumns=True).show(truncate=False)                        # unionByName() and allowMissingColumns statement