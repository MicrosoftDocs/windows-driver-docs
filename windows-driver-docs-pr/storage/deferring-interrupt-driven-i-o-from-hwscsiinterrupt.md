---
title: Deferring Interrupt-Driven I/O from HwScsiInterrupt
description: Deferring Interrupt-Driven I/O from HwScsiInterrupt
ms.assetid: 6bedad0c-8995-4c7b-8ee2-415ec63e0eb3
keywords:
- SCSI miniport drivers WDK storage , HwScsiInterrupt
- HwScsiInterrupt
- interrupts WDK SCSI
- deferred interrupt-driven I/O WDK SCSI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deferring Interrupt-Driven I/O from HwScsiInterrupt


## <span id="ddk_deferring_interrupt_driven_i_o_from_hwscsiinterrupt_kg"></span><span id="DDK_DEFERRING_INTERRUPT_DRIVEN_I_O_FROM_HWSCSIINTERRUPT_KG"></span>


If interrupt-driven I/O operations take a long time to complete, a miniport driver should have a pair of [**HwScsiEnableInterruptsCallback**](https://msdn.microsoft.com/library/windows/hardware/ff557295) and [**HwScsiDisableInterruptsCallback**](https://msdn.microsoft.com/library/windows/hardware/ff557288) routines.

For example, if a miniport driver must stall for longer than 50 microseconds doing PIO, its *HwScsiInterrupt* routine should *not* retain control of the CPU for the full polling interval to complete a requested operation. Instead, its *HwScsiInterrupt* routine should do the following:

1.  Disable interrupts from the HBA.

2.  Set up the device extension with any context necessary to complete the operation.

3.  Call [**ScsiPortNotification**](https://msdn.microsoft.com/library/windows/hardware/ff564657) with a pointer to the device extension, the *NotificationType***CallEnableInterrupts**, and the miniport driver's *HwScsiEnableInterruptsCallback* routine, described in [SCSI Miniport Driver's HwScsiEnableInterruptsCallback Routine](scsi-miniport-driver-s-hwscsienableinterruptscallback-routine.md).

4.  Return control.

The **ScsiPortNotification** routine calls the *HwScsiEnableInterruptsCallback* routine as a DPC routine. For more information about DPCs, see [DPC Objects and DPCs](https://msdn.microsoft.com/library/windows/hardware/ff544084).

If a miniport driver's *HwScsiInterrupt* routine cannot disable interrupts on the HBA but its interrupt-driven transfers can take more than 50 microseconds in the *HwScsiInterrupt* routine, the driver writer should tune the miniport driver by limiting the size of the transfers that it accepts. Otherwise, the mouse pointer will appear "jumpy" and/or serial and parallel throughput will degrade noticeably every time the miniport driver is transferring data concurrently.

Such a miniport driver's *HwScsiFindAdapter* routine should reset the **MaximumTransferLength** value in the PORT\_CONFIGURATION\_INFORMATION to a value that allows the miniport driver to carry out interrupt-driven transfers without noticeably affecting the performance of other system drivers.

Such a miniport driver also might call **ScsiPortNotification** with a miniport driver-supplied *HwScsiTimer* routine. For more information about *HwScsiTimer* routines, which are synchronized with *HwScsiInterrupt* routines, see [SCSI Miniport Driver's HwScsiTimer Routine](scsi-miniport-driver-s-hwscsitimer-routine.md).

 

 




