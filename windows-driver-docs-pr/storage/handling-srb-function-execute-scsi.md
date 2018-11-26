---
title: Handling SRB_FUNCTION_EXECUTE_SCSI
description: Handling SRB_FUNCTION_EXECUTE_SCSI
ms.assetid: 221e1070-12d8-4870-a23c-426ed4a25b84
keywords:
- SCSI miniport drivers WDK storage , HwScsiStartIo
- HwScsiStartIo
- SRB_FUNCTION_EXECUTE_SCSI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling SRB\_FUNCTION\_EXECUTE\_SCSI


## <span id="ddk_handling_srb_function_execute_scsi_kg"></span><span id="DDK_HANDLING_SRB_FUNCTION_EXECUTE_SCSI_KG"></span>


After the higher-level storage class drivers have loaded, most of the SRBs sent to the [**HwScsiStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557323) routine have the **Function** member set to SRB\_FUNCTION\_EXECUTE\_SCSI.

On receipt of an SRB\_FUNCTION\_EXECUTE\_SCSI request, a miniport driver's *HwScsiStartIo* routine does the following:

-   Gets and/or sets up whatever context the miniport driver maintains in its device, logical unit, and/or SRB extensions

    For example, a miniport driver might set up a logical unit extension with pointers to the SRB itself and the SRB **DataBuffer** pointer, the SRB **DataTransferLength** value, and a driver-defined value (or CDB SCSIOP\_*XXX* value) indicating the operation to be carried out on the HBA.

-   Calls an internal routine to program the HBA, as partially directed by the **SrbFlags**, for the requested operation

    For a device I/O operation, such an internal routine generally selects the target device and sends the CDB over the bus to the target logical unit.

If the miniport driver uses system DMA, it must call [**ScsiPortIoMapTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff564649)*before* programming the HBA to transfer data. **ScsiPortIoMapTransfer** sets up the system DMA controller and calls the miniport driver's *HwScsiDmaStarted* routine, described later in [SCSI Miniport Driver's HwScsiDmaStarted Routine](scsi-miniport-driver-s-hwscsidmastarted-routine.md).

All system-defined, required device I/O control requests sent to NT-based operating system storage class drivers are mapped to SRBs with the **Function** member set to SRB\_FUNCTION\_EXECUTE\_SCSI.

 

 




