---
title: Unregistering the Minifilter
author: windows-driver-content
description: Unregistering the Minifilter
ms.assetid: 4af2d4fd-bfbe-4a75-bbfb-2a1c4b5c2032
keywords: ["unregistering minifilters"]
---

# Unregistering the Minifilter


## <span id="ddk_unregistering_the_minifilter_if"></span><span id="DDK_UNREGISTERING_THE_MINIFILTER_IF"></span>


A minifilter driver's [**FilterUnloadCallback**](https://msdn.microsoft.com/library/windows/hardware/ff551085) routine must call [**FltUnregisterFilter**](https://msdn.microsoft.com/library/windows/hardware/ff544606) to unregister the minifilter driver. Calling **FltUnregisterFilter** causes the following things to happen:

-   The minifilter driver's callback routines are unregistered.

-   The minifilter driver's instances are torn down, and the minifilter driver's [**InstanceTeardownStartCallback**](https://msdn.microsoft.com/library/windows/hardware/ff551098) and **InstanceTeardownCompleteCallback** routines are called for each minifilter driver instance.

-   If the minifilter driver set any contexts on volumes, instances, streams, or stream handles, these contexts are deleted. If the minifilter driver has registered a [**CleanupContext**](https://msdn.microsoft.com/library/windows/hardware/ff551078) callback routine for a given context type, the filter manager calls the *CleanupContext* routine before deleting the context.

If there are outstanding rundown references on the minifilter driver's opaque filter pointer, **FltUnregisterFilter** enters a wait state until they are removed. Outstanding rundown references usually happen because the minifilter driver has called [**FltQueueGenericWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff543452) to insert a work item into a system work queue, and the work item has not yet been dequeued and processed. (The filter manager adds the rundown reference when the minifilter driver calls **FltQueueGenericWorkItem** and removes it when the minifilter driver's work routine returns.)

Outstanding rundown references can also happen if the minifilter driver has called any routines that add a rundown reference to the minifilter driver's opaque filter pointer, such as [**FltObjectReference**](https://msdn.microsoft.com/library/windows/hardware/ff543382) or [**FltGetFilterFromInstance**](https://msdn.microsoft.com/library/windows/hardware/ff543049), but did not subsequently call [**FltObjectDereference**](https://msdn.microsoft.com/library/windows/hardware/ff543378).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Unregistering%20the%20Minifilter%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


