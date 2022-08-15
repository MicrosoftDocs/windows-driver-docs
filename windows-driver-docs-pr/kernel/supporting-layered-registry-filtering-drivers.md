---
title: Supporting Layered Registry Filtering Drivers
description: Supporting Layered Registry Filtering Drivers
keywords: ["filtering registry calls WDK kernel , layered", "registry filtering drivers WDK kernel , layered", "layered registry filtering drivers WDK kernel"]
ms.date: 06/16/2017
---

# Supporting Layered Registry Filtering Drivers


Windows Vista and later operating system versions support a layered stack of registry filtering drivers. Each driver in the stack can participate in filtering registry operations by registering a [*RegistryCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ex_callback_function) routine. Each registry filtering driver is assigned an *altitude*, and drivers can register only one *RegistryCallback* routine for each altitude. When your driver calls [**CmRegisterCallbackEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-cmregistercallbackex), the driver specifies its altitude. For more information about altitudes, see [Load Order Groups and Altitudes for Minifilter Drivers](../ifs/load-order-groups-and-altitudes-for-minifilter-drivers.md).

When a thread makes a registry call, the configuration manager calls each *RegistryCallback* routine, in order, from the highest altitude to the lowest, until all drivers have been called or a *RegistryCallback* routine returns a status value for which [NT\_SUCCESS](using-ntstatus-values.md)(*status*) equals **FALSE**. Therefore, if a higher-level driver blocks or modifies a registry operation, the lower-level drivers are not called. (If a driver modifies an operation by calling a different registry function, the configuration manager does not restart at the top of the filter stack.)

Registry filtering drivers that were written before Windows Vista and therefore do not have an altitude assignment are inserted near the top of the Windows Vista filter stack, in the order that they call [**CmRegisterCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-cmregistercallback).

 

