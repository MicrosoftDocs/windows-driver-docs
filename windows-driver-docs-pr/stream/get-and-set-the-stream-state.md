---
title: Get and Set the Stream State
author: windows-driver-content
description: Get and Set the Stream State
MS-HAID:
- 'avcsguide\_40840902-e07c-49eb-8068-02c6df443ce2.xml'
- 'stream.get\_and\_set\_the\_stream\_state'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e2fde528-d0cf-4ffe-945a-8672b76db61f
keywords: ["Avcstrm.sys streaming filter driver WDK , stream states", "stream states WDK AV/C streaming", "states WDK AV/C streaming", "KSSTATE_STOP", "KSSTATE_ACQUIRE", "KSSTATE_PAUSE", "KSSTATE_RUN"]
---

# Get and Set the Stream State


## <a href="" id="ddk-getting-and-setting-the-stream-state-ksg"></a>


A subunit receives IOCTLs from a client application to get the current stream state or to set to a new stream state. When a data stream is created, it is initialized to the **KSSTATE\_STOP** state. The isochronous resource is allocated in the **KSSTATE\_ACQUIRE** state, and if it fails, it will return STATUS\_INSUFFICIENT\_RESOURCE (declared in *Ntstatus.h*) in the **KSSTATE\_PAUSE** state. Data streaming will commence in the **KSSTATE\_RUN** state.

The following code sample sets the stream to a new state:

```
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Get%20and%20Set%20the%20Stream%20State%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


