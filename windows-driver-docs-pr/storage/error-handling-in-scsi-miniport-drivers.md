---
title: Error Handling in SCSI Miniport Drivers
description: Error Handling in SCSI Miniport Drivers
ms.assetid: 0d9a2d60-c8e5-48f6-9c1f-d593e59095c8
keywords:
- SCSI miniport drivers WDK storage , errors
- errors WDK SCSI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Error Handling in SCSI Miniport Drivers


## <span id="ddk_error_handling_in_scsi_miniport_drivers_kg"></span><span id="DDK_ERROR_HANDLING_IN_SCSI_MINIPORT_DRIVERS_KG"></span>


Every SCSI miniport driver must notify the system port driver about the following kinds of SCSI errors. These errors should be set in the **SrbStatus** member before the driver completes the SRB it was processing when the error occurred:

-   SRB\_STATUS\_ERROR (if the HBA returns a nonspecific bus error)

-   SRB\_STATUS\_PARITY\_ERROR

-   SRB\_STATUS\_UNEXPECTED\_BUS\_FREE

-   SRB\_STATUS\_SELECTION\_TIMEOUT

-   SRB\_STATUS\_COMMAND\_TIMEOUT

-   SRB\_STATUS\_MESSAGE\_REJECTED

-   SRB\_STATUS\_NO\_DEVICE

-   SRB\_STATUS\_NO\_HBA

-   SRB\_STATUS\_DATA\_OVERRUN (also returned for underruns)

-   SRB\_STATUS\_PHASE\_SEQUENCE\_FAILURE

-   SRB\_STATUS\_BUSY (TID busy)

For a data underrun, the miniport driver must update the SRB's **DataTransferLength** to indicate how much data actually was transferred.

In addition, the miniport driver should use the following guidelines to log some of the preceding errors by passing the SRB to [**ScsiPortLogError**](https://msdn.microsoft.com/library/windows/hardware/ff564652):

Log an error at the discretion of the driver writer for SRB\_STATUS\_ERROR.

Always log an error for SRB\_STATUS\_PARITY\_ERROR.

Always log an error for SRB\_STATUS\_UNEXPECTED\_BUS\_FREE.

Always log an error for SRB\_STATUS\_SELECTION\_TIMEOUT.

Always log an error for SRB\_STATUS\_COMMAND\_TIMEOUT.

Log an error for SRB\_STATUS\_DATA\_OVERRUN whenever an overrun occurs, but not when an underrun occurs.

Always log an error for SRB\_STATUS\_PHASE\_SEQUENCE\_FAILURE.

Always log an error for SRB\_STATUS\_BUSY for hardware errors.

To log an error, a miniport driver calls [**ScsiPortLogError**](https://msdn.microsoft.com/library/windows/hardware/ff564652) by using one of the following system-defined error or warning codes:

SP\_BUS\_PARITY\_ERROR maps to SRB\_STATUS\_PARITY\_ERROR

SP\_UNEXPECTED\_DISCONNECT (by the target logical unit)

SP\_INVALID\_RESELECTION maps to SRB\_STATUS\_PHASE\_SEQUENCE\_FAILURE or SRB\_STATUS\_ERROR

SP\_BUS\_TIME\_OUT maps to SRB\_STATUS\_SELECTION\_TIMEOUT

SP\_REQUEST\_TIMEOUT maps to SRB\_STATUS\_COMMAND\_TIMEOUT

SP\_PROTOCOL\_ERROR maps to SRB\_STATUS\_PHASE\_SELECTION\_FAILURE, SRB\_STATUS\_UNEXPECTED\_BUS\_FREE, or SRB\_STATUS\_DATA\_OVERRUN for an overrun condition

SP\_INTERNAL\_ADAPTER\_ERROR maps to SRB\_STATUS\_ERROR

SP\_IRQ\_NOT\_RESPONDING (warning that the miniport driver has detected that the HBA is no longer generating interrupt requests)

SP\_BAD\_FW\_ERROR (where FW is *firmware*)

SP\_BAD\_FW\_WARNING

[**ScsiPortLogError**](https://msdn.microsoft.com/library/windows/hardware/ff564652) allocates an error-log packet, sets it up, and logs the I/O error in the event log on behalf of the miniport driver. System administrators or users can monitor the condition of an HBA by examining the system event log and, if necessary, reconfiguring, repairing, or replacing the HBA before it fails.

 

 




