---
title: AVCSTRM_ABORT_STREAMING
description: The AVCSTRM_ABORT_STREAMING function code cancels all the pending data requests and frees the resources used.
keywords: ["AVCSTRM_ABORT_STREAMING Streaming Media Devices"]
topic_type:
- apiref
api_name:
- AVCSTRM_ABORT_STREAMING
api_type:
- NA
ms.date: 10/06/2021
---

# AVCSTRM_ABORT_STREAMING

The **AVCSTRM_ABORT_STREAMING** function code cancels *all* the pending data requests and frees the resources used.

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
Use the [**INIT_AVCSTRM_HEADER**](/windows-hardware/drivers/ddi/avcstrm/nf-avcstrm-init_avcstrm_header) macro to initialize these members. Pass **AVCSTRM_ABORT_STREAMING** in the Request argument of the macro.

**AVCStreamContext**  
Specifies the stream context (handle) returned by an earlier **AVCSTRM_OPEN** call that is the target for the data write operation.

A subunit driver must first allocate an IRP and an [**AVC_STREAM_REQUEST_BLOCK**](/windows-hardware/drivers/ddi/avcstrm/ns-avcstrm-_avc_stream_request_block) structure.

Next, it should use the [**INIT_AVCSTRM_HEADER**](/windows-hardware/drivers/ddi/avcstrm/nf-avcstrm-init_avcstrm_header) macro to initialize the AVC_STREAM_REQUEST_BLOCK structure, passing **AVCSTRM_READ** as the Request argument to the macro.

Next, the subunit driver sets the **AVCStreamContext** member to the stream context (handle) of the stream to abort streaming.

To send this request, a subunit submits an [**IRP_MJ_INTERNAL_DEVICE_CONTROL**](../kernel/irp-mj-internal-device-control.md) IRP with the **IoControlCode** member of the IRP set to [**IOCTL_AVCSTRM_CLASS**](/windows-hardware/drivers/ddi/avcstrm/ni-avcstrm-ioctl_avcstrm_class) and the **Argument1** member of the IRP set to the AVC_STREAM_REQUEST_BLOCK structure that describes the abort streaming operation to take place.

This function code must be called at PASSIVE_LEVEL. When a data IRP is being canceled, it can be executed at DISPATCH_LEVEL. In this case, a subunit should start a work item and call this function in its work item routine, which is executing at the PASSIVE_LEVEL.

## Comments

Note, this functionality cancels *all* streaming IRPs. To cancel an individual IRP, use [**IoCancelIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocancelirp).

A subunit should call this when its target device is removed or the original data IRP is canceled to stop stream operation.

This function does not use any member of the **CommandData** union in the AVC_STREAM_REQUEST_BLOCK structure.

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

[**INIT_AVCSTRM_HEADER**](/windows-hardware/drivers/ddi/avcstrm/nf-avcstrm-init_avcstrm_header)

[**IRP_MJ_INTERNAL_DEVICE_CONTROL**](../kernel/irp-mj-internal-device-control.md)

[**IOCTL_AVCSTRM_CLASS**](/windows-hardware/drivers/ddi/avcstrm/ni-avcstrm-ioctl_avcstrm_class)

[**AVCSTRM_FUNCTION**](/windows-hardware/drivers/ddi/avcstrm/ne-avcstrm-_avcstrm_function)
