# Databricks notebook source
# MAGIC %md
# MAGIC **Notebook Overview**
# MAGIC
# MAGIC This notebook demonstrates how to orchestrate and modularize code in Databricks notebooks using `%run` and `dbutils.notebook.run`. It includes examples of passing parameters, handling outputs, and managing exceptions effectively.

# COMMAND ----------

# MAGIC %md
# MAGIC ***%run***

# COMMAND ----------

# MAGIC %md
# MAGIC %run without parameters

# COMMAND ----------

# MAGIC %run "/Workspace/Users/ng5030180@gmail.com/Databricks - Run One notebook from another/Utils without Param"

# COMMAND ----------

print("Test Variable=",test_variable)
print("Area of Circle=",area_of_circle(8))

# COMMAND ----------

# MAGIC %md
# MAGIC %run with parameters

# COMMAND ----------

# MAGIC %run "/Workspace/Users/ng5030180@gmail.com/Databricks - Run One notebook from another/Utils with Param" $name = "Naveen" $radius = "12"

# COMMAND ----------

# MAGIC %md
# MAGIC ***DButils***

# COMMAND ----------

# MAGIC %md
# MAGIC DButils without Parameters

# COMMAND ----------

dbutils.notebook.run("/Workspace/Users/ng5030180@gmail.com/Databricks - Run One notebook from another/Utils with Param",60)

# COMMAND ----------

# MAGIC %md
# MAGIC ***DButils***

# COMMAND ----------

# MAGIC %md
# MAGIC DButils with Parameters

# COMMAND ----------

dbutils.notebook.run("/Workspace/Users/ng5030180@gmail.com/Databricks - Run One notebook from another/Utils with Param",60,{"name":"Naveen","radius":"50"})

# COMMAND ----------

# MAGIC %md
# MAGIC DButils receive Output

# COMMAND ----------

circle_area = dbutils.notebook.run("/Workspace/Users/ng5030180@gmail.com/Databricks - Run One notebook from another/Dbutils with output",60,{"name":"Naveen","radius":"40"})
print("Circle Area:",circle_area)

# COMMAND ----------

# MAGIC %md
# MAGIC DButils Handle Exceptions

# COMMAND ----------

try:
    output = dbutils.notebook.run("/Workspace/Users/ng5030180@gmail.com/Databricks - Run One notebook from another/Exception Handling",60,{"name":"Naveen","radius":"40"})
    print(output)
except Exception as e:
    print("Child notebook failed:",e)

# COMMAND ----------

