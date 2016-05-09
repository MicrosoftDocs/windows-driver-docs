---
title: IRP-Based I/O Operations That Always Use Buffered I/O
author: windows-driver-content
description: IRP-Based I/O Operations That Always Use Buffered I/O
ms.assetid: ac9b62a2-a562-4f40-83af-e1c74d58ce2b
keywords: ["buffered I/O WDK file system"]
---

# IRP-Based I/O Operations That Always Use Buffered I/O


## <span id="ddk_irp_based_io_operations_that_always_use_buffered_io_if"></span><span id="DDK_IRP_BASED_IO_OPERATIONS_THAT_ALWAYS_USE_BUFFERED_IO_IF"></span>


The following IRP-based I/O operations always use buffered I/O, regardless of the value of the **Flags** member of the [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) structure for the file system volume:

-   IRP\_MJ\_CREATE ([**EaBuffer parameter**](https://msdn.microsoft.com/library/windows/hardware/ff544687))

-   IRP\_MJ\_QUERY\_INFORMATION

-   IRP\_MJ\_QUERY\_VOLUME\_INFORMATION

-   IRP\_MJ\_SET\_INFORMATION

-   IRP\_MJ\_SET\_VOLUME\_INFORMATION

Note that IRP\_MJ\_QUERY\_INFORMATION can also be a fast I/O operation. When it is a fast I/O operation, it uses neither buffered nor direct I/O. For more information about I/O operations that can be IRP-based or fast I/O operations, see [Operations That Can Be IRP-Based or Fast I/O](operations-that-can-be-irp-based-or-fast-i-o.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20IRP-Based%20I/O%20Operations%20That%20Always%20Use%20Buffered%20I/O%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


