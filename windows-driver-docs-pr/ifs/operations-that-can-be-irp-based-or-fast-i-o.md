---
title: Operations That Can Be IRP-Based or Fast I/O
description: Operations That Can Be IRP-Based or Fast I/O
ms.assetid: 768f5744-1aea-4fa8-b81b-d2670d6c878e
keywords: ["fast I/O buffers WDK file system", "Flags member WDK file system", "device object flags WDK file system"]
---

# Operations That Can Be IRP-Based or Fast I/O


## <span id="ddk_operations_that_can_be_irp_based_or_fast_io_if"></span><span id="DDK_OPERATIONS_THAT_CAN_BE_IRP_BASED_OR_FAST_IO_IF"></span>


The following types of operations can be IRP-based or fast I/O operations:

-   IRP\_MJ\_DEVICE\_CONTROL. (Note that IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL is always IRP-based.)

-   IRP\_MJ\_QUERY\_INFORMATION. This operation can be fast I/O if the **FileInformationClass** parameter is **FileBasicInformation**, **FileStandardInformation**, or **FileNetworkOpenInformation**.

-   IRP\_MJ\_READ. Minifilter drivers can set the FLTFL\_OPERATION\_REGISTRATION\_SKIP\_CACHED\_IO flag in the [**FLT\_OPERATION\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff544668) structure to avoid receiving fast I/O IRP\_MJ\_READ operations and cached IRP-based reads.

-   IRP\_MJ\_WRITE. Minifilter drivers can set the FLTFL\_OPERATION\_REGISTRATION\_SKIP\_CACHED\_IO flag in the FLT\_OPERATION\_REGISTRATION structure to avoid receiving fast I/O IRP\_MJ\_WRITE operations and cached IRP-based writes.

When any of these operations is a fast I/O operation, it always uses neither buffered nor direct I/O, even if the equivalent IRP-based operation uses a different buffering method.

When IRP\_MJ\_DEVICE\_CONTROL is a fast I/O operation, it always uses neither buffered nor direct I/O, regardless of the IOCTL's transfer type.

Although IRP\_MJ\_LOCK\_CONTROL can be an IRP-based or fast I/O operation, it has no buffers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Operations%20That%20Can%20Be%20IRP-Based%20or%20Fast%20I/O%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




