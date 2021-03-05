<html>
<head>
<?php
include 'con1.php';
?>
<style>
form{position:absolute;}
</style>
</head>
<body>
<form method="post">
Name:<input type="text" name="name"><br>
Rollno:<input type="text" name="rno"><br>
Gender:<input type="text" name="gen"><br>
Address:<input type="text" name="ad"><br>
<input type="submit" value="submit" name="sub">
<input type="submit" value="update" name="update">
<input type="submit" value="print"  name="print">
</form>
</body>
</html>
<?php
if(isset($_POST['sub']))
{
	$a=$_POST["name"];
	$b=$_POST["rno"];
	$c=$_POST["gen"];
	$d=$_POST["ad"];
	$sql="INSERT INTO STUREG (Name,Rollno,Gender,Addres) VALUES('$a','$b','$c','$d')";
	$f=mysqli_query($conn,$sql);
}
if(isset($_POST['update']))
{
	$sql1="UPDATE STUREG SET Rollno='20mca011' WHERE id=25";
}
$e=mysqli_query($con1,$sql1);
$l="SELECT * FROM rstudent";
$t=mysqli_query($conn,$l);
if(isset($_POST['print']))
{
	echo "<table>";
	echo "<tr>";
	echo "<td>Name</td>";
	echo "<td>Rollno</td>";
	echo "<td>Gender</td>";
	echo "<td>Addres</td>";
	echo "</tr>";
	while($s=mysqli_fetch_array($t))
	{
		echo "<tr>";
		echo "<td>".$s['Name']."</td>";
		echo "<td>".$s['Rollno']."</td>";
		echo "<td>".$s['Gender']."</td>";
		echo "<td>".$s['Addres']."</td>";
	}
	echo "</table>";
}
?>