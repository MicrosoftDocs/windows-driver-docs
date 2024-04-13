---
title: Accessing User Buffers
description: Accessing User Buffers
keywords:
- filter manager WDK file system minifilter , user buffers
- buffers WDK file system minifilter
- user buffers WDK file system minifilter
ms.date: 04/20/2017
---

# Accessing User Buffers


All parameters specific to a given I/O operation, including buffers and memory descriptor lists (MDLs), are defined in an [**FLT\_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) union. This union is contained in an [**FLT\_IO\_PARAMETER\_BLOCK**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block) structure that is accessed through the **Iopb** member of the [**FLT\_CALLBACK\_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data) structure that represents the I/O operation. Both the filter manager and minifilter drivers use **FLT\_CALLBACK\_DATA** structures to initiate and process I/O operations.

The [**FLT\_PARAMETERS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters) union also contains any parameter definitions for IRP-based operations that are specific to the buffering method used for that operation (buffered, direct I/O, or neither buffered nor direct I/O). It also contains parameter definitions for non-IRP-based operations (fast I/O and FsFilter callback routines).

A minifilter driver can call [**FltDecodeParameters**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdecodeparameters) to get pointers to the MDL address, buffer pointer, buffer length, and desired access parameters for an I/O operation. This saves minifilter drivers from having a switch statement to find the position of these parameters in helper routines that access these parameters across multiple I/O operations.

When processing an I/O operation that involves user buffers, a minifilter driver should always use an MDL if one is available. If so, the minifilter driver should call [**MmGetSystemAddressForMdlSafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemaddressformdlsafe) to get a system address for the MDL and use the system address to access the user buffer.

If only a buffer address is available, the minifilter driver should always enclose any attempts to access the buffer in a try/except block. If the minifilter driver needs to access the buffer in a postoperation callback routine that is not synchronized, or if the I/O operation is posted to a worker thread, the minifilter driver should also lock the user buffer by calling [**FltLockUserBuffer**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltlockuserbuffer). This function determines the appropriate access method to apply for the locked buffer based on the type of I/O operation and creates an MDL that points to the locked pages.

### <span id="Filter_Manager_Routines_for_Accessing_User_Buffers"></span><span id="filter_manager_routines_for_accessing_user_buffers"></span><span id="FILTER_MANAGER_ROUTINES_FOR_ACCESSING_USER_BUFFERS"></span>Filter Manager Routines for Accessing User Buffers

The filter manager provides the following support routines for accessing user buffers in preoperation and postoperation callback routines:

[**FltDecodeParameters**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltdecodeparameters)

[**FltLockUserBuffer**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltlockuserbuffer)

 

