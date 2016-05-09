---
title: Other SRB\_FUNCTION\_XXX Requests
description: Other SRB\_FUNCTION\_XXX Requests
ms.assetid: b0430d8e-e5cd-4f17-b77f-ec608b1469da
keywords: ["SCSI miniport drivers WDK storage , HwScsiStartIo", "HwScsiStartIo", "SRB_FUNCTION_XXX future use"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Other%20SRB_FUNCTION_XXX%20%20Requests%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




