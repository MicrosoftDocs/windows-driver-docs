---
title: Abort a Stream
description: Abort a Stream
ms.assetid: 46c726b6-8553-4588-9be1-2cf7779efec5
keywords:
- Avcstrm.sys streaming filter driver WDK , aborting streams
- abort streams WDK AV/C streaming
- stop streaming WDK AV/C streaming
- stream aborts WDK AV/C streaming
- canceling streams
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Abort a Stream





When a subunit encounters special conditions, such as device removal or stream data IOCTL cancellation, then the streaming operation should be aborted. The abort operation *Request* is synchronous, but the abort completion is not. Only the first abort stream request is accepted and processed; duplicate requests will be ignored but returned with STATUS\_SUCCESS. The AV/C Streaming filter driver, *Avcstrm.sys,* then schedules a work item to abort streaming. When a stream is aborted, it starts to complete the [**AVCSTRM\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff554130)/[**AVCSTRM\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff554135) request with STATUS\_CANCELLED. The stream state is not changed with the abort request, and the data stream still must be closed to clean up and release resources.

In the abort work item routine, AV/C Streaming will first stop the isochronous data transfer, but it does not affect the stream state. AV/C Streaming then goes through the attached streams data queue to detach stream buffers and return them with STATUS\_CANCELLED.

To issue this request, an AV/C Streaming request is initialized with the **AVCSTRM\_ABORT\_STREAMING** request and the data stream context.

```cpp
INIT_AVCSTRM_HEADER(pAVCStrmReq, AVCSTRM_ABORT_STREAMING);
pAVCStrmReq->AVCStreamContext = pStrmExt->AVCStreamContext;  // From cached context saved in OPEN_STREAM request

Status = 
    AVCStrmReqSubmitIrpSynch( 
        pStrmExt->pDevExt->pBusDeviceObject,
        pStrmExt->pIrpAbort,
        pAVCStrmReq
        );
```

When a data stream is aborted, it can be resumed (if the device has not been removed) after its stream state has been reset to **KSSTATE\_STOP** by its client application.

 

 




