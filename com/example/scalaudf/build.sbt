name := "scala_udf"

scalaVersion := "2.11.12"

organization := "com.aliazg"

val sparkVersion = "2.4.0"

libraryDependencies += "org.apache.spark" %% "spark-core" % sparkVersion

libraryDependencies += "org.apache.spark" %% "spark-sql" % sparkVersion