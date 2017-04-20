---
title: SpbAccelerometer driver overview
author: windows-driver-content
description: This sample UMDF driver controls an ADXL345 accelerometer that is connected to a simple peripheral bus (SPB).The ADXL345 is a low-power, 3-axis, accelerometer that can measure +/-16g along each axis.
ms.assetid: 355C753D-E5E3-4F8B-B16F-45EFA1E741F3
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SpbAccelerometer driver overview


This sample UMDF driver controls an ADXL345 accelerometer that is connected to a simple peripheral bus (SPB).The ADXL345 is a low-power, 3-axis, accelerometer that can measure +/-16g along each axis. This sensor supports both the SPI and I2C transports; the sample driver supports the I2C transport. (You can order an ADXL345 and breakout board from [SparkFun](http://go.microsoft.com/fwlink/p/?linkid=401463).)

Even if your system doesn't support this sensor, you can use the sample driver as a reference for integrating other devices over I2C.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20SpbAccelerometer%20driver%20overview%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


