---
title: Writing a FilterUnloadCallback Routine for a Minifilter Driver
author: windows-driver-content
description: Writing a FilterUnloadCallback Routine for a Minifilter Driver
ms.assetid: 0f4eac6d-08ef-47d5-8c1f-5397f058ecb2
keywords: ["file system minifilter drivers WDK , FilterUnloadCallback routine", "minifilter drivers WDK , FilterUnloadCallback routine", "FilterUnloadCallback", "unload routines WDK file system minifilter"]
---

# Writing a FilterUnloadCallback Routine for a Minifilter Driver


## <span id="ddk_writing_a_filterunloadcallback_routine_for_a_minifilter_driver_if"></span><span id="DDK_WRITING_A_FILTERUNLOADCALLBACK_ROUTINE_FOR_A_MINIFILTER_DRIVER_IF"></span>


A file system minifilter driver can optionally register a [**PFLT\_FILTER\_UNLOAD\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff551085)-typed routine as the minifilter driver's *FilterUnloadCallback* routine. This callback routine is also referred to as the minifilter driver's *unload routine*.

Minifilter drivers are not required to register a *FilterUnloadCallback* routine. However, we strongly recommend that a minifilter driver registers this callback routine, because if a minifilter driver does not register a *FilterUnloadCallback* routine, the driver cannot be unloaded.

To register this callback routine, the minifilter driver stores the address of a PFLT\_FILTER\_UNLOAD\_CALLBACK-typed routine in the **FilterUnloadCallback** member of the [**FLT\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff544811) structure that the minifilter driver passes as a parameter to [**FltRegisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544305) in its **DriverEntry** routine.

This section includes:

[When the FilterUnloadCallback Routine Is Called](when-the-filterunloadcallback-routine-is-called.md)

[Writing a FilterUnloadCallback Routine](writing-a-filterunloadcallback-routine.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Writing%20a%20FilterUnloadCallback%20Routine%20for%20a%20Minifilter%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


