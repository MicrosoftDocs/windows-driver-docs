---
title: Handling a Wait/Wake IRP in a Function (FDO) or Filter Driver (Filter DO)
description: Handling a Wait/Wake IRP in a Function (FDO) or Filter Driver (Filter DO)
ms.assetid: 752b6c3c-f42a-469d-8a43-0778ecbe4541
keywords: ["receiving wait/wake IRPs", "wait/wake IRPs WDK power management , receiving", "function drivers WDK power management", "FDOs WDK power management", "filter DOs WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling a Wait/Wake IRP in a Function (FDO) or Filter Driver (Filter DO)





When a driver that creates an FDO or filter DO receives an [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) request for the associated PDO, it can either simply pass the IRP down to the next-lower driver or take certain actions before passing down the IRP.

### For Devices That Support Wake-Up

Upon receiving a wait/wake IRP, a function or filter driver should take the following steps:

1.  Call [**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204), passing the current IRP, to ensure that the driver does not receive a PnP [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request while handling the wait/wake IRP.

    If [**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204) returns a failure status, the driver should not continue processing the IRP. Instead, it completes the IRP ([**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)), and return the failure status.

2.  Inspect the value at **Irp-&gt;Parameters.WaitWake.PowerState** and compare the current device power state with **DeviceState**\[SystemWake\] in the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure.

    If the device supports wake-up, but not from the specified [SystemWake](systemwake.md) state or not from the current device power state, the driver should fail the IRP as follows:

    -   Set STATUS\_INVALID\_DEVICE\_STATE in **Irp-&gt;IoStatus.Status**.
    -   Complete the IRP (**IoCompleteRequest**), specifying a priority boost of IO\_NO\_INCREMENT.
    -   Return the status set in **Irp-&gt;IoStatus.Status** from the [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine.

3.  Otherwise, set an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine for the IRP using [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679). The *IoCompletion* routine should perform whatever tasks the driver requires to return the device to the working state.

    The *IoCompletion* routine will also be called if the IRP is canceled.

4.  Save any information the driver might need in its *IoCompletion* routine.

5.  Call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) (in Windows 7 and Windows Vista) or [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) (in Windows Server 003, Windows XP, and Windows 2000), to pass the wait/wake IRP to the next-lower driver.

6.  Call [**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560) to release the previously acquired lock.

7.  Return STATUS\_PENDING from the [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine. The driver must not change the value in **Irp-&gt;IoStatus.Status** while it holds the IRP.

### For Devices That Do Not Support Wake-Up

If a function or filter driver receives a wait/wake IRP for a device that does not support wake-up, the driver should fail the IRP as follows:

1.  Complete the IRP (**IoCompleteRequest**), specifying a priority boost of IO\_NO\_INCREMENT.

2.  Return the status set in **Irp-&gt;IoStatus.Status** from the [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine.

 

 




