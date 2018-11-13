//////////////////////////////
/// print words in an array
val inuputwords = List("word1","word2","word3","word4","word5","word6","word7","word8")
val words = sc.parallelize(inuputwords)

for (word <- words.collect()) println(word) 

//////////////////////////////
/// count
val inuputwords = List("word1","word2","word3","word4","word5","word6","word7","word8")
val words = sc.parallelize(inuputwords)
println(words.count())
println(words.countByValue()) //gives a list
for (count <- words.countByValue()) print(count) //prints the map of each word to its count
for ((word,count) <- words.countByValue()) println(word + "occurs " + count + " times") (edited)

//////////////////////////////
/// biased take
val inputwords = List("word1","word2","word3","word4","word5","word6","word7","word8")
val words = sc.parallelize(inputwords)
words.take(90)   ///doesn't error even if the size is greater than the array size
val inputwords = List("word1","word2","word3","word4","word5","word6","word7","word8")
val words = sc.parallelize(inputwords)
words.take(3).saveAsTextFile(words.take("test.txt")

//////////////////////////////
/// redcue
val inputwords = List("word1","word2","word3","word4","word5","word6","word7","word8")
val numbers = List(1,2,3,4)
val words = sc.parallelize(inputwords)
val nums = sc.parallelize(numbers)
val sum = words.reduce((x,y) => x + y) //string concatenation
println(sum)
val intsum = nums.reduce((x,y) => x+y) //cannot reuse variable sum here it has been typed to a string now so use a new variable
println(intsum)

//////////////////////////////
/// sum from file
val file = sc.textFile("/zeppelin/test/test.txt")  ///file in the docker,is reading well but not writing to it
val prime = "2,3,5,7,9,,11,13,17,,19"
val content = sc.parallelize(prime)
val numbers = file.flatMap(lines => lines.split(","))
val non_zero = numbers.filter(x => !x.isEmpty)
val num = non_zero.map(x => x.toInt)
val sum = num.reduce((x,y) => x + y)
/// sum and print the formatted list
val file = sc.textFile("/zeppelin/test/test.txt")
val prime = "2,3,5,7,9,,11,13,17,,19"
val content = sc.parallelize(prime)
val numbers = file.flatMap(lines => lines.split(","))
val non_zero = numbers.filter(x => !x.isEmpty)
val num = non_zero.map(x => x.toInt)
for (i <- num.collect()) println(i)
val sum = num.reduce((x,y) => x + y)


//////////////////////////////
/// find type

val file = sc.textFile("/zeppelin/test/test.txt")
val prime = "2,3,5,7,9,,11,13,17,,19"
val content = sc.parallelize(prime)
val numbers = file.flatMap(lines => lines.split(","))
val non_zero = numbers.filter(x => !x.isEmpty)
val num = non_zero.map(x => x.toInt)
for (i <- num.collect()) println(i)
val sum = num.reduce((x,y) => x + y)
numbers
num
sum


//////////////////////////////
/// pairrdd/tuples

//method 1 to create the rdd  from a list of tuples
val flower = List(("rose",1),("daisy",2),("lily",3))
for (i<- flower){
   print(i._1) //key element
   print(i._2) // value element
   println()
}
//split and cretae key value pairs and then map them
val f_list = List("rose 1","daisy 2","lily 3")
val key_value = sc.parallelize(f_list).map(x => (x.split(" ")(0),x.split(" ")(1)))
for ((i,y) <- key_value.collect()){
   println(i,y)
}
key_value.saveAsTextFile("/zeppelin/test/out.txt")


