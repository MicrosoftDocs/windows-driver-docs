---
title: Unregistering the Minifilter
description: Unregistering the Minifilter
keywords:
- unregistering minifilters
ms.date: 04/20/2017
---

# Unregistering the Minifilter


## <span id="ddk_unregistering_the_minifilter_if"></span><span id="DDK_UNREGISTERING_THE_MINIFILTER_IF"></span>


A minifilter driver's [**FilterUnloadCallback**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_filter_unload_callback) routine must call [**FltUnregisterFilter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltunregisterfilter) to unregister the minifilter driver. Calling **FltUnregisterFilter** causes the following things to happen:

-   The minifilter driver's callback routines are unregistered.

-   The minifilter driver's instances are torn down, and the minifilter driver's [**InstanceTeardownStartCallback**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_instance_teardown_callback) and **InstanceTeardownCompleteCallback** routines are called for each minifilter driver instance.

-   If the minifilter driver set any contexts on volumes, instances, streams, or stream handles, these contexts are deleted. If the minifilter driver has registered a [**CleanupContext**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_context_cleanup_callback) callback routine for a given context type, the filter manager calls the *CleanupContext* routine before deleting the context.

If there are outstanding rundown references on the minifilter driver's opaque filter pointer, **FltUnregisterFilter** enters a wait state until they are removed. Outstanding rundown references usually happen because the minifilter driver has called [**FltQueueGenericWorkItem**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltqueuegenericworkitem) to insert a work item into a system work queue, and the work item has not yet been dequeued and processed. (The filter manager adds the rundown reference when the minifilter driver calls **FltQueueGenericWorkItem** and removes it when the minifilter driver's work routine returns.)

Outstanding rundown references can also happen if the minifilter driver has called any routines that add a rundown reference to the minifilter driver's opaque filter pointer, such as [**FltObjectReference**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltobjectreference) or [**FltGetFilterFromInstance**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetfilterfrominstance), but did not subsequently call [**FltObjectDereference**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltobjectdereference).

 

