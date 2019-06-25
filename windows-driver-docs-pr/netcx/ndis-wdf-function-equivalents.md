---
title: NDIS-WDF function equivalents
description: NDIS-WDF function equivalents
ms.assetid: 28C8DFA3-5602-422D-89AA-6EA05F501E15
keywords:
- NetAdapterCx NDIS-WDF function equivalents, NetCx NDIS-WDF function equivalents
ms.date: 06/05/2017
ms.localizationpriority: medium
---

# NDIS-WDF function equivalents

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

The following table lists NDIS functions and their WDF equivalents:

|NDIS API Family|WDF Equivalent|
|-|-|
|[**NdisAllocateIoWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisallocateioworkitem)|[**WdfWorkItemCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfworkitem/nf-wdfworkitem-wdfworkitemcreate)|
|[**NdisAllocateTimerObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisallocatetimerobject)|[**WdfTimerCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdftimer/nf-wdftimer-wdftimercreate)|
|[**NdisAcquireSpinLock**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisacquirespinlock)|[**WdfSpinLockAcquire**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff550040(v=vs.85))|
|[**NdisInterlockedIncrement**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisinterlockedincrement)|[**InterlockedIncrement**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-interlockedincrement)|
|[**NdisInitializeEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisinitializeevent)|[**KeInitializeEvent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keinitializeevent)|
|[**NdisMInitializeScatterGatherDma**](https://docs.microsoft.com/previous-versions/windows/hardware/network/ff553543(v=vs.85))|[**WdfDmaEnablerCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdmaenabler/nf-wdfdmaenabler-wdfdmaenablercreate)|
|[**NdisInitializeString**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisinitializestring)|[**WdfStringCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfstring/nf-wdfstring-wdfstringcreate)|
|[**NdisSystemActiveProcessorCount**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndissystemactiveprocessorcount)|[**KeGetCurrentProcessorNumberEx**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-kegetcurrentprocessornumberex) (kernel)|
|[**NdisWriteRegisterUchar**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndiswriteregisteruchar)|[**WDF_WRITE_REGISTER_UCHAR**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfhwaccess/nf-wdfhwaccess-wdf_write_register_uchar)|
