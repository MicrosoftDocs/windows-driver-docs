---
title: SCSI Miniport Driver's HwScsiTimer Routine
author: windows-driver-content
description: SCSI Miniport Driver's HwScsiTimer Routine
ms.assetid: 57ac7a6e-ada5-4185-89cf-b6c5ef9006d4
keywords: ["SCSI miniport drivers WDK storage , HwScsiTimer", "HwScsiTimer", "timers WDK SCSI"]
---

# SCSI Miniport Driver's HwScsiTimer Routine


## <span id="ddk_scsi_miniport_drivers_hwscsitimer_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_HWSCSITIMER_ROUTINE_KG"></span>


A miniport driver that does not have an [**HwScsiInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff557312) routine because it manages all HBA I/O operations by polling should have an [*HwScsiTimer*](https://msdn.microsoft.com/library/windows/hardware/ff557327)routine. However, miniport drivers with *HwScsiInterrupt* routines frequently have *HwScsiTimer* routines as well.

While a miniport driver can call [**ScsiPortStallExecution**](https://msdn.microsoft.com/library/windows/hardware/ff564757) to wait for a state change on the HBA, miniport drivers should *never* call this routine to wait for longer than one millisecond except, possibly, for an operation performed only when a miniport driver is initializing. **ScsiPortStallExecution** ties up the processor for the given interval, preventing other code in the system from doing useful work.

Instead of calling **ScsiPortStallExecution** with large input intervals and wasting many CPU cycles, a miniport driver should have an *HwScsiTimer* routine. One or more *HwScsiTimer* routines are particularly useful if the HBA does not generate a completion interrupt for every operation or if any commonly requested operation, such as a bus reset, takes longer than a millisecond.

After the HBA has been programmed for such an operation, the miniport driver calls [**ScsiPortNotification**](https://msdn.microsoft.com/library/windows/hardware/ff564657) with the *NotificationType***RequestTimerCall**, a pointer to its HBA-specific device extension containing context about the operation, its *HwScsiTimer* entry point, and a driver-determined interval.

**ScsiPortNotification** synchronizes calls to the *HwScsiTimer* routine with those to the *HwScsiInterrupt* routine so that it cannot execute concurrently while the *HwScsiTimer* routine is running.

*HwScsiTimer* is called once for each such call to **ScsiPortNotification**, which can be called from the *HwScsiTimer* routine itself. However, any call to **ScsiPortNotification** with the *NotificationType***RequestTimerCall** overrides a preceding call for which the specified interval has not expired. That is, there is only one outstanding request to call a miniport driver's *HwScsiTimer* routine at any given moment.

The interval passed in to **ScsiPortNotification** is in microseconds, and the minimum overhead for each call to an *HwScsiTimer* routine is approximately 10 microseconds. An input interval of zero cancels the preceding request to call the *HwScsiTimer* routine, provided it has not been called or dispatched for execution on another processor in a NT-based SMP machine.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SCSI%20Miniport%20Driver's%20HwScsiTimer%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


