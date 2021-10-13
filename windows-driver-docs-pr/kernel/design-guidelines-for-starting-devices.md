---
title: Design Guidelines for Starting Devices
description: Design Guidelines for Starting Devices
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Design Guidelines for Starting Devices





-   The PnP manager fails create requests for the device until the [**IRP\_MN\_START\_DEVICE**](./irp-mn-start-device.md) IRP completes, indicating that all the drivers for the device have performed their start operations.

-   Because a [*DispatchPnP*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine runs in the context of a system thread at IRQL PASSIVE\_LEVEL, any memory allocated with [**ExAllocatePoolWithTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtag) for use exclusively during initialization can be from paged pool as long as the driver does not control the device that holds a system page file. Such a memory allocation must be released with [**ExFreePool**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exfreepool) before the *DispatchPnP* routine returns control.

-   A WDM device driver's ISR should be capable of determining whether it has been called with a spurious interrupt even during device startup. On return from the call to [**IoConnectInterrupt**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioconnectinterrupt) in the code path that handles **IRP\_MN\_START\_DEVICE**, the ISR can be called immediately if interrupts are enabled on the device.

 

