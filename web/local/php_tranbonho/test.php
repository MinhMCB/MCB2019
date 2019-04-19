<?php

        include "static/data.php";
  
        $conn = mysqli_connect($HOST, $USER,$PASSWORD);
        if(!$conn)
            echo "Connect Error ".mysqli_error();
        else
        {   
            mysqli_select_db($conn, $DATABASE);
            $demSTT = mysqli_query($conn, "SELECT * FROM $TABLE ORDER BY STT DESC LIMIT 1");
	    $tmpp = mysqli_fetch_assoc($demSTT);
	    $length = $tmpp["STT"];
	    echo $length;

	    $RESULT = mysqli_query($conn, "SELECT $COLUM_TEMP, $COLUM_HUM, $COLUM_TIME FROM $TABLE WHERE STT > ($length-3)");
            $num = mysqli_num_rows($RESULT);
	    echo $num;
            $sensor = new Sensor1;
            for($i=0; $i<$num; $i++)
            {
                $tmp = mysqli_fetch_assoc($RESULT);
                array_push($sensor->temp, $tmp["$COLUM_TEMP"]);
                array_push($sensor->hum, $tmp["$COLUM_HUM"]);
                array_push($sensor->time, $tmp["$COLUM_TIME"]);
            }
            echo json_encode($sensor);
            mysqli_close($conn);
	}
	echo "thanhminh"    

?>
