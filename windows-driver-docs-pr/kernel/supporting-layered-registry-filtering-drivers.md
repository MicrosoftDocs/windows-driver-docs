---
title: Supporting Layered Registry Filtering Drivers
author: windows-driver-content
description: Supporting Layered Registry Filtering Drivers
ms.assetid: 5adeecdb-c26e-4502-87b4-bfb02a4aaba8
keywords: ["filtering registry calls WDK kernel , layered", "registry filtering drivers WDK kernel , layered", "layered registry filtering drivers WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting Layered Registry Filtering Drivers


Windows Vista and later operating system versions support a layered stack of registry filtering drivers. Each driver in the stack can participate in filtering registry operations by registering a [*RegistryCallback*](https://msdn.microsoft.com/library/windows/hardware/ff560903) routine. Each registry filtering driver is assigned an *altitude*, and drivers can register only one *RegistryCallback* routine for each altitude. When your driver calls [**CmRegisterCallbackEx**](https://msdn.microsoft.com/library/windows/hardware/ff541921), the driver specifies its altitude. For more information about altitudes, see [Load Order Groups and Altitudes for Minifilter Drivers](https://msdn.microsoft.com/library/windows/hardware/ff549689).

When a thread makes a registry call, the configuration manager calls each *RegistryCallback* routine, in order, from the highest altitude to the lowest, until all drivers have been called or a *RegistryCallback* routine returns a status value for which [NT\_SUCCESS](using-ntstatus-values.md)(*status*) equals **FALSE**. Therefore, if a higher-level driver blocks or modifies a registry operation, the lower-level drivers are not called. (If a driver modifies an operation by calling a different registry function, the configuration manager does not restart at the top of the filter stack.)

Registry filtering drivers that were written before Windows Vista and therefore do not have an altitude assignment are inserted near the top of the Windows Vista filter stack, in the order that they call [**CmRegisterCallback**](https://msdn.microsoft.com/library/windows/hardware/ff541918).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Supporting%20Layered%20Registry%20Filtering%20Drivers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


