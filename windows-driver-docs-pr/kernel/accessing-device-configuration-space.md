---
title: Accessing Device Configuration Space
description: Accessing Device Configuration Space
ms.assetid: 082500ae-9df2-4f8b-8be3-ff2b95067a12
keywords: ["I/O WDK kernel , device configuration space", "device configuration space WDK I/O", "configuration space WDK I/O", "space WDK I/O", "resource information WDK I/O", "driver stacks WDK configuration info"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Accessing Device Configuration Space





Some buses provide a way of accessing a special configuration space for each device attached to the bus. This section explains how a driver can get information from a target device's configuration space, provided the driver is loaded in the same driver stack as the driver for the target device, either as a function driver or a filter driver.

In Microsoft Windows NT 4.0, drivers get information from a target device's configuration space by scanning the bus and calling the [**HalGetBusData**](https://msdn.microsoft.com/library/windows/hardware/ff546599) and [**HalGetBusDataByOffset**](https://msdn.microsoft.com/library/windows/hardware/ff546606) routines. In Windows 2000 and later operating systems, the hardware buses are controlled by their respective bus drivers and not by HAL. Therefore, all of the HAL routines that used to help drivers retrieve bus-related information are obsolete in Windows 2000.

The configuration space for a device contains a description of the device and its resource requirements. On Windows 2000 and later operating systems, a driver does not need to query a device to find resources. The driver gets the resources from the Plug and Play (PnP) manager in its [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request. Typically, a well-written driver would not require any of this information to function correctly. If, for some reason, the driver requires this information, the code sample in the [Obtaining Device Configuration Information at IRQL = PASSIVE\_LEVEL](obtaining-device-configuration-information-at-irql---passive-level.md) section shows how to get the resources. The driver must be part of the target device's driver stack, because it requires the underlying physical device objects (PDO) of the target device to send the appropriate PnP request.

 

 




