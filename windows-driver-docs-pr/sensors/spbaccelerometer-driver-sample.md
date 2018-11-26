---
title: SpbAccelerometer driver sample
description: This sample UMDF driver controls an ADXL345 accelerometer that is connected to a simple peripheral bus (SPB).
ms.assetid: 5951CED5-13D5-44A4-862A-1C34E2122D99
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SpbAccelerometer driver sample


This sample UMDF driver controls an ADXL345 accelerometer that is connected to a simple peripheral bus (SPB).The ADXL345 is a low-power, 3-axis accelerometer that is capable of measuring up to +/-16g along each axis.

**Note**  The information in this section applies to Windows 8.1 and earlier operating systems. To evaluate the sensor driver sample for Windows 10 and later operating systems, see [Sensors sample driver](https://github.com/Microsoft/Windows-driver-samples/tree/master/sensors). For information about how to develop and build a sensor driver for Windows 10 and later operating systems, see [Write and deploy your universal sensor driver](write-and-deploy-your-universal-sensor-driver.md).

 

The sample is written with the assumption that the sensor is permanently connected to an I2C bus. The driver does not support Plug and Play. Instead, the ACPI system firmware for the hardware platform describes the sensor device's bus connection. The Plug and Play manager obtains the bus connection information from the ACPI driver, creates a connection ID to represent the bus connection, and passes the connection ID to the sample driver as a hardware resource. The sample driver uses the connection ID to open a logical connection to the sensor device, and obtains a handle to the connection. The driver specifies this handle as the target for I/O requests that it sends to the device.

Even if your system does not support a permanently connected ADXL345 sensor, you can use this sample as a reference for integrating other devices over SPB.

## Related topics
[Sensor driver development basics](sensor-driver-development-basics.md)  



