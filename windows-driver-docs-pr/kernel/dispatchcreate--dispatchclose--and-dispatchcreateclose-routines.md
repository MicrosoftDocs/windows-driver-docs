---
title: DispatchCreate, DispatchClose, and DispatchCreateClose Routines
description: DispatchCreate, DispatchClose, and DispatchCreateClose Routines
keywords: ["dispatch routines WDK kernel , DispatchCreate routine", "dispatch routines WDK kernel , DispatchClose routine", "dispatch routines WDK kernel , DispatchCreateClose routine", "DispatchCreateClose routine", "DispatchClose routine", "DispatchCreate routine", "IRP_MJ_CREATE I/O function code", "IRP_MJ_CLOSE I/O function code", "create dispatch routines WDK kernel", "close dispatch routines WDK kernel"]
ms.date: 06/16/2017
---

# DispatchCreate, DispatchClose, and DispatchCreateClose Routines





A driver's [*DRIVER_DISPATCH*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) IRPs with I/O function codes of [**IRP\_MJ\_CREATE**](./irp-mj-create.md) and [**IRP\_MJ\_CLOSE**](./irp-mj-close.md), respectively. Alternatively, a combined [*DispatchCreateClose*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine can handle IRPs for both of these I/O function codes.

A create request can originate either from a user-mode subsystem's attempt to get a handle to a file object representing a device (possibly on behalf of an application or subsystem-level driver) or in a higher-level driver's call to [**IoGetDeviceObjectPointer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceobjectpointer) or [**IoAttachDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevice).

A reciprocal close request originates from a user-mode subsystem's close of the file object handle associated with the driver's device object.

Each of these requests is inherently synchronous.

 

