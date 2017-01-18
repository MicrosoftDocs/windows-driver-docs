---
title: SpbAccelerometer driver cookbook
author: windows-driver-content
description: SpbAccelerometer driver cookbook
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3E7875E1-0810-4698-A5E1-7A4C6C366967
---

# SpbAccelerometer driver cookbook


## Get started


This guide shows you how to get started using a sample diver that was developed for Windows 8.1 and earlier operating systems (the SpbAccelerometer sample driver).

**Note**  To evaluate the sensor driver sample for Windows 10 and later operating systems, see [Sensors sample driver](https://github.com/Microsoft/Windows-driver-samples/tree/master/sensors). For information about how to develop and build a sensor driver for Windows 10 and later operating systems, see [Write and deploy your universal sensor driver](write-and-deploy-your-universal-sensor-driver.md).

 

You’ll start by installing Windows on your Sharks Cove board. They you'll configure the accelerometer and attach it to the Sharks Cove board. Next, you'll install Microsoft Visual Studio Express and the Windows Driver Kit (WDK). Then, you’ll install the sample driver. Once you’ve completed these tasks, you can start exploring the sample driver.

For information about the Sharks Cove board, see [SharksCove.org](http://go.microsoft.com/fwlink/p/?linkid=403167).

### Required hardware

Before you get started, make sure you have the following hardware:

-   Sharks Cove board with included power cord and adapter.
-   [ADXL345](http://go.microsoft.com/fwlink/p/?linkid=401463) accelerometer/breakout board
-   USB hub
-   USB keyboard
-   USB mouse
-   USB network adapter
-   Monitor and HDMI cable (and possibly adapters)

### Document conventions

In the sections that describe the sample driver, you’ll see short tables after each section heading:

![document conventions](images/document-conventions.png)

These tables identify the source modules and classes discussed in that section. Use this information to open the module and view its corresponding code in Visual Studio.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20SpbAccelerometer%20driver%20cookbook%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


