---
title: Function Drivers
author: windows-driver-content
description: Function Drivers
ms.assetid: a6ac329b-ffb0-4bd3-9d54-195fa025d532
keywords: ["function drivers WDK WDM", "raw mode WDK WDM", "WDM function drivers WDK"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Function Drivers


## <a href="" id="ddk-function-drivers-kg"></a>


A *function driver* is the main driver for a device (see the [Possible Driver Layers](types-of-wdm-drivers.md#possible-driver-layers) figure). A function driver is typically written by the device vendor and is required (unless the device is being used in [*raw mode*](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-raw-mode)). The PnP manager loads at most one function driver for a device. A function driver can service one or more devices.

A function driver provides the operational interface for its device. Typically the function driver handles reads and writes to the device and manages device power policy.

The function driver for a device can be implemented as a driver/minidriver pair, such as a port/miniport driver pair or a class/miniclass driver pair. In such driver pairs, the minidriver is linked to the second driver, which is a DLL.

If a device is being driven in raw mode, it has no function driver and no upper or lower-level filter drivers. All raw-mode I/O is done by the bus driver and optional bus filter drivers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Function%20Drivers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


