---
title: Handling a Wait/Wake IRP in a Function (FDO) or Filter Driver (Filter DO)
description: Handling a Wait/Wake IRP in a Function (FDO) or Filter Driver (Filter DO)
keywords: ["receiving wait/wake IRPs", "wait/wake IRPs WDK power management , receiving", "function drivers WDK power management", "FDOs WDK power management", "filter DOs WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling a Wait/Wake IRP in a Function (FDO) or Filter Driver (Filter DO)





When a driver that creates an FDO or filter DO receives an [**IRP\_MN\_WAIT\_WAKE**](./irp-mn-wait-wake.md) request for the associated PDO, it can either simply pass the IRP down to the next-lower driver or take certain actions before passing down the IRP.

### For Devices That Support Wake-Up

Upon receiving a wait/wake IRP, a function or filter driver should take the following steps:

1.  Call [**IoAcquireRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioacquireremovelock), passing the current IRP, to ensure that the driver does not receive a PnP [**IRP\_MN\_REMOVE\_DEVICE**](./irp-mn-remove-device.md) request while handling the wait/wake IRP.

    If [**IoAcquireRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioacquireremovelock) returns a failure status, the driver should not continue processing the IRP. Instead, it completes the IRP ([**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest)), and return the failure status.

2.  Inspect the value at **Irp-&gt;Parameters.WaitWake.PowerState** and compare the current device power state with **DeviceState**\[SystemWake\] in the [**DEVICE\_CAPABILITIES**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_capabilities) structure.

    If the device supports wake-up, but not from the specified [SystemWake](systemwake.md) state or not from the current device power state, the driver should fail the IRP as follows:

    -   Set STATUS\_INVALID\_DEVICE\_STATE in **Irp-&gt;IoStatus.Status**.
    -   Complete the IRP (**IoCompleteRequest**), specifying a priority boost of IO\_NO\_INCREMENT.
    -   Return the status set in **Irp-&gt;IoStatus.Status** from the [*DispatchPower*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine.

3.  Otherwise, set an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine for the IRP using [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine). The *IoCompletion* routine should perform whatever tasks the driver requires to return the device to the working state.

    The *IoCompletion* routine will also be called if the IRP is canceled.

4.  Save any information the driver might need in its *IoCompletion* routine.

5.  Call [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) (in Windows 7 and Windows Vista) or [**PoCallDriver**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver) (in Windows Server 003, Windows XP, and Windows 2000), to pass the wait/wake IRP to the next-lower driver.

6.  Call [**IoReleaseRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreleaseremovelock) to release the previously acquired lock.

7.  Return STATUS\_PENDING from the [*DispatchPower*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine. The driver must not change the value in **Irp-&gt;IoStatus.Status** while it holds the IRP.

### For Devices That Do Not Support Wake-Up

If a function or filter driver receives a wait/wake IRP for a device that does not support wake-up, the driver should fail the IRP as follows:

1.  Complete the IRP (**IoCompleteRequest**), specifying a priority boost of IO\_NO\_INCREMENT.

2.  Return the status set in **Irp-&gt;IoStatus.Status** from the [*DispatchPower*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine.

 

