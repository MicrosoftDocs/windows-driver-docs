---
title: Microcontroller commands for MALT
description: Defines commands between the PC and the microcontroller (Arduino) that is controlling the sensors in the MALT.
ms.date: 07/08/2021
---

# Microcontroller commands for MALT

This topic defines commands between the PC and the microcontroller (Arduino) that is controlling the sensors in the MALT. We recommended that the PC controlling the microcontroller is also the system or device under test (SUT/DUT).  

## Serial command interface

Communicate with the test rig via the following serial commands. 
Each command will write to and read from serial over a series of lines.


### LIGHT *light level*

Adjusts the light level based on the given input.

The [light panel](https://www.superbrightleds.com/moreinfo/led-panel-light/square-12v-led-panel-light-fixture-1ft-x-1ft-35w/2184/) used in the reference supports between .25 and 1.3 volts of input.

Using the data sheet for the reference DAC [Microchip MCP4821](https://www.microchip.com/wwwproducts/en/MCP4821), we can solve for the maximum *Vout* to send to the light panel.

1.3 = 2.048 * 1 * (D/(2^12))

D = 2600

**Example:** 

The following example sends the voltage required to get the light at maximum brightness (based on formula above).

```cmd
LIGHT 2600
```



**Serial output:**

| Line 0                |
|-----------------------|
| MALTERROR status code |

### READALSSENSOR *sensor number*

Sensor numbers are defined as follows:

1. Ambient Light Sensor (facing away from the screen)
2. Screen Light Sensor (facing toward the screen)

**Example:**

The following example writes the resulting raw data from the screen light sensor to serial. Lux can be calculated based on the [datasheet](https://www.ti.com/product/OPT3001) of sensors used.

```cmd
READALSSENSOR 2
```

**Serial output:**

| Line 0                  | Line 1                | Line 2                |
|-------------------------|-----------------------|-----------------------|
| Exponent (0 on failure) | Result (0 on failure) | MALTERROR status code |

### READCOLORSENSOR *sensor number*

Sensor numbers are defined as follows:

1. Ambient Color Sensor (facing away from the screen)
2. Screen Color Sensor (facing toward the screen)

**Example:**

The following example writes the resulting data from the screen color sensor to serial. These numbers have gone through an onboard calibration matrix to be converted to the XYZ colorspace.

```cmd
READCOLORSENSOR 2
```

**Serial output:**

| Line 1  | Line 2  | Line 3  |        Line 4         |
|---------|---------|---------|-----------------------|
| X value | Y value | Z value | MALTERROR status code |

### CONVERSIONTIME *conversion time in ms*

The [OPT3001](https://www.ti.com/product/OPT3001) light sensors used in the reference support 2 conversion times: 800ms and 100ms.
CONVERSIONTIME changes the conversion time of both sensors.

> [!NOTE] 
> If a measurement conversion is in progress when the configuration register is written, the active measurement conversion immediately aborts.

**Example:** 

The following example changes the conversion time of both sensors to 100ms.

The default conversion time used by MALT prototype is 800ms.

```cmd
CONVERSIONTIME 100
```

**Serial output:**

| Line 0                |
|-----------------------|
| MALTERROR status code |

### Unrecognized commands

For any unrecognized command: 

**Serial output:**

| Line 0                                                                        |
|-------------------------------------------------------------------------------|
| MALTERROR status code (where MALTERROR status code = `E_UNRECOGNIZED_COMMAND`)|



## MALT error code

| E_SUCCESS | E_INVALID_PARAM | E_UNRECOGNIZED_COMMAND |
|-----------| --------------- | ---------------------- |
| 0         | 1               | 2                      |
