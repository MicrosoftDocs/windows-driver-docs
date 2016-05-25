---
title: Writing a FilterUnloadCallback Routine
author: windows-driver-content
description: Writing a FilterUnloadCallback Routine
ms.assetid: 2f680770-38af-4dcb-93b8-7f770e0378b2
keywords: ["FilterUnloadCallback"]
---

# Writing a FilterUnloadCallback Routine


## <span id="ddk_writing_a_filterunloadcallback_routine_if"></span><span id="DDK_WRITING_A_FILTERUNLOADCALLBACK_ROUTINE_IF"></span>


The *FilterUnloadCallback* routine is defined as follows:

```
typedef NTSTATUS
(*PFLT_FILTER_UNLOAD_CALLBACK) (
    FLT_FILTER_UNLOAD_FLAGS Flags
    );
```

The *FilterUnloadCallback* routine has one input parameter, *Flags*, which can be **NULL** or FLTFL\_FILTER\_UNLOAD\_MANDATORY. The filter manager sets this parameter to FLTFL\_FILTER\_UNLOAD\_MANDATORY to indicate that the unload operation is mandatory. For more information about this parameter, see [**PFLT\_FILTER\_UNLOAD\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff551085).

A minifilter driver's *FilterUnloadCallback* routine must perform the following steps:

-   Close any open kernel-mode communication server port handles.

-   Call [**FltUnregisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544606) to unregister the minifilter driver.

-   Perform any needed global cleanup.

-   Return an appropriate NTSTATUS value.

This section includes:

[Closing the Communication Server Port](closing-the-communication-server-port.md)

[Unregistering the Minifilter](unregistering-the-minifilter.md)

[Performing Global Cleanup](performing-global-cleanup.md)

[Returning Status from a FilterUnloadCallback Routine](returning-status-from-a-filterunloadcallback-routine.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Writing%20a%20FilterUnloadCallback%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


