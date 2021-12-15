---
title: DispatchPower Routines
description: DispatchPower Routines
keywords: ["dispatch routines WDK kernel , DispatchPower routine", "DispatchPower routine", "power management WDK kernel , dispatch routines", "IRP_MJ_POWER I/O function code", "removable device power dispatch routines WDK kernel"]
ms.date: 06/16/2017
---

# DispatchPower Routines





A driver's [*DispatchPower*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine supports [power management](./introduction-to-power-management.md) by handling IRPs for the [**IRP\_MJ\_POWER**](./irp-mj-power.md) I/O function code. Associated with the **IRP\_MJ\_POWER** function code are several minor I/O function codes for Power Management. The power manager uses these minor function codes to direct drivers to change power states, to wait for and respond to system wake-up events, and to query drivers about their devices.

Each driver's *DispatchPower* routine performs the following tasks:

-   Handle the IRP if possible.

-   Pass the IRP to the next lower driver in the device stack, using [**PoCallDriver**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver).

-   If a bus driver, perform the requested power operation on the device and complete the IRP.

All drivers for a device must have the opportunity to handle power IRPs for the device, except in a few cases where a function or filter driver is allowed to fail the IRP. Most function and filter drivers either perform some processing or set an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine for each power IRP, then pass the IRP down to the next lower driver without completing it. Eventually the IRP reaches the bus driver, which physically changes the power state of the device if required and completes the IRP.

When the IRP has been completed, the I/O manager calls any *IoCompletion* routines set by drivers as the IRP traveled down the device stack. Whether a driver needs to set a completion routine depends upon the type of IRP and the driver's individual requirements.

Power IRPs that power up a device must be handled first by the lowest driver in the device stack (the underlying bus driver) and then by each successive driver up the stack. Power IRPs that power down a device must be handled first by the driver at the top of the device stack and then by each successive driver going down the stack.

### Special Handling for Removable Devices

In their *DispatchPower* routines, drivers of removable devices should check to see whether the device is still present. If the device has been removed, the driver should not pass the IRP down to the next lower driver. Instead, the driver should do the following:

-   Call [**PoStartNextPowerIrp**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-postartnextpowerirp) to begin processing the next power IRP.

-   Set **Irp-&gt;IoStatus.Status** to STATUS\_DELETE\_PENDING.

-   Call [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest), specifying IO\_NO\_INCREMENT, to complete the IRP.

-   Return STATUS\_DELETE\_PENDING.

 

