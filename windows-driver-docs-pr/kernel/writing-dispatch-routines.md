---
title: Writing Dispatch Routines
description: Writing Dispatch Routines
keywords: ["dispatch routines WDK kernel", "standard driver routines WDK kernel , dispatch routines", "driver routines WDK kernel , dispatch routines", "routines WDK kernel , dispatch routines", "system-space memory allocations WDK kernel", "system resource storage WDK kernel", "storing system resources", "dispatch routines WDK kernel , about dispatch routines", "IRPs WDK kernel , dispatch routines", "multiple I/O function codes WDK kernel", "IRP major function codes WDK kernel", "major function codes WDK kernel", "function codes WDK kernel"]
ms.date: 06/16/2017
---

# Writing Dispatch Routines





Processing any I/O request packet (IRP) begins in a dispatch routine that the driver registers to handle an [IRP major function code](./irp-major-function-codes.md) (<strong>IRP\_MJ\_*XXX</strong><em>). The driver's [</em>*DriverEntry*<em>](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine exports entry points for dispatch routines in a dispatch table within the driver's [</em>*DRIVER\_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_driver_object) structure.

A driver can provide a separate dispatch routine for each major I/O function code that it handles. Alternatively, dispatch routines can be written to handle multiple I/O function codes.

This section contains the following topics:

[Dispatch Routine Functionality](dispatch-routine-functionality.md)

[Required Dispatch Routines](required-dispatch-routines.md)

[Optional Dispatch Routines](optional-dispatch-routines.md)

[Dispatch Routines and IRQLs](dispatch-routines-and-irqls.md)

[When to Check the Driver's I/O Stack Location](when-to-check-the-driver-s-i-o-stack-location.md)

[DispatchCreate, DispatchClose, and DispatchCreateClose Routines](dispatchcreate--dispatchclose--and-dispatchcreateclose-routines.md)

[DispatchCleanup Routines](dispatchcleanup-routines.md)

[DispatchRead, DispatchWrite, and DispatchReadWrite Routines](dispatchread--dispatchwrite--and-dispatchreadwrite-routines.md)

[DispatchDeviceControl and DispatchInternalDeviceControl Routines](dispatchdevicecontrol-and-dispatchinternaldevicecontrol-routines.md)

[DispatchPnP Routines](dispatchpnp-routines.md)

[DispatchPower Routines](dispatchpower-routines.md)

[DispatchQueryInformation Routines](dispatchqueryinformation-routines.md)

[DispatchSetInformation Routines](dispatchsetinformation-routines.md)

[DispatchFlushBuffers Routines](dispatchflushbuffers-routines.md)

[DispatchShutdown Routines](dispatchshutdown-routines.md)

[DispatchSystemControl Routines](dispatchsystemcontrol-routines.md)
