---
title: Porting WMI
description: Porting WMI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting WMI


\[Applies to KMDF only\]

An [**IRP\_MJ\_SYSTEM\_CONTROL**](../kernel/irp-mj-system-control.md) request represents a request for WMI data. WDM drivers handle such requests by implementing a [*DispatchSystemControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) function and registering as a WMI data provider. WDM drivers that do not respond to such requests implement a *DispatchSystemControl* routine that simply passes the IRPs down to the next lower driver.

For KMDF drivers, the framework provides default handling for [**IRP\_MJ\_SYSTEM\_CONTROL**](../kernel/irp-mj-system-control.md). Drivers that do not provide WMI data are not required to include any WMI-related code. Instead, the framework passes the request to the next lower driver on behalf of the driver.

For implementation details, see [Supporting WMI in KMDF Drivers](introduction-to-wmi-for-kmdf-drivers.md).

 

