---
title: Types of WDM Device Objects
author: windows-driver-content
description: Types of WDM Device Objects
ms.assetid: 89cc888d-3097-4637-96d2-6b9c59878d2f
keywords: ["functional device objects WDK kernel", "FDO WDK kernel", "physical device objects WDK kernel", "PDOs WDK kernel", "device objects WDK kernel , types", "filter DOs WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Types of WDM Device Objects


## <a href="" id="ddk-types-of-wdm-device-objects-kg"></a>


There are three kinds of WDM device objects:

1.  Physical Device Object (PDO) – represents a device on a bus to a [bus driver](bus-drivers.md).

2.  Functional Device Object (FDO) – represents a device to a [function driver](function-drivers.md).

3.  Filter Device Object (filter DO) – represents a device to a [filter driver](filter-drivers.md).

The three kinds of device objects are all of the type [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147), but are used differently and can have different device extensions.

A driver adds itself to the stack of drivers that handle I/O for a device by creating a device object ([**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)) and attaching it to the device stack ([**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300)). **IoAttachDeviceToDeviceStack** determines the current top of the device stack and attaches the new device object to the top of the device stack.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Types%20of%20WDM%20Device%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


