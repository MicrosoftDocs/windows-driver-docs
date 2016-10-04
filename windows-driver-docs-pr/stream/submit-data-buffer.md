---
title: Submit Data Buffer
author: windows-driver-content
description: Submit Data Buffer
MS-HAID:
- 'avcsguide\_c306feec-94f5-4092-86b3-5580ecf8823f.xml'
- 'stream.submit\_data\_buffer'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 151f5139-3706-4255-9d71-d8e6e3416b7c
keywords: ["Avcstrm.sys streaming filter driver WDK , data buffer submissions", "data buffers WDK AV/C streaming", "submitting data buffers WDK AV/C streaming", "buffers WDK AV/C streaming", "pending streams WDK AV/C streaming"]
---

# Submit Data Buffer


## <a href="" id="ddk-submitting-a-data-buffer-ksg"></a>


With an open stream, a subunit driver can start to attach stream samples to AV/C Streaming. These samples can be either read or write operations, and they can be submitted in the same manner to the AV/C Streaming filter driver, *Avcstrm.sys*. This service is always asynchronous because of its dependency on the current stream state and stream data availability.

```
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Submit%20Data%20Buffer%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


