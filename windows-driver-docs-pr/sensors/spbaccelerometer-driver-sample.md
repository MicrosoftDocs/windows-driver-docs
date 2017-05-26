---
title: SpbAccelerometer driver sample
author: windows-driver-content
description: This sample UMDF driver controls an ADXL345 accelerometer that is connected to a simple peripheral bus (SPB).
ms.assetid: 5951CED5-13D5-44A4-862A-1C34E2122D99
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SpbAccelerometer driver sample


This sample UMDF driver controls an ADXL345 accelerometer that is connected to a simple peripheral bus (SPB).The ADXL345 is a low-power, 3-axis accelerometer that is capable of measuring up to +/-16g along each axis.

**Note**  The information in this section applies to Windows 8.1 and earlier operating systems. To evaluate the sensor driver sample for Windows 10 and later operating systems, see [Sensors sample driver](https://github.com/Microsoft/Windows-driver-samples/tree/master/sensors). For information about how to develop and build a sensor driver for Windows 10 and later operating systems, see [Write and deploy your universal sensor driver](write-and-deploy-your-universal-sensor-driver.md).

 

The sample is written with the assumption that the sensor is permanently connected to an I2C bus. The driver does not support Plug and Play. Instead, the ACPI system firmware for the hardware platform describes the sensor device's bus connection. The Plug and Play manager obtains the bus connection information from the ACPI driver, creates a connection ID to represent the bus connection, and passes the connection ID to the sample driver as a hardware resource. The sample driver uses the connection ID to open a logical connection to the sensor device, and obtains a handle to the connection. The driver specifies this handle as the target for I/O requests that it sends to the device.

Even if your system does not support a permanently connected ADXL345 sensor, you can use this sample as a reference for integrating other devices over SPB.

## Related topics
[Sensor driver development basics](sensor-driver-development-basics.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20SpbAccelerometer%20driver%20sample%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


