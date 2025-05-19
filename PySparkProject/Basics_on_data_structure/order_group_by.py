from os import truncate

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, min, max

spark = SparkSession.builder.appName("orderby sort").getOrCreate()

simpleData = [("Satish","","Developer","Platform_Services",80000,24,35000),
    ("Siva","Sai","Tester","Caremore",39000,27,40000),
    ("Sekhar","","Developer","HealthCare",39000,24,30000),
    ("Sanjay","Karthik","Tester","Members",39000,25,28000),
    ("Ayyappa","Maruthi","Developer","Platform_Services",120000,30,40000),
    ("Akhill","","Developer","Caremore",160000,32,25000),
    ("Lok","Sai","Developer","Members",180000,28,35000),
    ("Hari","Chandana","Tester","Platform_Services",80000,26,18000),
    ("Manasa","","Support","Claims",40000,24,24000)
  ]
columns= ["fname", "lname", "role","department","salary","age","bonus"]

df = spark.createDataFrame(simpleData, columns)
df.show(truncate=False)

df.sort("age","salary").show(truncate=False)                                                                      # sorting on multiple columns
df.sort(col("age"),col("bonus")).show(truncate=False)                                                             # sorting using col() function

df.orderBy("age","salary").show(truncate=False)                                                                   # order by on multiple columns
df.orderBy(col("department"),col("role")).show(truncate=False)                                                    # order by using col() function

df.sort(df.lname.asc(), df.salary.desc()).show(truncate=False)                                                    # sort with ascending and descending orders
df.sort(col("age"),col("salary"), ascending=[True, False]).show(truncate=False)                                   # sort(), col(), asc(), desc()
df.orderBy(col("lname").asc(), col("bonus").desc()).show(truncate=False)                                          # order by(), col(), asc(), desc()

df.createOrReplaceTempView("Emp_data")                                                                                  # Creation of temporary view
spark.sql("select fname, role, department, age, salary, bonus from Emp_data ORDER BY age asc").show(truncate=False)     # sql query statement for order by with asc
spark.sql("select fname, role, department, age, salary, bonus from Emp_data ORDER BY salary desc").show(truncate=False) # sql query statement for order by with desc

df.groupBy("department").count().show(truncate=False)                                                                   # Basic group by statement with count()
df.groupBy("department", "role").sum("bonus").show(truncate=False)                                                      # sum() min() max() count() mean() avg() pivot()
                                                                                                                        # group by with multiple aggregation functions
df.groupBy("department").agg \
        (max("age").alias("experience"), \
         min("bonus").alias("min_bonus"), \
         avg("salary").alias("avg_salary")).show(truncate=False)
                                                                                                                        # group by with multiple agg functions & where clause
df.groupBy("department").agg \
         (min("salary").alias("min_salary"), \
         max("salary").alias("max_salary"), \
         avg("bonus").alias("avg_bonus")) \
    .where(col("avg_bonus") >= 30000).show(truncate=False)
                                                                                                                        # sql query for group by with having clause
sql_string = """ SELECT department,                                                                                                
                 SUM(salary) as dept_budget,
                 AVG(bonus) as avg_bonus_allotted
                 from Emp_data GROUP BY department HAVING AVG(bonus) >= 30000 """
df2 = spark.sql(sql_string)
df2.show(truncate=False)
