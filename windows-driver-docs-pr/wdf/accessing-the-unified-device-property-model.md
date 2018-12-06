---
title: Accessing the Unified Device Property Model
description: This topic describes how a Windows Driver Frameworks (WDF) driver retrieves or modifies properties that are exposed through the unified device property model.
ms.assetid: C81988F9-E0DA-439F-B770-DAD86E33D5F3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing the Unified Device Property Model


This topic describes how a Windows Driver Frameworks (WDF) driver retrieves or modifies properties that are exposed through the unified device property model. The methods listed are available starting in User-Mode Driver Framework (UMDF) version 2.0 and Kernel-Mode Driver Framework (KMDF) version 1.13.

Both KMDF and UMDF drivers can call the following methods:

-   [**WdfDeviceAllocAndQueryPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/dn265599)
-   [**WdfDeviceAssignProperty**](https://msdn.microsoft.com/library/windows/hardware/dn265601)
-   [**WdfDeviceQueryPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/dn265608)

Both KMDF and UMDF drivers can call the following methods only before calling [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926). For more information about calling **WdfDeviceCreate**, see [Creating a Framework Device Object](creating-a-framework-device-object.md).

After calling [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926), a driver can obtain device property information by calling the corresponding **WdfDevice*Xxx*Property** method.

-   [**WdfFdoInitAllocAndQueryPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/dn265612)
-   [**WdfFdoInitQueryPropertyEx**](https://msdn.microsoft.com/library/windows/hardware/dn265613)

The *-Ex* methods above differ from their non*-Ex* counterparts in that they allow you to specify properties using the [**WDF\_DEVICE\_PROPERTY\_DATA**](https://msdn.microsoft.com/library/windows/hardware/dn265632) structure, instead of the subset that you can specify using [**DEVICE\_REGISTRY\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff543171).

Before receiving device property data, drivers typically call **Wdf*Xxx*QueryProperty** just to obtain the required buffer size. For some properties, the data size can change between when the required size is returned and when the driver calls **Wdf*Xxx*QueryProperty** again. Therefore, drivers should call **Wdf*Xxx*QueryProperty** inside a loop that executes until the return status is not **STATUS\_BUFFER\_TOO\_SMALL**.

It is best to use **Wdf*Xxx*QueryProperty** only if the required buffer size is known and unchanging, because in that case the driver has to call **Wdf*Xxx*QueryProperty** only once. If the required buffer size is unknown or varies, the driver should call **Wdf*Xxx*AllocAndQueryProperty**.

## Accessing Device Interface Properties


UMDF drivers can use the following methods to retrieve or modify [device interface properties](https://msdn.microsoft.com/library/windows/hardware/ff541409) that are exposed through the unified property model:

-   [**WdfDeviceAllocAndQueryInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/dn265598)
-   [**WdfDeviceAssignInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/dn265600)
-   [**WdfDeviceQueryInterfaceProperty**](https://msdn.microsoft.com/library/windows/hardware/dn265607)

To retrieve or modify a device interface property, a KMDF driver must call [**IoGetDeviceInterfacePropertyData**](https://msdn.microsoft.com/library/windows/hardware/hh439313) or [**IoSetDeviceInterfacePropertyData**](https://msdn.microsoft.com/library/windows/hardware/hh439388) directly.

 

 





