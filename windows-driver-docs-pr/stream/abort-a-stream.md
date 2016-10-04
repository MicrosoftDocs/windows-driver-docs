---
title: Abort a Stream
author: windows-driver-content
description: Abort a Stream
MS-HAID:
- 'avcsguide\_38c1d0f9-5d5b-4343-b54f-04a8f6e5b5b1.xml'
- 'stream.abort\_a\_stream'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 46c726b6-8553-4588-9be1-2cf7779efec5
keywords: ["Avcstrm.sys streaming filter driver WDK , aborting streams", "abort streams WDK AV/C streaming", "stop streaming WDK AV/C streaming", "stream aborts WDK AV/C streaming", "canceling streams"]
---

# Abort a Stream


## <a href="" id="ddk-aborting-a-stream-ksg"></a>


When a subunit encounters special conditions, such as device removal or stream data IOCTL cancellation, then the streaming operation should be aborted. The abort operation *Request* is synchronous, but the abort completion is not. Only the first abort stream request is accepted and processed; duplicate requests will be ignored but returned with STATUS\_SUCCESS. The AV/C Streaming filter driver, *Avcstrm.sys,* then schedules a work item to abort streaming. When a stream is aborted, it starts to complete the [**AVCSTRM\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff554130)/[**AVCSTRM\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff554135) request with STATUS\_CANCELLED. The stream state is not changed with the abort request, and the data stream still must be closed to clean up and release resources.

In the abort work item routine, AV/C Streaming will first stop the isochronous data transfer, but it does not affect the stream state. AV/C Streaming then goes through the attached streams data queue to detach stream buffers and return them with STATUS\_CANCELLED.

To issue this request, an AV/C Streaming request is initialized with the **AVCSTRM\_ABORT\_STREAMING** request and the data stream context.

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Abort%20a%20Stream%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


