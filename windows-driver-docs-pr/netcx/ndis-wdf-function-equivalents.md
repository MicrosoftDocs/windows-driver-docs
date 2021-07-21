---
title: NDIS-WDF function equivalents
description: NDIS-WDF function equivalents
keywords:
- NetAdapterCx NDIS-WDF function equivalents, NetCx NDIS-WDF function equivalents
ms.date: 06/05/2017
ms.localizationpriority: medium
---

# NDIS-WDF function equivalents

The following table lists NDIS functions and their WDF equivalents:

|NDIS API Family|WDF Equivalent|
|-|-|
|[**NdisAllocateIoWorkItem**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocateioworkitem)|[**WdfWorkItemCreate**](/windows-hardware/drivers/ddi/wdfworkitem/nf-wdfworkitem-wdfworkitemcreate)|
|[**NdisAllocateTimerObject**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatetimerobject)|[**WdfTimerCreate**](/windows-hardware/drivers/ddi/wdftimer/nf-wdftimer-wdftimercreate)|
|[**NdisAcquireSpinLock**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisacquirespinlock)|[**WdfSpinLockAcquire**](/previous-versions/windows/hardware/drivers/ff550040(v=vs.85))|
|[**NdisInterlockedIncrement**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisinterlockedincrement)|[**InterlockedIncrement**](/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockedincrement)|
|[**NdisInitializeEvent**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisinitializeevent)|[**KeInitializeEvent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializeevent)|
|[**NdisMInitializeScatterGatherDma**](/previous-versions/windows/hardware/network/ff553543(v=vs.85))|[**WdfDmaEnablerCreate**](/windows-hardware/drivers/ddi/wdfdmaenabler/nf-wdfdmaenabler-wdfdmaenablercreate)|
|[**NdisInitializeString**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisinitializestring)|[**WdfStringCreate**](/windows-hardware/drivers/ddi/wdfstring/nf-wdfstring-wdfstringcreate)|
|[**NdisSystemActiveProcessorCount**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndissystemactiveprocessorcount)|[**KeGetCurrentProcessorNumberEx**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-kegetcurrentprocessornumberex) (kernel)|
|[**NdisWriteRegisterUchar**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndiswriteregisteruchar)|[**WDF_WRITE_REGISTER_UCHAR**](/windows-hardware/drivers/ddi/wdfhwaccess/nf-wdfhwaccess-wdf_write_register_uchar)|
