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


A minifilter driver's [**FilterUnloadCallback**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/fltkernel/nc-fltkernel-pflt_filter_unload_callback) routine must perform any needed global cleanup. The following list includes examples of global cleanup tasks that a minifilter driver might perform:

-   Call [**ExDeleteResourceLite**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exdeleteresourcelite) to delete a global resource variable that was initialized by a previous call to [**ExInitializeResourceLite**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exinitializeresourcelite).

-   Call [**ExFreePool**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-exfreepool) or [**ExFreePoolWithTag**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exfreepoolwithtag) to free global memory that was allocated by a previous call to a routine such as [**ExAllocatePoolWithTag**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exallocatepoolwithtag).

-   Call [**ExDeleteNPagedLookasideList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exdeletenpagedlookasidelist) or [**ExDeletePagedLookasideList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exdeletepagedlookasidelist) to delete a lookaside list that was allocated by a previous call to [**ExInitializeNPagedLookasideList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exinitializenpagedlookasidelist) or [**ExInitializePagedLookasideList**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exinitializepagedlookasidelist), respectively.

-   Call [**PsRemoveCreateThreadNotifyRoutine**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-psremovecreatethreadnotifyroutine) or [**PsRemoveLoadImageNotifyRoutine**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-psremoveloadimagenotifyroutine) to unregister a global callback routine that was registered by a previous call to [**PsSetCreateThreadNotifyRoutine**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-pssetcreatethreadnotifyroutine) or [**PsSetLoadImageNotifyRoutine**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-pssetloadimagenotifyroutine), respectively.

 

 




