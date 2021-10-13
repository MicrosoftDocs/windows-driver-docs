---
title: Performing Global Cleanup
description: Performing Global Cleanup
keywords:
- global cleanup WDK file system minifilter
- cleanup globally WDK file system minifilter
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Performing Global Cleanup


## <span id="ddk_performing_global_cleanup_if"></span><span id="DDK_PERFORMING_GLOBAL_CLEANUP_IF"></span>


A minifilter driver's [**FilterUnloadCallback**](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_filter_unload_callback) routine must perform any needed global cleanup. The following list includes examples of global cleanup tasks that a minifilter driver might perform:

-   Call [**ExDeleteResourceLite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exdeleteresourcelite) to delete a global resource variable that was initialized by a previous call to [**ExInitializeResourceLite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializeresourcelite).

-   Call [**ExFreePool**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exfreepool) or [**ExFreePoolWithTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exfreepoolwithtag) to free global memory that was allocated by a previous call to a routine such as [**ExAllocatePoolWithTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtag).

-   Call [**ExDeleteNPagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exdeletenpagedlookasidelist) or [**ExDeletePagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exdeletepagedlookasidelist) to delete a lookaside list that was allocated by a previous call to [**ExInitializeNPagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializenpagedlookasidelist) or [**ExInitializePagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializepagedlookasidelist), respectively.

-   Call [**PsRemoveCreateThreadNotifyRoutine**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-psremovecreatethreadnotifyroutine) or [**PsRemoveLoadImageNotifyRoutine**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-psremoveloadimagenotifyroutine) to unregister a global callback routine that was registered by a previous call to [**PsSetCreateThreadNotifyRoutine**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-pssetcreatethreadnotifyroutine) or [**PsSetLoadImageNotifyRoutine**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-pssetloadimagenotifyroutine), respectively.

 

