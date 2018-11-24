---
Description: Creating the Sensor Devices
title: Creating the Sensor Devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating the Sensor Devices


The sensor circuits are based on the sample circuits that are provided by Parallax in their sensor data sheets. These circuits are designed to integrate each sensor with the Parallax BS2 programmable microcontroller.

For example, the datasheet for the Ultrasonic distance sensor shows the following circuit diagram and image:

![ultrasonic distance sensor](images/ping_datasheet.png)

In this diagram, Pin 15 on the BS2 receives the sensor data. The firmware for each of the sensors is very similar. It consists of two primary functions: PollSensor and RetrieveInterval.

The code found in the PollSensor function varies from sensor to sensor. In the case of the Ultrasonic distance sensor, the PollSensor function issues a pulse with the ultrasonic transducer, listens for a response, and then measures the time that it takes for the response to occur.

```cpp
PollSensor:
  PULSOUT 15, 5
  PULSIN 15, 1, time
  cmDistance = cmConstant ** time
RETURN
```

The RetrieveInterval function is identical for every sensor. This function retrieves a new interval packet from the WPD driver (if one was sent), and then updates the interval property accordingly in the firmware. If no interval was received from the driver, the RetrieveInterval function invokes a default Timeout function. This function transmits the sensor data back to the WPD driver.

```cpp
RetrieveInterval:
    SERIN 16, 16780, Interval, Timeout, [DEC NewInterval]   &#39;Retrieve interval
    IF NewInterval >= 10 AND NewInterval <= 60000 THEN
      Interval = NewInterval
    ENDIF
RETURN
```

The Timeout function has the following format:

```cpp
Timeout:
  SEROUT 16, 16780, [DEC1 SensorID, DEC1 ElementSize, DEC1 ElementCount, DEC5 cmDistance, DEC5 Interval]
GOTO Main
```

Be aware that the Timeout function returns to the Main routine, which invokes PollSensor.

```cpp
Main:
  GOSUB PollSensor                   &#39;Determine distance
  GOSUB RetrieveInterval             &#39;Retrieve interval data
```

The following is the complete source code for the ultrasonic distance sensor:

```cpp
&#39; Smart Sensors and Applications - PingMeasureCmAndIn.bs2
&#39; Measure distance with Ping))) sensor and display in both in & cm
&#39; {$STAMP BS2}
&#39; {$PBASIC 2.5}
&#39; Conversion constants for room temperature measurements.
CmConstant CON 2260
&#39;InConstant CON 890
cmDistance VAR Word
&#39;inDistance VAR Word
time VAR Word
SensorID  VAR   Byte  &#39;Sensor identifier = 5 for PIR
ElementSize VAR Byte  &#39;Size (in bytes) of each element
ElementCount  VAR   Byte  &#39;Count of elements in packet
Padding VAR Byte      &#39;Padding for the 8-byte element

SensorID = 4
ElementSize = 1
ElementCount = 5      &#39;5bytes for distance data

NewInterval VAR  Word  &#39;New interval requested by user
Interval  VAR   Word   &#39;Interval value utlized by firmware

Interval = 2000
NewInterval = 2000


Main:
  GOSUB PollSensor                  &#39;Was motion detected?
  GOSUB RetrieveInterval            &#39;Retrieve units data

Timeout:
  SEROUT 16, 16780, [DEC1 SensorID, DEC1 ElementSize, DEC1 ElementCount, DEC5 cmDistance, DEC5 Interval]
GOTO Main

PollSensor:
  PULSOUT 15, 5
  PULSIN 15, 1, time
  cmDistance = cmConstant ** time
RETURN

RetrieveInterval:
    SERIN 16, 16780, Interval, Timeout, [DEC NewInterval]   &#39;Retrieve interval
    IF NewInterval >= 10 AND NewInterval <= 60000 THEN
      Interval = NewInterval
    ENDIF
RETURN
```

## <span id="related_topics"></span>Related topics


****
[The WpdBasicHardwareDriverSample](the-wpdbasichardwaredriver-sample.md)

[The WPD Driver Samples](the-wpd-driver-samples.md)

 

 





