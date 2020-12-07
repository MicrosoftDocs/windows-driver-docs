---
title: Other SRB_FUNCTION_XXX Requests
description: Other SRB_FUNCTION_XXX Requests
keywords:
- SCSI miniport drivers WDK storage , HwScsiStartIo
- HwScsiStartIo
- SRB_FUNCTION_XXX future use
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Other SRB_FUNCTION_XXX Requests

The following SRB **Function** values are defined for use in future versions of the operating system:

- SRB_FUNCTION_RECEIVE_EVENT

- SRB_FUNCTION_RELEASE_RECOVERY

- SRB_FUNCTION_RESET_DEVICE

- SRB_FUNCTION_TERMINATE_IO

The NT-based operating system SCSI port driver processes requests with the following SRB **Function** values without calling any SCSI miniport driver:

- SRB_FUNCTION_CLAIM_DEVICE

- SRB_FUNCTION_RELEASE_QUEUE

- SRB_FUNCTION_FLUSH_QUEUE

- SRB_FUNCTION_RELEASE_DEVICE

- SRB_FUNCTION_LOCK_QUEUE

- SRB_FUNCTION_UNLOCK_QUEUE

For details about these functions, see [Storage Class Drivers](introduction-to-storage-class-drivers.md).

Miniport driver designers can assume that their miniport drivers will *never* be sent an SRB with any of the immediately preceding **Function** values. The NT-based operating system port driver handles these requests from storage class and filter drivers to protect higher-level drivers from having to access any HBA-specific (or miniport driver-specific) state information to find their devices or to cancel queued requests. This ensures that NT-based operating system storage class and filter drivers have no dependencies on any particular model of HBA.

See [**SCSI_REQUEST_BLOCK**](/windows-hardware/drivers/ddi/srb/ns-srb-_scsi_request_block) structure for more information.
