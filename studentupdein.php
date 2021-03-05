 <?php
$servername = "localhost";
$username = "20mca015";
$password = "2394";
$dbname = "20mca015";

$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

$sql = "UPDATE STUDENTS SET name=wedrt WHERE mark=23";
$sql = "UPDATE STUDENTS SET mark=23 WHERE mark=1";

if (mysqli_query($conn, $sql)) {
  echo "Record updated successfully";
} else {
  echo "Error updating record: " . mysqli_error($conn);
}

mysqli_close($conn);
 {
         ?>
               <form method = "post" action = "<?php $_PHP_SELF ?>">
                  <table width = "400" border =" 0" cellspacing = "1" 
                     cellpadding = "2">
                  
                     <tr>
                        <td width = "100">STUDENT NAME</td>
                        <td><input name = "name" type = "text" 
                           id = "name"></td>
                     </tr>
                  
                     <tr>
                        <td width = "100">BRANCH</td>
                        <td><input name = "branch" type = "text" 
                           id = "branch"></td>
                     </tr>
                     <tr>
                        <td width = "100">MARK</td>
                        <td><input name = "mark" type = "text" 
                           id = "mark"></td>
                     </tr>
                  
                        <td>
                           <input name = "update" type = "submit" 
                              id = "update" value = "Update">
                        </td>
                     </tr>
                  
                  </table>
               </form>
            <?php
         }
      ?>
      
   </body>
</html