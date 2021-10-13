---
title: Writing a FilterUnloadCallback Routine
description: Writing a FilterUnloadCallback Routine
keywords:
- FilterUnloadCallback
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing a FilterUnloadCallback Routine


## <span id="ddk_writing_a_filterunloadcallback_routine_if"></span><span id="DDK_WRITING_A_FILTERUNLOADCALLBACK_ROUTINE_IF"></span>


The *FilterUnloadCallback* routine is defined as follows:

```cpp
typedef NTSTATUS
(*PFLT_FILTER_UNLOAD_CALLBACK) (
    FLT_FILTER_UNLOAD_FLAGS Flags
    );
```

The *FilterUnloadCallback* routine has one input parameter, *Flags*, which can be **NULL** or FLTFL\_FILTER\_UNLOAD\_MANDATORY. The filter manager sets this parameter to FLTFL\_FILTER\_UNLOAD\_MANDATORY to indicate that the unload operation is mandatory. For more information about this parameter, see [**PFLT\_FILTER\_UNLOAD\_CALLBACK**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_filter_unload_callback).

A minifilter driver's *FilterUnloadCallback* routine must perform the following steps:

-   Close any open kernel-mode communication server port handles.

-   Call [**FltUnregisterFilter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltunregisterfilter) to unregister the minifilter driver.

-   Perform any needed global cleanup.

-   Return an appropriate NTSTATUS value.

This section includes:

[Closing the Communication Server Port](closing-the-communication-server-port.md)

[Unregistering the Minifilter](unregistering-the-minifilter.md)

[Performing Global Cleanup](performing-global-cleanup.md)

[Returning Status from a FilterUnloadCallback Routine](returning-status-from-a-filterunloadcallback-routine.md)

 

