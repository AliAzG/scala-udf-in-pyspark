package com.ossl.scala_udf
import org.apache.spark.sql.expressions.UserDefinedFunction
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import java.sql.Timestamp
import java.util.{Calendar, Date}

object ScalaPySparkUDFs {

    def testFunction1(x: Timestamp): String = { 
        var calendar: Calendar = Calendar.getInstance();
        calendar.setTime(x);
        calendar.get(Calendar.HOUR_OF_DAY).toString;
     }

    def getFun(): UserDefinedFunction = udf(testFunction1 _ )
}