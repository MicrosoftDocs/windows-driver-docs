---
title: Properties of Device Objects
description: Properties of Device Objects
ms.assetid: 6cd31263-e725-4a62-bec9-f40feb0b66cc
keywords: ["device objects WDK kernel , properties", "properties WDK device objects"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Properties of Device Objects





Each device object has certain properties that describe the device and how the device object interacts with the system. The device object properties include:

-   Device type. Specifies the device's type of hardware. For more information about device types, see [Specifying Device Types](specifying-device-types.md).

-   Device characteristics. Specifies flags that provide additional information about the device. For more information, see [Specifying Device Characteristics](specifying-device-characteristics.md).

-   Exclusive access. Specifies whether the device object represents an *exclusive device*. If the device is exclusive, only one handle can be open for the device object at a time. (If the underlying device supports overlapped I/O, multiple threads of the same process can send requests through a single handle.) For more information, see [Specifying Exclusive Access to Device Objects](specifying-exclusive-access-to-device-objects.md).

-   Security descriptor. Device objects have a security descriptor that controls access to the device. For more information, see [Securing Device Objects](securing-device-objects.md).

For each of these properties, a default value can be set when the device object is created. For more information about creating device objects, see [Creating a Device Object](creating-a-device-object.md).

Values for device object properties can also be set in the registry. See [Setting Device Object Properties in the Registry](setting-device-object-properties-in-the-registry.md) for more information.

 

 




