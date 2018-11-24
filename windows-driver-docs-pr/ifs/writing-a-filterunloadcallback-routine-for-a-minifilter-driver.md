---
title: Writing a FilterUnloadCallback Routine for a Minifilter Driver
description: Writing a FilterUnloadCallback Routine for a Minifilter Driver
ms.assetid: 0f4eac6d-08ef-47d5-8c1f-5397f058ecb2
keywords:
- file system minifilter drivers WDK , FilterUnloadCallback routine
- minifilter drivers WDK , FilterUnloadCallback routine
- FilterUnloadCallback
- unload routines WDK file system minifilter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing a FilterUnloadCallback Routine for a Minifilter Driver


## <span id="ddk_writing_a_filterunloadcallback_routine_for_a_minifilter_driver_if"></span><span id="DDK_WRITING_A_FILTERUNLOADCALLBACK_ROUTINE_FOR_A_MINIFILTER_DRIVER_IF"></span>


A file system minifilter driver can optionally register a [**PFLT\_FILTER\_UNLOAD\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff551085)-typed routine as the minifilter driver's *FilterUnloadCallback* routine. This callback routine is also referred to as the minifilter driver's *unload routine*.

Minifilter drivers are not required to register a *FilterUnloadCallback* routine. However, we strongly recommend that a minifilter driver registers this callback routine, because if a minifilter driver does not register a *FilterUnloadCallback* routine, the driver cannot be unloaded.

To register this callback routine, the minifilter driver stores the address of a PFLT\_FILTER\_UNLOAD\_CALLBACK-typed routine in the **FilterUnloadCallback** member of the [**FLT\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff544811) structure that the minifilter driver passes as a parameter to [**FltRegisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544305) in its **DriverEntry** routine.

This section includes:

[When the FilterUnloadCallback Routine Is Called](when-the-filterunloadcallback-routine-is-called.md)

[Writing a FilterUnloadCallback Routine](writing-a-filterunloadcallback-routine.md)

 

 




