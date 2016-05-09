---
title: Filtering I/O Operations in a Minifilter Driver
description: Filtering I/O Operations in a Minifilter Driver
ms.assetid: e35944c1-fcc6-44e0-838c-da8d24f95d51
keywords: ["preoperation callback routines WDK file system minifilter , guidelines", "postoperation callback routines WDK file system minifilter , guidelines"]
---

# Filtering I/O Operations in a Minifilter Driver


## <span id="ddk_filtering_io_operations_in_a_minifilter_driver_if"></span><span id="DDK_FILTERING_IO_OPERATIONS_IN_A_MINIFILTER_DRIVER_IF"></span>


The following list describes several guidelines for filtering specific types of I/O operations in a file system minifilter driver:

-   The [**preoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551109) for IRP\_MJ\_CREATE cannot query or set contexts for files, streams, or stream handles, because, at pre-create time, the file or stream (if any) that is going to be created has not yet been determined.

-   The [**postoperation callback routine**](https://msdn.microsoft.com/library/windows/hardware/ff551107) for IRP\_MJ\_CLOSE cannot set or query contexts for files, streams, or stream handles, because the system-internal structures that those items are associated with are freed before the post-close routine is called.

-   Minifilter drivers must never fail IRP\_MJ\_CLEANUP or IRP\_MJ\_CLOSE operations. These operations can be pended, returned to the filter manager, or completed with STATUS\_SUCCESS. However, a preoperation callback routine must never fail these operations.

-   Minifilter drivers cannot register a postoperation callback routine for IRP\_MJ\_SHUTDOWN.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Filtering%20I/O%20Operations%20in%20a%20Minifilter%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




