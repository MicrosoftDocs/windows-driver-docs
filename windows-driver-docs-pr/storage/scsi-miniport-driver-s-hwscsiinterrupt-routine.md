---
title: SCSI Miniport Driver's HwScsiInterrupt Routine
description: SCSI Miniport Driver's HwScsiInterrupt Routine
ms.assetid: 8760e7e4-1721-4e55-99e6-c9e234368fa1
keywords: ["SCSI miniport drivers WDK storage , HwScsiInterrupt", "HwScsiInterrupt"]
---

# SCSI Miniport Driver's HwScsiInterrupt Routine


## <span id="ddk_scsi_miniport_drivers_hwscsiinterrupt_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_HWSCSIINTERRUPT_ROUTINE_KG"></span>


On entry, an [**HwScsiInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff557312) routine should determine if its HBA actually generated an interrupt. *HwScsiInterrupt* must return **FALSE** as soon as possible if it detects a spurious interrupt so the ISR for the device that actually generated the interrupt can be called quickly.

Otherwise, a miniport driver's *HwScsiInterrupt* routine is generally responsible for completing the I/O operation that caused the interrupt. Depending on the HBA and the design of the miniport driver, an *HwScsiInterrupt* routine does some or all of the following:

-   Dismisses the interrupt on the HBA (required)

-   Notifies the port driver (by calling [**ScsiPortNotification**](https://msdn.microsoft.com/library/windows/hardware/ff564657) or [**ScsiPortCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff564608)) if the HBA indicates that certain SCSI error conditions occurred during the operation and possibly logs the error.

    For more information about logging errors, see [Error Handling in SCSI Miniport Drivers](error-handling-in-scsi-miniport-drivers.md).

-   Completes the requested operation that caused the interrupt, such as calling [**ScsiPortIoMapTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff564649) (see [SCSI Miniport Driver's HwScsiDmaStarted Routine](scsi-miniport-driver-s-hwscsidmastarted-routine.md)) if the interrupt came in from a previously selected target TID and LU, indicating a readiness to transfer data.

When the *HwScsiInterrupt* routine (or an internal miniport driver routine) completes an SRB, it calls **ScsiPortNotification** twice:

1.  First, with the *NotificationType***RequestComplete** and the just-satisfied SRB.

2.  Next, with the *NotificationType***NextRequest**, or with **NextLuRequest** if the HBA supports tagged queuing or multiple requests per logical unit.

For better overall system performance, a miniport driver's *HwScsiInterrupt* routine should do only the minimum necessary to process I/O requests. That is, the miniport driver should be designed to return control from the *HwScsiInterrupt* routine as quickly as possible. An *HwScsiInterrupt* routine must not call [**ScsiPortStallExecution**](https://msdn.microsoft.com/library/windows/hardware/ff564757) with large intervals, thereby monopolizing a processor and preventing other drivers from servicing their device interrupts.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SCSI%20Miniport%20Driver's%20HwScsiInterrupt%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




