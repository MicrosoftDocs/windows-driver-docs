---
title: IRP-Based I/O Operations That Always Use Buffered I/O
description: IRP-Based I/O Operations That Always Use Buffered I/O
keywords:
- buffered I/O WDK file system
ms.date: 04/20/2017
---

# IRP-Based I/O Operations That Always Use Buffered I/O


## <span id="ddk_irp_based_io_operations_that_always_use_buffered_io_if"></span><span id="DDK_IRP_BASED_IO_OPERATIONS_THAT_ALWAYS_USE_BUFFERED_IO_IF"></span>


The following IRP-based I/O operations always use buffered I/O, regardless of the value of the **Flags** member of the [**DEVICE\_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_object) structure for the file system volume:

-   IRP\_MJ\_CREATE ([**EaBuffer parameter**](./flt-parameters-for-irp-mj-create.md))

-   IRP\_MJ\_QUERY\_INFORMATION

-   IRP\_MJ\_QUERY\_VOLUME\_INFORMATION

-   IRP\_MJ\_SET\_INFORMATION

-   IRP\_MJ\_SET\_VOLUME\_INFORMATION

Note that IRP\_MJ\_QUERY\_INFORMATION can also be a fast I/O operation. When it is a fast I/O operation, it uses neither buffered nor direct I/O. For more information about I/O operations that can be IRP-based or fast I/O operations, see [Operations That Can Be IRP-Based or Fast I/O](operations-that-can-be-irp-based-or-fast-i-o.md).

 

