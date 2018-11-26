---
title: SpbAccelerometer driver overview
description: This sample UMDF driver controls an ADXL345 accelerometer that is connected to a simple peripheral bus (SPB).
ms.assetid: 355C753D-E5E3-4F8B-B16F-45EFA1E741F3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SpbAccelerometer driver overview


This sample UMDF driver controls an ADXL345 accelerometer that is connected to a simple peripheral bus (SPB).The ADXL345 is a low-power, 3-axis, accelerometer that can measure +/-16g along each axis. This sensor supports both the SPI and I2C transports; the sample driver supports the I2C transport. (You can order an ADXL345 and breakout board from [SparkFun](http://go.microsoft.com/fwlink/p/?linkid=401463).)

Even if your system doesn't support this sensor, you can use the sample driver as a reference for integrating other devices over I2C.

 

 




