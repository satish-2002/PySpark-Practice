import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
spark = SparkSession.builder.appName('Column Functions').getOrCreate()

data=[(101,76,18,'A'),(102,72,16,'A'),(103,64,14,'B'),(104,50,17,'C'),(105,66,None,'Absent'),(106,59,16,"B")]
df=spark.createDataFrame(data).toDF("SubjectCode","WrittenMarks","PracticalMarks","Grade")

#df.show()
df.select(df.WrittenMarks + df.PracticalMarks).show()                           # We can perform same on - * / % > < ==

#asc() & desc() functions
df.sort((df.WrittenMarks + df.PracticalMarks).desc()).show()                    # Descending order
df.sort(df.Grade.asc()).show()                                                  # Ascending order

#between() function
df.filter((col("WrittenMarks") + col("PracticalMarks")).between(75,90)).show()  # Between function

#startswith() & endswith() functions
df.filter(df.Grade.startswith('A')).show()                                      # startswith()
df.filter(df.Grade.endswith('sent')).show()                                     # endswith()

#isnull() & isnotnull() functions
df.filter(df.PracticalMarks.isNull()).show()                                     # isnull()
df.filter(df.PracticalMarks.isNotNull()).show()                                  # isnotnull()

#when(), between() & alias functions
df.select(df.SubjectCode, df.Grade,when(df.Grade == "A", "Distinction")     # A -> Distinction
          .when(df.Grade == "B", "First-Class")                             # B -> First Class
          .when(df.Grade == "C", "Second-Class")                            # C -> Second Class
          .when(df.Grade == "Absent", "Promoted")                           # Absent -> Promoted
          .otherwise("FAIL").alias("RESULTS")                                     # otherwise -> Fail
          ).show()