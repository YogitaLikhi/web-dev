<?php
$num1=$_POST["n1"];
$num2=$_POST["n2"];
echo "Prime numbers: ";
for($i=$num1;$i<=$num2;$i++)
{
    $count=0;
    for($x=1;$x<=$i;$x++)
    {
        if(($i%$x)==0)
        {
            $count++;
        }
    }
    if($count==2)
    {
        echo $i," ";
    }
}
?>
