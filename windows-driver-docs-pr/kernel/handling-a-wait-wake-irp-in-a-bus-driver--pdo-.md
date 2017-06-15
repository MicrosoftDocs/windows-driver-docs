---
title: Handling a Wait/Wake IRP in a Bus Driver (PDO)
author: windows-driver-content
description: Handling a Wait/Wake IRP in a Bus Driver (PDO)
MS-HAID:
- 'PwrMgmt\_76837e04-5b49-4011-ac83-6763a1e8c0e6.xml'
- 'kernel.handling\_a\_wait\_wake\_irp\_in\_a\_bus\_driver\_\_pdo\_'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9583b935-26e1-49c6-827d-932762af114d
keywords: ["receiving wait/wake IRPs", "wait/wake IRPs WDK power management , receiving", "bus drivers WDK power management"]
---

# Handling a Wait/Wake IRP in a Bus Driver (PDO)


## <a href="" id="ddk-handling-a-wait-wake-irp-in-a-bus-driver-pdo--kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20a%20Wait/Wake%20IRP%20in%20a%20Bus%20Driver%20%28PDO%29%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


