---
title: Get and Set the Stream State
description: Get and Set the Stream State
ms.assetid: e2fde528-d0cf-4ffe-945a-8672b76db61f
keywords:
- Avcstrm.sys streaming filter driver WDK , stream states
- stream states WDK AV/C streaming
- states WDK AV/C streaming
- KSSTATE_STOP
- KSSTATE_ACQUIRE
- KSSTATE_PAUSE
- KSSTATE_RUN
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Get and Set the Stream State





A subunit receives IOCTLs from a client application to get the current stream state or to set to a new stream state. When a data stream is created, it is initialized to the **KSSTATE\_STOP** state. The isochronous resource is allocated in the **KSSTATE\_ACQUIRE** state, and if it fails, it will return STATUS\_INSUFFICIENT\_RESOURCE (declared in *Ntstatus.h*) in the **KSSTATE\_PAUSE** state. Data streaming will commence in the **KSSTATE\_RUN** state.

The following code sample sets the stream to a new state:

```cpp
INIT_AVCSTRM_HEADER(pAVCStrmReq, AVCSTRM_SET_STATE);
pAVCStrmReq->AVCStreamContext = pStrmExt->AVCStreamContext; //  From cached context saved in OPEN_STREAM request
pAVCStrmReq->CommandData.StreamState = StreamState; // New stream state

Status = 
    AVCStrmReqSubmitIrpSynch( 
        pDevExt->pBusDeviceObject,
        pStrmExt->pIrpReq,
        pAVCStrmReq
        );
```

The following code sample queries for the current stream state:

```cpp
INIT_AVCSTRM_HEADER(pAVCStrmReq, AVCSTRM_GET_STATE);
pAVCStrmReq->AVCStreamContext = pStrmExt->AVCStreamContext;  // From cached context saved in OPEN_STREAM request

Status = 
    AVCStrmReqSubmitIrpSynch( 
        DeviceObject,
        pStrmExt->pIrpReq,
        pAVCStrmReq
        );

// If return STATUS_SUCCESS, the current stream state is in
// pAVCStrmReq->CommandData.StreamState 
```

 

 




