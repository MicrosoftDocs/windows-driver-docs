---
title: Performing Global Cleanup
description: Performing Global Cleanup
ms.assetid: 18e0fca0-16ec-4ca9-8b71-47f58f41c46d
keywords:
- global cleanup WDK file system minifilter
- cleanup globally WDK file system minifilter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Performing Global Cleanup


## <span id="ddk_performing_global_cleanup_if"></span><span id="DDK_PERFORMING_GLOBAL_CLEANUP_IF"></span>


A minifilter driver's [**FilterUnloadCallback**](https://msdn.microsoft.com/library/windows/hardware/ff551085) routine must perform any needed global cleanup. The following list includes examples of global cleanup tasks that a minifilter driver might perform:

-   Call [**ExDeleteResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff544578) to delete a global resource variable that was initialized by a previous call to [**ExInitializeResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545317).

-   Call [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590) or [**ExFreePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544593) to free global memory that was allocated by a previous call to a routine such as [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520).

-   Call [**ExDeleteNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff544566) or [**ExDeletePagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff544570) to delete a lookaside list that was allocated by a previous call to [**ExInitializeNPagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff545301) or [**ExInitializePagedLookasideList**](https://msdn.microsoft.com/library/windows/hardware/ff545309), respectively.

-   Call [**PsRemoveCreateThreadNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559947) or [**PsRemoveLoadImageNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559949) to unregister a global callback routine that was registered by a previous call to [**PsSetCreateThreadNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559954) or [**PsSetLoadImageNotifyRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559957), respectively.

 

 




