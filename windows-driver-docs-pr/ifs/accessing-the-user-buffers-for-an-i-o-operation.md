---
title: Accessing the User Buffers for an I/O Operation
description: Accessing the User Buffers for an I/O Operation
keywords:
- buffers WDK file system minifilter
- FLT_PARAMETERS
- memory descriptor lists WDK file system minifilter
- MDLs WDK file systems
- I/O WDK file systems
- IRP-based I/O operations WDK file system minifilter
ms.date: 04/20/2017
---

# Accessing the User Buffers for an I/O Operation


## <span id="ddk_accessing_the_user_buffers_for_an_io_operation_if"></span><span id="DDK_ACCESSING_THE_USER_BUFFERS_FOR_AN_IO_OPERATION_IF"></span>


The [**FLT\_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) structure for an I/O operation contains the operation-specific parameters for the operation, including buffer addresses and memory descriptor lists (MDL) for any buffers that are used in the operation.

For IRP-based I/O operations, the buffers for the operation can be specified by using:

-   MDL only (typically for paging I/O)

-   Buffer address only

-   Buffer address and MDL

For fast I/O operations, only the user-space buffer address is specified. Fast I/O operations that have buffers always use neither buffered nor direct I/O and thus never have MDL parameters.

The following topics provide guidelines for handling buffer addresses and MDLs for IRP-based and fast I/O operations in minifilter driver [**preoperation callback routines**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_pre_operation_callback) and [**postoperation callback routines**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_post_operation_callback):

[Accessing User Buffers in a Preoperation Callback Routine](accessing-user-buffers-in-a-preoperation-callback-routine.md)

[Accessing User Buffers in a Postoperation Callback Routine](accessing-user-buffers-in-a-postoperation-callback-routine.md)

 

