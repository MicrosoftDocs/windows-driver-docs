---
title: Performing Global Cleanup
author: windows-driver-content
description: Performing Global Cleanup
ms.assetid: 18e0fca0-16ec-4ca9-8b71-47f58f41c46d
keywords: ["global cleanup WDK file system minifilter", "cleanup globally WDK file system minifilter"]
---

# Performing Global Cleanup


## <span id="ddk_performing_global_cleanup_if"></span><span id="DDK_PERFORMING_GLOBAL_CLEANUP_IF"></span>


A minifilter driver's [**FilterUnloadCallback**](https://msdn.microsoft.com/library/windows/hardware/ff551085) routine must perform any needed global cleanup. The following list includes examples of global cleanup tasks that a minifilter driver might perform:

-   Call [**ExDeleteResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff544578) to delete a global resource variable that was initialized by a previous call to [**ExInitializeResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545317).

-   Call [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590) or [**ExFreePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544593) to free global memory that was allocated by a previous call to a routine such as [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520).

-   Call [**ExDeleteNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff544566) or [**ExDeletePagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff544570) to delete a lookaside list that was allocated by a previous call to [**ExInitializeNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff545301) or [**ExInitializePagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff545309), respectively.

-   Call [**PsRemoveCreateThreadNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559947) or [**PsRemoveLoadImageNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559949) to unregister a global callback routine that was registered by a previous call to [**PsSetCreateThreadNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559954) or [**PsSetLoadImageNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559957), respectively.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Performing%20Global%20Cleanup%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


