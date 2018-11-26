---
title: Submit Data Buffer
description: Submit Data Buffer
ms.assetid: 151f5139-3706-4255-9d71-d8e6e3416b7c
keywords:
- Avcstrm.sys streaming filter driver WDK , data buffer submissions
- data buffers WDK AV/C streaming
- submitting data buffers WDK AV/C streaming
- buffers WDK AV/C streaming
- pending streams WDK AV/C streaming
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Submit Data Buffer





With an open stream, a subunit driver can start to attach stream samples to AV/C Streaming. These samples can be either read or write operations, and they can be submitted in the same manner to the AV/C Streaming filter driver, *Avcstrm.sys*. This service is always asynchronous because of its dependency on the current stream state and stream data availability.

```cpp
INIT_AVCSTRM_HEADER(pAVCStrmReq, (pSrb->Command == SRB_READ_DATA) ?      <mark type="enumval">AVCSTRM_READ</mark> : AVCSTRM_WRITE);
pAVCStrmReq->AVCStreamContext = pStrmExt->AVCStreamContext;  // from cached context saved in OPEN_STREAM request

// Avcstrm.sys does not act as a clock provider. The subunit driver must provide this functionality if it wants to be the clock provider.

pAVCStrmReq->CommandData.BufferStruct.StreamHeader = pSrb->CommandData.DataBufferArray;

pAVCStrmReq->CommandData.BufferStruct.FrameBuffer =             
MmGetSystemAddressForMdlSafe(pSrb->Irp->MdlAddress,          NormalPagePriority);

// This is an asynchronous operation
NextIrpStack = IoGetNextIrpStackLocation(pIrpReq);
NextIrpStack->MajorFunction = IRP_MJ_INTERNAL_DEVICE_CONTROL;
NextIrpStack->Parameters.DeviceIoControl.IoControlCode = IOCTL_AVCSTRM_CLASS;
NextIrpStack->Parameters.Others.Argument1 = pAVCStrmReq;

// Cannot be canceled! Use <mark type="enumval">AVCSTRM_ABORT_STREAMING</mark> to abort
IoSetCancelRoutine(
    pIrpReq,
    NULL
    );

IoSetCompletionRoutine( 
    pIrpReq,
    AVCTapeReqReadDataCR,
    pDriverReq,
    TRUE,  // Success
    TRUE,  // Error
    TRUE   // or Cancel
    );

pSrb->Status = STATUS_PENDING;

Status = 
    IoCallDriver(
        pDevExt->pBusDeviceObject,
        pIrpReq
        );
```

Because the operation is asynchronous, the status should be STATUS\_PENDING. When the data is completed, the completion routine will be called. In the completion routine, a subunit driver can do post processing, including updating statistics of data processed and possibly add presentation time if the subunit is the clock provider.

```cpp
// Keep track of the number of frames processed
pStrmExt->FramesProcessed++;

// Retrieve current stream time
if(pStrmExt->hMasterClock) 
    pStrmExt->CurrentStreamTime = pSrb->CommandData.DataBufferArray->PresentationTime.Time;

// Update final status
pSrb->Status = pIrpReq->IoStatus.Status;

// Complete this data SRB
StreamClassStreamNotification( 
    StreamRequestComplete,
    pSrb->StreamObject,
    pSrb 
    );
```
