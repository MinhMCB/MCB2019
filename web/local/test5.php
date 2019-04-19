<?php

    include "static/data.php";
    if(isset($_POST['Sensor1']))
    {    
        $conn = mysqli_connect($HOST, $USER,$PASSWORD);
        if(!$conn)
            echo "Connect Error ".mysqli_error();
        else
        {   
            mysqli_select_db($conn, $DATABASE);
            $RESULT = mysqli_query($conn, "SELECT * FROM $TABLE1 ORDER BY STT DESC LIMIT 1");
            $sensor = new Sensor1;
                $tmp = mysqli_fetch_assoc($RESULT);
                array_push($sensor->temp, $tmp["$COLUM_TEMP"]);
                array_push($sensor->hum, $tmp["$COLUM_HUM"]);
                array_push($sensor->time, $tmp["$COLUM_TIME"]);
            echo json_encode($sensor);
            mysqli_close($conn);
        }    
     }

	// copy paste tuong tu.
    if(isset($_POST['Sensor2']))
    {    
        $conn = mysqli_connect($HOST, $USER,$PASSWORD);
        if(!$conn)
            echo "Connect Error ".mysqli_error();
        else
        {   
            mysqli_select_db($conn, $DATABASE);
            $RESULT = mysqli_query($conn, "SELECT * FROM $TABLE2 ORDER BY STT DESC LIMIT 1");
            $sensor = new Sensor1;
                $tmp = mysqli_fetch_assoc($RESULT);
                array_push($sensor->temp, $tmp["$COLUM_TEMP"]);
                array_push($sensor->hum, $tmp["$COLUM_HUM"]);
                array_push($sensor->time, $tmp["$COLUM_TIME"]);
            echo json_encode($sensor);
            mysqli_close($conn);
        }    
     }

    if(isset($_POST['Sensor3']))
    {    
        $conn = mysqli_connect($HOST, $USER,$PASSWORD);
        if(!$conn)
            echo "Connect Error ".mysqli_error();
        else
        {   
            mysqli_select_db($conn, $DATABASE);
            $RESULT = mysqli_query($conn, "SELECT * FROM $TABLE3 ORDER BY STT DESC LIMIT 1");
            $sensor = new Sensor1;
                $tmp = mysqli_fetch_assoc($RESULT);
                array_push($sensor->temp, $tmp["$COLUM_TEMP"]);
                array_push($sensor->hum, $tmp["$COLUM_HUM"]);
                array_push($sensor->time, $tmp["$COLUM_TIME"]);
            echo json_encode($sensor);
            mysqli_close($conn);
        }    
     }

    if(isset($_POST['Sensor4']))
    {    
        $conn = mysqli_connect($HOST, $USER,$PASSWORD);
        if(!$conn)
            echo "Connect Error ".mysqli_error();
        else
        {   
            mysqli_select_db($conn, $DATABASE);
            $RESULT = mysqli_query($conn, "SELECT * FROM $TABLE4 ORDER BY STT DESC LIMIT 1");
            $sensor = new Sensor1;
                $tmp = mysqli_fetch_assoc($RESULT);
                array_push($sensor->temp, $tmp["$COLUM_TEMP"]);
                array_push($sensor->hum, $tmp["$COLUM_HUM"]);
                array_push($sensor->time, $tmp["$COLUM_TIME"]);
            echo json_encode($sensor);
            mysqli_close($conn);
        }    
     }

    if(isset($_POST['Sensor5']))
    {    
        $conn = mysqli_connect($HOST, $USER,$PASSWORD);
        if(!$conn)
            echo "Connect Error ".mysqli_error();
        else
        {   
            mysqli_select_db($conn, $DATABASE);
            $RESULT = mysqli_query($conn, "SELECT * FROM $TABLE5 ORDER BY STT DESC LIMIT 1");
            $sensor = new Sensor1;
                $tmp = mysqli_fetch_assoc($RESULT);
                array_push($sensor->temp, $tmp["$COLUM_TEMP"]);
                array_push($sensor->hum, $tmp["$COLUM_HUM"]);
                array_push($sensor->time, $tmp["$COLUM_TIME"]);
            echo json_encode($sensor);
            mysqli_close($conn);
        }    
     }
?>
