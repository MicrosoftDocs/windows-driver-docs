---
title: Obtaining Configuration Information from Other Driver Stacks
description: Obtaining Configuration Information from Other Driver Stacks
ms.assetid: ca0f3d51-24c6-44df-828f-6aeb2565c1ae
keywords: ["I/O WDK kernel , device configuration space", "device configuration space WDK I/O", "configuration space WDK I/O", "space WDK I/O", "driver stacks WDK configuration info", "BUS_INTERFACE_STANDARD"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Obtaining Configuration Information from Other Driver Stacks





At times you need to obtain information from the configuration space of a device whose driver is on a stack other than the one that your driver is on. For instance, suppose you want to set a bit in the configuration space of a PCI-to-PCI bridge and you do not have a pointer to the PDO of the bridge. Although the operating system enumerates PCI-to-PCI bridges and creates a PDO for every bridge on the system, it does not register device interfaces for these devices. Therefore, you cannot use the device interface mechanism to access the configuration space of these bridges. For more information about device interfaces see [Introduction to Device Interfaces](https://msdn.microsoft.com/library/windows/hardware/ff549460).

In Windows NT 4.0, drivers could access the configuration space of such devices using the [**HalGetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff546599) and [**HalSetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff546628) routines. In Windows 2000 and later versions of Windows, this is no longer the case.

Windows 2000 and later versions of Windows do not allow drivers to access hardware belonging to other driver stacks. A filter driver can be written to provide the functionality needed. If you wish to access bridge hardware, for instance, you must design a filter driver that implements the required operations on the bridge's configuration space. You must also provide an INF file that specifies the bridge hardware's possible hardware IDs, so the PnP manager can load the filter driver onto the bridge's driver stack when it detects the device ID of the bridge.

Alternatively, you can install a filter programmatically using **SetupDi*Xxx*** functions in the co-installer for your device.

The filter driver can then access the bridge using the [**BUS\_INTERFACE\_STANDARD**](https://msdn.microsoft.com/library/windows/hardware/ff540707) interface.

 

 




