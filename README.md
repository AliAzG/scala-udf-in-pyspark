## General info
This project is a simple scala User Definde Function(UDF) that will be used in a pyspark file that is written in python.
By using scala UDFs in our PySpark codes we will see huge effect on performance and memory usage.
## Technologies
Project is created with:
* Python version: 2 or 3
* Scala version: 2.11.12
* SBT version: 1.0
* Spark version: 2.4.0
* Ubuntu version: 18.04
## Setup
To run this project, first install sbt using:
```
$ echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823
$ sudo apt-get update
$ sudo apt-get install sbt
```
and then make ```build.sbt``` file that contains configurations you want use in your project:
```
$ touch build.sbt
```
To build a jar file you need to run the command below where your scala file is:
```
$ sbt package
```
And in the end, when your jar file created successfully, you can run the pyspark code using:
```
$ spark-submit --jars path_to_your_jar_file/scala_udf_2.11-0.1.0-SNAPSHOT.jar test_scala_in_pyspark.py
```
