package com.example.scalaudf
import org.apache.spark.sql.expressions.UserDefinedFunction
import org.apache.spark.sql.functions._

// object StringLength {
//   def getStringLength(s: String) = s.length
//   def getFun(): UserDefinedFunction = udf(getStringLength _)
// }

object SumValue {
  def getSumToFive(value: Int) : Int = {
    var summed:Int = 0
    summed = value + 5
    return summed
  }
  def getFun(): UserDefinedFunction = udf(getSumToFive _)
}
