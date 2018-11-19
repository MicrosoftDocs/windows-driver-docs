---
title: Unregistering the Minifilter
description: Unregistering the Minifilter
ms.assetid: 4af2d4fd-bfbe-4a75-bbfb-2a1c4b5c2032
keywords:
- unregistering minifilters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unregistering the Minifilter


## <span id="ddk_unregistering_the_minifilter_if"></span><span id="DDK_UNREGISTERING_THE_MINIFILTER_IF"></span>


A minifilter driver's [**FilterUnloadCallback**](https://msdn.microsoft.com/library/windows/hardware/ff551085) routine must call [**FltUnregisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544606) to unregister the minifilter driver. Calling **FltUnregisterFilter** causes the following things to happen:

-   The minifilter driver's callback routines are unregistered.

-   The minifilter driver's instances are torn down, and the minifilter driver's [**InstanceTeardownStartCallback**](https://msdn.microsoft.com/library/windows/hardware/ff551098) and **InstanceTeardownCompleteCallback** routines are called for each minifilter driver instance.

-   If the minifilter driver set any contexts on volumes, instances, streams, or stream handles, these contexts are deleted. If the minifilter driver has registered a [**CleanupContext**](https://msdn.microsoft.com/library/windows/hardware/ff551078) callback routine for a given context type, the filter manager calls the *CleanupContext* routine before deleting the context.

If there are outstanding rundown references on the minifilter driver's opaque filter pointer, **FltUnregisterFilter** enters a wait state until they are removed. Outstanding rundown references usually happen because the minifilter driver has called [**FltQueueGenericWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff543452) to insert a work item into a system work queue, and the work item has not yet been dequeued and processed. (The filter manager adds the rundown reference when the minifilter driver calls **FltQueueGenericWorkItem** and removes it when the minifilter driver's work routine returns.)

Outstanding rundown references can also happen if the minifilter driver has called any routines that add a rundown reference to the minifilter driver's opaque filter pointer, such as [**FltObjectReference**](https://msdn.microsoft.com/library/windows/hardware/ff543382) or [**FltGetFilterFromInstance**](https://msdn.microsoft.com/library/windows/hardware/ff543049), but did not subsequently call [**FltObjectDereference**](https://msdn.microsoft.com/library/windows/hardware/ff543378).

 

 




