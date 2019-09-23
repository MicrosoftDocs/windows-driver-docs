---
title: DispatchCreate, DispatchClose, and DispatchCreateClose Routines
description: DispatchCreate, DispatchClose, and DispatchCreateClose Routines
ms.assetid: 5c1c0036-71b1-4410-b157-f9ebe3b6ecfc
keywords: ["dispatch routines WDK kernel , DispatchCreate routine", "dispatch routines WDK kernel , DispatchClose routine", "dispatch routines WDK kernel , DispatchCreateClose routine", "DispatchCreateClose routine", "DispatchClose routine", "DispatchCreate routine", "IRP_MJ_CREATE I/O function code", "IRP_MJ_CLOSE I/O function code", "create dispatch routines WDK kernel", "close dispatch routines WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# DispatchCreate, DispatchClose, and DispatchCreateClose Routines





A driver's [*DRIVER_DISPATCH*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) IRPs with I/O function codes of [**IRP\_MJ\_CREATE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-create) and [**IRP\_MJ\_CLOSE**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-close), respectively. Alternatively, a combined [*DispatchCreateClose*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_dispatch) routine can handle IRPs for both of these I/O function codes.

A create request can originate either from a user-mode subsystem's attempt to get a handle to a file object representing a device (possibly on behalf of an application or subsystem-level driver) or in a higher-level driver's call to [**IoGetDeviceObjectPointer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iogetdeviceobjectpointer) or [**IoAttachDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-ioattachdevice).

A reciprocal close request originates from a user-mode subsystem's close of the file object handle associated with the driver's device object.

Each of these requests is inherently synchronous.

 

 




