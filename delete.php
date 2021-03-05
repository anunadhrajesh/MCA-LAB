<?php
$con=mysqli_connect("localhost","20mca015","2394","20mca015");
$id=$_GET["id"];
if($con)
{

$qry1="delete from student_name where id='$id'";
if(mysqli_query($con, $qry1))
{
echo "Data Removed<br>";
} 
}
?>
