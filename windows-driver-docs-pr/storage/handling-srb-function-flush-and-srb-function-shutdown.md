---
title: Handling SRB\_FUNCTION\_FLUSH and SRB\_FUNCTION\_SHUTDOWN
description: Handling SRB\_FUNCTION\_FLUSH and SRB\_FUNCTION\_SHUTDOWN
ms.assetid: d4b8b3e5-d895-42ca-bd28-9d3cef805654
keywords: ["SCSI miniport drivers WDK storage , HwScsiStartIo", "HwScsiStartIo", "SRB_FUNCTION_FLUSH", "SRB_FUNCTION_SHUTDOWN"]
---

# Handling SRB\_FUNCTION\_FLUSH and SRB\_FUNCTION\_SHUTDOWN


## <span id="ddk_handling_srb_function_flush_and_srb_function_shutdown_kg"></span><span id="DDK_HANDLING_SRB_FUNCTION_FLUSH_AND_SRB_FUNCTION_SHUTDOWN_KG"></span>


If the HBA caches data internally, as indicated when [*HwScsiFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff557300) sets up the [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff563900), the [**HwScsiStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557323) routine must support the SRB\_FUNCTION\_FLUSH and SRB\_FUNCTION\_SHUTDOWN requests as follows:

-   An SRB with its **Function** member set to SRB\_FUNCTION\_FLUSH tells the miniport driver to transfer data cached in the HBA, usually to a disk. The miniport driver must hold on to the flush request until all cached data has been transferred and, then, complete the flush request.

-   Such a flush request might originate when an application closes a file or the application itself is terminated.

-   An SRB with its **Function** member set to SRB\_FUNCTION\_SHUTDOWN tells the miniport driver to complete transferring data, including flushing all cached data, out to the target device. The miniport driver must hold on to the shutdown request until no data remains in the HBA's internal cache for the target logical unit and, then, complete the shutdown request.

    Note that a miniport driver can be called with more than one shutdown request, possibly for the same logical unit or with several shutdown requests for different logical units, before the system itself is actually shut down.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Handling%20SRB_FUNCTION_FLUSH%20and%20SRB_FUNCTION_SHUTDOWN%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




