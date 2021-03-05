<html>
<head>
<title>Update a Record in MySQL Database</title>
</head>
<body>

<?php
if(isset($_POST['update']))
{
$conn = mysqli_connect("localhost","20mca015","2394","20mca015");
if(! $conn )
{
  die('Could not connect: ' . mysqli_error());
}
$emp_id = $_POST['emp_id'];
$employee_name= $_POST['employee_name'];

$sql = "UPDATE Employee SET employee_name = $employee_name  WHERE emp_id = $emp_id";     

$retval = mysqli_query( $conn,$sql );
if(! $retval )
{
  die('Could not update data: ' . mysqli_error());
}
echo "Updated data successfully\n";
mysqli_close($conn);
}
else
{
?>
<form method="post" action="<?php $_PHP_SELF ?>">
<table width="400" border="0" cellspacing="1" cellpadding="2">
<tr>
<td width="100">Student_id</td>
<td><input name="id" type="text" id="emp_id"></td>
</tr>
<tr>
<td width="100">Mark</td>
<td><input name="employee-name" type="text" id="employee_name"></td>
</tr>
<tr>
<td width="100"> </td>
<td> </td>
</tr>
<tr>
<td width="100"> </td>
<td>
<input name="update" type="submit" id="update" value="Update">
</td>
</tr>
</table>
</form>
<?php
}
?>
</body>
</html>