---
title: Filtering I/O Operations in a Minifilter Driver
description: Filtering I/O Operations in a Minifilter Driver
keywords:
- preoperation callback routines WDK file system minifilter , guidelines
- postoperation callback routines WDK file system minifilter , guidelines
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filtering I/O Operations in a Minifilter Driver


## <span id="ddk_filtering_io_operations_in_a_minifilter_driver_if"></span><span id="DDK_FILTERING_IO_OPERATIONS_IN_A_MINIFILTER_DRIVER_IF"></span>


The following list describes several guidelines for filtering specific types of I/O operations in a file system minifilter driver:

-   The [**preoperation callback routine**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_pre_operation_callback) for IRP\_MJ\_CREATE cannot query or set contexts for files, streams, or stream handles, because, at pre-create time, the file or stream (if any) that is going to be created has not yet been determined.

-   The [**postoperation callback routine**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_post_operation_callback) for IRP\_MJ\_CLOSE cannot set or query contexts for files, streams, or stream handles, because the system-internal structures that those items are associated with are freed before the post-close routine is called.

-   Minifilter drivers must never fail IRP\_MJ\_CLEANUP or IRP\_MJ\_CLOSE operations. These operations can be pended, returned to the filter manager, or completed with STATUS\_SUCCESS. However, a preoperation callback routine must never fail these operations.

-   Minifilter drivers cannot register a postoperation callback routine for IRP\_MJ\_SHUTDOWN.

 

