---
title: Properties of Device Objects
author: windows-driver-content
description: Properties of Device Objects
ms.assetid: 6cd31263-e725-4a62-bec9-f40feb0b66cc
keywords: ["device objects WDK kernel , properties", "properties WDK device objects"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Properties of Device Objects


## <a href="" id="ddk-properties-of-device-objects-kg"></a>


Each device object has certain properties that describe the device and how the device object interacts with the system. The device object properties include:

-   Device type. Specifies the device's type of hardware. For more information about device types, see [Specifying Device Types](specifying-device-types.md).

-   Device characteristics. Specifies flags that provide additional information about the device. For more information, see [Specifying Device Characteristics](specifying-device-characteristics.md).

-   Exclusive access. Specifies whether the device object represents an *exclusive device*. If the device is exclusive, only one handle can be open for the device object at a time. (If the underlying device supports overlapped I/O, multiple threads of the same process can send requests through a single handle.) For more information, see [Specifying Exclusive Access to Device Objects](specifying-exclusive-access-to-device-objects.md).

-   Security descriptor. Device objects have a security descriptor that controls access to the device. For more information, see [Securing Device Objects](securing-device-objects.md).

For each of these properties, a default value can be set when the device object is created. For more information about creating device objects, see [Creating a Device Object](creating-a-device-object.md).

Values for device object properties can also be set in the registry. See [Setting Device Object Properties in the Registry](setting-device-object-properties-in-the-registry.md) for more information.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Properties%20of%20Device%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


