---
title: Other SRB_FUNCTION_XXX Requests
description: Other SRB_FUNCTION_XXX Requests
ms.assetid: b0430d8e-e5cd-4f17-b77f-ec608b1469da
keywords:
- SCSI miniport drivers WDK storage , HwScsiStartIo
- HwScsiStartIo
- SRB_FUNCTION_XXX future use
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Other SRB\_FUNCTION\_XXX Requests


## <span id="ddk_other_srb_function_xxx_requests_kg"></span><span id="DDK_OTHER_SRB_FUNCTION_XXX_REQUESTS_KG"></span>


The following SRB **Function** values are defined for use in future versions of the operating system:

-   SRB\_FUNCTION\_RECEIVE\_EVENT

-   SRB\_FUNCTION\_RELEASE\_RECOVERY

-   SRB\_FUNCTION\_RESET\_DEVICE

-   SRB\_FUNCTION\_TERMINATE\_IO

The NT-based operating system SCSI port driver processes requests with the following SRB **Function** values without calling any SCSI miniport driver:

-   SRB\_FUNCTION\_CLAIM\_DEVICE

-   SRB\_FUNCTION\_RELEASE\_QUEUE

-   SRB\_FUNCTION\_FLUSH\_QUEUE

-   SRB\_FUNCTION\_RELEASE\_DEVICE

-   SRB\_FUNCTION\_LOCK\_QUEUE

-   SRB\_FUNCTION\_UNLOCK\_QUEUE

For details about these functions, see [Storage Class Drivers](storage-class-drivers.md).

Miniport driver designers can assume that their miniport drivers will *never* be sent an SRB with any of the immediately preceding **Function** values. The NT-based operating system port driver handles these requests from storage class and filter drivers to protect higher-level drivers from having to access any HBA-specific (or miniport driver-specific) state information to find their devices or to cancel queued requests. This ensures that NT-based operating system storage class and filter drivers have no dependencies on any particular model of HBA.

See [**SCSI\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff565393) structure for more information.

 

 




