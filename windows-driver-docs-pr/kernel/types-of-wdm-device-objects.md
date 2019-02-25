---
title: Types of WDM Device Objects
description: Types of WDM Device Objects
ms.assetid: 89cc888d-3097-4637-96d2-6b9c59878d2f
keywords: ["functional device objects WDK kernel", "FDO WDK kernel", "physical device objects WDK kernel", "PDOs WDK kernel", "device objects WDK kernel , types", "filter DOs WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Types of WDM Device Objects





There are three kinds of WDM device objects:

1.  Physical Device Object (PDO) – represents a device on a bus to a [bus driver](bus-drivers.md).

2.  Functional Device Object (FDO) – represents a device to a [function driver](function-drivers.md).

3.  Filter Device Object (filter DO) – represents a device to a [filter driver](filter-drivers.md).

The three kinds of device objects are all of the type [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147), but are used differently and can have different device extensions.

A driver adds itself to the stack of drivers that handle I/O for a device by creating a device object ([**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397)) and attaching it to the device stack ([**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300)). **IoAttachDeviceToDeviceStack** determines the current top of the device stack and attaches the new device object to the top of the device stack.

 

 




