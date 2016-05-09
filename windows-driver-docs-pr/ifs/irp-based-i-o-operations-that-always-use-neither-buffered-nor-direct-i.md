---
title: IRP-Based I/O Operations That Always Use Neither Buffered Nor Direct I/O
description: IRP-Based I/O Operations That Always Use Neither Buffered Nor Direct I/O
ms.assetid: 2d757904-e46c-476d-896c-77beacfe4b7c
keywords: ["neither buffered nor direct I/O WDK file system"]
---

# IRP-Based I/O Operations That Always Use Neither Buffered Nor Direct I/O


## <span id="ddk_irp_based_io_operations_that_always_use_neither_buffered_nor_direc"></span><span id="DDK_IRP_BASED_IO_OPERATIONS_THAT_ALWAYS_USE_NEITHER_BUFFERED_NOR_DIREC"></span>


The following IRP-based I/O operations always use neither buffered nor direct I/O, regardless of the value of the **Flags** member of the [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) structure for the file system volume:

-   IRP\_MJ\_PNP

-   IRP\_MJ\_QUERY\_SECURITY

-   IRP\_MJ\_SET\_SECURITY

-   IRP\_MJ\_SYSTEM\_CONTROL

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20IRP-Based%20I/O%20Operations%20That%20Always%20Use%20Neither%20Buffered%20Nor%20Direct%20I/O%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




