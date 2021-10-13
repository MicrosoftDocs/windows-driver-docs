---
title: SCSI Miniport Driver's HwScsiDmaStarted Routine
description: SCSI Miniport Driver's HwScsiDmaStarted Routine
keywords:
- SCSI miniport drivers WDK storage , HwScsiDmaStarted
- HwScsiDmaStarted
- DMA controllers WDK SCSI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SCSI Miniport Driver's HwScsiDmaStarted Routine

A miniport driver of an HBA that uses the system DMA controller must have an [**HwScsiDmaStarted**](/previous-versions/windows/hardware/drivers/ff557291(v=vs.85)) routine.

For a data transfer operation, such a miniport driver must call [**ScsiPortIoMapTransfer**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportiomaptransfer), passing in the pointers to its device extension for per-HBA data and to the SRB requesting the transfer, along with a range of logical addresses for the buffer from which or into which the data will be transferred.

Note that the logical address range passed to **ScsiPortIoMapTransfer** either must be the mapped values for the input SRB's **DataBuffer** and **DataTransferLength** or a proper subset of this range. For most transfer requests, a miniport driver writer can assume that all data specified in the input SRB can be transferred in a single DMA operation.

In particular, a miniport driver might have to carry out more than one subordinate DMA transfer operation to satisfy a given SRB only if the HBA provides application-dedicated support and the application sends large transfer requests directly to the miniport driver. Otherwise, it is the responsibility of the storage class drivers to split up large transfer requests into a set of partial transfer requests, each sized to suit the capabilities of the HBA (see [Storage Class Drivers](introduction-to-storage-class-drivers.md)).

**ScsiPortIoMapTransfer** calls the miniport driver's *HwScsiDmaStarted* routine when the system DMA controller is ready to transfer data between system memory and the HBA. *HwScsiDmaStarted* must set up the HBA for the transfer operation.

When a transfer operation is complete, the miniport driver must call [**ScsiPortFlushDma**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportflushdma) before it calls **ScsiPortNotification** with the SRB and/or calls **ScsiPortIoMapTransfer** to set up the DMA controller again for a subrange in an application-supplied buffer if the HBA is dedicated to the support of a user-mode application.

**ScsiPortFlushDma** flushes any remaining data cached in the DMA controller. Note that **ScsiPortFlushDma** also can be called to cancel a system DMA transfer, even if the miniport driver's *HwScsiDmaStarted* routine has not yet been called.

See [**ScsiPortIoMapTransfer**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportiomaptransfer) and [**ScsiPortFlushDma**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportflushdma) for more information.
