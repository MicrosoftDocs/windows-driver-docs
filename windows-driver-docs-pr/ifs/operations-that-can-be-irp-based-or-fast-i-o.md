---
title: Operations That Can Be IRP-Based or Fast I/O
description: Operations That Can Be IRP-Based or Fast I/O
ms.assetid: 768f5744-1aea-4fa8-b81b-d2670d6c878e
keywords:
- fast I/O buffers WDK file system
- Flags member WDK file system
- device object flags WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




