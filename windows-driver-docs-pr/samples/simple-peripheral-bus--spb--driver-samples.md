---
title: Simple peripheral bus (SPB) driver samples
author: windows-driver-content
description: The driver samples in this directory provide a starting point for writing a custom driver for your device.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: E9A667EA-3AE5-4A0E-BC3F-CD442141886B
---

# Simple peripheral bus (SPB) driver samples


The driver samples in this directory provide a starting point for writing a custom driver for your device.

## Simple peripheral bus (SPB)


| Sample Name                | Solution                                                       | Description                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Skeleton I2C Sample Driver | [SkeletonI2C](http://go.microsoft.com/fwlink/p/?LinkId=617969) | Demonstrates how to design a KMDF controller driver for Windows that conforms to the simple peripheral bus (SPB) device driver interface (DDI). SPB is an abstraction for low-speed serial buses (for example, I2C and SPI) that allows peripheral drivers to be developed for cross-platform use without any knowledge of the underlying bus hardware or device connections. |
| SpbTestTool                | [SpbTestTool](http://go.microsoft.com/fwlink/p/?LinkId=617970) | Demonstrates how to open a handle to the [SPB controller](https://msdn.microsoft.com/windows/hardware/drivers/spb/spb-controller-drivers), use the SPB interface from a KMDF driver, and employ GPIO [passive-level interrupts](https://msdn.microsoft.com/windows/hardware/drivers/wdf/supporting-passive-level-interrupts).                                                 |

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdkappendix\wdkappendix%5D:%20Simple%20peripheral%20bus%20%28SPB%29%20driver%20samples%20%20RELEASE:%20%289/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


