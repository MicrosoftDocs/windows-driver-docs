---
title: SCSI Miniport Driver's HwScsiInterrupt Routine
description: SCSI Miniport Driver's HwScsiInterrupt Routine
keywords:
- SCSI miniport drivers WDK storage , HwScsiInterrupt
- HwScsiInterrupt
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SCSI Miniport Driver's HwScsiInterrupt Routine


## <span id="ddk_scsi_miniport_drivers_hwscsiinterrupt_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_HWSCSIINTERRUPT_ROUTINE_KG"></span>


On entry, an [**HwScsiInterrupt**](/previous-versions/windows/hardware/drivers/ff557312(v=vs.85)) routine should determine if its HBA actually generated an interrupt. *HwScsiInterrupt* must return **FALSE** as soon as possible if it detects a spurious interrupt so the ISR for the device that actually generated the interrupt can be called quickly.

Otherwise, a miniport driver's *HwScsiInterrupt* routine is generally responsible for completing the I/O operation that caused the interrupt. Depending on the HBA and the design of the miniport driver, an *HwScsiInterrupt* routine does some or all of the following:

-   Dismisses the interrupt on the HBA (required)

-   Notifies the port driver (by calling [**ScsiPortNotification**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportnotification) or [**ScsiPortCompleteRequest**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportcompleterequest)) if the HBA indicates that certain SCSI error conditions occurred during the operation and possibly logs the error.

    For more information about logging errors, see [Error Handling in SCSI Miniport Drivers](error-handling-in-scsi-miniport-drivers.md).

-   Completes the requested operation that caused the interrupt, such as calling [**ScsiPortIoMapTransfer**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportiomaptransfer) (see [SCSI Miniport Driver's HwScsiDmaStarted Routine](scsi-miniport-driver-s-hwscsidmastarted-routine.md)) if the interrupt came in from a previously selected target TID and LU, indicating a readiness to transfer data.

When the *HwScsiInterrupt* routine (or an internal miniport driver routine) completes an SRB, it calls **ScsiPortNotification** twice:

1.  First, with the *NotificationType***RequestComplete** and the just-satisfied SRB.

2.  Next, with the *NotificationType***NextRequest**, or with **NextLuRequest** if the HBA supports tagged queuing or multiple requests per logical unit.

For better overall system performance, a miniport driver's *HwScsiInterrupt* routine should do only the minimum necessary to process I/O requests. That is, the miniport driver should be designed to return control from the *HwScsiInterrupt* routine as quickly as possible. An *HwScsiInterrupt* routine must not call [**ScsiPortStallExecution**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportstallexecution) with large intervals, thereby monopolizing a processor and preventing other drivers from servicing their device interrupts.

 

