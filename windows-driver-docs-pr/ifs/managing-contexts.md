---
title: Managing Contexts
description: Managing Contexts
ms.assetid: 1ad33c6c-a5dd-4b65-bfcc-a40453d3a6b5
keywords:
- filter manager WDK file system minifilter , contexts
- file system minifilter drivers WDK , contexts
- minifilter drivers WDK , context
- contexts WDK file system minifilter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing Contexts


The filter manager enables minifilter drivers to associate contexts with objects to preserve state across I/O operations. Objects that can have contexts include volumes, instances, streams, and stream handles.

Third-party file systems must use the [**FSRTL\_ADVANCED\_FCB\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff547334) structure (instead of the [**FSRTL\_COMMON\_FCB\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff547343) structure) to work properly with stream and stream handle contexts.

Contexts can be allocated from paged or nonpaged pool except for volume contexts, which must be allocated from nonpaged pool.

Contexts are freed automatically when all outstanding references have been released. If the minifilter driver defines a context cleanup callback routine, the filter manager calls the routine before the context is freed.

The filter manager takes care of deleting contexts when the associated object is deleted, when an instance is detached, and when the minifilter driver is unloaded.

If a minifilter driver supports only one instance per volume, use instance contexts rather than volume contexts for better performance. You can also improve performance by storing a pointer to the minifilter driver instance context inside stream or stream handle contexts.

Contexts are not supported for paging files or during the following operations:

-   Preoperation processing for create requests

-   Postoperation processing for close requests

-   Processing of IRP\_MJ\_NETWORK\_QUERY\_OPEN requests

See the CTX sample for an example of a minifilter driver that uses contexts.

### <span id="Filter_Manager_Routines_for_Context_Management"></span><span id="filter_manager_routines_for_context_management"></span><span id="FILTER_MANAGER_ROUTINES_FOR_CONTEXT_MANAGEMENT"></span>Filter Manager Routines for Context Management

The filter manager provides the following support routines for creating, registering, and setting contexts:

[**FltAllocateContext**](https://msdn.microsoft.com/library/windows/hardware/ff541710)

[**FltRegisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544305)

[**FltSetInstanceContext**](https://msdn.microsoft.com/library/windows/hardware/ff544521)

[**FltSetStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff544543)

[**FltSetStreamHandleContext**](https://msdn.microsoft.com/library/windows/hardware/ff544552)

[**FltSetVolumeContext**](https://msdn.microsoft.com/library/windows/hardware/ff544557)

The following routines are provided for querying context support:

[**FltSupportsStreamContexts**](https://msdn.microsoft.com/library/windows/hardware/ff544581)

[**FltSupportsStreamHandleContexts**](https://msdn.microsoft.com/library/windows/hardware/ff544586)

The following routines are provided for getting and referencing contexts:

[**FltGetContexts**](https://msdn.microsoft.com/library/windows/hardware/ff542997)

[**FltGetInstanceContext**](https://msdn.microsoft.com/library/windows/hardware/ff543058)

[**FltGetStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff543144)

[**FltGetStreamHandleContext**](https://msdn.microsoft.com/library/windows/hardware/ff543155)

[**FltGetVolumeContext**](https://msdn.microsoft.com/library/windows/hardware/ff543189)

[**FltReferenceContext**](https://msdn.microsoft.com/library/windows/hardware/ff544291)

The following routines are provided for releasing and deleting contexts:

[**FltDeleteContext**](https://msdn.microsoft.com/library/windows/hardware/ff541960)

[**FltDeleteInstanceContext**](https://msdn.microsoft.com/library/windows/hardware/ff541982)

[**FltDeleteStreamContext**](https://msdn.microsoft.com/library/windows/hardware/ff541997)

[**FltDeleteStreamHandleContext**](https://msdn.microsoft.com/library/windows/hardware/ff542016)

[**FltDeleteVolumeContext**](https://msdn.microsoft.com/library/windows/hardware/ff542030)

[**FltReleaseContext**](https://msdn.microsoft.com/library/windows/hardware/ff544314)

[**FltReleaseContexts**](https://msdn.microsoft.com/library/windows/hardware/ff544317)

### <span id="Minifilter_Driver_Callback_Routines_for_Context_Management"></span><span id="minifilter_driver_callback_routines_for_context_management"></span><span id="MINIFILTER_DRIVER_CALLBACK_ROUTINES_FOR_CONTEXT_MANAGEMENT"></span>Minifilter Driver Callback Routines for Context Management

The following callback routines are stored in the [**FLT\_REGISTRATION**](https://msdn.microsoft.com/library/windows/hardware/ff544811) structure that is passed as a parameter to [**FltRegisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544305) for minifilter drivers that manage contexts:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Callback Routine Name</th>
<th align="left">Callback Routine Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>ContextAllocateCallback</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551075" data-raw-source="[&lt;strong&gt;PFLT_CONTEXT_ALLOCATE_CALLBACK&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551075)"><strong>PFLT_CONTEXT_ALLOCATE_CALLBACK</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><em>ContextCleanupCallback</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551078" data-raw-source="[&lt;strong&gt;PFLT_CONTEXT_CLEANUP_CALLBACK&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551078)"><strong>PFLT_CONTEXT_CLEANUP_CALLBACK</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>ContextFreeCallback</em></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff551082" data-raw-source="[&lt;strong&gt;PFLT_CONTEXT_FREE_CALLBACK&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551082)"><strong>PFLT_CONTEXT_FREE_CALLBACK</strong></a></p></td>
</tr>
</tbody>
</table>

 

 

 




