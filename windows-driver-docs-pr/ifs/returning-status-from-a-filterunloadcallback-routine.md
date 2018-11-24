---
title: Returning Status from a FilterUnloadCallback Routine
description: Returning Status from a FilterUnloadCallback Routine
ms.assetid: 6fdaadc7-860d-49d6-833c-64624f435fd3
keywords:
- status values WDK file system
- returning status WDK file system
- refusing unload operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Returning Status from a FilterUnloadCallback Routine


## <span id="ddk_returning_status_from_a_filterunloadcallback_routine_if"></span><span id="DDK_RETURNING_STATUS_FROM_A_FILTERUNLOADCALLBACK_ROUTINE_IF"></span>


A minifilter driver's [**FilterUnloadCallback**](https://msdn.microsoft.com/library/windows/hardware/ff551085) routine normally returns STATUS\_SUCCESS.

To refuse an unload operation that is not mandatory, the minifilter driver should return an appropriate warning or error NTSTATUS value such as STATUS\_FLT\_DO\_NOT\_DETACH. For more information about mandatory unload operations, see [Writing a FilterUnloadCallback Routine](writing-a-filterunloadcallback-routine.md) and [**PFLT\_FILTER\_UNLOAD\_CALLBACK**](https://msdn.microsoft.com/library/windows/hardware/ff551085).

If the *FilterUnloadCallback* routine returns a warning or error NTSTATUS value and the unload operation is not mandatory, the minifilter driver will not be unloaded.

 

 




