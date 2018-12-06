---
title: Close a Stream
description: Close a Stream
ms.assetid: 1ed9b07c-8d22-485f-a7e8-3a27ca3768b0
keywords:
- Avcstrm.sys streaming filter driver WDK , closing streams
- stream closing WDK AV/C streaming
- closing streams
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Close a Stream

After a stream operation is completed, the data stream must be closed to free the resources that were allocated by the open stream request.

If the stream *State* is not stopped or there is pending I/O, the close stream request will complete the data request and set the status of the IRP to STATUS\_CANCELLED.

```cpp
INIT_AVCSTRM_HEADER(pAVCStrmReq, AVCSTRM_CLOSE);
pAVCStrmReq->AVCStreamContext = pStrmExt->AVCStreamContext;  // From cached context saved in OPEN_STREAM request
Status = 
    AVCStrmReqSubmitIrpSynch( 
        pDevExt->pBusDeviceObject,
        pStrmExt->pIrpReq,
        pAVCStrmReq
        );
```
