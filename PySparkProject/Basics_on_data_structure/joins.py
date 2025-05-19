''' PySpark Join is used to combine two DataFrames and by chaining these you can join multiple DataFrames;
 it supports all basic join type operations available in traditional SQL like
 INNER, LEFT OUTER, RIGHT OUTER, LEFT ANTI, LEFT SEMI, CROSS, SELF JOIN.'''

import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('join_functions').getOrCreate()

employee_Data = [("Satish","","Developer",165,80000,24,35000),
    ("Siva","Sai","Tester",125,39000,27,40000),
    ("Sekhar","","Developer",172,39000,24,30000),
    ("Sanjay","Karthik","Tester",452,39000,25,28000),
    ("Ayyappa","Maruthi","Developer",165,120000,30,40000),
    ("Akhill","","Developer",125,160000,32,25000),
    ("Lok","Sai","Developer",452,180000,28,35000),
    ("Hari","Chandana","Tester",165,80000,26,18000),
    ("Manasa","","Support",93,40000,24,24000),
    ("Hari", "Krishnan", "Manager", 323, 220000, 43, 35000)
  ]
emp_columns = ["fname", "lname", "role","project_id","salary","age","bonus"]

emp_df = spark.createDataFrame(employee_Data, emp_columns)

dept_details = [("165", "Platform_Services"),
                ("172", "HealthCare"),
                ("125", "Caremore"),
                ("452", "Members"),
                ("93", "Claims"),
                ("123", "Medicaid")]
dept_columns = ["dept_id", "dept_name"]

dept_df = spark.createDataFrame(dept_details, dept_columns)

emp_df.show(truncate=False)
dept_df.show(truncate=False)
inner_df = emp_df.join(dept_df,emp_df.project_id == dept_df.dept_id, "inner")                                      # inner
inner_df.show(truncate=False)
left_df = emp_df.join(dept_df,emp_df.project_id == dept_df.dept_id, "left")                                        # left / leftouter
left_df.show(truncate=False)
leftsemi_df = emp_df.join(dept_df,emp_df.project_id == dept_df.dept_id, "leftsemi")                                # leftsemi
leftsemi_df.show(truncate=False)
leftanti_df = emp_df.join(dept_df,emp_df.project_id == dept_df.dept_id, "leftanti")                                # leftanti
leftanti_df.show(truncate=False)
right_df = emp_df.join(dept_df,emp_df.project_id == dept_df.dept_id, "right")                                      # right / rightouter
right_df.show(truncate=False)
#Note: PySpark does not directly support right_semi or right_anti joins — you'd need to reverse the DataFrames
full_outer_df = emp_df.join(dept_df, emp_df.project_id == dept_df.dept_id, "outer")                                # full / outer / fullouter
full_outer_df.show(truncate=False)

emp_df.createOrReplaceTempView("EMP")                                                                                   # Creation of view for emp table
dept_df.createOrReplaceTempView("DEPT")                                                                                 # Creation of view for dept table

sql_string = spark.sql("Select * from EMP e, DEPT d WHERE e.project_id == d.dept_id").show(truncate=False)              # SQL query to join using where clause
join_DF = spark.sql("Select * from EMP e INNER JOIN DEPT d WHERE e.project_id == d.dept_id").show(truncate=False)       # SQL query to join using join condition

tech_data = [("Developer", ("Python", "JAVA", ".Net", "Pyspark", "SQL", "MongoDB")),
    ("Tester", ("Selenium", "Excel", "SQL", "MongoDB","","")),
    ("Support", ("API", "Excel", "UI/UX","","","")),
    ("Manager", ("Managing", "Directing", "Commanding","","",""))]
tech_columns = ["Designation", "Skills"]

tech_df = spark.createDataFrame(tech_data, tech_columns)
tech_df.show(truncate=False)
                                                                                                                        # SQL join on multiple dataframes
emp_df.join(dept_df, emp_df.project_id == dept_df.dept_id, 'inner')\
      .join(tech_df, emp_df.role == tech_df.Designation, 'inner').show(truncate=False)