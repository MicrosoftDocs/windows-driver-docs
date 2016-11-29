---
title: Create a Stream
author: windows-driver-content
description: Create a Stream
MS-HAID:
- 'avcsguide\_dbb9d67a-4e30-40d7-b2aa-27b1fe6b3fbb.xml'
- 'stream.create\_a\_stream'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9984275f-7ead-4df2-aa98-a3b4e5e85ae0
keywords: ["Avcstrm.sys streaming filter driver WDK , creating streams", "stream creation WDK AV/C streaming", "contexts WDK AV/C streaming"]
---

# Create a Stream


## <a href="" id="ddk-creating-a-stream-ksg"></a>


A data stream context must be created before the AV/C Streaming filter driver, *Avcstrm.sys*, can provide services. The context points to an opaque structure that contains the requested data format, data-stream state, and properties, similar to a stream extension. A data format structure and the direction of the data flow are its input parameters. If the stream can be created successfully, it will return a stream context. This context is cached by the subunit driver and is used for subsequent AV/C Streaming requests.

This is a synchronous operation. The operation first creates a stream request structure to open a stream. It then calls the user-defined IRP synchronous routine to call the lower driver to create a data stream that is based on the given data flow direction and data format that is defined in [**AVCSTRM\_FORMAT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff554117). The following code sample shows how to open a data stream context.

```
#include <avcstrm.h>

INIT_AVCSTRM_HEADER(pAVCStrmReq, AVCSTRM_OPEN);
pAVCStrmReq->CommandData.OpenStruct.AVCFormatInfo =            &AVCStrmFormatInfoTable[pDevExt->VideoFormatIndex]; 
pAVCStrmReq->CommandData.OpenStruct.AVCStreamContext = NULL;
pAVCStrmReq->CommandData.OpenStruct.DataFlow         = DataFlow;

Status = 
    AVCStrmReqSubmitIrpSynch( 
        pDevExt->pBusDeviceObject,
        pStrmExt->pIrpReq,
        pAVCStrmReq
        );

if(STATUS_SUCCESS == Status) {
    // Save the context, which is used for a 
    // Subsequent call to the AVCStrm filter driver    
    pStrmExt->AVCStreamContext = 
        pAVCStrmReq->CommandData.OpenStruct.AVCStreamContext;
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Create%20a%20Stream%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


