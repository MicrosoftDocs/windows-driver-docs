---
title: Handling a Wait/Wake IRP in a Bus Driver (PDO)
description: Handling a Wait/Wake IRP in a Bus Driver (PDO)
ms.assetid: 9583b935-26e1-49c6-827d-932762af114d
keywords: ["receiving wait/wake IRPs", "wait/wake IRPs WDK power management , receiving", "bus drivers WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling a Wait/Wake IRP in a Bus Driver (PDO)





Like other power IRPs, each wait/wake IRP must be passed all the way down the device stack to the bus driver (PDO), which is ultimately responsible for completing the IRP. Upon receiving the IRP, the bus driver can either fail it immediately or hold it pending for later completion. The following are the steps the bus driver must take:

1.  Inspect the value at **Irp-&gt;Parameters.WaitWake.PowerState**. If the device supports wake-up, but not from the specified [**SystemWake**](systemwake.md) state or not from the current device power state, the driver should fail the IRP as follows:

    -   Set STATUS\_INVALID\_DEVICE\_STATE in **Irp-&gt;IoStatus.Status**.

    -   Complete the IRP ([**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)), specifying a priority boost of IO\_NO\_INCREMENT.

    -   Return the status set in **Irp-&gt;IoStatus.Status** from the [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine.

2.  Check whether a wait/wake IRP is already pending for the PDO. If so, set **Irp-&gt;IoStatus.Status** to STATUS\_DEVICE\_BUSY, increment the driver's internal count of wait/wake IRPs, and complete the IRP as described in the previous step.

    Only one wait/wake IRP can be pending for a PDO.

3.  If the device supports wake-up from the specified system power state and no wait/wake IRP is already pending, call [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) to indicate to the I/O manager that the IRP will be completed or canceled later. Do not set an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine.

4.  Set the device hardware to enable wake-up.

    The specific mechanism by which a bus driver enables its hardware for wake-up is device-dependent. For a PCI device, Pci.sys is responsible for setting the PME-enable bit because this driver owns the PME register. For other devices, refer to the device-class-specific documentation.

5.  If the PDO is the child of an FDO, [request a wait/wake IRP](sending-a-wait-wake-irp.md) for the FDO, making sure to set a [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine for the current IRP (the IRP that it holds pending). Do not attempt to pass on or reuse the current IRP.

6.  Return STATUS\_PENDING from the *DispatchPower* routine.

7.  When a wake-up signal arrives, call **IoCompleteRequest** to complete the pending wait/wake IRP, setting **Irp-IoStatus.Status** to STATUS\_SUCCESS, and specifying a priority boost of IO\_NO\_INCREMENT.

### For Devices That Do Not Support Wake-Up

If the device does not support wake-up, the bus driver (PDO) should proceed as follows:

1.  Complete the wait/wake IRP by calling **IoCompleteRequest**, specifying IO\_NO\_INCREMENT.

2.  Return from the *DispatchPower* routine, passing the value at **Irp-&gt;IoStatus.Status** as its return value.

 

 




