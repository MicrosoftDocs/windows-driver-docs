---
title: Create a Stream
description: Create a Stream
ms.assetid: 9984275f-7ead-4df2-aa98-a3b4e5e85ae0
keywords:
- Avcstrm.sys streaming filter driver WDK , creating streams
- stream creation WDK AV/C streaming
- contexts WDK AV/C streaming
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Create a Stream





A data stream context must be created before the AV/C Streaming filter driver, *Avcstrm.sys*, can provide services. The context points to an opaque structure that contains the requested data format, data-stream state, and properties, similar to a stream extension. A data format structure and the direction of the data flow are its input parameters. If the stream can be created successfully, it will return a stream context. This context is cached by the subunit driver and is used for subsequent AV/C Streaming requests.

This is a synchronous operation. The operation first creates a stream request structure to open a stream. It then calls the user-defined IRP synchronous routine to call the lower driver to create a data stream that is based on the given data flow direction and data format that is defined in [**AVCSTRM\_FORMAT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff554117). The following code sample shows how to open a data stream context.

```cpp
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

 

 




