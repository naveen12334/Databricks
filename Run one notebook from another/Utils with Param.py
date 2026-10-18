# Databricks notebook source
dbutils.widgets.text("name","default_name")
dbutils.widgets.text("radius","5")

# COMMAND ----------

name = dbutils.widgets.get("name")
radius = float(dbutils.widgets.get("radius"))

# COMMAND ----------

def greet_user():
    return f"Hello, {name}!"

# COMMAND ----------

def area_of_circle(r):
    return 3.14159 * r * r

# COMMAND ----------

circle_area = area_of_circle(radius)

# COMMAND ----------

print(f"Helper notebook executed with name = {name}, radius = {radius}")

# COMMAND ----------

