---
title: AVCSTRM_CLOSE
description: The AVCSTRM_CLOSE function code closes the specified stream and frees any resources allocated in AVCSTRM_OPEN.
keywords: ["AVCSTRM_CLOSE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVCSTRM_CLOSE
api_type:
- NA
ms.date: 10/06/2021
---

# AVCSTRM_CLOSE

The **AVCSTRM_CLOSE** function code closes the specified stream and frees any resources allocated in AVCSTRM_OPEN.

## I/O Status Block

If successful, *avcstrm.sys* sets **Irp-&gt;IoStatus.Status** to STATUS_SUCCESS.

Possible error return values include:

| Error Status | Description |
|--|--|
| STATUS_DEVICE_REMOVED | The device corresponding to the **AVCSTRM_READ** operation no longer exists. |
| STATUS_CANCELLED | The request was unable to be completed. |
| STATUS_INVALID_PARAMETER | A parameter specified in the IRP is incorrect, |
| STATUS_INSUFFICIENT_RESOURCES | There were not sufficient system resources to complete the request. |
| STATUS_PENDING | The request has been received but requires further processing. The I/O completion routine will handle the final response. |

## AVC_STREAM_REQUEST_BLOCK Input

**SizeOfThisBlock, Version and Function**  
Use the [**INIT_AVCSTRM_HEADER**](/windows-hardware/drivers/ddi/avcstrm/nf-avcstrm-init_avcstrm_header) macro to initialize these members. Pass **AVCSTRM_CLOSE** in the Request argument of the macro.

**AVCStreamContext**  
Specifies the stream context (handle) of the stream to close. If **AVCSTRM_CLOSE** returns successfully, this value is no longer valid.

The following is an example of how to specify the stream to close:

```cpp
    pAVCStrmReq = &pStrmExt->AVCStrmReq;
    RtlZeroMemory(pAVCStrmReq, sizeof(AVC_STREAM_REQUEST_BLOCK));
    INIT_AVCSTRM_HEADER(pAVCStrmReq, AVCSTRM_CLOSE);

    pAVCStrmReq->AVCStreamContext = pStrmExt->AVCStreamContext;

    Status = 
        AVCStrmReqSubmitIrpSynch ( 
            pDevExt->pBusDeviceObject,
            pStrmExt->pIrpReq,
            pAVCStrmReq
            );
```

A subunit driver must first allocate an IRP and an [**AVC_STREAM_REQUEST_BLOCK**](/windows-hardware/drivers/ddi/avcstrm/ns-avcstrm-_avc_stream_request_block) structure.

Next, it should use the [**INIT_AVCSTRM_HEADER**](/windows-hardware/drivers/ddi/avcstrm/nf-avcstrm-init_avcstrm_header) macro to initialize the AVC_STREAM_REQUEST_BLOCK structure, passing **AVCSTRM_CLOSE** as the Request argument to the macro.

Next, the subunit driver sets the **AVCStreamContext** member to the stream to close.

To send this request, a subunit submits an [**IRP_MJ_INTERNAL_DEVICE_CONTROL**](../kernel/irp-mj-internal-device-control.md) IRP with the **IoControlCode** member of the IRP set to [**IOCTL_AVCSTRM_CLASS**](/windows-hardware/drivers/ddi/avcstrm/ni-avcstrm-ioctl_avcstrm_class) and the **Argument1** member of the IRP set to the AVC_STREAM_REQUEST_BLOCK structure that describes the close operation to take place.

A subunit driver can expect this command to complete synchronously. The result returns immediately without pending operation in *avcstrm.sys*.

This function code must be called at IRQL = PASSIVE_LEVEL.

## Comments

This function uses the **AVCStreamContext** member of the **CommandData** union in the AVC_STREAM_REQUEST_BLOCK structure as shown below.

```cpp
typedef struct _AVC_STREAM_REQUEST_BLOCK {
  ULONG  SizeOfThisBlock;
  ULONG  Version;
  AVCSTRM_FUNCTION  Function;
  .
  .
  PVOID AVCStreamContext;
  .
  .
} AVC_STREAM_REQUEST_BLOCK, *PAVC_STREAM_REQUEST_BLOCK;
```

## Requirements

**Headers:** Declared in *avcstrm.h*. Include *avcstrm.h*.

## See Also

[**AVC_STREAM_REQUEST_BLOCK**](/windows-hardware/drivers/ddi/avcstrm/ns-avcstrm-_avc_stream_request_block)

[**INIT_AVCSTRM_HEADER**](/windows-hardware/drivers/ddi/avcstrm/nf-avcstrm-init_avcstrm_header)

[**IRP_MJ_INTERNAL_DEVICE_CONTROL**](../kernel/irp-mj-internal-device-control.md)

[**IOCTL_AVCSTRM_CLASS**](/windows-hardware/drivers/ddi/avcstrm/ni-avcstrm-ioctl_avcstrm_class)

[**AVCSTRM_FUNCTION**](/windows-hardware/drivers/ddi/avcstrm/ne-avcstrm-_avcstrm_function)
