---
title: Error Handling in Storport Miniport Drivers
description: Error Handling in Storport Miniport Drivers
ms.date: 09/25/2024
---

# Error handling in Storport miniport drivers

Every Storport miniport driver must notify the system port driver about the following kinds of SCSI errors. The driver should set these errors in the [**SrbStatus**](/windows-hardware/drivers/ddi/storport/ns-storport-_storage_request_block) member before completing the SRB it was processing when the error occurred:

* SRB_STATUS_ERROR (if the HBA returns a nonspecific bus error)

* SRB_STATUS_PARITY_ERROR

* SRB_STATUS_UNEXPECTED_BUS_FREE

* SRB_STATUS_SELECTION_TIMEOUT

* SRB_STATUS_COMMAND_TIMEOUT

* SRB_STATUS_MESSAGE_REJECTED

* SRB_STATUS_NO_DEVICE

* SRB_STATUS_NO_HBA

* SRB_STATUS_DATA_OVERRUN (also returned for underruns)

* SRB_STATUS_PHASE_SEQUENCE_FAILURE

* SRB_STATUS_BUSY (TID busy)

For a data underrun, the miniport driver must update the SRB's **DataTransferLength** to indicate how much data actually was transferred.

In addition, the miniport driver should use the following guidelines to log some of the preceding errors by passing the SRB to [**StorPortLogError**](/windows-hardware/drivers/ddi/storport/nf-storport-storportlogerror):

* Log an error at the discretion of the driver writer for SRB_STATUS_ERROR.
* Always log an error for SRB_STATUS_PARITY_ERROR.
* Always log an error for SRB_STATUS_UNEXPECTED_BUS_FREE.
* Always log an error for SRB_STATUS_SELECTION_TIMEOUT.
* Always log an error for SRB_STATUS_COMMAND_TIMEOUT.
* Log an error for SRB_STATUS_DATA_OVERRUN whenever an overrun occurs, but not when an underrun occurs.
* Always log an error for SRB_STATUS_PHASE_SEQUENCE_FAILURE.
* Always log an error for SRB_STATUS_BUSY for hardware errors.

To log an error, a miniport driver calls [**StorPortLogError**](/windows-hardware/drivers/ddi/storport/nf-storport-storportlogerror) by using one of the following system-defined error or warning codes:

* SP_BUS_PARITY_ERROR maps to SRB_STATUS_PARITY_ERROR
* SP_UNEXPECTED_DISCONNECT (by the target logical unit)
* SP_INVALID_RESELECTION maps to SRB_STATUS_PHASE_SEQUENCE_FAILURE or SRB_STATUS_ERROR
* SP_BUS_TIME_OUT maps to SRB_STATUS_SELECTION_TIMEOUT
* SP_REQUEST_TIMEOUT maps to SRB_STATUS_COMMAND_TIMEOUT
* SP_PROTOCOL_ERROR maps to SRB_STATUS_PHASE_SELECTION_FAILURE, SRB_STATUS_UNEXPECTED_BUS_FREE, or SRB_STATUS_DATA_OVERRUN for an overrun condition
* SP_INTERNAL_ADAPTER_ERROR maps to SRB_STATUS_ERROR
* SP_IRQ_NOT_RESPONDING (warning that the miniport driver detected that the HBA is no longer generating interrupt requests)
* SP_BAD_FW_ERROR (where FW is *firmware*)
* SP_BAD_FW_WARNING

[**StorPortLogError**](/windows-hardware/drivers/ddi/storport/nf-storport-storportlogerror) allocates an error-log packet, sets it up, and logs the I/O error in the event log for the miniport driver. System administrators or users can monitor the condition of an HBA by examining the system event log and, if necessary, reconfiguring, repairing, or replacing the HBA before it fails.
